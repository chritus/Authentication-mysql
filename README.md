

Fuctionalities:
Users can input their email and password in the provided entry fields.
The script validates the input data, ensuring that all fields are filled and that the password matches the confirmation.
It checks if the email already exists in the database to avoid duplicate registrations.
Upon successful registration, the user data is inserted into the MySQL database.
Error messages are displayed if any issues occur during the registration process.

How you can run the script:
Install the required libraries: pip install mysql-connector-python pillow
Set up a MySQL database with the following details:
Host: localhost
User: root
Password: 123prince

Files:
signup.py: Main Python script containing the user signup application code.
background_image.jpg: Background image displayed on the signup window.
signin_page.py: Module for importing the signin page (not provided in the script).
