import time
import sys
import os
from rich.progress import track
import urlchecker as url
import managementmodes as mm

mm.show_functions()

def management_mode_picker():
    mm.show_functions()
    inputnum = input("Please choose a mode")
    match (inputnum):
        case ("1"):
            print("hello")
        case ("2"):
            print("hello")
        case("3"):
            print("hello")
        case("4"):
            print("hello")
        case("Q"):
            
            

#region openingurls
#checks for dir called history,
#if it doesn't exist makes the dir
DIR = "history"
if not os.path.exists(DIR):
    os.mkdir(DIR)

#opens the list in read and append mode,
#if the file doesn't exist it also
#creates it in the dir
listofurls = open(f"{DIR}/urls.json","a")
checkurls = open(f"{DIR}/urls.json","r")
urls = checkurls.readlines()

#removes \n from urls
for i,line in enumerate(urls):
    urls[i] = line.replace(R'\n','')
#endregion
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
                    for i in track(
                        range(100),
                        description="[#3a86ff]Loading...",
                        style="#E5E5E5",
                        finished_style="#FF006E",
                    ):
                        time.sleep(0.03)
                    print(":)")
                case ("--check" | "--c"):
                    # do check
                    print("world")
                case (_):
                    # skip + send "argument not recognized"
                    print("Argument not recognized, skipping...")

if __name__ == "__main__":
    main()
