# Tercet Generator

An intelligent system for generating tercets (three-line poems) using both rule-based and LLM-based approaches.

## Project Structure
```
tercet-generator/
├── app/
│   ├── __init__.py        # Flask app initialization
│   ├── api.py             # API endpoints
│   ├── models/            # Generator models
│   │   ├── __init__.py
│   │   ├── rule_based.py  # Rule-based generation
│   │   └── llm_based.py   # LLM-based generation
│   ├── static/            # Frontend static files
│   │   ├── main.js
│   │   └── styles.css
│   └── templates/         # Frontend templates
│       └── index.html
├── data/                  # Data files
│   ├── poetry_kb/         # Knowledge base
│   │   ├── adjectives.txt
│   │   ├── nouns.txt
│   │   ├── verbs.txt
│   │   └── adverbs.txt
│   └── templates/         # Tercet templates
│       └── basic_templates.txt
├── run.py                 # Application entry point
├── requirements.txt       # Python dependencies
└── README.md
```

## Features
- Dual-approach tercet generation:
  - Rule-based generation using poetry templates and knowledge base
  - LLM-based generation using state-of-the-art language models
- RESTful API endpoints for tercet generation
- Clean and intuitive web interface

## Installation
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the Flask server:
   ```bash
   python run.py
   ```
2. Visit `http://localhost:5000` in your web browser

## Development
- `app/models/rule_based.py`: Contains rule-based generation logic
- `app/models/llm_based.py`: Contains LLM-based generation using transformers
- `app/api.py`: Flask API endpoints for serving tercet generation
- `app/static/` and `app/templates/`: Frontend files
