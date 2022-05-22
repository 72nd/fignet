import typer

from pathlib import Path


app = typer.Typer()


@app.command()
def srt(
    in_file: Path = typer.Option(
        ...,
        "-i",
        "--input",
        help="path to subtitle srt file",
    ),
    out_file: Path = typer.Option(
        "-o",
        "--output",
        help="path to the Gephi output file",
    )
):
    """Outputs a network based on the apperance per scenes."""


@app.command()
def visualize(
    in_file: Path = typer.Option(
        ...,
        "-i",
        "--input",
        help="path to Gephi file",
    ),
):
    """Renders a visual representation of the graph."""


def run():
    app()
