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

def history_creator():
    """
    Creates dir
    """
    if not os.path.exists(dir):
        os.mkdir(dir)


def delete_new_lines(ls_url: list):
    """
    This function gives the user a list without '\\n'
    """
    newlist = []
    for line in ls_url:
        newlist.append(line.replace("\n", ""))
    return newlist


def is_website_url_already_given(url_to_check: str):
    """
    This function checks if the given item is already in urls.json
    """
    dir = "history"
    check = open(f"{dir}/urls.json", "r", encoding="UTF-8")
    url_list = delete_new_lines(check.readlines())
    if url_to_check not in url_list:
        return True
    return False


# region add_mode
def add_websites():
    """
    This function allows you to add websites to urls.json,\n
    also checks if the given item is already in urls.json
    """
    while True:
        dir = "history"
        urltxt = open(f"{dir}/urls.json", "a", encoding="UTF-8")
        websiteurl = input(
            "Give a valid url (https://www.site.com) or leave empty to exit: "
        )
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


# endregion add_mode


# region view_mode
def view_websites():
    """
    This function allows you to view all the websites in urls.json
    """
    dir = "history"
    check = open(f"{dir}/urls.json", "r", encoding="UTF-8")
    urls = delete_new_lines(check.readlines())
    print(*urls, sep="\n")


# endregion view_mode


# region delete_mode
def delete_websites():
    """
    This function allows you to delete websites from urls.json\n
    it also writes the non delete items in urls.json
    """
    dir = "history"
    check = open(f"{dir}/urls.json", "r", encoding="UTF-8")
    urls = delete_new_lines(check.readlines())
    newtxt = open(f"{dir}/urls.json", "w", encoding="UTF-8")
    urldictionary = {}
    print("The urls are:")
    for i, link in enumerate(urls):
        urldictionary[f"{i+1}"] = link
        print(f"{i+1}. '{link}'")
    while True:
        url_to_delete = input(
            "Give me a number for the urls that you want to delete or leave empty to exit: "
        )
        if url_to_delete == "":
            break
        if url_to_delete not in urldictionary.keys():
            print("This item does not exist \nor is already deleted.")
            continue
        else:
            urldictionary.pop(url_to_delete)
    for key in urldictionary:
        newtxt.write(f"{urldictionary[key]}\n")


# endregion delete_mode


def schedule_check():
    dir = "history"
    read_schedulejson = open(f"{dir}/schedule.json", "r", encoding="UTF-8")
    schedule_settings = read_schedulejson()
    # writeschedulejson = open(f"{dir}/schedule.json","w",encoding="UTF-8")


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
                input("Press enter to continue.")
            case ("3"):
                delete_websites()
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
                    for _ in track(
                        range(100),
                        description="[#3a86ff]Loading...",
                        style="#E5E5E5",
                        finished_style="#FF006E",
                    ):
                        time.sleep(0.03)
                    management_mode_picker()
                case ("--check" | "--c"):
                    # do check
                    print("world")
                case (_):
                    # skip + send "argument not recognized"
                    print("Argument not recognized, skipping...")


if __name__ == "__main__":
    dir = "history"
    history_creator()
    urltext = open(f"{dir}/urls.json", "a", encoding="UTF-8")
    checkurls = open(f"{dir}/urls.json", "r", encoding="UTF-8")
    main()
