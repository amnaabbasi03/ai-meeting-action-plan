# 🧠 AI-Powered Meeting Action Plan Generator

**AI Meeting Action Plan Generator** is a simple web application that lets you upload meeting transcripts and automatically generates structured action plans using OpenAI's GPT models. It is built with **Streamlit** for easy deployment and user interaction.

---

## 📋 Overview

This tool is designed to help users quickly turn raw meeting transcripts into clear summaries and task lists.  
It supports transcripts from **Zoom**, **Google Meet**, or **Teams**, and generates:

- ✅ Clear action items (with owners and deadlines)  
- 🧠 Key decisions  
- 📝 Summary bullet points  

You can optionally push the extracted tasks directly to a **Notion** task database.

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Create a `.env` file

Create a file named `.env` in the project root and add the following:

```env
OPENAI_API_KEY=your-openai-key-here
NOTION_API_KEY=your-notion-key-here
NOTION_DATABASE_ID=your-database-id-here
```

> 💡 You can refer to `.env.example` for guidance.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Streamlit app

```bash
streamlit run main.py
```

The app will open in your default browser.  
You can upload a transcript file (`.txt` or `.md`) and it will display:

- Key decisions  
- Action items with deadlines and owners  
- Summary bullets  

You can then click to push these directly to your Notion task table.

---

## 💼 Use Cases

1. **Product and project managers** summarizing meetings  
2. **Customer success teams** capturing client discussions  
3. **Executive assistants** preparing follow-up notes  
4. **Teachers and facilitators** generating summaries of learning sessions  
5. **Government offices** automating task tracking from inter-departmental meetings  

---

## ⚠️ Disclaimer

This is a demonstration project intended for educational and prototyping purposes.  
It is not optimized for production use. Please handle all API keys securely and avoid uploading sensitive or confidential transcripts without proper safeguards.

---
