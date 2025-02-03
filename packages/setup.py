import os


def install(package):
    os.system("python -m pip install " + package)


def setup():
    try:
        import numpy
    except:
        install("numpy")

    try:
        import PySimpleGUI
    except:
        install("PySimpleGUI==4.57.0")

    try:
        import Crypto
    except:
        install("pycryptodome")
        install("pycryptodomex")
    try:
        import elgamal
    except:
        install("elgamal")
