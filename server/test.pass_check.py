from sys import argv as a
from models import *

j = User.query.first()
j.check_pass(a[1])
