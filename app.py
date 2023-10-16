from database import add_entry, get_entries, create_table

menu = """Please select one of the following options:
1. Add new entry for today.
2. View entries.
3. Exit

Your selection: """

welcome = "Welcome to the Python diary"

def prompt_new_entry():
    """take in user info"""
    entry_content = input("What did you learn today?: ")
    entry_date = input("Date: ")
    add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")

#create table
create_table()

user_input = input(menu)

while user_input != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        entries = get_entries()
        view_entries(entries)
    else:
        print("invalid option, please try again!")
    
    user_input = input(menu)