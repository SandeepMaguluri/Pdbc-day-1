from day1 import connection1
con=connection1()
cur=con.cursor()
def add_emp():
    id=int(input("Enter employee ID: "))
    name=input("Enter employee NAME: ")
    sal=int(input("Enter employee SAL: "))
    location=input("Enter employee LOCATION: ")
    dept=input("Enter employee DEPT: ")
    query="insert into PRACTISE(id,name,sal,location,dept) values(%s,%s,%s,%s,%s)"
    cur.execute(query,(id,name,sal,location,dept))
    con.commit()
    con.close()
    print("-"*15)


def view_emp():
    query="select * from PRACTISE"
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        print(i)
    con.close()
    print("="*20)

def update_emp():
    idu=int(input("Enter employee ID: "))
    nameu=input("Enter employee NAME: ")
    salu=int(input("Enter employee SAL: "))
    locationu=input("Enter employee LOCATION: ")
    deptu=input("Enter employee DEPT: ")
    query="update PRACTISE set name=%s, sal=%s, location=%s, dept=%s where id=%s"
    cur.execute(query,(nameu,salu,locationu,deptu,idu))
    con.commit()
    con.close()
    print("="*5, "Successfully updated", "="*5)


def del_emp():
    idn=int(input("enter the emp Id to delete: "))
    cur.execute("delete from PRACTISE where id=idn")
    con.commit()
    con.close()
    print("="*5, "Successfully Deleted", "="*5)
