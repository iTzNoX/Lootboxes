import random
import json
import os

class BoxSetting(): #Vererbt filename an newBox und führt Befehle aus, welche nicht mit Box erstellen oder Spielern zu tun haben
    
    filename = "BoxList.json"

    def addBoxAmount(): #Fügt bei bedarf Boxen hinzu
        if os.path.exists(BoxSetting.filename):
            with open(BoxSetting.filename, "r") as file:
                data = json.load(file)
                
                keys = list(data.keys())
                for i in range (0, len(keys), 3):
                    key = keys[i]
                    print(key)
            
            boxname = input("Von welcher Box möchtest du die Anzahl erhöhen?")

            if boxname in data:
                boxamount = int(input("Wieviele willst du hinzufügen?"))
                data[boxname + "Amount"]+= boxamount

                with open(BoxSetting.filename, "w") as file:
                    json.dump(data, file, indent=4)
                print("Die Anzahl wurde erfolgreich erhöht")

            else:
                print("Diese Box existiert nicht")
        else:
            print("Erstelle zuerst eine Box")
            
    def delBox(): #Überprüft die Datei und löscht bei richtigkeit die gewählte Box
        if os.path.exists(BoxSetting.filename):
            with open(BoxSetting.filename, "r") as file:
                data = json.load(file)
                
                keys = list(data.keys())
                for i in range (0, len(keys), 3):
                    key = keys[i]
                    print(key)
            
            box = input("Welche Box möchtest du Löschen?")

            if box in data:
                del data[box]
                del data[box + "Amount"]
                del data[box + "Value"]

            else:
                print("Diese Box existiert nicht")

            with open(BoxSetting.filename, "w") as file:
                json.dump(data, file, indent=4)
        
        else:
            print("Erstelle zuerst eine Box!")
