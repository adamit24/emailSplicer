# Name: Taylor Adami
# Date
# Project: Python Beginner Project - Email Slicer
# File: emailSlicer --> main.py
# ---------------------------------------------------------------------------

# Grab the input from the user- this should collect their email address
email = input('Please enter your email: \n'). strip()

# the .slice() function will be take the user input and remove any spaces from the beginning or end of the input
# The email variable will then how the email address, minus the spaces that we stripped out

# Now we want to create a variable to pull the username from the email
userName = email[:email.index('@')]

# in the variable userName, we are using the email variable.
# the .index() is a search function to locate the first occurrence of the symbol or word typed in the parenthesis
# After the email variable, within the [] we are locating the range of the text from the start of the email string
# to the first instance of the @ symbol.
# the text in between the beginning to the @ symbol will be pulled and put into the userName variable

# Now we have to slice out the domain name
domainName = email[email.index('@') + 1:]

# the domain name variable is the same way as the userName, but opposite (the end of the string, after the the @)
# The domainName variable is using the email input.
# between the the brackets is where we put the range.
# The email.index is looking for the first occurrence of the @ symbol, so we will go to right before the at symbole
# Since we do not want to include the @ symbol in the domain, we need to increase the position by one
# Anything after the @ symbol will be saved as the domain name

# Create the message for the user
print('Your username is {} and your domain name is {}'.format(userName, domainName))

# Using the .format method to concat the user information into the string
# the {} will create placeholders to hold the variables identified in the format()
# separate the variables with commas, and you must call enough braces to make it happen

# Extra Practice:

# 1) Create an email for the user based off of there first and last name
# the program ask the user if they would like to create a an email, instead of slice it
# Then have the program have the user ask if you are creating an email for a student or a teacher.
# Follow the format below to set up the emails for the teachers and students:
# Format for student email:
# username should be lastnameF
# domain name should be 'students.uppervalleycc.org'

# format for teacher
# username: lastnameF
# domain : uppervalleycc.org

# 2) Create a login section that gives the user there username and temporary password
# The temporary password should be be the following: lastname(length of lastname)
# output:
# First Name: Taylor
# Last Name: Adami
# Username: adamit
# Password: adamit6

# 3) Super Advanced: Is there a way for us to store the information?
# Currently, everytime we close the program we are going to lose the information generated
# We can do this by importing a databaseL sqlite3, django, etc
