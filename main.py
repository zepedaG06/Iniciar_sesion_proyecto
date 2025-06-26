from dao.entrenador_dao import registrar_entrenador, iniciar_sesion, listar_entrenadores

def menu_login():
    while True:
        print("\n=== MENÚ INICIO DE SESIÓN ===")
        print("1. Iniciar sesión")
        print("2. Registrar nuevo entrenador")
        print("3. Ver lista de entrenadores")
        print("4. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            usuario = iniciar_sesion()
            if usuario:
                print(f"Has iniciado sesión como: {usuario}")
                break  

        elif opcion == "2":
            registrar_entrenador()

        elif opcion == "3":
            listar_entrenadores()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")
            
            
            
    