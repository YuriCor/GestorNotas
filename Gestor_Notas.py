from collections import deque

cursos = []             # Lista de tuplas: (nombre, nota)
historial = []          # Pila (lista)
cola_revision = deque() # Cola (deque)

# Registrar cursos--------------------------------------------------------
def registrar_curso():
    print("REGISTRAR CURSO")

    # solicitar nombre con validaciones
    while True:
        nombre_curso = input("Ingrese el nombre del curso: ")
        if nombre_curso.strip() == "":
            print("Error: El nombre del curso no puede estar vacio.")
        else:
            break

    # Solicitar nota Y su validacion
    while True:
        try:
            nota_input = input("Ingrese la nota obtenida (0-100): ")
            if nota_input.strip() == "":
                print("Error: La nota no puede estar vacia. ")
                continue

            nota = float(nota_input)
            if nota < 0 or nota > 100:
                print("Error: La nota debe estar 0 y 100.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un valor numerico.")

    # Guardar curso como tupla
    cursos.append((nombre_curso, nota))
    historial.append(f"Se registro el curso '{nombre_curso}' con nota {nota:.2f}")

    print(f"Curso '{nombre_curso}' con nota {nota:.2f} registrado con exito.")
    return nombre_curso, nota

# Mostrar cursos ------------------------------------------------------------------
def mostrar_curso():
    print("CURSOS REGISTRADOS")
    if not cursos:
        print("No hay cursos registrados.")
    else:
        for i, (curso, nota) in enumerate (cursos, start=1):
            print(f"{i}. {curso} - {nota:.2f}")
        print()

# Calcular promedio -------------------------------------------------------
def calcular_promedio():
    print("PROMEDIO")
    if not cursos:
        print("No hay cursos registrados.")
    else:
        promedio = sum(nota for _, nota in cursos) / len(cursos)
        print(f"El promedio general es: {promedio:.2f}")

#cursos aprobados y reprobados ------------------------------------------------------
def contar_aprobados_reprobados():
    print("CURSOS APROBADOS Y REPROBADOS")
    if not cursos:
        print("No hay cursos registrados.")
    else:
        aprobados = sum(1 for _, nota in cursos if nota >= 61)
        reprobados = len(cursos) - aprobados
        print(f"Cursos aprobados: {aprobados}")
        print(f"Cursos reprobados: {reprobados}")

# buscar cursos lineal
def buscar_curso_lineal(nombre):
    print("BUSCAR CURSO (LINEAL)")
    for curso, nota in cursos:
        if curso.lower() == nombre.lower():

            return (curso, nota)
    print("Curso no encontrado.")
    return None
    
# Actualizar nota ---------------------------------------------------------------------
def actualizar_nota():
    print("ACTUALIZAR NOTA DE UN CURSO")
    if not cursos:
        print("No hay cursos registrados.")
        return
    
    nombre = input("Ingrese el nombre del curso a actualizar: ").strip()
    for i, (curso, nota) in enumerate (cursos):
        if curso.lower() == nombre.lower():
            while True:
                try:
                    nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
                    if not (0 <= nueva_nota <= 100):
                        print("Error: La nota debe estar entre 0 y 100.")
                        continue
                    cursos[i] = (curso, nueva_nota)
                    historial.append(f"Se actualizo la nota del curso '{curso}' a {nueva_nota:.2f}")
                    print(f"Nota del curso '{curso}' actualizada a {nueva_nota:.2f}")
                    return
                except ValueError:
                    print("Error: Debe ingresar un valor numerico.")
    print("Curso no encontrado")

# Eliminar curso -----------------------------------------------------------
def eliminar_curso():
    print("ELIMINAR CURSO")
    if not cursos:
        print("No hay cursos registrados")
        return
    
    nombre = input("Ingrese el nombre del curso a eliminar: ").strip()
    for i, (curso, _) in enumerate(cursos):
        if curso.lower() == nombre.lower():
            eliminado = cursos.pop(i)
            historial.append(f"Se elimino el curso '{eliminado[0]}'")
            print(f"Curso '{eliminado[0]}' eliminado con exito. ")
            return
    print("Curso no encontrado.")

# Ordenamiento burbuja----------------------------------------------------------------------
def ordenar_burbuja():
    print("ORDENAR CURSOS POR NOTA (BURBUJA)")
    if not cursos:
        print("No hay cursos registrados. ")
        return
    
    lista = cursos[:]
    n = len(lista)
    for i in range(n -1):
        for j in range(n - i - 1):
            if lista[j][1] > lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    for curso, nota in lista:
        print(f"{curso} - {nota:.2f}")
    print()

# Ordenamiento insercion ----------------------------------------------------
def ordenar_insercion():
    print("ORDENAR CURSOS POR NOMBRE (INSERCION)")
    if not cursos:
        print("No hay cursos registrados. ")
        return
    
    lista = cursos[:]
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i -1
        while j >= 0 and lista[j][0].lower() > clave[0].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

    for curso, nota in lista:
        print(f"{curso} - {nota:.2f}")
    print()

# Busqueda binaria -----------------------------------------------------
def buscar_binaria(nombre):
    print("BUSCAR CURSO (BINARIA)")
    if not cursos:
        print("No hay cursos registrados")
        return None
    
    lista = sorted(cursos, key=lambda x: x[0].lower())
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio][0].lower() == nombre.lower():
           
            return lista[medio]
        elif lista[medio][0].lower() < nombre.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    print("Curso no encontrado.")
    return None

# Simular cola-----------------------------------------------------------------------
def simular_cola_revision():
    print("COLA DE SOLICITUDES PARA REVISION")
    while True:
        print("1. Agregar solicitud")
        print("2. Atender solicitud")
        print("3. Mostrar cola")
        print("4. Volver al menu principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese el curso a revisar: ").strip()
            if nombre:
                cola_revision.append(nombre)
                print(f"Solicitud para revisar '{nombre}' agregada. ")
            else:
                print("El nombre no puede estar vacio. ")

        elif opcion == "2":
            if cola_revision:
                atendido = cola_revision.popleft()
                print(f"Se atendio la solicitud de '{atendido}'. ")
            else:
                print("No hay solicitudes en cola. ")

        elif opcion == "3":
            print("Cola de solicitudes: ", list(cola_revision), )

        elif opcion == "4":
            break

        else:
            print("Opcion invalida.")

# Historial -----------------------------------------------------------
def mostrar_historial():
    print("HISTORIAL DE CAMBIOS")
    if not historial:
        print("No hay cambios registrados.")
    else:
        for i, cambio in enumerate(reversed(historial), start=1):
            print(f"{i}. {cambio}")
        print()

# Menu principal -------------------------------------------------------------------------
def main():
    while True:
        print("GESTOR DE NOTAS")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar curso por nombre (busqueda lineal)")
        print("6. Actualizar nota de un curso")
        print("7. Eliminar un curso")
        print("8. Ordenar cursos por nota (burbuja)")
        print("9. Ordenar cursos por nombre (insercion)")
        print("10. Buscar curso por nombre (busqueda binaria)")
        print("11. Simular cola de solicitudes de revision")
        print("12. Mostrar historial de cambios (pila)")
        print("13. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_curso()
        elif opcion == "2":
            mostrar_curso()
        elif opcion == "3":
            calcular_promedio()
        elif opcion == "4":
            contar_aprobados_reprobados()
        elif opcion == "5":
            nombre = input("Ingrese el nombre del curso a buscar: ").strip()
            curso = buscar_curso_lineal(nombre)
            if curso:
                print(f"Curso encontrado: {curso[0]} - {curso[1]:.2f}")
            else:
                print("Curso no encontrado. ")
        elif opcion == "6":
            actualizar_nota()
        elif opcion == "7":
            eliminar_curso()
        elif opcion == "8":
            ordenar_burbuja()
        elif opcion == "9":
            ordenar_insercion()
        elif opcion == "10":
            nombre = input("Ingrese el nombre del curso a buscar: ").strip()
            curso = buscar_binaria(nombre)
            if curso:
                print(f"Curso encontrado: {curso[0]} - {curso[1]:.2f}" )
            else:
                print("Curso no encontrado.")
        elif opcion == "11":
            simular_cola_revision()
        elif opcion == "12":
            mostrar_historial()
        elif opcion == "13":
            print("Saliendo del sistema.....")
            break
        else:
            print("Opcion invalida.")

#----------------------------------------------------------------------
if __name__ == "__main__":
    main()







