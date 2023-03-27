"""
This code is used to ping a list of websites \n
to check if they are online or not
"""
import time
import sys
import os

from rich.progress import track

import urlchecker as url
import displaytable as dt
import managementmodes as mm

def history_creator():
    """
    Creates dir
    """
    if not os.path.exists(dir):
        os.mkdir(dir)

def management_mode_picker():
    """
    This function is used to let the user pick a mode
    """
    while True:
        os.system("cls")
        dt.show_functions_management()
        inputnum = input("Please choose a mode: ")
        match (inputnum):
            case ("1"):
                mm.add_websites()
            case ("2"):
                mm.view_websites()
                input("Press enter to continue.")
            case ("3"):
                mm.delete_websites()
            case ("4"):
                mm.schedule_check()
            case ("Q"):
                quit()
            case (_):
                print("Not recognized, try again")
                time.sleep(1)


def main():
    """
    This function is used to interpret the given arguments
    """
    if len(sys.argv) > 0:
        for argument in sys.argv[1:]:
            if url.is_string_an_url(argument):
                if mm.is_website_url_already_given(argument):
                    urltext.write(f"{argument}\n")
                    print(f"Added website '{argument}' to list.")
                else:
                    print(f"{argument} is already part of the list.")
                continue

            match (argument):
                case ("--manage" | "--m"):
                    os.system("cls")
                    print("You have chosen management mode.")
                    for _ in track(
                        range(100),
                        description="[#3a86ff]Loading...",
                        style="#E5E5E5",
                        finished_style="#FF006E"
                    ):
                        time.sleep(0.03)
                    management_mode_picker()
                case ("--check" | "--c"):
                    mm.perform_ping_check()
                    for _ in track(range(10),description="[#0EAD69]Pinging...",style="#E5E5E5",finished_style="#FF006E"):
                        time.sleep(0.01)
                    input("Results written in status.json")
                case (_):
                    print("Argument not recognized, skipping...")

if __name__ == "__main__":
    dir = "history"
    history_creator()
    urltext = open(f"{dir}/urls.txt", "a", encoding="UTF-8")
    checkurls = open(f"{dir}/urls.txt", "r", encoding="UTF-8")
    main()
