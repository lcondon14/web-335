/*
======================================
; Title: condon-mongodb-shell.js
; Author: Laurel Condon
; Date: 3 September 2023
; Description: Queries list
======================================
*/

const { localeData } = require("moment");

// Loads users
load("users.js")

// Displays all documents in the collection
db.users.find({})

// Displays the user with the email address jbach@me.com
db.users.find({ email: "jbach@me.com" })

// Displays the user with the last name Mozart
db.users.find({ lastName: "Mozart" })

// Displays the user with the first name Richard
db.users.find({ firstName: "Richard" })

// Displays the user with the employee id 1010
db.users.find({ employeeId: "1010" })