'''
MAIN MODULE

Author: AtomMushroom
October 2022
Module version: Pre-Alpha
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
        elif terminal[0:5] == "break":
            core.Break()
        elif terminal[0:5] == "about":
            core.about()
            main()
        elif terminal[0:12] == "show modules":
            core.show_modules()
            main()
        else:
            main()
    except KeyboardInterrupt:
        core.Break()


if __name__ == '__main__':
    main()