# CSV Profiler

Analyze CSV files in seconds.

Two ways to use it: **Web Interface** or **Command-line**.

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

### Option A: Web Interface (Recommended - Easiest)

```bash
python -m streamlit run app.py
```


### Option B: Command-line

#### Interactive Mode (Choose File)

```bash
csv-profiler
```

#### View Results

```bash
# Windows
type outputs\report.md

# Linux/Mac
cat outputs/report.md
```



