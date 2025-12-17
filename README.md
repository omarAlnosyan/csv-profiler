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

```bash
python -m csv_profiler.cli profile data/employees.csv --output outputs
```

View results:
```bash
cat outputs/report.json
cat outputs/report.md
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
