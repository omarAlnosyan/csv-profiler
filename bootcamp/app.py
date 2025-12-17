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
# Styled Title with Gradient
# ============================================================================
st.markdown(
    """
    <h1 style="
        background: linear-gradient(to right, #1f77b4, #ff7f0e, #2ca02c);
        -webkit-background-clip: text;
        color: transparent;
        font-size: 3rem;
        text-align: center;
        padding: 1rem 0;
    ">
        CSV Profiler
    </h1>
    """,
    unsafe_allow_html=True
)

# ============================================================================
# Subtitle and Description
# ============================================================================
st.markdown("""
<div style="text-align: center; font-size: 1.1rem; color: #555;">
    <strong>Upload → Analyze → View Results</strong>
    <br>
    Analyze your data quality with automatic profiling that detects missing values, data types, and column statistics.
</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================================================
# File Upload Section
# ============================================================================
st.markdown("### Step 1: Upload Your CSV File")
st.markdown("*Drag and drop or click to select a CSV file*")

uploaded_file = st.file_uploader(
    label="Select CSV file",
    label_visibility="collapsed",
    type=["csv"],
    help="Upload a CSV file to analyze. Supported format: .csv"
)

# Show uploaded file info
if uploaded_file:
    st.info(f"File selected: **{uploaded_file.name}** ({uploaded_file.size} bytes)")

st.divider()

# ============================================================================
# Generate Report Button
# ============================================================================
st.markdown("### Step 2: Generate Report")

if st.button("Generate Report", use_container_width=True, type="primary"):
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
        
        # Generate markdown content
        markdown_content = render_markdown(report)
        st.session_state["markdown_content"] = markdown_content
        
        # Create output directory if it doesn't exist
        output_dir = Path(__file__).parent / "outputs"
        output_dir.mkdir(exist_ok=True)
        
        # Save JSON report to outputs folder
        json_filename = f"{uploaded_file.name.replace('.csv', '')}_report.json"
        json_filepath = output_dir / json_filename
        with open(json_filepath, "w") as f:
            json.dump(report, f, indent=2)
        
        # Save Markdown report to outputs folder
        md_filename = f"{uploaded_file.name.replace('.csv', '')}_report.md"
        md_filepath = output_dir / md_filename
        with open(md_filepath, "w") as f:
            f.write(markdown_content)
        
        # Show success message
        st.success("Report generated successfully!")

st.divider()

# ============================================================================
# Display Results (only if report was generated)
# ============================================================================
if "report_data" in st.session_state:
    st.markdown("### Step 3: Analysis Results")
    
    # Show markdown report with formatted output
    if "report" in st.session_state:
        markdown_content = st.session_state.get("markdown_content", render_markdown(st.session_state["report"]))
        st.markdown(markdown_content)
    
    st.divider()
    
    # Display the uploaded data as a table
    st.markdown("### Data Preview")
    import pandas as pd
    df = pd.DataFrame(st.session_state["report_data"])
    st.dataframe(df, use_container_width=True)
    
    st.divider()
    
    # Download Report Section
    st.markdown("### Export Reports")
    
    col1, col2 = st.columns(2)
    
    with col1:
        json_str = json.dumps(st.session_state["report"], indent=2)
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name=f"{st.session_state['filename'].replace('.csv', '')}_report.json",
            mime="application/json",
            use_container_width=True
        )
    
    with col2:
        markdown_content = st.session_state.get("markdown_content", render_markdown(st.session_state["report"]))
        st.download_button(
            label="Download Markdown",
            data=markdown_content,
            file_name=f"{st.session_state['filename'].replace('.csv', '')}_report.md",
            mime="text/markdown",
            use_container_width=True
        )
    
    st.divider()
    
    # Expandable JSON Preview
    with st.expander("View JSON (Click to expand)", expanded=False):
        st.json(st.session_state["report"])


