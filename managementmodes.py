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
    This function checks if the given item is already in urls.json
    """
    dir = "history"
    check = open(f"{dir}/urls.json", "r", encoding="UTF-8")
    url_list = delete_new_lines(check.readlines())
    if url_to_check not in url_list:
        return True
    return False

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

def view_websites():
    """
    This function allows you to view all the websites in urls.json
    """
    dir = "history"
    check = open(f"{dir}/urls.json", "r", encoding="UTF-8")
    urls = delete_new_lines(check.readlines())
    print(*urls, sep="\n")

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

