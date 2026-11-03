# ==========================================
# AGENDA MEDICA DEL SISTEMA RURAL-PE
# ==========================================
class AgendaMedica:
    def __init__(self):
        # Lista donde se almacenarán las citas
        self.__lista_citas = []

    # Agregar una cita a la agenda
    def agregar_cita(self, cita):
        if self.verificar_disponibilidad(cita):
            self.__lista_citas.append(cita)
            return True

        return False

    # Buscar una cita por su código
    def buscar_cita(self, codigo):
        for cita in self.__lista_citas:
            if cita.codigo == codigo:
                return cita

        return None

    # Mostrar todas las citas registradas
    def listar_citas(self):
        return self.__lista_citas

    # Verificar si el médico está disponible
    def verificar_disponibilidad(self, nueva_cita):
        for cita in self.__lista_citas:
            if (
                cita.medico.codigo_medico == nueva_cita.medico.codigo_medico
                and cita.fecha == nueva_cita.fecha
                and cita.estado == "Programada"
                and nueva_cita.hora_inicio < cita.hora_fin
                and nueva_cita.hora_fin > cita.hora_inicio
            ):
                return False

        return True
    