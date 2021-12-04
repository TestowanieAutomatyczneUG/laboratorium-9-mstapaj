import unittest
from src.CarImpl import CarImpl
from src.Car import Car
from unittest.mock import Mock


class test_CarImpl(unittest.TestCase):
    def setUp(self):
        self.temp = Car()

    def test_needsFuel_false(self):
        self.temp.needsFuel = Mock(name='needsFuel')
        self.temp.needsFuel.return_value = False
        carimpl=CarImpl(self.temp)
        self.assertEqual(carimpl.car_checkFuel(),"Mało paliwa")

    def test_needsFuel_true(self):
        self.temp.needsFuel = Mock(name='needsFuel')
        self.temp.needsFuel.return_value = True
        carimpl=CarImpl(self.temp)
        self.assertEqual(carimpl.car_checkFuel(),"Paliwo w normie")

    def test_getEngineTemperature_80(self):
        self.temp.getEngineTemperature = Mock(name='getEngineTemperature')
        self.temp.getEngineTemperature.return_value = 80
        carimpl=CarImpl(self.temp)
        self.assertEqual(carimpl.car_checkEngineTemperature(),"Temperatura silnika w normie")

    def test_getEngineTemperature_110(self):
        self.temp.getEngineTemperature = Mock(name='getEngineTemperature')
        self.temp.getEngineTemperature.return_value = 110
        carimpl=CarImpl(self.temp)
        self.assertEqual(carimpl.car_checkEngineTemperature(),"Za wysoka temperatura silnika")

    def test_driveTo_Gdansk(self):
        self.temp.driveTo=Mock(name='driveTo')
        self.temp.driveTo.return_value='Gdańsk'
        carimpl=CarImpl(self.temp)
        self.assertEqual(carimpl.car_setDesitnation('Gdańsk'),"Cel ustawiono na Gdańsk")

    def test_driveTo_Wroclaw(self):
        self.temp.driveTo=Mock(name='driveTo')
        self.temp.driveTo.return_value='Wrocław'
        carimpl=CarImpl(self.temp)
        self.assertEqual(carimpl.car_setDesitnation('Wrocław'),"Cel ustawiono na Wrocław")
