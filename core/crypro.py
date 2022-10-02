### CRYPTO MODULE ###
'''
Author: AtomMushroom
October 2022
Module version: 0.1
'''
from re import findall

def getNumbers(text): #Return numbers from any text
    template = r"[0-9]+"
    return findall(template, text)

### A1Z26 ###
def a1z26(mode, message, final = ""):
    message = message.upper()
    alpha = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if mode == 'E':
        for symbol in message:
            if symbol not in [chr(x) for x in range(65,91)]:
                message = message.replace(symbol, '')
        for symbol in message:
            final += "%hu "%(alpha.index(symbol)+1)
    else:
        for number in getNumbers(message):
            final += "%s"%alpha[int(number)-1]
    return final
### A1Z26 ###

### Atbash ###
### Atbash ###