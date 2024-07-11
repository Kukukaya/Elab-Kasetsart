ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "Ad31n15Tr@t012"

# "Username=admin" and "Password=Ad31n15Tr@t012"

# Username: admin
# Password: Ad31n15Tr@t012
# Welcome, admin.

user = input("Username: ")
passw = input("Password: ")

if user == ADMIN_USERNAME and passw == ADMIN_PASSWORD:
    print("Welcome, admin.")

else:
    print("You are not admin.")

