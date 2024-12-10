import random as r, string as s

elements = s.ascii_letters+s.digits+s.ascii_lowercase+s.ascii_uppercase+s.hexdigits+s.punctuation

lenght = int(input("Introduzca la longitud de la contraseña: "))

password = ""

for i in range(lenght):
    password += r.choice(elements)

print(password)