# CSV Profiler

Analyze CSV files in seconds.

## Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler
cd bootcamp
```

**Note on Directory Structure:**

The repository has a nested structure. After cloning, you may be in:
- `csv-profiler/bootcamp/` (correct - this has the code)
- OR `csv-profiler/bootcamp/bootcamp/` (also correct - alternate structure)

**How to verify you're in the right place:**

Run:
```bash
ls
```

You should see:
- `src/` (folder with csv_profiler code)
- `data/` (folder with sample.csv and employees.csv)
- `app.py`
- `pyproject.toml`
- `requirements.txt`

If you see these files, **STOP** - you're in the right directory!

## Quick Start - Step by Step

### 1. Create a Virtual Environment

```bash
uv venv -p 3.11
```

### 2. Activate the Virtual Environment

**Windows:**
```bash
.\.venv\Scripts\activate
```

**Linux/Mac:**
```bash
. .venv/bin/activate
```

You should see `(bootcamp)` in your terminal prompt.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Package in Development Mode

This is **critical** - it makes the `csv_profiler` module available:

```bash
pip install -e .
```

This installs the package so you can use `python -m csv_profiler.cli` command.

### 5. Run the CLI

To analyze a CSV file:

```bash
python -m csv_profiler.cli data/sample.csv
```

Or with the employees data:

```bash
python -m csv_profiler.cli data/employees.csv
```

To save output to a specific directory:

```bash
python -m csv_profiler.cli data/employees.csv --output outputs
```

### 6. Run the Web App

Start the Streamlit web interface:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Troubleshooting

### Error: "No module named 'csv_profiler'"

**Cause:** The package wasn't installed or `pip install -e .` wasn't run.

**Solution:** Run this command (while in the correct directory):

```bash
pip install -e .
```

Wait for it to complete, then try:
```bash
python -m csv_profiler.cli data/sample.csv
```

### Error: "Cannot find path" or directory not found

**Cause:** You're in the wrong directory.

**Solution:** 
1. Check your current path with `ls` or `Get-Location`
2. You should see `src/`, `data/`, `app.py` listed
3. If not, navigate correctly (may need one more `cd bootcamp`)

### Error: "File does not exist"

**Cause:** The `data/` folder is missing or you're not in the right directory.

**Solution:** Make sure you're in a directory that has a `data/` folder with CSV files.

