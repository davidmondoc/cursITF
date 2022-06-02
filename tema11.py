# Avand ca exemplu pagina https://the-internet.herokuapp.com/login
# Feature: User Authentication
# Mergeti backwards si ganditi ca un product owner

# Generati un epic (doar o propozitie care sa descrie functionalitatea majora ce urmeaza sa fie dezvoltata)
'''
We are creating log in page
'''
# Generati un user story pentru login care sa aiba 2 acceptance criteria
# Un login valid (positive)
'''
as a frequent user i want to save credentials, so i will log in automatically when opening the login page

given frequent log ins
when a user opens the login page
then login automatically
'''
# Un login Invalid (negative)
'''
as a high clearance user, i want to receive a only "login error" text when wrong credentials are typed in, 
so that login process will be more secure
'''
# Generati un alt user story care sa acopere functionalitatea de register. Sa contina 2 acceptance criteria
# Email e nou, deci user poate face register (positive)
'''
For a new customer, i want to sent a welcome message with username and password when registering,
so that he has his credetials on personal email

Given we have a new customer
When a new customer registers
Then send an email with username and password
'''
# Email e deja existent in baza de date (negative)
'''
For an existing customer, i want to send and email when registering with the same email, 
so he can be reminded he is already registered with us and reset password

Given we have an existing customer
When the existing customers register
Then send a reminder email that he is already registered
'''
# Generati un ultim user story care sa acopere functionalitatea de reset password. Sa contina 2 acceptance criteria
# Email e in baza de date
'''
For an existing user, send and email with password reset steps, so he can change his password and access the account

Given we have an existing user
When clicking "forgot password"
Then send an email with password reset steps
'''
# Email nu e in baza de date
'''
For an unsubscribed user, when he request password reset, post the following error message: "email not found".

Given we have an unregistered user
When requesting password reset
Then post a pop-up the following error message: "email not found"
'''

# Reminder:
# Un user story are forma
# As a …
# I want to …
# So that …
#
# Un Acceptance criteria are forma
# Given …
# When …
# Then …

Implementați 3 pagini în noul proiect BDD cu POM
Home page https://the-internet.herokuapp.com/
Sa aiba cel putin 3 elemente inclusiv Form Authentication
Sa contina metode de click pe ele
Login page https://the-internet.herokuapp.com/login
Sa contina user, pass, login_btn si metode pt interactiune cu ele
Secure page https://the-internet.herokuapp.com/secure
Sa contina mesajul de succes si verificare ca e displayed
Sa contina logout_btn si click pe el
'''
