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

**Available CSV Files in `data/` folder:**
- `data/employees.csv`
- `data/iris.csv`
- `data/sample.csv`

Or use your own CSV file.

---

#### Basic Usage (Generates both JSON + Markdown)

```bash
python -m csv_profiler.cli profile data/employees.csv --output outputs
```

This creates:
- `outputs/report.json` (machine-readable)
- `outputs/report.md` (human-readable)

---

#### Choose Output Format

**JSON Only:**
```bash
python -m csv_profiler.cli profile data/employees.csv --output outputs --format json
```
Result: `outputs/report.json`

**Markdown Only:**
```bash
python -m csv_profiler.cli profile data/employees.csv --output outputs --format markdown
```
Result: `outputs/report.md`

**Both (Default):**
```bash
python -m csv_profiler.cli profile data/employees.csv --output outputs --format both
```
Result: `outputs/report.json` + `outputs/report.md`

---

#### Custom Output Folder

```bash
python -m csv_profiler.cli profile data/employees.csv --output my_reports
```

---

#### View Generated Reports

**View Markdown Report (Human-Readable):**
```bash
# Windows
type outputs\report.md

# macOS/Linux
cat outputs/report.md
```

**View JSON Report (Raw Data):**
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
