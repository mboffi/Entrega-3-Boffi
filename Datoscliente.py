class Cliente:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
