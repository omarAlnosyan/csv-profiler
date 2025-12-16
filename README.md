# CSV Profiler CLI

A fast, simple Python tool to profile CSV files and generate data quality reports.

## Quick Start (5 minutes)

### 1. Setup
```bash
cd bootcamp
python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install -e .
```

### 2. Run the Bootcamp CLI

#### Basic Usage
```bash
python -m csv_profiler.cli data/employees.csv
```

#### With Custom Output Directory
```bash
python -m csv_profiler.cli data/employees.csv --out-dir results
```

#### With Custom Report Name
```bash
python -m csv_profiler.cli data/employees.csv --report-name employees_2024
```

#### Full Example with All Options
```bash
python -m csv_profiler.cli data/employees.csv --out-dir reports --report-name emp_profile_20241216
```

#### View Help
```bash
python -m csv_profiler.cli --help
```

### 3. Command Options

```
Arguments:
  input_path                Path to input CSV file (required)

Options:
  --out-dir PATH           Output folder (default: outputs)
  --report-name NAME       Base name for outputs (default: report)
  --help                   Show this help message
```

### 4. Real Examples

Example 1: Basic profiling with date in report name
```bash
python -m csv_profiler.cli data/employees.csv --report-name employees_20241216
```
Output: outputs/employees_20241216.json, outputs/employees_20241216.md

Example 2: Profile to custom folder
```bash
python -m csv_profiler.cli data/employees.csv --out-dir 2024_reports --report-name dec_analysis
```
Output: 2024_reports/dec_analysis.json, 2024_reports/dec_analysis.md

Example 3: Profile multiple files
```bash
python -m csv_profiler.cli data/employees.csv --report-name employees_q4
python -m csv_profiler.cli data/sample.csv --report-name sample_q4
```
Output: outputs/employees_q4.json, outputs/sample_q4.md, outputs/sample_q4.json

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
