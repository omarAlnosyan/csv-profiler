# CSV Profiler

Analyze CSV files in seconds. Detect data types, missing values, and generate reports.

## Setup (1 minute)

```bash
# Clone repository
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler
cd bootcamp
```

Now you're in the bootcamp folder. Continue:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\Activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Done! Now ready to use.

## Usage

### Option 1: Web Interface

```bash
python -m streamlit run app.py
```

This opens the app in your browser automatically. The URL will be displayed in the console (typically `http://localhost:8501`).

To use a different port:
```bash
python -m streamlit run app.py --server.port 8502
```

**Steps:**
1. Upload CSV file
2. Click "Generate Report"
3. Download results (auto-saved to `outputs/` folder)

---

### Option 2: Command Line

**Interactive (Choose file + format):**
```bash
python -m csv_profiler.cli profile
```

Select file number, then choose format:
- `--format json` → JSON only
- `--format markdown` → Markdown only
- `--format both` → Both (default)

**Direct (Specify in one command):**
```bash
python -m csv_profiler.cli profile data/employees.csv --format json
python -m csv_profiler.cli profile data/sample.csv --format markdown
python -m csv_profiler.cli profile data/employees.csv --format both
```

**View results:**
```bash
# Windows
type outputs\report.json
type outputs\report.md

# macOS/Linux
cat outputs/report.json
cat outputs/report.md
```

## License

MIT
