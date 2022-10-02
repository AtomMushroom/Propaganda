'''
CRYPTO MODULE

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
def atbash(message):
    return message[::-1]
### Atbash ###

### ROT13 ###
def rot13(message):
    message = list(message.upper())
    for symbol in range(len(message)):
        message[symbol] = chr(ord(message[symbol])%26+ord('A'))
    return "".join(message)
### ROT13 ###

### XOR ###
def xor(message, key):
    message = list(message)
    for symbol in range(len(message)):
        try: message[symbol] = chr(ord(message[symbol]) ^ int(key))
        except: return ":: Key is not int type ::"
    return "".join(message)
### XOR ###