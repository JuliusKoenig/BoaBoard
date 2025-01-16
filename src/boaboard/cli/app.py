from pathlib import Path

import typer

from boaboard import __title__, __version__, __author__, __author_email__, __license__
from boaboard.core.console import console

cli_app = typer.Typer()


@cli_app.command(name="version", help=f"Show the version of {__title__}.")
def version() -> None:
    """
    Show the version of BoaBoard.

    :return: None
    """

    console.print(f"{__title__} v{__version__} by {__author__}")
    console.print(f"E-Mail: {__author_email__}")
    console.print(f"License: {__license__}")


cli_db_app = typer.Typer(help="Database commands.")


@cli_db_app.command(name="dump", help="Backup the database.")
def backup_database(dump_path: Path = typer.Argument(..., help="Path to save the backup. Can be a ZIP file or a directory."),
                    force: bool = typer.Option(False, "--force", "-f", help="Force to overwrite existing backup.")) -> None:
    """
    Backup the database.

    :param dump_path: Path to save the backup. Can be a ZIP file or a directory.
    :param force: Force to overwrite existing backup.
    :return: None
    """

    console.print(f"Backup database to '{dump_path}'.")

    from rich.prompt import Prompt

    from boaboard.core.logger import logger
    from boaboard.core.db import db

    # initiate logging
    logger()

    # check if dump path is existing
    if dump_path.exists() and not force:
        if Prompt.ask(f"Path '{dump_path}' already exists. Overwrite?", choices=["y", "n"], default="n", console=console) == "n":
            return

    # dump database
    db().dump(path=dump_path, overwrite=True)

    console.print(f"[green]Database backup finished successfully.[/green]")


@cli_db_app.command(name="restore", help="Restore the database.")
def restore_database(dump_path: Path = typer.Argument(..., help="Path to the backup. Can be a ZIP file or a directory."),
                     force: bool = typer.Option(False, "--force", "-f", help="Force to overwrite existing database.")) -> None:
    """
    Restore the database.

    :param dump_path: Path to the backup. Can be a ZIP file or a directory.
    :param force: Force to overwrite existing database.
    :return: None
    """

    console.print(f"Restore database from '{dump_path}'.")

    from boaboard.core.logger import logger
    from boaboard.core.db import db

    # initiate logging
    logger()

    # check if dump path is existing
    if not dump_path.exists():
        console.print(f"[red]Path '{dump_path}' does not exist.[/red]")
        return

    try:
        # restore database
        db().restore(path=dump_path, overwrite=force)
    except FileExistsError as e:
        console.print(f"[red]Could not restore database. {e}[/red]")
        return

    console.print(f"[green]Database restore finished successfully.[/green]")


cli_app.add_typer(cli_db_app, name="db")


@cli_app.command(name="serve", help=f"Start the {__title__} server.")
def serve() -> None:
    """
    Start the BoaBoard server.

    :return: None
    """

    from boaboard.assets.ascii_logo import ASCII_LOGO

    console.print(ASCII_LOGO)
    console.print(f"Start {__title__} server v{__version__} ...")

    from boaboard.core.logger import logger
    from boaboard.core.server import Server

    # initiate logging
    logger()

    # start server
    Server()


@cli_app.command(name="shell", help="Start the BoaBoard shell.")
def shell() -> None:
    """
    Start the BoaBoard shell.

    :return: None
    """

    console.print(f"Start {__title__} shell ...")

    from boaboard.cli.shell import shell

    shell()
