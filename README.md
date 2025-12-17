# CSV Profiler

Analyze CSV files in seconds.

## Clone the Repository

```bash
git clone https://github.com/omarAlnosyan/csv-profiler.git
cd csv-profiler
cd bootcamp
```

## Quick Start

1. **Navigate to the bootcamp directory:**
   ```bash
   cd bootcamp
   ```

2. **Create virtual environment:**
   ```bash
   uv venv -p 3.11
   ```

3. **Activate it:**
   ```bash
   .\.venv\Scripts\activate
   ```
   (Linux/Mac: `. .venv/bin/activate`)

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install the package in development mode:**
   ```bash
   pip install -e .
   ```

6. **Run CLI:**
   ```bash
   python -m csv_profiler.cli data/sample.csv
   ```

7. **Run Web App:**
   ```bash
   streamlit run app.py
   ```

