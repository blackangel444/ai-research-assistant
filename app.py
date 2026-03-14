import streamlit as st
from search import search_web
from scraper import scrape_page
from summarizer import summarize

# Page config
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🧠",
    layout="wide"
)

# Sidebar
st.sidebar.title("AI Research Assistant")
st.sidebar.write("An AI tool that searches the web and summarizes research topics.")

st.sidebar.markdown("### How it works")
st.sidebar.write("""
1. Search the web  
2. Extract article content  
3. Summarize using AI  
""")

# Title
st.title("🧠 AI Research Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
query = st.chat_input("Ask a research question...")

if query:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    with st.spinner("🔎 Researching the web..."):

        links = search_web(query)

        combined_text = ""

        for link in links:
            text = scrape_page(link)
            combined_text += text

        summary = summarize(combined_text,query)

    # Show AI response
    with st.chat_message("assistant"):
        st.write(summary)

        st.markdown("### Sources")
        for link in links:
            st.markdown(f"- {link}")

    st.session_state.messages.append({"role": "assistant", "content": summary})