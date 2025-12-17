# CSV Profiler

Analyze CSV files in seconds.

Two ways to use it: **Web Interface** or **Command-line**.

## Setup

```bash
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler
cd bootcamp
```

## Installation

```bash
uv venv -p 3.11
.\.venv\Scripts\activate  # Windows
. .venv/bin/activate      # Linux/Mac

pip install -r requirements.txt
pip install -e .
```

## Run

### Option A: Web Interface (Recommended - Easiest)

```bash
python -m streamlit run app.py
```

Then:
1. A browser window opens at http://localhost:8501
2. Drag and drop your CSV file (or click to upload)
3. View instant results in the browser
4. Download JSON or Markdown reports

Features:
- Drag-and-drop file upload
- Real-time data analysis
- View summary statistics
- Column-by-column breakdown
- Download reports as JSON or Markdown

### Option B: Command-line

#### Interactive Mode (Choose File)

```bash
csv-profiler
```




#### View Results

```bash
# Windows
type outputs\report.md

# Linux/Mac
cat outputs/report.md
```



