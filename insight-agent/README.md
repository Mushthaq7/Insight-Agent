# Insight Agent

A modular, agent-powered CLI tool for data analysis and reporting.

## Features

- Plan tasks from questions using AI agents
- Analyze data (CSV/JSON/SQL) with pandas and duckdb
- Generate charts with matplotlib or plotly
- Export insights to PDF (optional)

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the CLI:
   ```bash
   python main.py
   ```

## Project Structure

```
insight-agent/
├── main.py
├── agents/
│   ├── planner.py
│   ├── analyst.py
│   └── reporter.py
├── utils/
│   ├── loader.py
│   ├── visualizer.py
│   └── pdf_generator.py
├── config/
│   └── settings.py
├── data/
│   └── sample_sales.csv
├── output/
│   └── reports/
├── requirements.txt
└── README.md
```
