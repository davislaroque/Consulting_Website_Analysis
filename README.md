# Website Analysis with the OpenAI API

A Python tool that reads a company's website and turns the extracted evidence into a structured consulting report. I built it to connect web data collection with an LLM workflow and a simple interface for exploring business positioning.

**Python · OpenAI API · BeautifulSoup · prompt design · evidence grounding · input validation**

## How it works

1. Fetch one HTML page with timeouts and a download-size limit.
2. Extract its title, meta description, headings, and paragraph text.
3. Build a bounded prompt that separates source evidence from instructions.
4. Ask the model for observations, prioritized recommendations, and limitations.
5. Display or save the Markdown report.

The workflow is inspectable: `--preview` shows exactly what would be sent to the model. Page text is treated as untrusted input, and the prompt restricts claims to available evidence. It cannot infer visual design, page speed, rankings, or traffic from paragraph text.

## Run the offline preview

Requires Python 3.11 or 3.12.

```bash
git clone https://github.com/davislaroque/Consulting_Website_Analysis.git
cd Consulting_Website_Analysis
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app1.py --sample
python -m pytest -q
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

The local [fictional company page](examples/sample_site.html) demonstrates extraction and prompt construction. This is an input preview, not a model-generated report, and it makes no external requests.

## Generate a report

Set `OPENAI_API_KEY` in your shell. `.env.example` documents the variables; this application does not automatically load `.env` files.

```bash
export OPENAI_API_KEY="YOUR_KEY"
export OPENAI_MODEL="gpt-5"
python app1.py --url https://example.com --preview
python app1.py --url https://example.com --notes "Assess the clarity of the offering" --output reports/example.md
```

Use `--model` to select a model available to your account. Generating a report sends the extracted website content and notes to the OpenAI API and uses your API quota.

For the original Jupyter interface:

```python
from app1 import run_app
run_app()
```

## Code and checks

- [app1.py](app1.py): reusable extraction, request, prompt, analysis, CLI, and notebook UI functions.
- [tests/test_analysis.py](tests/test_analysis.py): extraction limits, empty pages, failed fetches, and a mocked model call. Tests need no credentials.
- API client creation is lazy, so importing helpers does not require a key or launch UI.
- Website failures stop the workflow before model generation; failed requests are not treated as source material.

## Scope

This is a single-page, text-based analysis prototype. It does not crawl a whole site, execute JavaScript, use visual screenshots, or autonomously take actions. Reports need human review. The next useful additions are structured output validation and a small evaluation set measuring whether observations are supported by the supplied page.
