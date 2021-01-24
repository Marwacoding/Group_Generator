#Faire des groupe de 2 de maniere aleatoire
#Lire mon fichier texte
#Faire des logs pour se premunier de tout beug (librairie = )
#Retourner le resultat du script dans un format JSON
#Packager dans le terminal sans utiliser python


###
import random 
import logging
import json
import os

###





logging.basicConfig(filename = "info.log", level= logging.INFO, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')

try:
    file_names = open("/Users/marwamajbri/Desktop/simplon/Groups/groups_marwa/my_names.txt", "r") 
    lines = file_names.readlines()
    list_name = [elem.strip() for elem in lines]
    logging.info('Student list successfully found in my file')
    file_names.close()
except OSError:
    logging.info("file cannot be read")


data = dict()
data["group"]= []

try:
    json_groups = open("student_name.json", 'w')
    logging.info("Storing groups in JSON file")
except OSError:
    logging.info("JSON file cannot be read")


def final_groups(name_list, n):

    logging.info('forming groups : start')

    logging.info("shuffling the list : start")
    random.shuffle(name_list)
    logging.info("shuffling the list : end")

    print(name_list)
    logging.info('forming groups : start')
    if n == int and n!=0:
        for j in range(len(name_list)//n):
            selected= name_list[j:j+n]
            name_list = name_list[1:]
            data["group"].append(selected)
            
            logging.info("slicing the list -> not using the names")
    else:
        logging.info("error, caanot forms groups of n != int")

    json.dump(data, json_groups, indent=4)

    logging.info('forming groups : end')
    

final_groups(list_name, 2)







