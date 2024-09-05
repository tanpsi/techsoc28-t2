from helper import Role, warn, err, id_exists, input_role, input_int, input_id, input_grade, hash, calc_spi, calc_cpi

def add_user(db):
    """ Add or Modify user"""
    id = input("Enter ID: ")
    h = hash(input("Enter Password: "))
    role = input_role()
    if id_exists(db, id):
        warn("Modified already present user.")
        return
    db["users"][id] = [h, role]
    db["grades"][id] = list()

def add_grade(db):
    "Add or Modify Student grade"
    id = input_id(db)
    if db["users"][id][1] == Role.admin:
        err(f"{id} is a admin")
        return
    course = input("Enter Course code (like MA101N): ")
    sem = input_int("Enter Semester for which the student took the course: ")
    grade = input_grade()
    for x in db["grades"][id]:
        if x[0] == sem and x[1] == course:
            x[2] = grade
            return
    db["grades"][id].append([sem, course, grade])

def show_users(db):
    """Show all users in db"""
    d = {Role.admin: "admin", Role.student: "student"}
    for x in db["users"]:
        print(f"{x} ({d[db['users'][x][1]]})")

def show_grade(db, id=None, sem=None):
    if not id:
        id = input_id(db)
    if not sem:
        if len(db["grades"][id]) == 0:
            print(f"No grades for {id}")
            return
        print(f"CPI ({id}): {calc_cpi(db, id)}")
        for i in range(max(x[0] for x in db["grades"][id])):
            show_grade(db, id, i+1)
        return
    if len([x for x in db["grades"][id] if x[0] == sem]) == 0:
        print(f"No grades for sem {sem}")
        return
    print(f"Sem {sem} (SPI: {calc_spi(db, id, sem)})")
    [print(f"{x[1]}\t{x[2]}") for x in db["grades"][id] if x[0] == sem]
