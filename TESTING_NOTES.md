# HCI Study Buddy — Testing Notes

## Project Information

**Project:** HCI Study Buddy — An LLM-Based Educational Chatbot  
**Student:** Janardhan Reddy Bommireddy  
**Course:** MSAI-631-A02 — Artificial Intelligence for Human-Computer Interaction  
**Operating System:** Windows  
**Test Date:** October 12, 2026

## Development Environment

The application was developed and tested using Python 3.14.3. The installed libraries included Gradio 6.30.0, Transformers 5.19.0, and PyTorch 2.14.1. The computer had approximately 15.8 GB of RAM, and PyTorch reported that CUDA was unavailable, so the application used CPU inference.

The selected language model was Qwen2.5-1.5B-Instruct, downloaded from Hugging Face. The Gradio application was accessed locally through the address displayed in the terminal, typically `http://127.0.0.1:7860`.

## Tests Performed

### 1. Library Installation and Import

Gradio and Transformers were installed in the project's Python virtual environment. A verification command successfully imported both libraries and displayed their installed versions. PyTorch was subsequently installed and imported successfully, with the environment reporting CPU execution. These checks established that the main software dependencies were available in the development environment.

**Observed result:** Passed.

### 2. Language Model Download and Loading

The application downloaded the Qwen2.5-1.5B-Instruct model files from Hugging Face. The model-loading process completed, and the terminal displayed a successful model-loading message. The first launch required additional time because the model files had to be downloaded and initialized. The application was then able to proceed to the Gradio interface.

**Observed result:** Passed.

### 3. Chatbot Interface Launch

The Gradio application launched and displayed a local URL in the terminal. The interface opened in a web browser and provided a conversational area for entering questions and viewing responses. The application displayed the HCI Study Buddy title and introductory information. This confirmed that the user interface was accessible in the local development environment.

**Observed result:** Passed.

### 4. Human-Computer Interaction Question

The chatbot was asked to explain Human-Computer Interaction. It generated an answer describing HCI and discussing its relevance to the interaction between people and computer systems. The response demonstrated that the application could accept a natural-language question and display a generated answer. The response was reviewed visually, although this test alone does not establish the factual accuracy of every statement.

**Observed result:** Passed for response generation.

### 5. Usability Question

The chatbot was asked to explain usability and related concepts. It generated an answer discussing usability and provided explanatory content relevant to the question. This demonstrated that the model could respond to another educational prompt within the intended project scope. The output also illustrated that response length and detail can vary depending on the question.

**Observed result:** Passed for response generation.

### 6. Follow-Up Conversation

Additional questions were submitted within the same conversation. The chatbot continued generating responses to the follow-up prompts. This demonstrated basic conversational interaction beyond a single isolated question. Further systematic testing is still needed to assess how reliably the model uses earlier messages and handles ambiguous references.

**Observed result:** Follow-up responses observed; context quality requires further evaluation.

## Limitations Observed

The application runs on the CPU in the tested environment, which can make response generation slower than GPU-based inference. The initial model download and loading process also required additional time and disk space. The model can generate long explanations, and generated content may contain inaccuracies or unnecessary detail. The application has not been fine-tuned on course materials or evaluated through a formal user study.

These limitations mean that the chatbot should be treated as an educational prototype rather than an authoritative source. Important information should be checked against course materials and reliable references. Additional testing can help identify response-quality problems and opportunities to improve the interface.

## Additional Tests to Complete

The following tests should be performed and documented before the final project report is completed:

- Test how the application handles an empty message.
- Ask a question outside the chatbot's main educational scope.
- Ask a follow-up question that depends on a specific detail in the previous response.
- Test the conversation-clearing or restarting behavior.
- Restart the application after the model has been cached locally.
- Record approximate response times for several representative questions.
- Review responses for factual errors, repetition, relevance, and readability.

Record the actual result of each additional test after performing it. Do not mark a test as passed unless the behavior has been observed.

## Conclusion

The initial tests demonstrated that HCI Study Buddy could load the selected language model, launch its Gradio interface, and generate responses to educational questions. These results establish a working foundation for the individual project. Further testing is required to evaluate error handling, response quality, performance, and conversational context more systematically. The final project report should incorporate the actual outcomes of these additional tests and describe any modifications made during development.