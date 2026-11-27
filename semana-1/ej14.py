username = input("Usuario: ").lower()
password = input("Contraseña: ").lower()

print(username, password)

if username == "dilan" and password == "1234":
    print("Acceso concidido")
else:
    print("Acceso denegado")