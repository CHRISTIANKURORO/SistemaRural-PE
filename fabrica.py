# ==========================================
# FABRICA DE CITAS DEL SISTEMA RURAL-PE
# ==========================================
from modelos import CitaMedica

class CitaFactory:

    # Crear una nueva cita medica
    def crear_cita(
        self, codigo, paciente, medico, centro, area,
        fecha, hora_inicio, hora_fin
    ):
        nueva_cita = CitaMedica(
            codigo,
            paciente,
            medico,
            centro,
            area,
            fecha,
            hora_inicio,
            hora_fin
        )

        return nueva_cita
