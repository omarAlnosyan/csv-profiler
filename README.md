# CSV Profiler

Analyze CSV files in seconds. Automatically detect data types, missing values, and generate reports.

## Setup (1 minute)

```bash
# Clone repository
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler/bootcamp

# Activate virtual environment
.venv\Scripts\Activate          # Windows
source .venv/bin/activate       # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

## Usage Options

### Option 1: Web Interface (Recommended)

```bash
python -m streamlit run app.py
```

Then open: **http://localhost:8501**

**Steps:**
1. Upload CSV file
2. Click "Generate Report"
3. View results and download

Reports auto-save to `outputs/` folder.

---

### Option 2: Command Line

#### Interactive Mode (Recommended)

**Step 1: Start the CLI without file argument**
```bash
python -m csv_profiler.cli profile
```

**Step 2: Select CSV file from list**
```
Available CSV files:
  1. employees.csv
  2. sample.csv

Select file number: 1
```
(Enter `1` or `2`)

**Step 3: Choose output format**
```bash
--format json          # JSON only
--format markdown      # Markdown only  
--format both          # Both (default)
```

**Example - Interactive Workflow:**
```bash
python -m csv_profiler.cli profile
# Select file: 1
# Generates: outputs/report.json + outputs/report.md
```

---

#### Direct Mode (Specify everything in one command)

**Select data file + Choose format:**

```bash
python -m csv_profiler.cli profile data/employees.csv --format json
```

**Available CSV Files:**
- `data/employees.csv`
- `data/sample.csv`

**Output Format Options:**
- `--format json` → JSON only
- `--format markdown` → Markdown only
- `--format both` → Both files (default)

**Examples:**

```bash
# JSON only
python -m csv_profiler.cli profile data/employees.csv --format json

# Markdown only
python -m csv_profiler.cli profile data/sample.csv --format markdown

# Both formats (default)
python -m csv_profiler.cli profile data/sample.csv --format both

# Custom output folder
python -m csv_profiler.cli profile data/employees.csv --out-dir my_reports --format both
```

---

#### View Generated Reports

**View Markdown (Human-Readable):**
```bash
# Windows
type outputs\report.md

# macOS/Linux
cat outputs/report.md
```

**View JSON (Raw Data):**
```bash
# Windows
type outputs\report.json

# macOS/Linux
cat outputs/report.json
```

## What It Does

- Detects data types (string, number, etc.)
- Finds missing values and percentages
- Counts unique values per column
- Generates JSON and Markdown reports

## Requirements

- Python 3.9+
- Dependencies: streamlit, pandas, typer, numpy

## License

MIT
