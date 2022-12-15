import configparser, os

config = configparser.ConfigParser()
config.add_section("config")
#config.set("config", "first_time", "True")



def first_config():
    path = input('''Set Path to the archive.
It can be wherever you want.
Example: D:\osu songs \n''')
    config.set("config", "path", r"{}".format(path))

    path = input(r'''Set path to Osu!'s Songs folder.
You must go to Osu! folder and get whole path from Osu!'s Songs folder.
Example: C:\Users\barca\AppData\Local\osu!\Songs 
''')
    config.set("config", "path_to_osu", r"{}".format(path))

    

    with open(r"configfile.ini", 'w') as configfile:
        config.write(configfile)

def change_config():
    os.system("cls")
    print("You are changing Configuration")
    print("[1] Set new destination path")
    print("[2] Set new Osu! path")
    print("[3] Show configuration")

    choice = str(input("Choose: "))

    if choice == "1":
        os.system("cls")
        choice1 = str(input("Setting new destination path: "))
        config.set("config", "path", r"{}".format(choice1))

    elif choice == "2":
        os.system("cls")
        choice1 = str(input("Setting new Osu! path: "))
        config.set("config", "path", r"{}".format(choice1))

    elif choice == "3":
        os.system("cls")
        
    
    