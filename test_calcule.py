import pytest
from calcul import adunare, scadere, inmultire, impartire

def test_adunare():
    assert adunare(2, 3) == 5

def test_scadere():
    assert scadere(5, 3) == 2

def test_inmultire():
    assert inmultire(4, 3) == 12

def test_impartire():
    assert impartire(10, 2) == 5

def test_impartire_zero():
    with pytest.raises(ValueError):
        impartire(10, 0)
