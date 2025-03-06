import os
import datetime
import sys

# Crear carpeta para los clientes
def inicializar_directorio():
    if not os.path.exists('clientes'):
        os.makedirs('clientes')
    return True

# Función para mostrar menú
def mostrar_menu():
    print("\n=== GESTOR DE CLIENTES SKY ===")
    print("1. Ver lista de clientes")
    print("2. Ver cliente")
    print("3. Crear cliente nuevo")
    print("4. Agregar servicio")
    print("5. Salir")
    print("=============================")
    return input("Elija una opción: ")

# Función para ver lista de clientes
def ver_lista():
    print("\nCLIENTES:")
    archivos = os.listdir('clientes')
    if len(archivos) == 0:
        print("No hay clientes")
    else:
        for archivo in archivos:
            print(f"- {archivo}")
    return True

# Función para ver un cliente
def ver_cliente(nombre=None):
    if nombre is None:
        nombre = input("\nNombre del cliente: ")
    
    ruta = f"clientes/{nombre}.txt"

    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo:
            contenido = archivo.read()
        print("\nINFORMACIÓN DEL CLIENTE:")
        print(contenido)
        return True
    else:
        print("Cliente no existe")
        return False

# Función para crear cliente nuevo
def crear_cliente(nombre=None, direccion=None, telefono=None, servicio=None):
    if nombre is None:
        nombre = input("\nNombre del cliente nuevo: ")
    
    ruta = f"clientes/{nombre}.txt"

    if os.path.exists(ruta):
        print("Este cliente ya existe")
        return False

    if direccion is None:
        direccion = input("Dirección: ")
    
    if telefono is None:
        telefono = input("Teléfono: ")
    
    if servicio is None:
        servicio = input("Servicio: ")
    
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")

    with open(ruta, 'w') as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Dirección: {direccion}\n")
        archivo.write(f"Teléfono: {telefono}\n")
        archivo.write(f"Fecha registro: {fecha}\n\n")
        archivo.write(f"SERVICIOS:\n")
        archivo.write(f"- {servicio} ({fecha})\n")

    print("Cliente creado correctamente")
    return True

# Función para agregar servicio
def agregar_servicio(nombre=None, servicio=None):
    if nombre is None:
        nombre = input("\nNombre del cliente: ")
    
    ruta = f"clientes/{nombre}.txt"

    if os.path.exists(ruta):
        if servicio is None:
            servicio = input("Nuevo servicio: ")
        
        fecha = datetime.datetime.now().strftime("%Y-%m-%d")

        with open(ruta, 'a') as archivo:
            archivo.write(f"- {servicio} ({fecha})\n")

        print("Servicio agregado correctamente")
        return True
    else:
        print("Cliente no existe")
        return False

# Función principal que se puede llamar desde CLI o ejecutar interactivamente
def main():
    # Inicializar directorio
    inicializar_directorio()
    
    # Verificar si hay argumentos de línea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        
        # Ejecutar comando desde argumentos
        if comando == "listar":
            return ver_lista()
        
        elif comando == "ver" and len(sys.argv) > 2:
            return ver_cliente(sys.argv[2])
        
        elif comando == "crear" and len(sys.argv) > 5:
            return crear_cliente(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        
        elif comando == "agregar" and len(sys.argv) > 3:
            return agregar_servicio(sys.argv[2], sys.argv[3])
        
        else:
            print("Uso:")
            print("  python gestor_clientes.py listar")
            print("  python gestor_clientes.py ver <nombre>")
            print("  python gestor_clientes.py crear <nombre> <direccion> <telefono> <servicio>")
            print("  python gestor_clientes.py agregar <nombre> <servicio>")
            return False
    
    # Modo interactivo
    else:
        while True:
            opcion = mostrar_menu()

            if opcion == "1":
                ver_lista()
            elif opcion == "2":
                ver_cliente()
            elif opcion == "3":
                crear_cliente()
            elif opcion == "4":
                agregar_servicio()
            elif opcion == "5":
                print("Adiós")
                break
            else:
                print("Opción no válida")
        
        return True

# Ejecutar el programa
if __name__ == "__main__":
    main()
