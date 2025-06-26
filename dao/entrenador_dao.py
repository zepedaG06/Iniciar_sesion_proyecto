entrenadores = {}

def registrar_entrenador():
    usuario = input("Usuario: ").strip()
    if usuario in entrenadores:
        print("Usuario ya existe.")
        return False
    contrasena = input("Contraseña: ").strip()
    entrenadores[usuario] = contrasena
    print(f"Entrenador '{usuario}' registrado correctamente.")
    return True

def iniciar_sesion():
    usuario = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()
    if usuario in entrenadores and entrenadores[usuario] == contrasena:
        print(f"Bienvenido, {usuario}!")
        return usuario
    print("Usuario o contraseña incorrectos.")
    return None

def listar_entrenadores():
    if not entrenadores:
        print("No hay entrenadores registrados.")
    else:
        print("\nLista de entrenadores registrados:")
        for usuario in entrenadores:
            print(f"- {usuario}")
