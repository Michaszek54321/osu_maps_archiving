import os
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read("configfile.ini")
config = config["config"]
path_to_osu = config["path_to_osu"]

def wyciaganie():
    dirlist = os.listdir(r'{}'.format(path_to_osu))

    dict = {'map': dirlist}
    dirlist = pd.DataFrame(dict)
    del dict
    return dirlist
    #wyciąganie listy piosenek z folderu i przydzielanie ich do bazy

def tworzenie(dirlist):
    dirlist.to_csv("preupdate_List.csv")
    return True
    #tworzenie listy starych piosenek (pliku)


