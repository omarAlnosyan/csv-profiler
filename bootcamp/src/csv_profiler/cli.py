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
    """Interactive file selection - local or from data directory."""
    files = get_available_files()
    
    typer.echo("\n" + "="*60)
    typer.echo("CSV FILE SELECTION")
    typer.echo("="*60)
    
    # Show options
    typer.echo("\nChoose file location:")
    typer.echo("  1. From data/ directory")
    typer.echo("  2. Custom path on your machine")
    
    while True:
        try:
            location_choice = typer.prompt("Select option (1-2)")
            
            if location_choice == "1":
                if not files:
                    typer.secho("Error: No CSV files found in data/ directory", fg=typer.colors.RED)
                    typer.echo("Try option 2 to specify a custom path.")
                    continue
                
                typer.echo("\nAvailable CSV files in data/ directory:")
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
                break
            
            elif location_choice == "2":
                while True:
                    file_path = typer.prompt("\nEnter the full path to your CSV file").strip()
                    # Remove quotes if user copied path with quotes
                    file_path = file_path.strip('"').strip("'")
                    file_path = Path(file_path)
                    
                    if not file_path.exists():
                        typer.secho(f"Error: File not found at {file_path}", fg=typer.colors.RED)
                        retry = typer.prompt("Try another path? (yes/no)").lower()
                        if retry != "yes" and retry != "y":
                            raise typer.Exit(code=1)
                    elif not file_path.is_file():
                        typer.secho(f"Error: {file_path} is not a file", fg=typer.colors.RED)
                        retry = typer.prompt("Try another path? (yes/no)").lower()
                        if retry != "yes" and retry != "y":
                            raise typer.Exit(code=1)
                    elif not str(file_path).lower().endswith('.csv'):
                        typer.secho("Warning: File does not have .csv extension", fg=typer.colors.YELLOW)
                        confirm = typer.prompt("Continue anyway? (yes/no)").lower()
                        if confirm == "yes" or confirm == "y":
                            return file_path
                    else:
                        return file_path
                break
            else:
                typer.secho("Invalid option. Please enter 1 or 2.", fg=typer.colors.RED)
        except ValueError:
            typer.secho("Invalid input. Enter a number.", fg=typer.colors.RED)

def choose_format() -> str:
    """Interactive format selection."""
    formats = ["json", "markdown", "both"]
    
    typer.echo("\n" + "="*60)
    typer.echo("OUTPUT FORMAT")
    typer.echo("="*60)
    typer.echo("\nSelect output format:")
    for i, fmt in enumerate(formats, 1):
        typer.echo(f"  {i}. {fmt}")
    
    while True:
        try:
            choice = typer.prompt("Select format number (1-3)")
            idx = int(choice) - 1
            if 0 <= idx < len(formats):
                return formats[idx]
            else:
                typer.secho("Invalid selection. Please enter 1, 2, or 3.", fg=typer.colors.RED)
        except ValueError:
            typer.secho("Invalid input. Enter a number.", fg=typer.colors.RED)

@app.command()
def profile(
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
