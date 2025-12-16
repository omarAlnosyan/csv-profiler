import streamlit as st
import json
from pathlib import Path
from io import StringIO
from src.csv_profiler.io import read_csv_rows
from src.csv_profiler.profile import basic_profile
from src.csv_profiler.render import write_json, write_markdown

st.set_page_config(page_title="CSV Profiler", layout="wide")

st.title("CSV Profiler")
st.markdown("Drag and drop or upload a CSV file to analyze its data quality")

# File upload section
col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader(
        "Upload CSV file",
        type=["csv"],
        label_visibility="collapsed"
    )

if uploaded_file is not None:
    st.success(f"File uploaded: {uploaded_file.name}")
    
    # Read file
    try:
        stringio = StringIO(uploaded_file.getvalue().decode("utf8"))
        rows = []
        
        # Parse CSV manually to get list of dicts
        import csv
        reader = csv.DictReader(stringio)
        rows = list(reader)
        
        if not rows:
            st.error("No data found in file")
        else:
            st.info(f"Loaded {len(rows)} rows with {len(rows[0])} columns")
            
            # Generate profile
            with st.spinner("Analyzing data..."):
                report = basic_profile(rows)
            
            # Display Summary
            st.header("Summary")
            col1, col2, col3 = st.columns(3)
            
            summary = report.get("summary", {})
            with col1:
                st.metric("Rows", summary.get("rows", 0))
            with col2:
                st.metric("Columns", summary.get("columns", 0))
            with col3:
                col_names = summary.get("column_names", [])
                st.text(f"Column Names:\n{', '.join(col_names)}")
            
            # Display Columns Overview
            st.header("Columns Overview")
            
            columns_data = report.get("columns", [])
            
            if columns_data:
                table_data = []
                for col in columns_data:
                    table_data.append({
                        "Column": col.get("name", ""),
                        "Type": col.get("type", ""),
                        "Missing": col.get("missing", 0),
                        "Missing %": f"{col.get('missing_pct', 0):.1f}%",
                        "Unique": col.get("unique", 0),
                        "Total": col.get("total", 0)
                    })
                
                st.dataframe(table_data, use_container_width=True)
            
            # Download buttons
            st.header("Download Reports")
            
            col1, col2 = st.columns(2)
            
            # JSON download
            with col1:
                json_str = json.dumps(report, indent=2)
                st.download_button(
                    label="Download JSON Report",
                    data=json_str,
                    file_name=f"{uploaded_file.name.replace('.csv', '')}_report.json",
                    mime="application/json"
                )
            
            # Markdown download
            with col2:
                md_content = generate_markdown_report(report, uploaded_file.name)
                st.download_button(
                    label="Download Markdown Report",
                    data=md_content,
                    file_name=f"{uploaded_file.name.replace('.csv', '')}_report.md",
                    mime="text/markdown"
                )
            
            # Display Markdown Preview
            st.header("Markdown Preview")
            st.markdown(md_content)
    
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")

else:
    st.info("Upload a CSV file to get started")

def generate_markdown_report(report: dict, filename: str) -> str:
    """Generate markdown report from profile data."""
    lines = []
    
    lines.append(f"# CSV Profile: {filename}\n")
    
    summary = report.get("summary", {})
    lines.append("## Summary\n")
    lines.append(f"- **Rows:** {summary.get('rows', 0):,}")
    lines.append(f"- **Columns:** {summary.get('columns', 0):,}\n")
    
    lines.append("## Columns Overview\n")
    lines.append("| Column | Type | Missing | Missing % | Unique |")
    lines.append("|--------|------|---------|-----------|--------|")
    
    for col in report.get("columns", []):
        col_name = col.get("name", "")
        col_type = col.get("type", "")
        missing = col.get("missing", 0)
        missing_pct = col.get("missing_pct", 0)
        unique = col.get("unique", 0)
        
        lines.append(f"| {col_name} | {col_type} | {missing} | {missing_pct:.1f}% | {unique} |")
    
    lines.append("\n## Column Details\n")
    
    for col in report.get("columns", []):
        col_name = col.get("name", "")
        col_type = col.get("type", "")
        
        lines.append(f"### {col_name}")
        lines.append(f"**Type:** {col_type}")
        lines.append(f"**Total:** {col.get('total', 0)}")
        lines.append(f"**Missing:** {col.get('missing', 0)}")
        lines.append(f"**Unique:** {col.get('unique', 0)}")
        lines.append("")
    
    return "\n".join(lines)
