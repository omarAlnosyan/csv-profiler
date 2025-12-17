# CSV Profiler - Week 3 Day 5

A professional Python package + Streamlit web app for CSV data profiling and analysis.

## 📋 Overview

**CSV Profiler** helps you analyze CSV files by:
- ✅ Detecting data types (string, number, date, etc.)
- ✅ Identifying missing values
- ✅ Counting unique values per column
- ✅ Generating detailed profiling reports (JSON & Markdown)

## 🚀 Quick Start

### Option 1: Using Streamlit Web Interface (Recommended)

```bash
# Clone the repository
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler/bootcamp

# Activate virtual environment
.venv\Scripts\Activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
python -m streamlit run csv_upload_app.py
```

**Access the app:** Open `http://localhost:8501` in your browser

**How to use:**
1. Click "Upload File" and select your CSV
2. Click "Generate Report" button
3. View the analysis results (markdown format)
4. Download JSON or Markdown report

### Option 2: Using Command Line

```bash
cd bootcamp

# Profile a CSV file
python -m csv_profiler.cli profile data/employees.csv --output outputs

# View results
cat outputs/report.json
cat outputs/report.md
```

## 📁 Project Structure

```
bootcamp/
├── csv_upload_app.py          # Streamlit web app (Main interface)
├── src/
│   └── csv_profiler/
│       ├── __init__.py
│       ├── models.py          # ColumnProfile class
│       ├── profile.py         # Profiling logic
│       ├── render.py          # Report generation
│       ├── cli.py             # Command-line interface
│       └── io.py              # File I/O utilities
├── data/
│   └── employees.csv          # Sample data
└── outputs/                   # Generated reports
```

## 🔧 CLI Reference

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

## 📊 Input/Output

### Input
- **CSV files** with headers
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
- **Rows:** 5
- **Columns:** 4

## Columns Overview
| Column | Type   | Missing | Unique |
|--------|--------|---------|--------|
| name   | string | 0%      | 5      |
| age    | int    | 20%     | 4      |

## Column Details
### name
**Type:** string
**Total:** 5
**Missing:** 0
**Missing %:** 0.0%
**Unique:** 5
```

## 🎨 Streamlit App Features

| Feature | Description |
|---------|-------------|
| 📁 File Upload | Drag-and-drop or browse CSV files |
| 🔍 Analysis | Automatic profiling with statistics |
| 📄 Markdown View | Formatted report with tables |
| 💾 Downloads | Export as JSON or Markdown |
| 💬 User-Friendly | Step-by-step interface |

## 📦 Requirements

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

## 🐍 Python Version
- Python 3.9+

## 📝 Code Documentation

Each code block is documented with clear comments explaining:
- What each section does
- Why it's structured that way
- How to modify it

Example:
```python
# ============================================================================
# File Upload Section
# ============================================================================
st.subheader("Step 1: Upload File")
uploaded_file = st.file_uploader(...)  # User selects CSV file
```

## 🔄 How It Works

### Processing Pipeline

```
CSV File Upload
      ↓
Parse CSV Data (DictReader)
      ↓
Generate Profile (basic_profile)
      ↓
Render Markdown (render_markdown)
      ↓
Display & Download Results
```

### ColumnProfile Model

Each column gets analyzed with:
- **name**: Column header
- **type**: Inferred data type
- **total**: Row count
- **missing**: Count of empty values
- **unique**: Distinct values
- **missing_pct**: Missing percentage

## 💡 Example Usage

### Data
```csv
name,age,script,salary
Ahmed,28,python,50000
Fatima,,javascript,55000
Hassan,25,,45000
Layla,29,python,
Mohammed,31,python,58000
```

### Report Output
- **Total Rows:** 5
- **Total Columns:** 4
- **Missing Values:**
  - age: 1 missing (20%)
  - script: 1 missing (20%)
  - salary: 1 missing (20%)

## 🚀 Deployment

### Local Deployment
```bash
python -m streamlit run csv_upload_app.py
```

### Remote Deployment (Streamlit Cloud)
1. Push to GitHub
2. Go to https://share.streamlit.io/
3. Connect your GitHub repository
4. Select `csv_upload_app.py` as the main file

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Typer CLI Documentation](https://typer.tiangolo.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## 🤝 Contributing

Feel free to:
- Report issues
- Suggest features
- Submit pull requests

## 📄 License

MIT License

## 👨‍💻 Author

Created for SDAIA Bootcamp - Week 3 Day 5

---

**Happy profiling! 📊**
  1. employees.csv
  2. sample.csv
Select file number: 1
```

##### Direct Mode (Specify File)
```bash
python -m csv_profiler.cli data/employees.csv
```

##### With Custom Output Directory
```bash
python -m csv_profiler.cli data/employees.csv --out-dir results
```

##### With Custom Report Name
```bash
python -m csv_profiler.cli data/employees.csv --report-name employees_2024
```

##### Full Example with All Options
```bash
python -m csv_profiler.cli data/employees.csv --out-dir reports --report-name emp_profile_20241216 --format both
```

##### View Help
```bash
python -m csv_profiler.cli --help
```

### 3. Command Options

```
Usage:
  python -m csv_profiler.cli [input_file] [OPTIONS]

Arguments:
  input_file                Path to input CSV file (optional)
                           If omitted, opens interactive file selection

Options:
  --out-dir PATH           Output folder (default: outputs)
  --report-name NAME       Base name for outputs (default: report)
  --format TEXT            Output format: json, markdown, or both (default: both)
  -f, --format TEXT        Short form of --format
  --help                   Show this help message
```

### 4. Real Examples

Example 1: Interactive file selection
```bash
python -m csv_profiler.cli
# Select from available CSV files in data/ folder
```

Example 2: Direct profiling with custom report name and date
```bash
python -m csv_profiler.cli data/employees.csv --report-name employees_20241216
```
Output: outputs/employees_20241216.json, outputs/employees_20241216.md

Example 3: Profile to custom folder with custom name
```bash
python -m csv_profiler.cli data/employees.csv --out-dir 2024_reports --report-name dec_analysis
```
Output: 2024_reports/dec_analysis.json, 2024_reports/dec_analysis.md

Example 4: Generate only JSON output
```bash
python -m csv_profiler.cli data/employees.csv --format json
```
Output: outputs/report.json

Example 5: Generate only Markdown output
```bash
python -m csv_profiler.cli data/employees.csv --format markdown
```
Output: outputs/report.md

Example 6: Use web interface (drag-drop)
```bash
python -m streamlit run app.py
```
Open browser to http://localhost:8501

### 5. View Results

Terminal mode:
Output files in outputs/ folder:
- report.json - Machine-readable data
- report.md - Human-readable report

View report:
```bash
# Windows
type outputs\report.md

# Linux/Mac
cat outputs/report.md
```

Web mode:
Results display instantly in browser with download buttons
Output: outputs/report.json

Example 5: Generate only Markdown output
```bash
python -m csv_profiler.cli data/employees.csv --format markdown
```
Output: outputs/report.md

Example 6: Profile multiple files
```bash
python -m csv_profiler.cli data/employees.csv --report-name employees_q4
python -m csv_profiler.cli data/sample.csv --report-name sample_q4
```
Output: outputs/employees_q4.json, outputs/employees_q4.md, outputs/sample_q4.json, outputs/sample_q4.md

### 5. View Results
Output files are generated in your specified folder:
- report.json - Machine-readable profile
- report.md - Human-readable markdown report

View the markdown report:
```bash
# Windows
type outputs\report.md

# Linux/Mac
cat outputs/report.md
```

## What It Does

- Analyzes CSV data types (text, number)
- Calculates missing values and percentages
- Counts unique values per column
- Computes statistics (min, max, mean for numbers)
- Generates JSON and Markdown reports

## Project Structure

```
bootcamp/
├── src/csv_profiler/
│   ├── cli.py           # Command-line interface
│   ├── models.py        # ColumnProfile class
│   ├── profile.py       # Profiling logic
│   ├── io.py            # CSV reading
│   └── render.py        # Report generation
├── data/
│   └── employees.csv    # Sample dataset
├── pyproject.toml       # Package config
└── README.md
```

## Requirements

- Python 3.11+
- Dependencies: typer, pandas, numpy

## License

MIT
│       ├── io.py             # Input/output operations
│       ├── profile.py        # Profiling logic
│       ├── render.py         # Report rendering
│       └── cli.py            # Command-line interface
├── data/
│   └── sample.csv            # Sample data
├── outputs/                  # Generated reports
├── pyproject.toml            # Project configuration
└── README.md                 # This file
```

## Usage

```bash
# Profile a CSV file
python -m csv_profiler.cli input.csv

# View help
python -m csv_profiler.cli --help
```

## Development

Install in development mode:
```bash
uv pip install -e ".[dev]"
```

## License

MIT
