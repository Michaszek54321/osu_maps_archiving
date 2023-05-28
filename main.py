import config
import os
import time
import psutil
import configparser
#first configuration
if os.path.isfile("configfile.ini") == False:
    print('''This is your first time you are running this code.
You have to configure the paths to your Osu! folder and destination folder.
Then I'll create first archive of your Songs Folder and that would wrap up the configuration.\n''')
    time.sleep(1)
    config.first_config()
    print("Config file created.")
    time.sleep(0.1)
    import old_list
    old_list.tworzenie(old_list.wyciaganie())
    import archive 
    print("Up to date list of maps created.")
    # time.sleep(0.1)
    # print("Now Archiving. This might take a while depending on the number of maps in the folder")
    # print("I'll inform you when it's done. Do not close the program...")
    # archive.Archive()
    # time.sleep(2)
else:
    import old_list
    import archive

def waiting_osu():
    osu_process = []
    process = filter(lambda p: p.name() == "osu!.exe", psutil.process_iter())
    for i in process:
        osu_process = i.pid

    if len(osu_process)>0:
        return psutil.pid_exists(osu_process)
    else:
        return False

def last_changes():
    c = configparser.ConfigParser()
    c.read("configfile.ini")
    c = c["config"]
    os.system("cls")
    print(c["difflist"])
    print("U can find last archived maps in this codes folder in 'configfile.ini'")
    input("Press Enter to continue:")

def export_last_changes():
    c = configparser.ConfigParser()
    c.read("configfile.ini")
    c = c["config"]
    t = open("last changes.txt","w")
    t.write(c["difflist"])
    os.system("cls")
    print("File is in this programs rolder")
    input("Press Enter to continue:")


def base():
    ongoing = True
    
    while ongoing == True:
        os.system("cls")
        print("[1] Archive New Maps")
        print("[2] Force Archive")
        print("[3] Change Configuration")
        print("[4] Show last changes")
        print("[5] Export last changes")
        print("[0] Exit")

        choice = str(input("Choose: "))

        if choice == "1":
            archive.add_archive()
        
        elif choice == "2":
            archive.Archive()
        
        elif choice == "3":
            config.change_config()

        elif choice == "4":
            last_changes()

        elif choice == "5":
            export_last_changes()

        elif choice == "0":
            ongoing = False


base()
# while True:
#     print(waiting_osu())
