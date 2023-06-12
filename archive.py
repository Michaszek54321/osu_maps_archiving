import pandas as pd
import os
import old_list
import zipfile
import shutil
import configparser
import itertools
import time

config1 = configparser.ConfigParser()
config1.read("configfile.ini")
config = config1["config"]

path_to_osu = config["path_to_osu"]

AD = True
#wywołanie na górze starej listy
#na dole aktualnej listy


def Archive():
    if os.path.isfile("%s\osu_songs.zip"%config["path"]) == False:
        shutil.make_archive("%s\osu_songs"%config["path"], 'zip', config["path_to_osu"])
        print("Done!")
    else:
        os.remove("%s\osu_songs.zip"%config["path"])
        shutil.make_archive("%s\osu_songs"%config["path"], 'zip', config["path_to_osu"])
        print("Done!")
    return True
#archiwizacja całego folderu

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def add_archive():#dodaje mapy do archiwum
    oldlist = pd.read_csv("preupdate_List.csv", index_col=0)
    newlist = old_list.wyciaganie()
    difflist = pd.concat([oldlist,newlist]).drop_duplicates(keep=False)
    
    if len(difflist["map"])>0:
        with open("last changes.txt",'a+') as t: #wkładam difflist do txt
            for i in difflist["map"]:
                t.write("%s\n"%i)
            t.write("\n")
        t.close()
        AD = False
    else:
        AD = True
    #różnica między bazami piosenek
    os.system("cls")
    if AD == False:
        print("{} maps were added".format(len(difflist)))
        print(difflist)
        print("archiving...")
        time.sleep(1)
        for i in difflist["map"]:
            inside = listdir_fullpath("{}\{}".format(path_to_osu, i)) 
            inside2 = os.listdir("{}\{}".format(path_to_osu, i))
            #lista z komponentami map

            with zipfile.ZipFile("%s\osu_songs.zip"%config["path"], "a") as newzip:
                newzip.write("{}\{}".format(path_to_osu,i),"\{}".format(i))
                for (name,l) in zip(inside,inside2):
                    newzip.write(name,"{}\{}".format(i, l))
                    print("Archivised: ",name)
            #dodaje je do archiwum
        print("DONE!")
        time.sleep(4)
    else:
        print("Already done")
        time.sleep(1.5)

    old_list.tworzenie(old_list.wyciaganie())
    #akualizuje liste piosenek o te zarchiwizowane
    
    return True

