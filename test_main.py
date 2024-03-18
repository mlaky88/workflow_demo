import main

def test_sestej():
    assert main.sestej(1, 2) == 3
    assert main.sestej(0, 0) == 0

def test_odstej():
    assert main.odstej(1, 2) == -1
    assert main.odstej(0, 0) == 0

def test_zmnozi():
    assert main.zmnozi(1, 2) == 2
    assert main.zmnozi(0, 0) == 0
    assert main.zmnozi(1, 0) == 0