import ollama
import base64
import requests

def check_ollama_server(host="http://localhost:11434"):
    """
    Checks if the Ollama server is running at the specified host.
    Returns: (is_running: bool, message: str)
    """
    try:
        response = requests.get(f"{host}/api/tags", timeout=5)
        response.raise_for_status()
        return True, ""
    except requests.exceptions.ConnectionError:
        return False, f"Ollama server not running at {host}. Please start Ollama app."
    except Exception as e:
        return False, f"Error checking Ollama server: {e}"

def check_ollama_model(model_name: str):
    """
    Checks if a specific Ollama model is pulled and available.
    Robustly handles different response formats from the ollama library.
    Returns: (is_available: bool, message: str)
    """
    try:
        response = ollama.list()
    
        models_list = []
        if hasattr(response, 'models'):

            models_list = response.models
        elif isinstance(response, dict):
 
            models_list = response.get('models', [])
        elif isinstance(response, list):

            models_list = response
            

        for m in models_list:
            name = ""

            if hasattr(m, 'model'): 
                name = m.model 
            elif hasattr(m, 'name'):
                name = m.name  
            elif isinstance(m, dict):
                name = m.get('name') or m.get('model')
            

            if name and name.startswith(model_name):
                return True, ""
                
        return False, f"Ollama model '{model_name}' not found. Run 'ollama pull {model_name}' in terminal."
        
    except Exception as e:
        return False, f"Error listing Ollama models: {e}"

def analyze_image(image_bytes: bytes, prompt: str, model: str) -> str:
    """
    Sends an image and a prompt to a multimodal Ollama model (e.g., LLaVA).
    """
    try:

        base64_image = base64.b64encode(image_bytes).decode('utf-8')
        
        response = ollama.generate(
            model=model,
            prompt=prompt,
            images=[base64_image],
            options={'temperature': 0.1} 
        )
        return response['response'].strip()
    except Exception as e:
        return f"Error processing image with model '{model}': {str(e)}"

def summarize_text(text: str, model: str) -> str:
    """
    Summarizes text using an Ollama model (e.g., Phi-3).
    """
    try:
        prompt = f"Summarize the following clinical notes concisely:\n\n{text}\n\nSummary:"
        response = ollama.generate(
            model=model, 
            prompt=prompt,
            options={'temperature': 0.1, 'num_predict': 200}
        )
        return response['response'].strip()
    except Exception as e:
        return f"Error summarizing text with model '{model}': {str(e)}"

def generate_synthesis(final_prompt: str, model: str) -> str:
    """
    Generates the final consolidated report using an LLM.
    """
    try:
        response = ollama.generate(
            model=model,
            prompt=final_prompt,
            options={'temperature': 0.3, 'num_predict': 1500}
        )
        return response['response'].strip()
    except Exception as e:
        return f"Error generating report with model '{model}': {str(e)}"