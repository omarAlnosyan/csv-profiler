# CSV Profiler 

A professional Python package + Streamlit web app for CSV data profiling and analysis.

## Overview

CSV Profiler helps you analyze CSV files by:
- Detecting data types (string, number, date, etc.)
- Identifying missing values
- Counting unique values per column
- Generating detailed profiling reports (JSON & Markdown)

## Quick Start

### Option 1: Using Streamlit Web Interface (Recommended)

1. Clone and setup:
```bash
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler/bootcamp
```

2. Activate virtual environment:
```bash
# Windows
.venv\Scripts\Activate

# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python -m streamlit run app.py
```

5. Open your browser to: **http://localhost:8501**

**How to use the web app:**
1. Upload a CSV file (drag-drop or click to browse)
2. Click "Generate Report" button
3. View analysis results in markdown format
4. Preview data table
5. Download JSON or Markdown reports
6. View raw JSON statistics (expandable section)

Reports are automatically saved to the `outputs/` folder.

### Option 2: Using Command Line

```bash
cd bootcamp

# Profile a CSV file
python -m csv_profiler.cli profile data/employees.csv --output outputs

# View results
cat outputs/report.json
cat outputs/report.md
```

## Project Structure

```
bootcamp/
├── app.py                     # Streamlit web app (Main interface)
├── src/
│   └── csv_profiler/
│       ├── __init__.py
│       ├── models.py          # ColumnProfile class
│       ├── profile.py         # Profiling logic
│       ├── render.py          # Report generation
│       ├── cli.py             # Command-line interface
│       └── io.py              # File I/O utilities
├── data/
│   ├── employees.csv          # Sample data
│   ├── iris.csv               # Sample data
│   └── sample.csv             # Sample data
├── outputs/                   # Generated reports (auto-created)
└── README.md                  # This file
```

## CLI Reference

### Command: `profile`

**Syntax:**
```bash
python -m csv_profiler.cli profile <INPUT_FILE> [OPTIONS]
```

**Options:**
- `--output`, `-o`: Output directory (default: `outputs/`)
- `--format`, `-f`: Output format: `json`, `markdown`, `both` (default: `both`)

**Examples:**

```bash
# Profile with default settings (saves JSON + Markdown)
python -m csv_profiler.cli profile data/employees.csv

# Custom output directory
python -m csv_profiler.cli profile data/sample.csv -o reports/

# JSON only
python -m csv_profiler.cli profile data/data.csv --format json

# Markdown only
python -m csv_profiler.cli profile data/data.csv -f markdown

# Interactive mode (select file from current directory)
python -m csv_profiler.cli
```

## Input/Output

### Input
- CSV files with headers
- Supports UTF-8 encoding
- Any number of rows and columns

### Output

#### JSON Report Structure
```json
{
  "summary": {
    "rows": 5,
    "columns": 4,
    "column_names": ["name", "age", "script", "salary"]
  },
  "columns": [
    {
      "name": "name",
      "type": "string",
      "total": 5,
      "missing": 0,
      "unique": 5,
      "missing_pct": 0.0
    }
  ]
}
```

#### Markdown Report Format
```markdown
# CSV Profiling Report

## Summary
- Rows: 5
- Columns: 4

## Columns Overview
| Column | Type   | Missing | Unique |
|--------|--------|---------|--------|
| name   | string | 0%      | 5      |
| age    | int    | 20%     | 4      |

## Column Details
### name
Type: string
Total: 5
Missing: 0
Missing %: 0.0%
Unique: 5
```

## Streamlit Web App Features

| Feature | Description |
|---------|-------------|
| File Upload | Drag-and-drop or browse CSV files (up to 200MB) |
| Analysis | Automatic profiling with statistics |
| Markdown Report | Formatted report with tables and details |
| Data Preview | View your data as an interactive table |
| Downloads | Export as JSON or Markdown format |
| JSON Viewer | Expandable raw JSON statistics |
| Auto-Save | Reports automatically saved to outputs/ folder |
| User-Friendly | Step-by-step interface with clear instructions |

## Requirements

```
streamlit>=1.28.0
pandas>=2.0.0
typer>=0.9.0
numpy>=1.24.0
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

## Python Version
- Python 3.9+

## How It Works

### Processing Pipeline

```
CSV File Upload
      |
Parse CSV Data (DictReader)
      |
Generate Profile (basic_profile)
      |
Render Reports (JSON + Markdown)
      |
Display & Download Results
      |
Auto-Save to outputs/ folder
```

### ColumnProfile Model

Each column gets analyzed with:
- **name**: Column header
- **type**: Inferred data type (string, int, float)
- **total**: Row count
- **missing**: Count of empty values
- **unique**: Distinct value count
- **missing_pct**: Missing percentage

## Example Usage

### Sample Data
```csv
name,age,script,salary
Ahmed,28,python,50000
Fatima,,javascript,55000
Hassan,25,,45000
Layla,29,python,
Mohammed,31,python,58000
```

### Report Output
- Total Rows: 5
- Total Columns: 4
- Missing Values:
  - age: 1 missing (20%)
  - script: 1 missing (20%)
  - salary: 1 missing (20%)

## Deployment

### Local Deployment
```bash
python -m streamlit run app.py
```

### Remote Deployment (Streamlit Cloud)
1. Push to GitHub
2. Go to https://share.streamlit.io/
3. Connect your GitHub repository
4. Select `app.py` as the main file

## Code Documentation

Each code block is documented with clear comments explaining:
- What each section does
- Why it's structured that way
- How to modify it

Example:
```python
# ============================================================================
# File Upload Section
# ============================================================================
st.markdown("### Step 1: Upload Your CSV File")
uploaded_file = st.file_uploader(...)  # User selects CSV file
```

## Contributing

Feel free to:
- Report issues
- Suggest features
- Submit pull requests

## License

MIT License

## Author

Created for SDAIA Bootcamp - Week 3 Day 5

---

For questions or issues, check the GitHub repository: https://github.com/omarAlnosyan/csv-profiler
