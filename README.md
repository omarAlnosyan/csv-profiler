# CSV Profiler

**Analyze CSV files in seconds** with this powerful profiling tool that generates detailed statistical reports and visualizations.

---

## ⚡ Quick Start (3 Steps)

### 1️⃣ Clone & Navigate

```bash
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler
cd bootcamp
```

### 2️⃣ Setup Virtual Environment

```bash
uv venv -p 3.11
.\.venv\Scripts\activate  # Windows
. .venv/bin/activate      # Linux/Mac
```

### 3️⃣ Install & Run

```bash
pip install -r requirements.txt
pip install -e .
python -m csv_profiler.cli data/sample.csv
```

✅ **Done!** You should see the profiling report printed to console.

---

## 📋 Complete Setup Guide

### Step 1: Verify Directory

Make sure you're in the correct location by running:

```bash
ls
```

You should see these files:
```
src/                 (csv_profiler code)
data/                (sample.csv, employees.csv)
app.py              
pyproject.toml      
requirements.txt    
```

**If you don't see these, do:** `cd bootcamp` one more time.

### Step 2: Create Virtual Environment

```bash
uv venv -p 3.11
```

This creates a `.venv/` folder with Python 3.11 isolated environment.

### Step 3: Activate Virtual Environment

**Windows (PowerShell):**
```bash
.\.venv\Scripts\activate
```

**Linux/Mac:**
```bash
. .venv/bin/activate
```

You should see `(bootcamp)` in your terminal prompt = ✅ Success!

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs: pandas, numpy, typer, streamlit

### Step 5: Install the Package (CRITICAL)

```bash
pip install -e .
```

This installs the `csv_profiler` package in development mode. **Don't skip this step!**

### Step 6: Run the CLI

```bash
python -m csv_profiler.cli data/sample.csv
```

**Example outputs:**
```bash
# Basic profile
python -m csv_profiler.cli data/sample.csv

# With employees data
python -m csv_profiler.cli data/employees.csv

# Save to specific output directory
python -m csv_profiler.cli data/employees.csv --output outputs
```

### Step 7: Run the Web App (Optional)

```bash
streamlit run app.py
```

Opens interactive web interface at: `http://localhost:8501`

---

## 🆘 Troubleshooting

### ❌ Error: "ModuleNotFoundError: No module named 'csv_profiler'"

**Cause:** Missing `pip install -e .` step

**Solution:**
```bash
# Make sure you're in the correct directory (with app.py, src/, data/)
pip install -e .
python -m csv_profiler.cli data/sample.csv
```

---

### ❌ Error: "Cannot find path 'bootcamp'" or directory not found

**Cause:** Wrong working directory

**Solution:**
1. Check current location: `ls` or `Get-Location`
2. Look for `src/`, `data/`, `app.py` in the output
3. If not found, run: `cd bootcamp`
4. Verify again with: `ls`

---

### ❌ Error: "File does not exist" when running CLI

**Cause:** Running from wrong directory or data folder missing

**Solution:**
1. Verify you're in a directory with `data/` folder
2. Run: `python -m csv_profiler.cli data/sample.csv`
3. Check that `data/sample.csv` exists: `ls data/`

---

### ❌ Error: "No module named 'typer'" or other dependencies

**Cause:** Dependencies not installed properly

**Solution:**
```bash
pip install -r requirements.txt
pip install -e .
```

---

## 📚 Features

✅ **CSV Analysis** - Generates detailed statistical profiles
✅ **Missing Values Detection** - Shows data quality issues
✅ **Type Detection** - Automatically identifies column types
✅ **Report Generation** - JSON & Markdown outputs
✅ **Web Interface** - Interactive Streamlit dashboard
✅ **CLI Tool** - Command-line profiler

---

## 📁 Project Structure

```
csv-profiler/
├── bootcamp/               # Main project directory
│   ├── src/
│   │   └── csv_profiler/  # Python package
│   │       ├── cli.py      # Command-line interface
│   │       ├── profile.py  # Profiling logic
│   │       ├── render.py   # Report rendering
│   │       └── ...
│   ├── data/              # Sample CSV files
│   │   ├── sample.csv
│   │   └── employees.csv
│   ├── app.py             # Streamlit web app
│   ├── pyproject.toml     # Package configuration
│   └── requirements.txt   # Dependencies
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit changes: `git commit -m "Add my feature"`
4. Push: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📝 License

MIT License - See LICENSE file for details

