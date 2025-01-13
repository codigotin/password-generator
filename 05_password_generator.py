import random as r

# Listas
arr_letters = 'abcdefghijklmnopqrstuvwxyz'  # Usa un string para simplificar
arr_numbers = '0123456789'  # También un string
arr_symbols = '!@#$%^&*()-_=+[]{};:\'",.<>/?|\\'

print("Welcome to password generator!!!")

# Pedir la cantidad de cada tipo de carácter
qy_letters = int(input("How many letters? "))
qy_numbers = int(input("How many numbers? "))
qy_symbols = int(input("How many symbols? "))

# Generar la contraseña con una combinación de letras, números y símbolos
password_list = (
    r.choices(arr_letters, k=qy_letters) +
    r.choices(arr_numbers, k=qy_numbers) +
    r.choices(arr_symbols, k=qy_symbols)
)

# Mezclar los caracteres seleccionados
r.shuffle(password_list)

# Convertir la lista mezclada a un string
shuffled_password = ''.join(password_list)

print("Generated password:", shuffled_password)
