# AI Research Assistant

An AI-powered research tool that searches the web, extracts information from articles, and generates clear explanations using **Google Gemini AI**. The application provides a chat-style interface where users can ask questions and receive summarized research results along with source links.

---

## Overview

The **AI Research Assistant** automates the process of researching topics online. It performs web searches, scrapes relevant article content, and uses a large language model to produce a concise explanation of the topic.

The goal of this project is to demonstrate how **AI, web scraping, and information retrieval** can be combined to build an intelligent research assistant.

---

## Features

* Web search integration using DuckDuckGo
* Automatic article scraping from multiple sources
* AI-powered summaries using Gemini
* Chat-style research interface built with Streamlit
* Source links displayed with each answer
* Environment variable support for secure API key handling

---

## Technologies Used

* **Python**
* **Streamlit** – Web interface
* **Google Gemini API** – AI text generation
* **BeautifulSoup** – Web scraping
* **Requests** – Fetching web pages
* **DuckDuckGo Search** – Web search integration
* **python-dotenv** – Environment variable management

---

## Project Structure

```
ai-research-assistant
│
├── app.py
├── search.py
├── scraper.py
├── summarizer.py
├── requirements.txt
├── README.md
└── .gitignore
```

**File Descriptions**

* `app.py` – Main Streamlit application interface
* `search.py` – Handles web search queries
* `scraper.py` – Extracts text content from webpages
* `summarizer.py` – Sends research data to Gemini for summarization

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/blackangel444/ai-research-assistant-small-scale-.git
```

### 2. Navigate to the project folder

```
cd ai-research-assistant-small-scale-
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Create a `.env` file

Inside the project folder create a file named `.env` and add:

```
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Application

Start the Streamlit app:

```
streamlit run app.py
```

Your browser will open automatically with the application interface.

---

## Example Questions

You can test the assistant with questions such as:

* What is quantum computing?
* Explain artificial intelligence in simple terms.
* What are the applications of machine learning?
* How does photosynthesis work?

---

## How It Works

1. The user asks a question in the interface.
2. The system searches the web for relevant articles.
3. Article text is extracted using web scraping.
4. The combined research content is sent to Gemini AI.
5. Gemini generates a clear explanation.
6. The final answer and source links are displayed.

---

## Security Note

The `.env` file containing your API key is excluded from version control using `.gitignore`. Never commit API keys to public repositories.

---

## Author

**Suyash Gawde**
