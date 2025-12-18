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

**Make sure you are in the `bootcamp` directory (after cloning):**

```bash
uv venv -p 3.11
.\.venv\Scripts\activate  # Windows
. .venv/bin/activate      # Linux/Mac

pip install -e .
```

**✅ After installation, verify the CLI works:**
```bash
python -m csv_profiler.cli --help
```

If you get a "ModuleNotFoundError", you're in the wrong directory. Make sure you're in the `csv-profiler/bootcamp` directory (not nested deeper).

## Run

### Option A: Web Interface

```bash
streamlit run app.py
```

### Option B: Command-line

```bash
csv-profiler
```

#### Reading CSV from Local Machine

You can read CSV files from anywhere on your local machine:

**Interactive Mode (Recommended):**
```bash
csv-profiler
```
This will prompt you to:
1. Choose file location (data/ directory or custom path)
2. Enter your CSV file path
3. Select output format (json, markdown, or both)

**Direct Mode with Custom File Path:**
```bash
# Windows example
csv-profiler "C:\Users\YourName\Documents\mydata.csv"

# Linux/Mac example
csv-profiler "/Users/yourname/Documents/mydata.csv"
```

**With Custom Output Options:**
```bash
csv-profiler "C:\path\to\file.csv" --out-dir my_outputs --report-name my_report --format json
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



