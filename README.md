# CSV Profiler

Analyze CSV files in seconds.

Two ways to use it: **Web Interface** or **Command-line**.

## Setup

```bash
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler
cd bootcamp
cd bootcamp
```

## Installation

```bash
uv venv -p 3.11
.\.venv\Scripts\activate  # Windows
. .venv/bin/activate      # Linux/Mac

pip install -e .
```

## Run

### Option A: Web Interface

```bash
streamlit run app.py
```

### Option B: Command-line

```bash
csv-profiler
```

## View Results

```bash
# Windows - Markdown
type outputs\report.md

# Windows - JSON
type outputs\report.json

# Linux/Mac - Markdown
cat outputs/report.md

# Linux/Mac - JSON
cat outputs/report.json
```



