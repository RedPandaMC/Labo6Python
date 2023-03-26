"""
This code is used to ping a list of websites \n
to check if they are online or not
"""
import time
import sys
import os
from rich.progress import track
import urlchecker as url
import managementmodes as mm

def delete_new_lines(ls_url: list):
    """
    This function gives the user a list without '\\n'
    """
    newlist = []
    for line in ls_url:
        newlist.append(line.replace("\n", ""))
    return newlist

def is_website_url_already_given(url_to_check:str):
    """
    This function checks if the given item is already in urls.txt
    """
    check = open(f"{DIR}/urls.txt", "r",encoding="UTF-8")
    url_list = delete_new_lines(check.readlines())
    if url_to_check not in url_list:
        return True
    return False

def add_websites():
    """
    This function allows you to add websites to urls.txt,\n
    also checks if the given item is already in urls.txt
    """
    while True:
        urltxt = open(f"{DIR}/urls.txt", "a",encoding="UTF-8")
        websiteurl = input("Give a valid url (https://www.site.com) or leave empty to exit: ")
        if websiteurl == "":
            break
        if url.is_string_an_url(websiteurl):
            if is_website_url_already_given(websiteurl):
                urltxt.write(f"{websiteurl}\n")
                print(f"Added website '{websiteurl}' to list.")
            else:
                print(f"'{websiteurl}' is already part of the list.")
        else:
            print("That isn't a valid URL")
        continue

def view_websites():
    """
    This function allows you to view all the websites in urls.txt
    """
    urls = delete_new_lines(checkurls.readlines())
    print(*urls,sep='\n')
    input("Press enter to continue.")



def management_mode_picker():
    """
    This function is used to let the user pick a mode
    """
    while True:
        os.system("cls")
        mm.show_functions()
        inputnum = input("Please choose a mode: ")
        match (inputnum):
            case ("1"):
                add_websites()
            case ("2"):
                view_websites()
            case ("3"):
                print("hello")
            case ("4"):
                print("hello")
            case ("Q"):
                quit()
            case (_):
                print("Not recognized, try again")

def main():
    """
    This function is used to interpret the given arguments
    """
    if len(sys.argv) > 0:
        for argument in sys.argv[1:]:
            if url.is_string_an_url(argument):
                if is_website_url_already_given(argument):
                    urltext.write(f"{argument}")
                    print(f"Added website '{argument}' to list.")
                else:
                    print(f"{argument} is already part of the list.")
                continue

            match (argument):
                case ("--manage" | "--m"):
                    os.system("cls")
                    print("You have chosen management mode.")
                    for _ in track(range(100),description="[#3a86ff]Loading...",style="#E5E5E5",
                                   finished_style="#FF006E",):
                        time.sleep(0.03)
                    management_mode_picker()
                case ("--check" | "--c"):
                    # do check
                    print("world")
                case (_):
                    # skip + send "argument not recognized"
                    print("Argument not recognized, skipping...")


if __name__ == "__main__":
    # region openingurls
    # checks for dir called history,
    # if it doesn't exist makes the dir
    DIR = "history"
    if not os.path.exists(DIR):
        os.mkdir(DIR)
    # open documents to be used later
    urltext = open(f"{DIR}/urls.txt", "a",encoding="UTF-8")
    checkurls = open(f"{DIR}/urls.txt", "r",encoding="UTF-8")
    # endregion

    main()
