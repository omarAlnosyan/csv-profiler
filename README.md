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

### 2. Run the Profiler
```bash
# Profile with default settings (outputs to ./outputs/)
python -m csv_profiler.cli data/employees.csv

# Custom output directory and name
python -m csv_profiler.cli data/employees.csv --out-dir my_reports --report-name employees

# View options
python -m csv_profiler.cli --help
```

### 3. View Results
Output files are generated in the `outputs/` folder (or your custom directory):
- `report.json` - Machine-readable profile
- `report.md` - Human-readable markdown report

## What It Does

- ✅ Analyzes CSV data types (text, number)
- ✅ Calculates missing values and percentages
- ✅ Counts unique values per column
- ✅ Computes statistics (min, max, mean for numbers)
- ✅ Generates JSON and Markdown reports

## Usage Examples

```bash
# Basic
python -m csv_profiler.cli data/employees.csv

# Custom output
python -m csv_profiler.cli data/sample.csv --out-dir results --report-name my_data

# View generated reports
cat outputs/report.md
```

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
