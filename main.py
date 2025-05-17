import streamlit as st
from ai_engine import extract_action_plan
from notion_api import send_to_notion

st.title("🎯 AI-Powered Meeting Action Plan Generator")

uploaded_file = st.file_uploader("Upload meeting transcript file", type=["txt", "md"])

# If user cleared file uploader (clicked the x), clear session data for fresh canvas
if uploaded_file is None:
    if 'action_plan_data' in st.session_state:
        del st.session_state['action_plan_data']

if uploaded_file:
    transcript = uploaded_file.read().decode("utf-8")
    st.text_area("Transcript Preview", transcript, height=200)

    if st.button("Generate Action Plan"):
        with st.spinner("Generating action plan..."):
            summary, decisions, action_items = extract_action_plan(transcript)
            if summary and decisions and action_items:
                st.session_state['action_plan_data'] = {
                    "summary": summary,
                    "decisions": decisions,
                    "action_items": action_items
                }
            else:
                st.error("Failed to generate action plan from transcript.")

if 'action_plan_data' in st.session_state:
    data = st.session_state['action_plan_data']

    st.subheader("📌 Summary")
    st.write("\n".join(f"- {s}" for s in data["summary"]))

    st.subheader("🧠 Key Decisions")
    st.write("\n".join(f"- {d}" for d in data["decisions"]))

    st.subheader("✅ Action Items")
    for item in data["action_items"]:
        st.markdown(f"- **Task:** {item['task']} | **Owner:** {item['owner']} | **Deadline:** {item['deadline']}")

    if st.button("Push to Notion Task Table"):
        success = send_to_notion(data["summary"], data["decisions"], data["action_items"])
        if success:
            st.success("Action items pushed to Notion successfully!")
        else:
            st.error("Failed to push to Notion. Check your config.")

