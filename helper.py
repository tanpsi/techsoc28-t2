from hashlib import sha256

grades = {'AP': 10, 'AA': 10, 'AB': 9, 'BB': 8, 'BC': 7, 'CC': 6, 'CD': 5, 'DD': 4, 'FR': 0}

class Role:
    admin = 0
    student = 1

default_db = {"users": {"admin": ['8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', Role.admin]},
              "grades":{"admin": list()}}

def warn(s):
    print("WARNING:", s)

def err(s):
    print("ERROR:", s)

def id_exists(db, id):
    return True if id in db["users"] else False

def input_role():
    while True:
        s = input("Enter role (admin/student): ")
        if s == 'admin':
            return Role.admin
        elif s == 'student':
            return Role.student
        else:
            err("Unsupported role")

def input_int(s):
    while True:
        try:
            s = int(input(s))
        except ValueError:
            err("Integer only")
        else:
            return s

def input_id(db):
    while True:
        id = input("Enter ID: ")
        if id_exists(db, id):
            break
        err("No such user present")
    return id

def input_grade():
    while True:
        s = input("Enter grade: ")
        if s in grades:
            return s
        else:
            err("Invalid grade")

def hash(s):
    return sha256(s.encode("utf8")).hexdigest()

def calc_spi(db, id, sem):
    l = [grades[x[2]] for x in db["grades"][id] if x[0]==sem]
    # assuming same credit (4) for all courses
    return round(sum(l)/len(l), 2)

def calc_cpi(db, id):
    l = [grades[x[2]] for x in db["grades"][id]]
    # assuming same credit (4) for all courses
    return round(sum(l)/len(l), 2)
