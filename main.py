import time
import sys
import os
from rich.progress import track
import urlchecker as url
import managementmodes as mm

def management_mode_picker():
    mm.show_functions()
    input("Please input a number")
    match 

websitesToCheck = []
if len(sys.argv) > 0:
    for argument in sys.argv[1:]:
        if url.is_string_an_url(argument):
            websitesToCheck.append(argument)
            print(f"Added website '{argument}' to list.")
            continue
        match (argument):
            case ("--manage" | "--m"):
                os.system("cls")
                print("You have chosen management mode.")
                for i in track(
                    range(100),
                    description="[#3a86ff]Loading...",
                    style="#E5E5E5",
                    finished_style="#FF006E",
                ):
                    time.sleep(0.03)
                print(":)")
            case ("--check" | "--c"):
                # comment: do check
                print("world")
            case (_):
                # comment: skip + send "argument not recognized"
                print("Argument not recognized, skipping...")
