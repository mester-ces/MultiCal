#Librerias

from sys import stdout 

#Color Rojo

def red() :
    RED = "\033[1;31m"
    stdout.write(RED)

#Color Amarillo

def yellow() :
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

#Color Verde

def green() :
    GREEN = "\033[1;34m"
    stdout.write(GREEN)

#Negrita

def bold() :
    BOLD = "\033[1m"
    stdout.write(BOLD)

#Color Azul

def blue() :
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

#Morado

def purple() :
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

#Resetear

def reset() :
    RESET = "\033[0m"
    stdout.write(RESET)
