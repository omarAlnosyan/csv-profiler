# CSV Profiler

Analyze CSV files in seconds.

Two ways to use it: **Web Interface** or **Command-line**.

![CSV Profiler Interface](assets/interface.png)

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

This will launch an interactive prompt where you can:
1. **Choose file location:**
   - Option 1: Select from CSV files in the `data/` directory
   - Option 2: Enter your own CSV file path from anywhere on your local machine

2. **Select output format:**
   - json
   - markdown
   - both

#### Example with Custom File Path

```bash
# Interactive mode (will prompt you to enter file path)
python -m csv_profiler.cli profile

# Direct mode with custom file
python -m csv_profiler.cli profile "C:\Users\YourName\Documents\mydata.csv" -f json

# Direct mode with custom file and custom output
python -m csv_profiler.cli profile "C:\Users\YourName\Documents\mydata.csv" --out-dir custom_outputs --report-name my_report -f both
```

#### Command Options

- `INPUT_PATH` (optional): Path to your CSV file
- `--out-dir` (default: `outputs`): Output directory for reports
- `--report-name` (default: `report`): Base name for output files
- `-f, --format` (optional): Output format (json, markdown, or both)

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



