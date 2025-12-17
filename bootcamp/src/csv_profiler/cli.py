import typer
from pathlib import Path
from csv_profiler.io import read_csv_rows
from csv_profiler.profile import basic_profile
from csv_profiler.render import write_json, write_markdown

app = typer.Typer()

def get_available_files() -> list[Path]:
    """Get all CSV files in the data directory."""
    data_dir = Path("data")
    if not data_dir.exists():
        return []
    return sorted(data_dir.glob("*.csv"))

def choose_file() -> Path:
    """Interactive file selection."""
    files = get_available_files()
    
    if not files:
        typer.secho("Error: No CSV files found in data/ directory", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    
    typer.echo("\nAvailable CSV files:")
    for i, file in enumerate(files, 1):
        typer.echo(f"  {i}. {file.name}")
    
    while True:
        try:
            choice = typer.prompt("Select file number")
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                return files[idx]
            else:
                typer.secho("Invalid selection. Try again.", fg=typer.colors.RED)
        except ValueError:
            typer.secho("Invalid input. Enter a number.", fg=typer.colors.RED)

def choose_format() -> str:
    """Interactive format selection."""
    formats = ["json", "markdown", "both"]
    
    typer.echo("\nOutput format:")
    for i, fmt in enumerate(formats, 1):
        typer.echo(f"  {i}. {fmt}")
    
    while True:
        try:
            choice = typer.prompt("Select format number")
            idx = int(choice) - 1
            if 0 <= idx < len(formats):
                return formats[idx]
            else:
                typer.secho("Invalid selection. Try again.", fg=typer.colors.RED)
        except ValueError:
            typer.secho("Invalid input. Enter a number.", fg=typer.colors.RED)
@app.command()def profile(
    input_path: Path = typer.Argument(None, help="Input CSV file (optional - choose interactively if omitted)"),
    out_dir: Path = typer.Option(Path("outputs"), "--out-dir", help="Output folder"),
    report_name: str = typer.Option("report", "--report-name", help="Base name for outputs"),
    format: str = typer.Option(None, "--format", "-f", help="Output format: json, markdown, or both (optional - choose interactively if omitted)"),
):
    """Profile a CSV file and generate data quality reports."""
    
    try:
        # If no input file provided, prompt user to choose
        if input_path is None:
            input_path = choose_file()
        
        # If no format provided, prompt user to choose
        if format is None:
            format = choose_format()
        
        # Validate input file exists
        if not input_path.exists():
            typer.secho(f"Error: File not found: {input_path}", fg=typer.colors.RED)
            raise typer.BadParameter(f"Input file does not exist: {input_path}")
        
        typer.secho(f"\nProfiling: {input_path}", fg=typer.colors.BLUE)
        
        rows = read_csv_rows(input_path)
        if not rows:
            typer.secho("Error: No data found in file", fg=typer.colors.RED)
            raise typer.Exit(code=1)
        
        typer.secho(f"Loaded {len(rows)} rows", fg=typer.colors.GREEN)
        
        report = basic_profile(rows)
        
        out_dir.mkdir(parents=True, exist_ok=True)
        
        if format in ["json", "both"]:
            json_file = out_dir / f"{report_name}.json"
            write_json(report, json_file)
            typer.secho(f"Saved: {json_file}", fg=typer.colors.GREEN)
        
        if format in ["markdown", "both"]:
            md_file = out_dir / f"{report_name}.md"
            write_markdown(report, md_file)
            typer.secho(f"Saved: {md_file}", fg=typer.colors.GREEN)
            
            with open(md_file) as f:
                typer.echo("\n" + "="*60)
                typer.echo(f.read())
    
    except typer.BadParameter:
        raise
    except FileNotFoundError as e:
        typer.secho(f"Error: File not found - {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    except ValueError as e:
        typer.secho(f"Error: Invalid data - {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.secho(f"Error: {type(e).__name__}: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
