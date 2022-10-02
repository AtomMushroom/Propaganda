### CORE MODULE ###
'''
Author: AtomMushroom
October 2022
Module version: 0.1
'''
global art
art = '''                                                                                                                                                                                                                               

88888888ba                ,a8888a,                  ,ad88PPP88ba,                ,ad88PPP88ba,                       88   ,ad88PPP88ba,   
88      "8b             ,8P"'  `"Y8,               d8"  .ama.a "8a              d8"  .ama.a "8a                      88  d8"  .ama.a "8a  
88      ,8P            ,8P        Y8,             d8'  ,8P"88"  88             d8'  ,8P"88"  88                      88 d8'  ,8P"88"  88  
88aaaaaa8P' 8b,dPPYba, 88          88 8b,dPPYba,  88  .8P  8P   88  ,adPPYb,d8 88  .8P  8P   88 8b,dPPYba,   ,adPPYb,88 88  .8P  8P   88  
88""""""'   88P'   "Y8 88          88 88P'    "8a 88  88   8'   8P a8"    `Y88 88  88   8'   8P 88P'   `"8a a8"    `Y88 88  88   8'   8P  
88          88         `8b        d8' 88       d8 88  8B ,d8 ,ad8' 8b       88 88  8B ,d8 ,ad8' 88       88 8b       88 88  8B ,d8 ,ad8'  
88          88          `8ba,  ,ad8'  88b,   ,a8" "8a "88P"888P"   "8a,   ,d88 "8a "88P"888P"   88       88 "8a,   ,d88 "8a "88P"888P"    
88          88            "Y8888P"    88`YbbdP"'   `Y8aaaaaaaad8P   `"YbbdP"Y8  `Y8aaaaaaaad8P  88       88  `"8bbdP"Y8  `Y8aaaaaaaad8P   
                                      88              """""""""     aa,    ,88     """""""""                                """""""""     
                                      88                             "Y8bbdP"                                                             
Type "help", to see all commands

'''
class color:
    Green = '\033[32m'
    Red = '\033[31m'
    Blue = '\033[34m'
    Purple = '\033[95m'
    Cyan = '\033[96m'
    Yellow = '\033[93m'
    Bold = '\033[1m'
    Endc = '\033[0m'


def help():
    print("\n")
    print(color.Blue + "Commands\t\tDescription" + color.Endc)
    print(color.Green + "---------------\t\t----------------" + color.Endc)
    print("help \t\t\tShow All Commands")
    print("show modules \t\t\tShow All Modules")
    print("use \t\t\tSelect Module to Use")
    print("back \t\t\tExit Current Module")
    print("run \t\t\tExecute Module")
    print("about \t\t\tAbout Author")