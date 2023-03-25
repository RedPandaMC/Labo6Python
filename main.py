import time
import sys
import os
from rich.progress import track
import urlchecker as url
import managementmodes as mm

def delete_new_lines(list:list):
    newlist = []
    for line in list:
        newlist.append(str(line).replace(R"\n", ""))
    return newlist

def management_mode_picker():
    while True:
        os.system("cls")
        mm.show_functions()
        inputnum = input("Please choose a mode: ")
        match (inputnum):
            case ("1"):
                while True:
                    DIR = "history"
                    urltxt = open(f"{DIR}/urls.txt", "a")
                    check = open(f"{DIR}/urls.txt", "r")

                    websiteurl = input(
                        "Give a valid url (https://www.site.com) or leave empty to exit: "
                    )

                    if websiteurl == "":
                        break

                    url_list = check.readlines()
                    url_list_no_newlines = delete_new_lines(url_list)
                    print(url_list_no_newlines)

                    if url.is_string_an_url(websiteurl):
                        if websiteurl not in url_list_no_newlines:
                            urltxt.write(f"{websiteurl}\n")
                            print(f"Added website '{websiteurl}' to list.")
                        else:
                            print(f"{websiteurl} is already part of the list.")
                    else:
                        print("That isn't a valid URL")
                    continue
            case ("2"):
                urls = checkurls.readlines()
                for i, line in enumerate(urls):
                    urls[i] = line.replace(R"\n", "")
                print(*urls,sep='\n')
            case ("3"):
                print("hello")
            case ("4"):
                print("hello")
            case ("Q"):
                quit()
            case (_):
                print("Not recognized, try again")


# region openingurls
# checks for dir called history,
# if it doesn't exist makes the dir
DIR = "history"
if not os.path.exists(DIR):
    os.mkdir(DIR)

# opens the list in read and append mode,
# if the file doesn't exist it also
# creates it in the dir
listofurls = open(f"{DIR}/urls.txt", "a")
checkurls = open(f"{DIR}/urls.txt", "r")
urls = checkurls.readlines()

# removes \n from urls
for i, line in enumerate(urls):
    urls[i] = line.replace(R"\n", "")
# endregion


def main():
    if len(sys.argv) > 0:
        for argument in sys.argv[1:]:
            if url.is_string_an_url(argument):
                if argument not in urls:
                    listofurls.write(f"{argument}")
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
    main()
