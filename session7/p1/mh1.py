first_name = (input("enter your first name:"))
last_name = (input("enter your last name:"))
if first_name.isdigit() or last_name.isdigit():
    print("wrong, re-enter")
    first_name = (input("enter your first name:"))
    last_name = (input("enter your last name:"))
    print(last_name, first_name)
else:
    print(last_name, first_name) 