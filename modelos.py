
# ==========================================
# MODELOS INICIALES DEL SISTEMA RURAL-PE
# ==========================================

# Clase principal Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_datos(self):
        return self.nombre


# Clase Paciente: hereda de Persona
class Paciente(Persona):
    def __init__(self, nombre, codigo_paciente):
        super().__init__(nombre)
        self.codigo_paciente = codigo_paciente

    def mostrar_datos(self):
        return f"Paciente: {self.nombre} - Código: {self.codigo_paciente}"


# Clase Medico: hereda de Persona
class Medico(Persona):
    def __init__(self, nombre, codigo_medico, especialidad):
        super().__init__(nombre)
        self.codigo_medico = codigo_medico
        self.especialidad = especialidad

    def mostrar_datos(self):
        return f"Médico: {self.nombre} - Especialidad: {self.especialidad}"


# Clase CentroSalud
class CentroSalud:
    def __init__(self, nombre, direccion, distrito):
        self.nombre = nombre
        self.direccion = direccion
        self.distrito = distrito

    def mostrar_informacion(self):
        return f"{self.nombre} - {self.distrito}"


# Clase AreaAtencion
class AreaAtencion:
    def __init__(self, codigo, nombre, piso, puerta):
        self.codigo = codigo
        self.nombre = nombre
        self.piso = piso
        self.puerta = puerta

    def mostrar_ubicacion(self):
        return f"{self.nombre} - Piso {self.piso} - Puerta {self.puerta}"


# Clase CitaMedica
class CitaMedica:
    def __init__(self, codigo, paciente, medico, centro, area,
                 fecha, hora_inicio, hora_fin):
        self.codigo = codigo
        self.paciente = paciente
        self.medico = medico
        self.centro = centro
        self.area = area
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.estado = "Programada"

    def modificar(self, fecha, hora_inicio, hora_fin):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def cancelar(self):
        self.estado = "Cancelada"

    def mostrar_detalle(self):
        return (
            f"Cita: {self.codigo}\n"
            f"Paciente: {self.paciente.nombre}\n"
            f"Médico: {self.medico.nombre}\n"
            f"Fecha: {self.fecha}\n"
            f"Horario: {self.hora_inicio} - {self.hora_fin}\n"
            f"Estado: {self.estado}"
        )
