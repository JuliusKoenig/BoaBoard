import typer

from boaboard import __title__, __version__, __author__, __author_email__, __license__
from boaboard.core.settings import Settings

cli_app = typer.Typer()





@cli_app.command(name="version", help="Show the version of the application.")
def version():
    typer.echo(f"{__title__} v{__version__} by {__author__}")
    typer.echo(f"E-Mail: {__author_email__}")
    typer.echo(f"License: {__license__}")


if __name__ == "__main__":
    cli_app()
