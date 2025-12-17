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

Then:
1. A browser window opens at http://localhost:8501
2. Drag and drop your CSV file (or click to upload)
3. View instant results in the browser
4. Download JSON or Markdown reports

Features:
- Drag-and-drop file upload
- Real-time data analysis
- View summary statistics
- Column-by-column breakdown
- Download reports as JSON or Markdown

### Option B: Command-line

#### Interactive Mode (Choose File)

```bash
python -m csv_profiler.cli
# or
csv-profiler
```

Output:
```
Available CSV files:
  1. employees.csv
  2. sample.csv
Select file number: 1

Output format:
  1. json
  2. markdown
  3. both
Select format number: 3

Profiling: data\employees.csv
Loaded 8 rows
Saved: outputs/report.json
Saved: outputs/report.md

============================================================
# CSV Profiling Report
...
```

#### Direct Mode (Specify File)

```bash
# Profile with default format (both)
python -m csv_profiler.cli data/sample.csv

# Profile with JSON only
python -m csv_profiler.cli data/employees.csv --format json
# or
csv-profiler data/employees.csv -f json

# Profile with Markdown only
python -m csv_profiler.cli data/employees.csv --format markdown

# Save to specific directory
python -m csv_profiler.cli data/employees.csv --out-dir reports

# Custom report name
python -m csv_profiler.cli data/employees.csv --report-name employees_2024
```

#### View Results

```bash
# Windows
type outputs\report.md

# Linux/Mac
cat outputs/report.md
```

## Examples

```bash
# Example 1: Interactive selection
python -m csv_profiler.cli
csv-profiler

# Example 2: JSON output only
python -m csv_profiler.cli data/employees.csv --format json
csv-profiler data/employees.csv -f json

# Example 3: Markdown output only
python -m csv_profiler.cli data/employees.csv --format markdown

# Example 4: Custom output folder and name
python -m csv_profiler.cli data/employees.csv --out-dir reports --report-name emp_profile_q4

# Example 5: Web interface (Drag & drop uploads)
python -m streamlit run app.py
```

## Features

- CSV statistical profiling
- Missing values detection
- Type detection
- JSON & Markdown reports
- Interactive web dashboard
- Command-line tool with interactive selection

