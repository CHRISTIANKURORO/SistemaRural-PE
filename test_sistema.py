
import unittest

from modelos import (
    Paciente,
    Medico,
    CentroSalud,
    AreaAtencion,
    CitaMedica
)
from agenda import AgendaMedica


class TestSistemaRural(unittest.TestCase):

    # Preparar los objetos necesarios para las pruebas
    def setUp(self):
        self.paciente = Paciente("Ana Torres", "P001")
        self.paciente2 = Paciente("Pedro Ruiz", "P002")

        self.medico = Medico(
            "Luis Perez", "M001", "Medicina General"
        )

        self.centro = CentroSalud(
            "Centro de Salud Rural Santa Rosa",
            "Av. Principal s/n",
            "Chugur"
        )

        self.area = AreaAtencion(
            "A001", "Medicina General", 1, 1
        )

        self.agenda = AgendaMedica()

    # Prueba 1: registrar una cita disponible
    def test_registrar_cita(self):
        cita = CitaMedica(
            "C001", self.paciente, self.medico,
            self.centro, self.area,
            "2026-11-20", "09:00", "09:30"
        )

        resultado = self.agenda.agregar_cita(cita)

        self.assertTrue(resultado)
        self.assertEqual(len(self.agenda.listar_citas()), 1)

    # Prueba 2: impedir dos citas del mismo medico
    # en horarios que se cruzan
    def test_evitar_cruce_horarios(self):
        cita1 = CitaMedica(
            "C001", self.paciente, self.medico,
            self.centro, self.area,
            "2026-11-20", "09:00", "09:30"
        )

        cita2 = CitaMedica(
            "C002", self.paciente2, self.medico,
            self.centro, self.area,
            "2026-11-20", "09:15", "09:45"
        )

        self.assertTrue(self.agenda.agregar_cita(cita1))
        self.assertFalse(self.agenda.agregar_cita(cita2))

    # Prueba 3: permitir un horario cuando la cita anterior
    # ha sido cancelada
    def test_horario_disponible_despues_de_cancelar(self):
        cita1 = CitaMedica(
            "C001", self.paciente, self.medico,
            self.centro, self.area,
            "2026-11-20", "09:00", "09:30"
        )

        self.agenda.agregar_cita(cita1)
        cita1.cancelar()

        cita2 = CitaMedica(
            "C002", self.paciente2, self.medico,
            self.centro, self.area,
            "2026-11-20", "09:00", "09:30"
        )

        self.assertTrue(self.agenda.agregar_cita(cita2))


if __name__ == "__main__":
    unittest.main()
