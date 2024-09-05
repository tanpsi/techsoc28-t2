from helper import default_db, warn, err, hash, input_id, input_int
from db import add_user, add_grade, show_users, show_grade

import sys
import json
from pathlib import Path
from copy import deepcopy

DBFILE = Path(__file__).parent/Path("db.json")

def quit(db):
    if db == old_db:
        print("Bye")
        sys.exit(0)
    else:
        warn("Unsaved Changes")
        printm = lambda: print("""1. Save and Quit
2. Don't save and quit
3. Cancel""")
        printm()
        while True:
            match input_int("> "):
                case 1:
                    save(db)
                    sys.exit(0)
                case 2:
                    sys.exit(0)
                case 3:
                    return
                case _:
                    printm()
                    pass

def save(db):
    global old_db
    with open(DBFILE, "wt") as f:
        json.dump(db, f)
    old_db = deepcopy(db)
    print("Saved")

def handle_admin(db, id):
    printm = lambda: print("""1. Add/Modify User
2. Add/Modify grade
3. Show users
4. Show grades (including cpi/spi)
5. Show this menu
6. Save changes to db
7. Quit""")
    printm()
    while True:
        match input_int("> "):
            case 1:
                add_user(db)
            case 2:
                add_grade(db)
            case 3:
                show_users(db)
            case 4:
                show_grade(db)
            case 5:
                printm()
            case 6:
                save(db)
            case 7:
                quit(db)
            case _:
                err("Invalid Choice")
                printm()

def handle_stud(db, id):
    printm = lambda: print("""1. Show grades (including cpi/spi)
2. Show this menu
3. Quit""")
    printm()
    while True:
        match input_int("> "):
            case 1:
                sem = input_int("Enter Semester (enter 0 to see all sems): ")
                show_grade(db, id, sem)
            case 2:
                printm()
            case 3:
                break
            case _:
                printm()
                err("Invalid Choice")

def login(db):
    id = input_id(db)
    while True:
        h = hash(input("Enter password: "))
        if db["users"][id][0] == h:
            return (id, db["users"][id][1])
        err("Wrong Password")

if __name__ == "__main__":
    try:
        with open(DBFILE, "rt") as f:
            db = json.load(f)
        old_db = deepcopy(db)
    except FileNotFoundError or json.decoder.JSONDecodeError:
        warn("DB file not there or corrupted. Fresh file will be created on save")
        db = default_db
        old_db = None
    id, role = login(db)
    [handle_admin, handle_stud][role](db, id)
