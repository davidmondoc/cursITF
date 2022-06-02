# password checker

user_name='admin'
user_password='admin'

input_user_name=input('introdu nume utilizator')
input_user_password=input('introdu parola')

#TESTEZA CODUL DE LA LINIILE 10-13
if user_name==input_user_name and user_name==input_user_password:
   print('utilizator logat')
else:
    print('mai incearca')


assert user_name==input_user_name
assert user_password==input_user_password
