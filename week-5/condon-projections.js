/*
==================================
; Title: condon-projections.js
; Author: Laurel Condon
; Date: 09/09/2023
; Description: projections 5.2 assignment
===============================
*/

const { db } = require("../../web-420/models/condon-composer")

// Creates ans new user to the collection
const newUser = {
    "firstName": "Calvin",
    "lastName": "Minopolis",
    "employeeId": "1013",
    "email": "calminopolis@me.com",
    "dateCreated": new Date()
}

// Inserts new user
db.users.insertOne()

// Update Mozart's email
db.users.updateOne(
    {firstName: "Mozart" },
    { $set: {email: "mozart@me.com" }}
)

// Finds the user Mozart
db.users.find({ lastName: "Mozart" })

// Finds all users
db.users.find({}, { _id: 0, firstName: 1, lastName: 1, email: 1 });
