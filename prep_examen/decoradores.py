def verificar_permisos(func):
    def wrapper():
        if usuario_tiene_permisos():
            func()
        else:
            print("Lo siento, no tienes permisos para ejecutar esta función.")
    return wrapper

def usuario_tiene_permisos():
    return False

@verificar_permisos
def saludar():
    print("¡Hola, mundo!")


saludar()

