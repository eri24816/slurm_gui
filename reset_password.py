import sys, os
from werkzeug.security import generate_password_hash

pw = sys.argv[1]
salt = '123456uwu654321'
hash = generate_password_hash(salt+pw)

with open(f'{os.path.dirname(__file__)}/src/password.txt', 'w') as f:
    f.write(hash)