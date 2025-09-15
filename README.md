# Consulting_Website_Analysis
Scrapes a website, extracts text, and generates a consultant-style analysis  using the OpenAI API. Includes a simple widget-based UI for interactive use.


# Website Analysis App

A simple Python app that scrapes a company’s website and generates a **consultant-style analysis** using the OpenAI API.  
Built with `requests`, `BeautifulSoup`, and `ipywidgets`.

---

## 🚀 Features
- Scrapes website text (paragraph tags only).
- Generates a structured analysis (SEO, design, branding) via GPT.
- Interactive widget-based UI for Jupyter Notebooks.
- Example use case: quick business intelligence reports.

---

## 📂 Project Structure
app1.py # main application code
README.md # project documentation

## 🔧 Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/yourusername/website-analysis-app.git
cd website-analysis-app
pip install -r requirements.txt

Dependencies:
openai
requests
beautifulsoup4
ipywidgets
jupyter

Setup:
Before running, set your OpenAI API key:
export OPENAI_API_KEY="your_api_key_here"
