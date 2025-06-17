# 📝 Text Summarization App with DistilBART (CNN/DailyMail)

This project uses the pre-trained **DistilBART** model (`sshleifer/distilbart-cnn-12-6`) from Hugging Face 🤗 for efficient and fast **abstractive text summarization**. The model is served through a simple and clean **Gradio UI**, allowing users to input long-form text and get concise summaries.

---

## 🔍 About the Model

- **Model**: `sshleifer/distilbart-cnn-12-6`
- **Base**: Distilled version of Facebook’s BART
- **Task**: Text Summarization
- **Dataset**: CNN / DailyMail news articles
- **Advantages**:
  - Faster inference time
  - Lighter model size
  - Competitive summarization performance

---

## 🚀 Features

- 🧠 Summarizes long articles into short, readable text
- 🎛️ User-friendly web interface built with Gradio
- ⚡ Fast & light using a distilled transformer model
- 📄 Optionally supports PDF input and summarization
- 📦 Ready for deployment (local or cloud)

---

## 🛠️ Tech Stack

| Tool/Library         | Purpose                                |
|----------------------|----------------------------------------|
| Python               | Core language                          |
| Hugging Face Transformers | Model & pipeline support        |
| Gradio               | UI for model interaction               |
| Streamlit (optional) | Alternative UI interface               |
| PyPDF / Pillow       | PDF/text/image support (optional)      |

---

## 📂 Project Structure
->Create an Environment variable to the code (python version used 3.13.3)
->textsummary.py - Which contains code to summarize the text provided by the user
->Model - Create a folder (eg:"Model") , Ensure the model dataset is in the code file
->import all the neccessary modules which are provided in the requirement files 
-> Model cannot be easily uploaded because they are large data sets and takes more time 


