MISSING = {"", "na", "n/a", "null", "none", "nan"}

def is_missing(value: str | None) -> bool:
    if value is None:
        return True
    f = value.strip().lower() # or we cn use cassfold for better unicode handling
    return f in MISSING


if __name__ == "__main__":
    result = is_missing(" NA ")
    print(f'is_missing(" NA ") is {result}') 
