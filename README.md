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
python -m csv_profiler.cli profile
```

#### Reading CSV from Local Machine

You can read CSV files from anywhere on your local machine:

**Interactive Mode (Recommended):**
```bash
python -m csv_profiler.cli profile
```
This will prompt you to:
1. Choose file location (data/ directory or custom path)
2. Enter your CSV file path
3. Select output format (json, markdown, or both)

**Direct Mode with Custom File Path:**
```bash
# Windows example
python -m csv_profiler.cli profile "C:\Users\YourName\Documents\mydata.csv"

# Linux/Mac example
python -m csv_profiler.cli profile "/Users/yourname/Documents/mydata.csv"
```

**With Custom Output Options:**
```bash
python -m csv_profiler.cli profile "C:\path\to\your\file.csv" --out-dir my_outputs --report-name my_report -f json
```

**Command Options:**
- `INPUT_PATH` - Path to your CSV file (optional - interactive if omitted)
- `--out-dir` - Output directory (default: outputs)
- `--report-name` - Report name (default: report)
- `-f, --format` - Format: json, markdown, or both

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



