# AI-Powered Meeting Action Plan Generator

AI Meeting Action Plan Generator is a simple web application that lets you upload meeting transcripts and automatically generates structured action plans using OpenAI's GPT models. It is built with Streamlit for easy deployment and user interaction.

## Overview
This tool is designed to help users quickly turn raw meeting transcripts into clear summaries and task lists. 
It extracts: meeting transcripts from Zoom, Google Meet, or Teams, and generates:

- ✅ Clear action items (with owners and deadlines)
- 🧠 Key decisions
- 📝 Summary bullets

Optionally, you can push the extracted tasks to a **Notion** task database.

## 🚀 How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

2. Create .env file
Create a file named .env in the project root and add your OpenAI and Notion API keys in the following format:
OPENAI_API_KEY=your-openai-key-here
NOTION_API_KEY=your-notion-key-here
NOTION_DATABASE_ID=your-database-id-here

3. Install the required Python packages
pip install -r requirements.txt

4. Start the Streamlit app
streamlit run main.py

The app will open in your browser. Upload a transcript file (TXT or Markdown), and it will display a structured action plan. You can optionally push the tasks to Notion with a single click.

** Use Cases**

1.Product and project managers summarizing meetings
2.Customer success teams capturing client discussions
3.Executive assistants preparing meeting notes
4.Teachers and facilitators generating session summaries
5. Government offices automating task follow-ups from inter-departmental meetings

**Disclaimer**

This is a demonstration project intended for educational and prototyping purposes. It is not yet optimized for production use. Please handle all API keys securely and avoid uploading sensitive or confidential transcripts without proper safeguards.
