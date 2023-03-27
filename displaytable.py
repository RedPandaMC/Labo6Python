"""
This code is used to display a table with all\nthe modes in management mode
"""
import json
from rich.console import Console
from rich.table import Table



def show_functions_management():
    """
    This function generates a table for all functions in the management mode.
    """
    # region table
    tablemodes = Table(title="[not italic]𝙼𝚘𝚍𝚎𝚜[/not italic]")
    tablemodes.add_column("N.", justify="right", style="#FF006E", no_wrap=True)
    tablemodes.add_column("Purpose", justify="left", style="#3A86FF", no_wrap=True)
    tablemodes.add_row("1", "Add website")
    tablemodes.add_row("2", "View websites")
    tablemodes.add_row("3", "Remove websites")
    tablemodes.add_row("4", "Change checking schedule")
    tablemodes.add_row("Q", "Leave management mode")
    # endregion
    console = Console()
    console.print(tablemodes)


def show_schedule_settings():
    dir = "history"
    read_schedulejson = open(f"{dir}/schedule.json", "r", encoding="UTF-8")
    settings = json.load(read_schedulejson)
    # region table
    tablesettings = Table(title="[not italic]𝚂𝚎𝚝𝚝𝚒𝚗𝚐𝚜[/not italic]")
    tablesettings.add_column("Name", justify="right", style="#FF006E", no_wrap=True)
    tablesettings.add_column("Current Value", justify="left", style="#3A86FF", no_wrap=True)
    for name in settings.keys():
        tablesettings.add_row(f"{name.replace('-',' ')}", f"{settings[name]}")
    # endregion
    console = Console()
    console.print(tablesettings)