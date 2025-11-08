from ..database.studentdatabase import studentdict
def viewrecord():
    for k,v in studentdict.items:
        print(f"{k} = {v}")
    