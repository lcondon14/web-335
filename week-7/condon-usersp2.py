
#==================================
# Title: condon-usersp2.py
# Author: Laurel Condon
# Date: 09/24/2023
# Description: projections 7.3 assignment
#===============================

from pymongo import MongoClient

# Connection string
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.ytwiz26.mongodb.net/")

# Variable to access database
db =  client['web335DB']

# defines the new user document
new_user = {
    "firstName": "Laurel",
    "lastName": "Condon",
    "employeeId": "1014",
    "email": "lkleck14@gmail.com"
}

# Insert the new user document into the "users" collection
inserted_user = db.users.insert_one(new_user).inserted_id
print(f"Inserted user: {inserted_user}")

# Displays created user
new_created_user = db.users.find_one({"employeeId": "1014"})
print("New created user: ")
print(new_created_user)

# Update user email
new_email = "lmcondon@my365.bellevue.edu"
db.users.update_one({"employeeId": "1014"}, {"$set": {"email": new_email}})
print(f"Email updated successfully!")

# Displays updated user
updated_user = db.users.find_one({"employeeId": "1014"})
print("Updated user: ")
print(updated_user)

# Deletes user
db.users.delete_one({"employeeId": "1014"})
print(f"Deleted document: {inserted_user}")

# Deleted user is proved
deleted_user = db.users.find_one({"employeeId": "1014"})
if deleted_user:
    print("User was deleted successfully")
else:
    print("User was not deleted")