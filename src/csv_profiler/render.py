from __future__ import annotations
import json
from pathlib import Path

def write_json(report: dict, path: str | Path, *args, **kwargs) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    indent = kwargs.get('indent', 2)
    ensure_ascii = kwargs.get('ensure_ascii', False)
    path.write_text(json.dumps(report, indent=indent, ensure_ascii=ensure_ascii) + "\n")

def md_header(source: str = "CSV Report") -> list[str]:
    return [f"# {source}\n"]

def md_table_header() -> list[str]:
    return [
        "| Column | Type | Missing | Unique |",
        "|--------|------|---------|--------|"
    ]

def write_markdown(report: dict, path: str | Path, *args, **kwargs) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    summary = report.get("summary", {})
    rows = summary.get("rows", 0)
    
    lines: list[str] = []
    
    lines.extend(md_header("CSV Profiling Report"))
    
    lines.append("## Summary\n")
    lines.append(f"- **Rows:** {rows:,}")
    lines.append(f"- **Columns:** {summary.get('columns', 0):,}\n")
    
    lines.append("## Columns Overview\n")
    lines.extend(md_table_header())
    
    columns = report.get("columns", [])
    for col_report in columns:
        col_name = col_report.get("name", "unknown")
        col_type = col_report.get("type", "unknown")
        missing_pct = col_report.get("missing_pct", 0)
        unique = col_report.get("unique", 0)
        
        lines.append(f"| {col_name} | {col_type} | {missing_pct:.1f}% | {unique} |")
    
    lines.append("")
    
    lines.append("## Column Details\n")
    
    for col_report in columns:
        col_name = col_report.get("name", "unknown")
        lines.append(f"### {col_name}")
        lines.append(f"**Type:** {col_report.get('type', 'unknown')}")
        lines.append(f"**Total:** {col_report.get('total', 0)}")
        lines.append(f"**Missing:** {col_report.get('missing', 0)}")
        lines.append(f"**Missing %:** {col_report.get('missing_pct', 0):.1f}%")
        lines.append(f"**Unique:** {col_report.get('unique', 0)}")
        
        lines.append("")
    
    path.write_text("\n".join(lines) + "\n")

