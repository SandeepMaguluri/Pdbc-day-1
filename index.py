from operations import *

print("1. Add Employees")
print("2. View Emloyees")
print('3. Update Employees')
print("4. Delete Employees")
print("5. Exit")

opt=int(input("Enter your Choice: "))

if opt==1:
    add_emp()

elif opt==2:
    view_emp()

elif opt==3:
    update_emp()

elif opt==4:
    del_emp()

elif opt==5:
    exit_emp()

else:
    print("Enter a value between 1 and 5")

    