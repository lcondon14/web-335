#---------------------------------------
# Title: condon-hobbies.py
# Author: Laurel Condon
# Date: 09 September 2023
# Description: Hobbies assignment 5.3
#---------------------------------------

# List of hobbies
hobbies = ["Drawing", "Painting", "Reading" "Motorcycles", "Music"]

# Print the list of hobbies
print("My hobbies:")
for hobby in hobbies:
    print("- " + hobby)

# List of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Iterate over the list of days to display correct message
for day in days:
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: You are off and should enjoy your hobbies!")
    else:
        print(f"{day}: It is a work day.")