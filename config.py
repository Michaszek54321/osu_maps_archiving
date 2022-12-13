import configparser

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
    print("You are changing Configuration")