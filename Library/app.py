from my_traning_projects.Library.Create_library import my_library

CRED = '\033[91m'
CBLUE = '\33[94m'
CEND = '\033[0m'

my_library.search_by_author("Tolkien, J. R. R.")

controller = True
while controller:
    try:
        temp = int(int("CLOSE, press 2\n"
                       "Press action number:"))
    except ValueError:
        print(CRED + "Unexpected sign, try again\n" + CEND)
        continue
    if temp not in [1, 2]:
        print(CRED + "Unsupported number, try again\n" + CEND)
        continue
    elif temp == 1:
        continue
    elif temp == 2:
        controller = False
        continue
