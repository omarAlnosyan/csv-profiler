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

**Note:** The repository has a nested `bootcamp/bootcamp` structure. You need to navigate into both to reach the actual code.

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

**Solution:** Make sure you are:
1. Inside the nested `bootcamp/bootcamp` directory
2. Virtual environment is activated (you see `(bootcamp)` in prompt)
3. You ran `pip install -e .` successfully

### Error: "File does not exist"

**Solution:** Make sure you're in the correct directory with `data/` folder. List files with:
```bash
ls
```

You should see `data/`, `src/`, `app.py`, etc.

