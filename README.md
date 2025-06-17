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

