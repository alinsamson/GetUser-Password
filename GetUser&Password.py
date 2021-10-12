import getpass
import string
import time
#import datetime
from datetime import datetime
from random import *


class PasswordGenerator:
    ''' Program care genereaza si creaza o parola si un username.
    :arg
        Name - primeste numele pentru generare username
        Prename - primeste prenumele pentru crearea username-ului

    :returns
        Genereaza un username bazat pe datele utilizatorului
        & o parola aleatoare, pentru care solicita schimbarea acesteia
        cu o parola preferentiala.
    '''

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_password(self):
        user_name = self.surname[0].lower() + '.' + self.name.capitalize()
        characters = string.ascii_letters + string.digits
        password = "".join(choice(characters) for x in range(randint(8, 12)))
        print('-' * 57)
        print(f'Username:{user_name} -- Password: {password}')
        print('After your first login, please change the password.')
        print('-'*57)

    def change_password(self):
        user_name = self.surname[0].lower() + '.' + self.name.capitalize()
        characters = string.ascii_letters + string.digits
        password = "".join(choice(characters) for x in range(randint(8, 12)))
        password = getpass.getpass('Insert a password:')
        afisare = input('Do you want to show your password?  Yes/No - ')
        if afisare.lower() == 'yes':
            print(f'Username: {user_name} -- New Password:{password}')
        print('-' * 57)


def ProgramControl():
    Name = input('Surname:')
    Surname = input('Name:')
    User_name1 = PasswordGenerator(Name, Surname)
    User_name1.get_password()
    User_name1.change_password()


ProgramControl()
