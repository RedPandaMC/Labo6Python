"""
This code is used to display a table with all\nthe modes in management mode
"""
from rich.console import Console
from rich.table import Table
def show_functions():
    """
    This function generates a table for all functions in the management mode.
    """
    #region table
    table = Table(title="[not italic]ᴍᴏᴅᴇs[/not italic]")
    table.add_column("N.", justify="right", style="#FF006E", no_wrap=True)
    table.add_column("Purpose", justify="left", style="#3A86FF", no_wrap=True)
    table.add_row("1", "Add website")
    table.add_row("2", "View websites")
    table.add_row("3", "Remove websites")
    table.add_row("4", "Change checking schedule")
    table.add_row("Q", "Leave management mode")
    #endregion
    console = Console()
    console.print(table)
