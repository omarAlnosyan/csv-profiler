def get_columns(rows: list[dict[str, str]]) -> list[str]:
    if  rows:
         return list(rows[0].keys())
    return [] 

