/*
==================================
; Title: condon-aggregate-queries.js
; Author: Laurel Condon
; Date: 09/17/2023
; Description: projections 6.2 assignment
===============================
*/

const { db } = require("../../web-420/models/condon-composer");

// Lists of documents in collection
db.houses.find()

// Lists students in collection
db.students.find()

// Adds a new student
db.students.insertOne(
    { firstName: "Harry", 
    lastName: "Potter",
     studentId: "s1018", 
     houseId: "h1007" })

// Deletes student
db.students.deleteOne({ firstName: "Harry" })

// Shows a list of students by house name
db.houses.aggregate([{ $lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'students' }}])

// Finds certain house Gryffindor
db.houses.aggregate([{ $match: { houseId: 'h1009' }}, { $lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'students' }}])

// Finds certain house Eagles
db.houses.aggregate([{ $match: { mascot: 'Eagle' }}, { $lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'students' }}])

