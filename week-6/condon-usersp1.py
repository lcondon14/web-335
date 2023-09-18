
#==================================
# Title: condon-usersp1.py
# Author: Laurel Condon
# Date: 09/17/2023
# Description: projections 6.2 assignment
#===============================

# Imports MongoClient
from pymongo import MongoClient

# Connection string
client = MongoClient("mongodb+srv://web335_user:s3cret>@bellevueuniversity.ytwiz26.mongodb.net/")

# Variable to access database
db =  client['web335DB']

# Prints all users info
users = db.users.find({})
for user in users:
  print(user)

# Find a user document by employeeId
print(db.users.find_one({"employeeId": "1011"}))

# Find a user by last name
print(db.users.find_one({"lastName": "Mozart"}))


