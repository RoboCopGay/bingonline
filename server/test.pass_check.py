from pages.models import *
from sys import argv as a

j = User.query.first()
j.check_pass(a[1])
