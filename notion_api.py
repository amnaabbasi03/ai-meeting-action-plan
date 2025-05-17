import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()
notion = Client(auth=os.getenv("NOTION_API_KEY"))
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def send_to_notion(summary, decisions, action_items):
    try:
        for item in action_items:
            notion.pages.create(
                parent={"database_id": DATABASE_ID},
                properties={
                    "Name": {
                        "title": [{"text": {"content": item['task']}}]
                    },
                    "Owner": {
                        "rich_text": [{"text": {"content": item['owner']}}]
                    },
                    "Deadline": {
                        "date": {"start": item['deadline']}
                    }
                }
            )
        return True
    except Exception as e:
        print("Notion API error:", e)
        return False

