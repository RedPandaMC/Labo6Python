import json
import os
import displaytable as dt
import urlchecker as url


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
    This function checks if the given item is already in urls.txt
    """
    dir = "history"
    check = open(f"{dir}/urls.txt", "r", encoding="UTF-8")
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
        dir = "history"
        urltxt = open(f"{dir}/urls.txt", "a", encoding="UTF-8")
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


def view_websites():
    """
    This function allows you to view all the websites in urls.txt
    """
    dir = "history"
    check = open(f"{dir}/urls.txt", "r", encoding="UTF-8")
    urls = delete_new_lines(check.readlines())
    print(*urls, sep="\n")


def delete_websites():
    """
    This function allows you to delete websites from urls.txt\n
    it also writes the non delete items in urls.txt
    """
    dir = "history"
    check = open(f"{dir}/urls.txt", "r", encoding="UTF-8")
    urls = delete_new_lines(check.readlines())
    newtxt = open(f"{dir}/urls.txt", "w", encoding="UTF-8")
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


def does_file_exist(filename: str):
    """
    This function checks if a file exists in the dir = "history" folder.
    """
    dir = "history"
    if os.path.exists(f"{dir}/{filename}"):
        return True
    return False


def create_schedule_settings_if_not_exists():
    """
    This function checks if the schedule settings already exist.
    """
    dir = "history"
    if not does_file_exist("schedule.json"):
        basesettings = {"do-scheduled-ping": False, "schedule-time-in-minutes": 0}
        write_schedulejson = open(f"{dir}/schedule.json", "w", encoding="UTF-8")
        json.dump(basesettings, write_schedulejson, indent=2)


def schedule_check():
    """
    This function lets you choose if you want to schedule a ping task,
    it also lets you decide the amount of time between tasks.
    """
    create_schedule_settings_if_not_exists()
    dir = "history"
    readschedulejson = open(f"{dir}/schedule.json", "r", encoding="UTF-8")
    settings = json.load(readschedulejson)
    dt.show_schedule_settings()
    writeschedulejson = open(f"{dir}/schedule.json", "w", encoding="UTF-8")
    change_settings = input("Do you want to change the settings? (Y/N)").upper()
    if change_settings == "Y":
        scheduled_pings = input("Do you want to turn scheduled pings on? (Y/N)").upper()
        if scheduled_pings == "Y":
            settings["do-scheduled-ping"] = True
        elif scheduled_pings == "N":
            settings["do-scheduled-ping"] = False

        if settings["do-scheduled-ping"] is True:
            if input("Do you want to change the interval? (Y/N)").upper() == "Y":
                settings["schedule-time-in-minutes"] = float(input("Time (in min): "))
    readschedulejson.close()
    json.dump(settings, writeschedulejson, indent=2)
    writeschedulejson.close()
    dt.show_schedule_settings()
    input("Press enter to continue")
