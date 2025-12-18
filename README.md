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

**Make sure you are in the `bootcamp` directory (after cloning):**

```bash
uv venv -p 3.11
.\.venv\Scripts\activate  # Windows
. .venv/bin/activate      # Linux/Mac

pip install -e .
```

## Run

### Option A: Web Interface

```bash
streamlit run app.py
```

### Option B: Command-line

```bash
csv-profiler
```

The CLI will prompt you interactively:
1. **Choose file location**: Select from data/ directory or enter your own custom path
2. **Enter CSV file path**: Paste the full path to your CSV file (with or without quotes)
3. **Select output format**: Choose json, markdown, or both
4. **Choose output location**: Enter the path where you want to save the report

## View Results

After profiling, your report will be saved in the location you specified, or in the `outputs` folder by default.

```bash
# Example: View the report
type outputs\report.json
cat outputs/report.md
```



