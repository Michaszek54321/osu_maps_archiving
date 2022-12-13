import config
import configparser
import os
import time
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
    time.sleep(0.1)
    print("Now Archiving. This might take a while depending on the number of maps in the folder")
    print("I'll inform you when it's done. Do not close the program...")
    archive.Archive()
else:
    import old_list
    import archive

print("[1] nowe piosenki")

choice = str(input("wybierz"))



# print("[2] archiwizuj do folderu")
# print("[3] domyślna ścieżka")




# if choice == "2":
#     #archive

# if choice == "3":
#     #config



