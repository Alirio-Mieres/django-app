# Overview

This repository contains a notes app made with the Django framework. As a software developer, I have had experience working with Node.js and React. Since I have been working with Python lately I took the initiative to learn Django.

This app consists of a notes app where users can create, view, update, and delete notes (CRUD). It also has a login and registration form.

To run the project you must have the python and Django versions specified below and run the following commands:

1. `pip install -r requirements.txt`
2. `python manage.py migrate`
3. `python manage.py runserver`

# Web Pages

1. Login Page
    * Description: User authentication.
    * Transitions: Redirects to Notes Page on success
    * Dynamic Content: Error messages, input fields.

2. Sign Up Page
    * Description: User registration.
    * Transitions: Redirects to Login Page after signup.
    * Dynamic Content: Validation errors, input fields.

3. Notes Page
    * Description: Displays user notes.
    * Transitions: Accessed after login; links to Create Note Page and Edit Profile Page.
    * Dynamic Content: List of notes, edit/delete options.

4. Create Note Page
    * Description: Create a new note.
    * Transitions: Accessed from Notes Page; redirects back after saving.
    * Dynamic Content: Note form.

5. Edit Profile Page
    * Description: Update user profile.
    * Transitions: Accessed from Notes Page; redirects back after saving.
    * Dynamic Content: Pre-filled form.

Transition Summary
* Sign Up → Login
* Login → Notes
* Notes → Create Note
* Notes → Edit Profile
* Create Note → Notes

# Development Environment

* **Editor**: Visual Studio Code
* **Version Control**: Git and GitHub
* **Language**: Python 3.12.0
* **Framework**: Django 5.1.2
* **Database**: SQLite

# Useful Websites

* [Django documentation](https://docs.djangoproject.com/en/5.1/)

# Future Work

* Add the option to add notifications to remind users of notes with pending tasks.
* Improve model Note.