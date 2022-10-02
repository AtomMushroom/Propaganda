'''
MAIN MODULE

Author: AtomMushroom
October 2022
Module version: 0.1
'''
from core import core
from core import crypro
print(core.color.Red + core.art + core.color.Endc)
def main():
    try:
        terminal = input(" > ")
        if terminal[0:4] == "help":
            core.help()
            main()
    except (KeyboardInterrupt):
        print(core.color.Red + "\n[*] (Ctrl + C ) Detected, Trying To Exit ..." + core.color.Endc)
        print(core.color.Yellow + "[*] Thank You For Using Propaganda toolkit =)" + core.color.Endc)

if __name__ =='__main__':
    main()