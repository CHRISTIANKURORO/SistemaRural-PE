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
