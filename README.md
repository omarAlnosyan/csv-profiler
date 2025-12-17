# CSV Profiler

Analyze CSV files in seconds.

## Prerequisites

Make sure you have:
- Git installed ([Download Git](https://git-scm.com/))
- Python 3.11+ installed ([Download Python](https://www.python.org/))
- `uv` package manager installed (`pip install uv`)

## Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler
cd bootcamp
```

## Step 2: Quick Start (Setup & Run)

1. **Create virtual environment:**
   ```bash
   uv venv -p 3.11
   ```

2. **Activate the virtual environment:**
   
   **Windows:**
   ```bash
   .\.venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   . .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the CLI to analyze a CSV:**
   ```bash
   python -m csv_profiler.cli data/sample.csv
   ```

5. **Run the Web App:**
   ```bash
   streamlit run app.py
   ```

## Step 3: Make Changes & Push to GitHub

1. **Make your changes** to the code

2. **Check what changed:**
   ```bash
   git status
   ```

3. **Stage your changes:**
   ```bash
   git add .
   ```

4. **Commit with a message:**
   ```bash
   git commit -m "Describe your changes here"
   ```

5. **Push to GitHub:**
   ```bash
   git push
   ```

