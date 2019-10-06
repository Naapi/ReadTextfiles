import sys
import json
import os.path
from collections import OrderedDict

#TODO Text in alphabetical order // listOfStrings.sort() ? 

txtfile = sys.argv[1]
def readTextFile():
    try:
        f = open(txtfile)
        f.close()
    except FileNotFoundError:
        print('File does not exist')
    else:
        #print('file is here!')
        with open(txtfile) as json_file:
            data = json.load(json_file)
            alldata = data['library']
            #sorted_string = json.dumps(x, indent=4, sort_keys=True) ?
            # alldata = OrderedDict(sorted(alldata.data['library']['writer']))
            # alldata = sorted(alldata, key=data['library'][0])
            #print(alldata)
            return alldata

usr_input = 0
while usr_input != 3:
    #TODO create user_input try except validation
    print(f"""

    Reading the file {sys.argv[1]}
    Do you want to:
    1) Add new book
    2) Print current database content in ascending order by writer’s name
    3) Exit the program?
    """)
    usr_input = int(input("Select option? "))
    #print(usr_input)
    if(usr_input == 1):
        #txtfile = sys.argv[1]
        book_name = input("\nAdd name of the book: ")
        writer_name = input("Add name of the writer: ")
        isbn_name = input("Add ISBN of the book: ")
        print(f'{book_name} {writer_name} {isbn_name}')
        ask_send_db = input('Do you want to send the data to database. yes/no ')
        if ask_send_db == 'yes':
            print('Send to database!')
            send_db_data = {"book": book_name,
                            "writer": writer_name,
                            "isbn": isbn_name
                            }
            print(send_db_data)

            #refactor this into a function --->
            #Fix appending outside objects array
            with open(txtfile, 'a') as f:
                #json.dump(data['library'], f)
                f.write(json.dumps(send_db_data))
                f.close()
            #<-----------
            continue
        if ask_send_db == 'no':
            print('Return to main menu')
            continue
        else:
            print('Computer says no')

    if(usr_input == 2):
        print(readTextFile())
        continue
    if(usr_input == 3):
        print('Quit the program')
        break

    else:
        print('You did nothing John Snow')