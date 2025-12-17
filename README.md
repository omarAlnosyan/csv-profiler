# CSV Profiler

Analyze CSV files in seconds. Detect data types, missing values, and generate reports.

## Installation

### Step 1: Set up a virtual environment

```bash
uv venv -p 3.11
```

### Step 2: Activate it

**Windows (PowerShell):**
```bash
.\.venv\Scripts\activate
```

**Linux / Mac:**
```bash
. .venv/bin/activate
```

## Usage

### CLI

Use this command:

```bash
uv run python -m csv_profiler.cli data/sample.csv
```

### Open Streamlit (GUI)

Command:

```bash
uv run streamlit run app.py
```

