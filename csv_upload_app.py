"""
CSV Profiler - Streamlit Web Application
=========================================
A user-friendly web app to upload CSV files and generate detailed profiling reports.
"""

import csv
from io import StringIO
import streamlit as st
import sys
from pathlib import Path
import json

# ============================================================================
# Setup: Add src directory to Python path for imports
# ============================================================================
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Import csv_profiler modules for data analysis
from csv_profiler.profile import basic_profile
from csv_profiler.render import render_markdown

# ============================================================================
# Page Configuration
# ============================================================================
st.set_page_config(
    page_title="CSV Profiler",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# Title and Description
# ============================================================================
st.title("CSV Profiler")
st.markdown("""
**Upload a CSV file** → **Generate Report** → **View Analysis**

Analyze your data quality with automatic profiling that detects missing values, 
data types, and column statistics.
""")

st.divider()

# ============================================================================
# File Upload Section
# ============================================================================
st.subheader("Step 1: Upload File")
uploaded_file = st.file_uploader(
    "Drag and drop your CSV file or click to browse",
    type=["csv"],
    help="Upload a CSV file to analyze"
)

# ============================================================================
# Generate Report Button (Always visible)
# ============================================================================
st.subheader("Step 2: Generate Report")
if st.button("Generate Report", use_container_width=True):
    # Validate: Check if file was uploaded
    if uploaded_file is None:
        st.error("Please upload a CSV file first!")
    else:
        # Decode CSV file to text
        text = uploaded_file.getvalue().decode("utf-8-sig")
        
        # Parse CSV into list of dictionaries (each row is a dict)
        rows = list(csv.DictReader(StringIO(text)))
        
        # Analyze CSV: Generate profiling report with statistics
        report = basic_profile(rows)
        
        # Store results in session state (persists across reruns)
        st.session_state["report_data"] = rows
        st.session_state["report"] = report
        st.session_state["filename"] = uploaded_file.name
        
        # Show success message
        st.success("Report generated successfully!")

st.divider()

# ============================================================================
# Display Results (only if report was generated)
# ============================================================================
if "report_data" in st.session_state:
    st.subheader("Step 3: Analysis Results")
    
    # Show markdown report with formatted output
    if "report" in st.session_state:
        markdown_content = render_markdown(st.session_state["report"])
        st.markdown(markdown_content)
    
    # Download Report Section
    st.divider()
    st.subheader("Download Report")
    
    col1, col2 = st.columns(2)
    
    with col1:
        json_str = json.dumps(st.session_state["report"], indent=2)
        st.download_button(
            label="Download JSON Report",
            data=json_str,
            file_name=f"{st.session_state['filename'].replace('.csv', '')}_report.json",
            mime="application/json",
            use_container_width=True
        )
    
    with col2:
        st.download_button(
            label="Download Markdown Report",
            data=markdown_content,
            file_name=f"{st.session_state['filename'].replace('.csv', '')}_report.md",
            mime="text/markdown",
            use_container_width=True
        )
    
    # Expandable JSON Preview
    st.divider()
    with st.expander("View JSON (Click to expand)"):
        st.json(st.session_state["report"])
