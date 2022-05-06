import pytest

from dlg_monte_carlo import MonteCarloDROP, MyDataDROP

given = pytest.mark.parametrize


def test_myApp_class():
    assert MonteCarloDROP("a", "a").run() == "Hello from MonteCarloDROP"


def test_myData_class():
    assert MyDataDROP("a", "a").getIO() == "Hello from MyDataDROP"


def test_myData_dataURL():
    assert MyDataDROP("a", "a").dataURL == "Hello from the dataURL method"
