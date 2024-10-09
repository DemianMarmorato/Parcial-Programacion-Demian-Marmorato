# Función que muestra el menú interactivo. 
def menuPrincipal():
    print("1. Cargar paciente.")
    print("2. Mostrar lista de pacientes.")
    print("3. Búsqueda de paciente.")
    print("4. Ordenamiento de pacientes.")
    print("5. Mostrar paciente con mayor días de internación.")
    print("6. Mostrar paciente con menos días de internación.")
    print("7. Mostrar pacientes con más de 5 días de internación.")
    print("8. Mostrar promedio de días de internación de todos los pacientes.")
    print("9. Salir de la interfaz de manejo de pacientes del fantabuloso Demian :P")

# Función que mediante inputs toma los datos del paciente a cargar y los guarda en las variables. Hace la verificación con .isdigit() y .isalpha() que los datos correspondientes sean numeros o letras, más q nada para depuración y que el usuario no rompa el programa. 
def cargarPaciente():
    historia_clinica = input("Ingrese el número de historia clínica del paciente: ")
    if not historia_clinica.isdigit():
        print("Error: El número de historia clínica debe ser un número.")
        return
    historia_clinica = int(historia_clinica)

    nombre = input("Ingrese el nombre del paciente: ")
    if not nombre.isalpha():
        print("Error: El nombre debe contener solo letras.")
        return

    edad = input("Ingrese la edad del paciente: ")
    if not edad.isdigit():
        print("Error: La edad debe ser un número entero.")
        return
    edad = int(edad)

    genero = input("Ingrese el género del paciente (M/F): ").upper()
    if genero not in ['M', 'F']:
        print("Error: El género debe ser 'M' o 'F'.")
        return
    
    enfermedad = input("Ingrese la enfermedad del paciente: ")
    if not enfermedad.replace(" ", "").isalpha():
        print("Error: La enfermedad debe contener solo letras y espacios.")
        return
    
    dias_internacion = input("Ingrese los días de internación: ")
    if not dias_internacion.isdigit():
        print("Error: Los días de internación deben ser un número entero.")
        return
    dias_internacion = int(dias_internacion)

    paciente = {
        "historia_clinica": historia_clinica,
        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "enfermedad": enfermedad,
        "dias_internacion": dias_internacion
    }
    pacientes.append(paciente)
    print("Paciente cargado exitosamente.")

# Función que hace un bucle for enumerando los pacientes y que con f string inserta los datos del paciente en un print, más que nada para ahorrar tiempo en el debugging y que sea más leible al utilizar el programa.
def mostrarListaPacientes():
    if not pacientes:
        print("No hay pacientes cargados.")
    else:
        for i, paciente in enumerate(pacientes, start=1):
            print(f"Paciente {i}:")
            print(f"  Historia Clínica: {paciente['historia_clinica']}")
            print(f"  Nombre: {paciente['nombre']}")
            print(f"  Edad: {paciente['edad']}")
            print(f"  Género: {paciente['genero']}")
            print(f"  Enfermedad: {paciente['enfermedad']}")
            print(f"  Días de internación: {paciente['dias_internacion']}")
            print("-" * 20)

# Función que busca un paciente por su historia clinico, itera entre entre la variable de historial clinica hasta que encuentra el historial clinico introducido en el input y muestra la información de dicho paciente si es que lo encuentra, para eso está el if, si no, tira no encontrado.
def buscarPaciente():
    historia_clinica = input("Ingrese el número de historia clínica del paciente a buscar: ")
    if not historia_clinica.isdigit():
        print("Error: El número de historia clínica debe ser un número.")
        return
    historia_clinica = int(historia_clinica)
    for paciente in pacientes:
        if paciente.get("historia_clinica") == historia_clinica:
            print(f"Paciente encontrado:")
            print(f"  Nombre: {paciente['nombre']}")
            print(f"  Edad: {paciente['edad']}")
            print(f"  Género: {paciente['genero']}")
            print(f"  Enfermedad: {paciente['enfermedad']}")
            print(f"  Días de internación: {paciente['dias_internacion']}")
            return
    print("Paciente no encontrado.")

# Esta función ordena los pacientes ascendentemente por su historial clinico usando bubbleshort. Lo que hace es almacenar la totalidad de los pacientes en la variable "n", el for i in range (n) recorre la lista,  el segundo bucle hace que el numero de clientes más grande vaya a lo ultimo de la lista y el if compara  e intercambia si hay otro mayor.
def ordenamientoAscPacientes():
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n-i-1):
            if pacientes[j]["historia_clinica"] > pacientes[j+1]["historia_clinica"]:
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]
    print("Pacientes ordenados por número de historia clínica.")
    mostrarListaPacientes()

# Esta función usa un bucle for para iterar entre la lista de pacientes comparando y guardando la variable de dias_internación mas baja, la guarda y la muestra en el print, mostrando los datos del paciente.
def pacienteMayorDiasInternacion():
    if not pacientes:
        print("No hay pacientes cargados.")
        return
    
    paciente_mayor = pacientes[0]
    for paciente in pacientes:
        if paciente["dias_internacion"] > paciente_mayor["dias_internacion"]:
            paciente_mayor = paciente
    
    print("Paciente con mayor cantidad de días de internación:")
    print(f"  Historia Clínica: {paciente_mayor['historia_clinica']}")
    print(f"  Nombre: {paciente_mayor['nombre']}")
    print(f"  Edad: {paciente_mayor['edad']}")
    print(f"  Género: {paciente_mayor['genero']}")
    print(f"  Enfermedad: {paciente_mayor['enfermedad']}")
    print(f"  Días de internación: {paciente_mayor['dias_internacion']}")

# Lo mismo pero con menor días.
def pacienteMenorDiasInternacion():
    if not pacientes:
        print("No hay pacientes cargados.")
        return
    
    paciente_menor = pacientes[0]
    for paciente in pacientes:
        if paciente["dias_internacion"] < paciente_menor["dias_internacion"]:
            paciente_menor = paciente
    
    print("Paciente con menor cantidad de días de internación:")
    print(f"  Historia Clínica: {paciente_menor['historia_clinica']}")
    print(f"  Nombre: {paciente_menor['nombre']}")
    print(f"  Edad: {paciente_menor['edad']}")
    print(f"  Género: {paciente_menor['genero']}")
    print(f"  Enfermedad: {paciente_menor['enfermedad']}")
    print(f"  Días de internación: {paciente_menor['dias_internacion']}")

# Esta función lo que hace es aparte de verificar en caso de error del usuario, si no hay pacientes, tira el error, al igual q las demas funciones. La función inicia un contador o flag con 0, y tiene un bucle for que compara que los días_internados sea mayor a 5, si son mayor a 5 suma 1 al contador, luego se imprime el numero de pacientes.
def contarPacientesMasDe5Dias():
    if not pacientes:
        print("No hay pacientes cargados.")
        return

    contador = 0
    for paciente in pacientes:
        if paciente["dias_internacion"] > 5:
            contador += 1
    print(f"Cantidad de pacientes con más de 5 días de internación: {contador}")

# Esta función lo que usa es ver la lista de pacientes y sumar el total de los días_internación de todos y lo guarda en una variable, luego usa la variable y la divde por el total de pacientes utilizando len(pacientes) y printea el resultado. 
def promedioDiasInternacion():
    if not pacientes:
        print("No hay pacientes cargados.")
        return
    
    total_dias = sum(paciente["dias_internacion"] for paciente in pacientes)
    promedio = total_dias / len(pacientes)
    
    print(f"Promedio de días de internación de todos los pacientes: {promedio:.2f}")

# Esta es la función principal donde hace q el menú sea interactivo, dependiendo de la opción desencadena las funciones.
def main():
    while True:
        menuPrincipal()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            cargarPaciente()
        elif opcion == 2:
            mostrarListaPacientes()
        elif opcion == 3:
            buscarPaciente()
        elif opcion ==4:
            ordenamientoAscPacientes()
        elif opcion == 5:
            pacienteMayorDiasInternacion()
        elif opcion == 6:
            pacienteMenorDiasInternacion()
        elif opcion == 7:
            contarPacientesMasDe5Dias()
        elif opcion == 8:
            promedioDiasInternacion()
        elif opcion == 9:
            print("Gracias por usar el programa.")
            break


pacientes = []


main()
