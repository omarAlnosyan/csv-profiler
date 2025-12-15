from __future__ import annotations
import json
from pathlib import Path

def write_json(report: dict, path: str | Path, *args, **kwargs) -> None:
    """Write report to JSON file with pretty printing."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    indent = kwargs.get('indent', 2)
    ensure_ascii = kwargs.get('ensure_ascii', False)
    path.write_text(json.dumps(report, indent=indent, ensure_ascii=ensure_ascii) + "\n")

def md_header(source: str = "CSV Report") -> list[str]:
    """Generate markdown header."""
    return [f"# {source}\n"]

def md_table_header() -> list[str]:
    """Generate markdown table header."""
    return [
        "| Column | Type | Missing | Unique |",
        "|--------|------|---------|--------|"
    ]

def write_markdown(report: dict, path: str | Path, *args, **kwargs) -> None:
    """Write comprehensive markdown report."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    summary = report.get("summary", {})
    rows = summary.get("rows", 0)
    
    lines: list[str] = []
    
    # Header
    lines.extend(md_header("CSV Profiling Report"))
    
    # Summary section
    lines.append("## Summary\n")
    lines.append(f"- **Rows:** {rows:,}")
    lines.append(f"- **Columns:** {summary.get('columns', 0):,}\n")
    
    # Columns table
    lines.append("## Columns Overview\n")
    lines.extend(md_table_header())
    
    for col_name, col_report in report.get("columns", {}).items():
        col_type = col_report.get("type", "unknown")
        missing = col_report.get("missing", 0)
        missing_pct = (missing / rows * 100) if rows > 0 else 0
        unique = col_report.get("unique", 0)
        
        lines.append(f"| {col_name} | {col_type} | {missing_pct:.1f}% | {unique} |")
    
    lines.append("")
    
    # Per-column details
    lines.append("## Column Details\n")
    
    for col_name, col_report in report.get("columns", {}).items():
        lines.append(f"### {col_name}")
        lines.append(f"**Type:** {col_report.get('type', 'unknown')}")
        lines.append(f"**Count:** {col_report.get('count', 0)}")
        lines.append(f"**Missing:** {col_report.get('missing', 0)}")
        lines.append(f"**Unique:** {col_report.get('unique', 0)}")
        
        if col_report.get("type") == "number":
            lines.append(f"**Min:** {col_report.get('min', 'N/A')}")
            lines.append(f"**Max:** {col_report.get('max', 'N/A')}")
            lines.append(f"**Mean:** {col_report.get('mean', 0):.2f}")
        else:
            lines.append("**Top Values:**")
            for item in col_report.get("top", []):
                lines.append(f"- {item['value']}: {item['count']}")
        
        lines.append("")
    
    path.write_text("\n".join(lines) + "\n")

