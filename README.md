# HCI Study Buddy

**An LLM-Powered Educational Chatbot for Human-Computer Interaction**

## Project Overview

HCI Study Buddy is an educational chatbot developed by Janardhan Reddy Bommireddy for the University of the Cumberlands course Artificial Intelligence for Human-Computer Interaction (MSAI-631-A02). The application uses the Qwen2.5-1.5B-Instruct large language model through Hugging Face Transformers and provides a browser-based conversational interface using Gradio.

The purpose of the application is to help students explore concepts related to Human-Computer Interaction (HCI), usability, accessibility, user-interface design, and artificial intelligence. Users can enter questions in natural language, receive model-generated explanations, and ask follow-up questions within the same conversation.

## Features

- Natural-language questions and model-generated answers.
- A browser-based conversational interface built with Gradio.
- Support for follow-up questions using conversation history.
- Educational responses focused on HCI, usability, accessibility, and interface design.
- A simple interface that does not require users to interact directly with a command-line model.
- Local model inference without a paid OpenAI API token.

## Technologies Used

- **Python:** Main programming language.
- **Gradio:** Conversational web interface.
- **PyTorch:** Machine-learning inference framework.
- **Hugging Face Transformers:** Model loading and text generation.
- **Qwen2.5-1.5B-Instruct:** Instruction-following language model.
- **Git and GitHub:** Source-code version control and project sharing.

## System Requirements

The application was developed and tested on Windows using Python 3.14.3. The observed environment used Gradio 6.30.0, Transformers 5.19.0, and PyTorch 2.14.1 with CPU support.

An internet connection is required to download the model during the first launch. The model file downloaded during development was approximately 3.09 GB, and additional disk space is needed for libraries, configuration files, and cached model files. The computer used during development had approximately 15.8 GB of RAM and did not have CUDA available, so model inference ran on the CPU.

Performance will vary depending on the computer's available memory, processor, and software environment. The first launch may take several minutes because the model must be downloaded and loaded into memory.

## Installation and Setup

### Step 1: Open the Project

Download or clone the HCI Study Buddy repository and open the project folder in Visual Studio Code.

### Step 2: Create a Virtual Environment

Run the following command in the VS Code terminal:

```powershell
python -m venv .venv
```

### Step 3: Install Dependencies

Install the packages listed in `requirements.txt`:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Step 4: Run the Application

Start the chatbot using:

```powershell
.\.venv\Scripts\python.exe app.py
```

Wait until the model finishes loading and Gradio displays a local address in the terminal. Open the address shown by Gradio, usually:

`http://127.0.0.1:7860`

To stop the application, return to the terminal and press `Ctrl+C`.

## Example Questions

The following questions can be used to test the chatbot:

1. What is Human-Computer Interaction? Explain it in simple language and give one practical example.
2. What is usability, and what are five characteristics of a usable interface?
3. What is user-centered design?
4. How can a website be made more accessible to users with disabilities?
5. How does usability testing work in a mobile banking application?
6. How does accessibility improve the user experience?
7. Can you provide another example of the concept you just explained?

Follow-up questions should be asked within the same conversation to examine whether the chatbot uses previous messages appropriately.

## Model Information

The application uses `Qwen/Qwen2.5-1.5B-Instruct`, obtained through Hugging Face. The model is loaded locally by the application and generates responses on the computer after the model files have been downloaded.

The application does not call a paid OpenAI API. Users should nevertheless understand that the chatbot can produce incorrect, incomplete, repetitive, or overly detailed responses. Important information should be verified against course materials and reliable academic sources.

## Testing and Observed Results

During development, the Gradio and Transformers libraries imported successfully, PyTorch was installed, and the Qwen2.5-1.5B-Instruct model loaded successfully. The application launched at the local Gradio address and generated responses to questions about Human-Computer Interaction and usability. Follow-up prompts also produced additional responses within the conversation.

These observations confirm that the application was able to run and generate model responses in the development environment. They do not establish that every response is factually correct or that the chatbot has been evaluated across all possible questions. Additional tests should be documented as they are performed.

## Known Limitations

The application uses CPU inference in the tested environment, which can make response generation slower than GPU-based inference. Initial setup requires downloading the model, and the application depends on compatible Python libraries and sufficient memory. The model has not been fine-tuned on the course's materials and does not use a verified educational knowledge base.

Generated responses may contain factual errors, ambiguous explanations, repetition, or unnecessary detail. Retrieval-augmented generation, a curated course-document knowledge base, and additional response-quality controls could be considered as future improvements. The current application should be treated as an educational prototype rather than an authoritative source of academic information.

## Project Structure

The main project files are organized as follows:

```text
HCI-Study-Buddy/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── TESTING_NOTES.md

```

The `.venv` virtual environment and downloaded model files should remain local and should not be uploaded to GitHub.

## References and Resources

Gradio. (n.d.). *Gradio documentation*. https://www.gradio.app/docs

Hugging Face. (n.d.). *Transformers documentation*. https://huggingface.co/docs/transformers/index

Qwen. (n.d.). *Qwen2.5-1.5B-Instruct*. Hugging Face. https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct

## Author

**Janardhan Reddy Bommireddy**  
University of the Cumberlands  
Artificial Intelligence for Human-Computer Interaction (MSAI-631-A02)
