# Bootcamp CSV Profiler

A Python tool for profiling and analyzing CSV files with comprehensive data quality reports.

## Features

- CSV file analysis and profiling
- Data quality assessment
- Statistical summaries
- Report generation
- Command-line interface

## Installation

### Prerequisites
- Python 3.11+
- UV (package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/bootcamp.git
cd bootcamp
```

2. Activate the virtual environment:
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

3. Install dependencies:
```bash
uv pip install -e .
# or
pip install -e .
```

## Project Structure

```
bootcamp/
├── .venv/                    # Virtual environment
├── src/
│   └── csv_profiler/         # Main package
│       ├── __init__.py
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
