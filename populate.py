import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User

from faker import Faker

fakegen = Faker()

def addUsers(N=5):
    i = 0
    for i in range(N):
        fake_fn = fakegen.first_name_male()

        fake_ln = fakegen.first_name_male()

        fake_email = fakegen.email()

        User.objects.get_or_create(first_name = fake_fn,
                                   last_name = fake_ln,
                                   email = fake_email)
if __name__ == '__main__':
    print('populating script!')
    addUsers(50)
    print("populating complete")