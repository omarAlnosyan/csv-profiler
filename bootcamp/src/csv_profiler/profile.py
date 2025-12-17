from __future__ import annotations

from .models import ColumnProfile

MISSING = {"", "na", "n/a", "null", "none", "nan"}

def is_missing(value: str | None) -> bool:
    if value is None:
        return True
    return value.strip().lower() in MISSING

def try_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None

def infer_type(values: list[str]) -> str:
    usable = [v for v in values if not is_missing(v)]
    if not usable:
        return "text"
    for v in usable:
        if try_float(v) is None:
            return "text"
    return "number"

def column_values(rows: list[dict[str, str]], col: str) -> list[str]:
    return [row.get(col, "") for row in rows]

def numeric_stats(values: list[str]) -> dict:
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)

    nums: list[float] = []
    for v in usable:
        x = try_float(v)
        if x is None:
            raise ValueError(f"Non-numeric value found: {v!r}")
        nums.append(x)
    
    count = len(nums)
    unique = len(set(nums))
    return {
        "count": count,
        "missing": missing,
        "unique": unique,
        "min": min(nums),
        "max": max(nums),
        "mean": sum(nums) / count if count > 0 else 0
    }

def text_stats(values: list[str], top_k: int = 5) -> dict:
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)
    
    counts: dict[str, int] = {}
    for v in usable:
        counts[v] = counts.get(v, 0) + 1

    top_items = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    top = [{"value": v, "count": c} for v, c in top_items[:top_k]]
    
    return {
        "count": len(usable),
        "missing": missing,
        "unique": len(counts),
        "top": top
    }

def get_columns(rows: list[dict[str, str]]) -> list[str]:
    return list(rows[0].keys()) if rows else []

def basic_profile(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"summary": {"rows": 0, "columns": 0}, "columns": {}}
    
    cols = get_columns(rows)
    column_profiles: list[ColumnProfile] = []
    
    for col in cols:
        values = column_values(rows, col)
        typ = infer_type(values)
        
        if typ == "number":
            stats = numeric_stats(values)
        else:
            stats = text_stats(values)
        
        # Create ColumnProfile instance
        profile = ColumnProfile(
            name=col,
            inferred_type=typ,
            total=len(rows),
            missing=stats["missing"],
            unique=stats["unique"]
        )
        column_profiles.append(profile)
    
    # Convert to dict for JSON export
    report = {
        "summary": {
            "rows": len(rows),
            "columns": len(cols),
            "column_names": cols,
        },
        "columns": [c.to_dict() for c in column_profiles]
    }
    
    return report
