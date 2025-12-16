import typer
from pathlib import Path
from csv_profiler.io import read_csv_rows
from csv_profiler.profile import basic_profile
from csv_profiler.render import write_json, write_markdown

def profile(
    input_path: Path = typer.Argument(..., help="Input CSV file"),
    out_dir: Path = typer.Option(Path("outputs"), "--out-dir", help="Output folder"),
    report_name: str = typer.Option("report", "--report-name", help="Base name for outputs"),
):
    """Profile a CSV file and generate data quality reports."""
    
    try:
        # Validate input file exists
        if not input_path.exists():
            typer.secho(f"Error: File not found: {input_path}", fg=typer.colors.RED)
            raise typer.BadParameter(f"Input file does not exist: {input_path}")
        
        typer.secho(f"📊 Profiling: {input_path}", fg=typer.colors.BLUE)
        
        rows = read_csv_rows(input_path)
        if not rows:
            typer.secho("Error: No data found in file", fg=typer.colors.RED)
            raise typer.Exit(code=1)
        
        typer.secho(f"✓ Loaded {len(rows)} rows", fg=typer.colors.GREEN)
        
        report = basic_profile(rows)
        
        out_dir.mkdir(parents=True, exist_ok=True)
        
        if report_name in ["json", "both"]:
            json_file = out_dir / f"{report_name}.json"
            write_json(report, json_file)
            typer.secho(f"✓ Saved: {json_file}", fg=typer.colors.GREEN)
        
        if report_name in ["markdown", "both"]:
            md_file = out_dir / f"{report_name}.md"
            write_markdown(report, md_file)
            typer.secho(f"✓ Saved: {md_file}", fg=typer.colors.GREEN)
            
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
    typer.run(profile)
