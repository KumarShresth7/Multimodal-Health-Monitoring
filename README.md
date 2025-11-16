Multimodal Health Monitoring System

A local, privacy-focused health assessment tool that uses Multimodal Large Language Models (MLLMs) running via Ollama to analyze clinical notes, chest X-rays, and ECG traces simultaneously.

Built with Streamlit and Ollama Python.

📋 Overview

This application acts as an AI assistant for preliminary health assessments. It ingests three distinct types of data:

Visual Data (Radiology): Chest X-rays.

Visual Data (Cardiology): ECG traces.

Textual Data: Clinical patient notes.

It uses specialized AI agents (Vision models for images, LLMs for text) to analyze each input independently, then synthesizes a unified risk assessment report.

✨ Features

100% Local Privacy: All processing happens on your machine via Ollama. No patient data is sent to the cloud.

Multimodal Analysis: Combines vision (image) and language (text) understanding.

Interactive UI: Simple web interface built with Streamlit.

Customizable Models: easily switch between different local models (e.g., LLaVA, BakLLaVA, Phi-3, Mistral).

🛠️ Prerequisites

1. System Requirements

Ollama: You must have Ollama installed and running. Download Ollama here.

Python: Version 3.8 or higher.

2. Required AI Models

You need to pull the models used by the app before running it. Open your terminal and run:

# Pull a vision model (default in app is llava)
ollama pull llava

# Pull a text model (default in app is phi3)
ollama pull phi3


Note: You can use other models (like bakllava or mistral), but ensure you update the configuration in the app sidebar.

📦 Installation

Clone the repository (or place app.py and models.py in a folder):

mkdir health-monitor
cd health-monitor


Install Python Dependencies:

pip install streamlit ollama requests


🚀 Usage

Start the Ollama Server:
Make sure the Ollama application is running in the background. You can verify this by visiting http://localhost:11434 in your browser (it should say "Ollama is running").

Run the Streamlit App:

streamlit run app.py


Interact with the App:

Sidebar: Verify "Server detected" is green. If your models have different names (e.g., llava:v1.6), type the exact name in the text fields.

Inputs: Upload sample X-ray/ECG images and paste clinical text.

Generate: Click "Generate Assessment" to receive the AI synthesis.

📂 Project Structure

app.py: The frontend user interface. Handles file uploads, user inputs, and displays the final report.

models.py: The backend logic. Contains functions to check server status, interface with the Ollama API, and process images/text.

⚙️ Configuration

You can configure the models dynamically in the application sidebar:

Host URL: Default is http://localhost:11434. Change this if you are hosting Ollama on a different machine on your network.

Vision Model: Must be a model that supports images (e.g., llava, moondream, llava-phi3).

LLM Model: Any standard chat model (e.g., phi3, llama3, neural-chat).

⚠️ Disclaimer

This tool is for educational and research purposes only. It is NOT a medical device and should not be used for actual medical diagnosis or treatment. AI models can hallucinate or provide incorrect medical information.Multimodal Health Monitoring System (Local AI)

A local, privacy-focused health assessment tool that uses Multimodal Large Language Models (MLLMs) running via Ollama to analyze clinical notes, chest X-rays, and ECG traces simultaneously.

Built with Streamlit and Ollama Python.

📋 Overview

This application acts as an AI assistant for preliminary health assessments. It ingests three distinct types of data:

Visual Data (Radiology): Chest X-rays.

Visual Data (Cardiology): ECG traces.

Textual Data: Clinical patient notes.

It uses specialized AI agents (Vision models for images, LLMs for text) to analyze each input independently, then synthesizes a unified risk assessment report.

✨ Features

100% Local Privacy: All processing happens on your machine via Ollama. No patient data is sent to the cloud.

Multimodal Analysis: Combines vision (image) and language (text) understanding.

Interactive UI: Simple web interface built with Streamlit.

Customizable Models: easily switch between different local models (e.g., LLaVA, BakLLaVA, Phi-3, Mistral).

🛠️ Prerequisites

1. System Requirements

Ollama: You must have Ollama installed and running. Download Ollama here.

Python: Version 3.8 or higher.

2. Required AI Models

You need to pull the models used by the app before running it. Open your terminal and run:

# Pull a vision model (default in app is llava)
ollama pull llava

# Pull a text model (default in app is phi3)
ollama pull phi3


Note: You can use other models (like bakllava or mistral), but ensure you update the configuration in the app sidebar.

📦 Installation

Clone the repository (or place app.py and models.py in a folder):

mkdir health-monitor
cd health-monitor


Install Python Dependencies:

pip install streamlit ollama requests


🚀 Usage

Start the Ollama Server:
Make sure the Ollama application is running in the background. You can verify this by visiting http://localhost:11434 in your browser (it should say "Ollama is running").

Run the Streamlit App:

streamlit run app.py


Interact with the App:

Sidebar: Verify "Server detected" is green. If your models have different names (e.g., llava:v1.6), type the exact name in the text fields.

Inputs: Upload sample X-ray/ECG images and paste clinical text.

Generate: Click "Generate Assessment" to receive the AI synthesis.

📂 Project Structure

app.py: The frontend user interface. Handles file uploads, user inputs, and displays the final report.

models.py: The backend logic. Contains functions to check server status, interface with the Ollama API, and process images/text.

⚙️ Configuration

You can configure the models dynamically in the application sidebar:

Host URL: Default is http://localhost:11434. Change this if you are hosting Ollama on a different machine on your network.

Vision Model: Must be a model that supports images (e.g., llava, moondream, llava-phi3).

LLM Model: Any standard chat model (e.g., phi3, llama3, neural-chat).

⚠️ Disclaimer

This tool is for educational and research purposes only. It is NOT a medical device and should not be used for actual medical diagnosis or treatment. AI models can hallucinate or provide incorrect medical information.
