# ==========================================
# AGENDA MEDICA DEL SISTEMA RURAL-PE
# ==========================================
from functools import reduce
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

    # Filtrar las citas que estan programadas
    def filtrar_citas_programadas(self):
        return list(filter(
            lambda cita: cita.estado == "Programada",
            self.__lista_citas
        ))

    # Obtener los codigos de todas las citas
    def obtener_codigos_citas(self):
        return list(map(
            lambda cita: cita.codigo,
            self.__lista_citas
        ))

    # Contar las citas que estan programadas
    def contar_citas_programadas(self):
        citas = self.filtrar_citas_programadas()

        return reduce(
            lambda total, cita: total + 1,
            citas,
            0
        )

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
    