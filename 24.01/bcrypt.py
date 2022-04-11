

import bcrypt

parole = b'abols'

salt = bcrypt.gensalt()

savienots = bcrypt.hashpw(parole,salt)

print(parole)
print(salt)
print(savienots)


