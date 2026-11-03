# ==========================================
# GESTOR DE CITAS DEL SISTEMA RURAL-PE
# ==========================================
from agenda import AgendaMedica
from fabrica import CitaFactory

class GestorCitas:

    def __init__(self):
        self.__agenda = AgendaMedica()
        self.__fabrica = CitaFactory()

    # Registrar una nueva cita
    def registrar_cita(
        self, codigo, paciente, medico, centro, area,
        fecha, hora_inicio, hora_fin
    ):
        nueva_cita = self.__fabrica.crear_cita(
            codigo, paciente, medico, centro, area,
            fecha, hora_inicio, hora_fin
        )

        if self.__agenda.agregar_cita(nueva_cita):
            return nueva_cita

        raise ValueError("El medico ya tiene una cita en ese horario")

    # Consultar todas las citas
    def consultar_citas(self):
        return self.__agenda.listar_citas()

    
    # Consultar solamente las citas programadas
    def filtrar_citas_programadas(self):
        return self.__agenda.filtrar_citas_programadas()

    # Obtener los codigos de las citas
    def obtener_codigos_citas(self):
        return self.__agenda.obtener_codigos_citas()

    # Contar las citas programadas
    def contar_citas_programadas(self):
        return self.__agenda.contar_citas_programadas()

    # Buscar una cita por su codigo
    def buscar_cita(self, codigo):
        cita = self.__agenda.buscar_cita(codigo)

        if cita is None:
            raise ValueError("No se encontro la cita")

        return cita

    # Modificar una cita existente
    def modificar_cita(self, codigo, fecha, hora_inicio, hora_fin):
        cita = self.buscar_cita(codigo)

        if cita.estado == "Cancelada":
            raise ValueError("No se puede modificar una cita cancelada")

        cita_temporal = self.__fabrica.crear_cita(
            cita.codigo, cita.paciente, cita.medico,
            cita.centro, cita.area, fecha, hora_inicio, hora_fin
        )

        if not self.__agenda.verificar_disponibilidad(cita_temporal):
            raise ValueError("El medico ya tiene una cita en ese horario")

        cita.modificar(fecha, hora_inicio, hora_fin)
        return cita

    # Cancelar una cita
    def cancelar_cita(self, codigo):
        cita = self.buscar_cita(codigo)

        if cita.estado == "Cancelada":
            raise ValueError("La cita ya se encuentra cancelada")

        cita.cancelar()
        return cita
