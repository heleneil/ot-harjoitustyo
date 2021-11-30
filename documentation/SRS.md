# Software requirements specification

## Purpose

In the app users can create notes and edit them. To make notes the first-time user must create an account with a username.

## Description: Basic function

###### Before signing in

* the user can create a username
  * the username must not exist in the database already

* [x] the user can log in after creating a valid username (only with one of the usernames that already exist in the csv-file for now) 
  * a successful login requires an existent username
  * username invalid notification

###### Signed in

* the user can create notes
* the user sees the title of each note
* the notes are only visible to the user that is signed in
* the user can log out

###### Note interface
* the user can edit a note and save it
* the user can delete a note

## Ideas for further development

* improving the UI
* remove user option
* adding links and images
* making a checklist
* login requires password
