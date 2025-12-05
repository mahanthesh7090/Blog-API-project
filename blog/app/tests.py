from django.test import TestCase

from django.contrib.auth.models import User
for u in User.objects.all():
    print(u.username)