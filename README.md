# CSV Profiler

Analyze CSV files in seconds.

## Setup

```bash
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler
cd bootcamp
```

## Installation

```bash
uv venv -p 3.11
.\.venv\Scripts\activate  # Windows
. .venv/bin/activate      # Linux/Mac

pip install -r requirements.txt
pip install -e .
```

## Run

### Command Line
```bash
python -m csv_profiler.cli data/sample.csv
python -m csv_profiler.cli data/employees.csv --output outputs
```

### Streamlit Web App
```bash
streamlit run app.py
```
Opens at: http://localhost:8501

## Features

- CSV statistical profiling
- Missing values detection
- Type detection
- JSON & Markdown reports
- Interactive web dashboard
- Command-line tool

