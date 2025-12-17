# CSV Profiler

Analyze CSV files in seconds.

## Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler
cd bootcamp
cd bootcamp
```

**IMPORTANT:** The repository has a nested `bootcamp/bootcamp` structure. 

Your final path should end with: `...\csv-profiler\bootcamp\bootcamp\`

To verify you're in the right place, run:
```bash
ls
```

You should see these files/folders:
- `src/` (folder with csv_profiler code)
- `data/` (folder with sample.csv and employees.csv)
- `app.py`
- `pyproject.toml`
- `requirements.txt`

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

**This means you're in the WRONG directory!**

Check your current path - it should end with `\bootcamp\bootcamp\` with **two** `bootcamp` folders.

**Solution:** 
1. Run `pwd` or check the path in your terminal
2. If you see `\bootcamp\` with only ONE bootcamp at the end, you need to run:
   ```bash
   cd bootcamp
   ```
3. Verify with: `ls` - you should see `src/`, `data/`, `app.py`, etc.

Then try again:
```bash
python -m csv_profiler.cli data/sample.csv
```

### Error: "File does not exist"

**Solution:** Make sure you're in the correct nested `bootcamp/bootcamp` directory with the `data/` folder. Run:
```bash
ls
```

You should see `data/` folder listed.

