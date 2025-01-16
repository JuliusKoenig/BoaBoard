from IPython.terminal.embed import InteractiveShellEmbed as _InteractiveShellEmbed

def shell():
    # modify globals
    for k in list(globals().keys()):
        if k in ["_InteractiveShellEmbed"]:
            continue
        globals().pop(k)

    from boaboard import __name__, __title__, __description__, __version__, __author__, __author_email__, __license__
    globals()["__name__"] = __name__
    globals()["__title__"] = __title__
    globals()["__description__"] = __description__
    globals()["__version__"] = __version__
    globals()["__author__"] = __author__
    globals()["__author_email__"] = __author_email__
    globals()["__license__"] = __license__


    # import modules
    from boaboard.core.console import console
    from boaboard.core.environment import environment
    from boaboard.core.settings import settings
    from boaboard.core.logger import logger
    from boaboard.core.db import db

    # initiate logging
    logger()


    # define local namespace
    local_ns = {
        "console": console,
        "print": console.print,
        "environment": environment(),
        "settings": settings(),
        "db": db(),
        "logger": logger()
    }

    # create interactive shell
    interactive_shell = _InteractiveShellEmbed()

    # print welcome message
    console.print("-" * 80)
    console.print(f"Interactive Shell for {__title__} v{__version__} by {__author__}")
    console.print(f"Use 'exit' to leave the shell.")
    console.print("-" * 80)

    # start interactive shell
    interactive_shell.mainloop(local_ns=local_ns)

    # disconnect from database (if connected, to prevent logging errors)
    db().disconnect()

    console.print("Interactive Shell closed.")