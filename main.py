# ==========================================
# PROGRAMA PRINCIPAL - SISTEMA RURAL-PE
# ==========================================
from modelos import Paciente, Medico, CentroSalud, AreaAtencion
from gestor import GestorCitas

# Crear datos ficticios
paciente1 = Paciente("Ana Torres", "P001")
medico1 = Medico("Luis Perez", "M001", "Medicina General")

centro = CentroSalud(
    "Centro de Salud Rural Santa Rosa",
    "Av. Principal s/n",
    "Chugur"
)

area = AreaAtencion("A001", "Medicina General", 1, 1)

# Crear el gestor del sistema
gestor = GestorCitas()

# Registrar una cita de prueba
try:
    cita = gestor.registrar_cita(
        "C001",
        paciente1,
        medico1,
        centro,
        area,
        "2026-11-10",
        "09:00",
        "09:30"
    )

    print("CITA REGISTRADA CORRECTAMENTE")
    print(cita.mostrar_detalle())

except ValueError as error:
    print("Error:", error)

# Consultar las citas registradas
print("\nLISTA DE CITAS")

for cita in gestor.consultar_citas():
    print(cita.codigo, "-", cita.paciente.nombre, "-", cita.fecha)


# ==========================================
# PRUEBA DE HORARIO OCUPADO
# ==========================================
print("\nPRUEBA DE HORARIO OCUPADO")

try:
    gestor.registrar_cita(
        "C002",
        Paciente("Pedro Ruiz", "P002"),
        medico1,
        centro,
        area,
        "2026-11-10",
        "09:15",
        "09:45"
    )

except ValueError as error:
    print("No se pudo registrar:", error)

# ==========================================
# PRUEBAS DE PROGRAMACION FUNCIONAL
# ==========================================

# 1. FILTER: filtrar citas programadas
print("\nCITAS PROGRAMADAS")

citas_programadas = gestor.filtrar_citas_programadas()

for cita in citas_programadas:
    print(cita.codigo, "-", cita.estado)


# 2. MAP: obtener los codigos de las citas
print("\nCODIGOS DE LAS CITAS")

codigos = gestor.obtener_codigos_citas()
print(codigos)


# 3. REDUCE: contar las citas programadas
print("\nTOTAL DE CITAS PROGRAMADAS")

total = gestor.contar_citas_programadas()
print(total)


# ==========================================
# PRUEBA DE MANEJO DE ERRORES
# ==========================================

print("\nPRUEBA DE FECHA INCORRECTA")

try:
    gestor.registrar_cita(
        "C003",
        Paciente("Maria Lopez", "P003"),
        medico1,
        centro,
        area,
        "2026-15-40",
        "10:00",
        "10:30"
    )

except ValueError as error:
    print("Error controlado:", error)


# ==========================================
# PRUEBA DE HORARIO INCORRECTO
# ==========================================

print("\nPRUEBA DE HORARIO INCORRECTO")

try:
    gestor.registrar_cita(
        "C004",
        Paciente("Carlos Ruiz", "P004"),
        medico1,
        centro,
        area,
        "2026-11-10",
        "11:00",
        "10:00"
    )

except ValueError as error:
    print("Error controlado:", error)


# ==========================================
# PRUEBA DE BUSQUEDA INEXISTENTE
# ==========================================

print("\nPRUEBA DE BUSQUEDA INEXISTENTE")

try:
    gestor.buscar_cita("C999")

except ValueError as error:
    print("Error controlado:", error)


# ==========================================
# PRUEBA DE CANCELACION Y MODIFICACION
# ==========================================

print("\nPRUEBA DE CANCELACION")

try:
    gestor.cancelar_cita("C001")
    print("Cita C001 cancelada correctamente")

except ValueError as error:
    print("Error controlado:", error)


print("\nPRUEBA DE MODIFICACION DE CITA CANCELADA")

try:
    gestor.modificar_cita(
        "C001",
        "2026-11-11",
        "11:00",
        "11:30"
    )

except ValueError as error:
    print("Error controlado:", error)
