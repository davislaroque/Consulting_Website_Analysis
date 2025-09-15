# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
"""
Website Analysis App
---------------------
Scrapes a website, extracts text, and generates a consultant-style analysis 
using the OpenAI API. Includes a simple widget-based UI for interactive use.
"""

import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import ipywidgets as widgets
from IPython.display import display, clear_output


# --- Setup API Key ---
# Make sure to set your OpenAI API key in the environment before running:
# export OPENAI_API_KEY="your_key_here"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# --- Scraper Function ---
def scrape_website(url: str, max_chars: int = 2000) -> str:
    """Scrape text content from a website (paragraph tags only)."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join([p.get_text() for p in soup.find_all("p")])
        return text[:max_chars] if text else "No text found on the page."
    except Exception as e:
        return f"Error scraping site: {e}"


# --- GPT Analysis Function ---
def analyze_company(url: str, notes: str) -> str:
    """Generate a structured analysis of a company website using GPT."""
    site_text = scrape_website(url)
    messages = [
        {"role": "system", "content": "You are a professional consultant analyzing a company's website for SEO, design, and branding."},
        {"role": "user", "content": f"Company URL: {url}\nNotes: {notes}\n\nWebsite Extract: {site_text}\n\nTask: Provide a structured consultant-style report."}
    ]
    try:
        response = client.chat.completions.create(
            model="gpt-5",  # update with your available model
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error during GPT analysis: {e}"


# --- UI Components ---
url_input = widgets.Text(
    value="https://example.com",
    description="Website:",
    layout=widgets.Layout(width="600px")
)

notes_input = widgets.Textarea(
    value="Looking for SEO, design, or branding issues.",
    description="Notes:",
    layout=widgets.Layout(width="600px", height="100px")
)

button = widgets.Button(
    description="Generate Report",
    button_style="success",
    layout=widgets.Layout(width="200px")
)

output_area = widgets.Output()


# --- Button Logic ---
def on_button_click(b):
    with output_area:
        clear_output()
        print("🔎 Analyzing website... please wait.\n")
        report = analyze_company(url_input.value, notes_input.value)
        print("📊 Website Report\n")
        print(report)


button.on_click(on_button_click)


# --- Launch App ---
def run_app():
    """Display the widget-based app."""
    display(widgets.VBox([url_input, notes_input, button, output_area]))


if __name__ == "__main__":
    run_app()