import random
import json
import os
from BoxSetting import BoxSetting

class newBox(BoxSetting): #init überarbeiten, save box überarbeiten
    
    boxListe = []
    
    def __init__(self):
        super().__init__()
        
        self.boxAmount = {}
        self.value = {}
        self.BoxNames = [] #speichert die in newBox erstellten BoxNamen, um BoxNames zu übersichtlich zu halten
        self.SkinList = [] #speichert vorübergehend die Skinnamen für BoxInv
        self.SkinValue = [] #speichert vorübergehend die Skinpreise für Boxinv
        
        self._createBox()
        
    def _saveBoxInv(self):
        temp = {}
        
        #fügt Boxname mit anhängenden Skinnamen mit angängendem Skinpreis hinzu
        if os.path.exists(BoxSetting.filename): #(Nur wenn die datei bereits exisitert)
            with open(BoxSetting.filename, "r") as file:
                temp = json.load(file)
                
        temp.update(self.BoxInv) #Fügt der Datei Boxnamen anhängend an Skinnamen anhängend an Skinpreise hinzu
        temp.update(self.value) #Fügt Boxnamen anhängend an Boxpreisen hinzu
        temp.update(self.boxAmount) #fügt Boxnamen anhängend an Kistenanzahl hinzu
                     
        with open(BoxSetting.filename, "w") as file: #Ansonsten wird diese hier einfach erstellt
            json.dump(temp, file, indent=4)

        
    def _finishBox(self): #gibt der Box einen namen und fässt Skinlist und Skinpreis im dic zusammen
        self.name = input("wie soll die Box heißen?")
        self.name = self.name.lower()
        
        if self.name in newBox.boxListe:
            print("Eine Box mit diesem Namen existiert bereits.")
        else:
            newBox.boxListe.append(self.name)
        
            self.BoxNames.append(self.name)
        
            self.boxdic = {self.name: {}}
        
            for i in range(len(self.SkinList)): #Aktuallisiert die Listen um das Fertige Dictionary zu erstellen
                skinName = self.SkinList[i]
                skinValue = self.SkinValue[i]
                self.boxdic[self.name][skinName] = skinValue
            
            self.BoxInv = self.boxdic
            
            boxAmount = int(input("Wieviele Boxen soll man kaufen können?"))
            self.boxAmount[self.name + "Amount"] = boxAmount
            
            value = float(input("Wieviel soll die Ungeöffnete Kiste Kosten?"))
            self.value[self.name + "Value"] = value
    
    def _addSkinSeries(self): #erstellt Skinnamen und Preise / Variable Menge an Inhalten
        
        x = 0
        
        while True:
            
            if x == 1:
                break
            
            skinname = input("Wie soll dein Skin heißen?")
            self.SkinList.append(skinname)
            skinvalue = float(input("Wieviel soll dein Skin Wert sein? Bedenke, dass alle Skins die gleiche Chance haben!"))
            self.SkinValue.append(skinvalue)
            
            
            while True:
                y = input("Willst du einen weiteren Skin hinzufügen? j/n")

                if y == "n":
                    x = 1
                    break

                elif y == "j":
                    break

                else:
                    print("Ungültige Antwort, bitte versuchen sie es erneut")
        
    def _createBox(self): #Wird in newBox im Konstruktor aufgerufen, um beim erstellen des Objektes die Inhalte der Box festzulegen
        self.BoxInv = {}
                     
        newBox._addSkinSeries(self)
        newBox._finishBox(self)
        self._saveBoxInv()
        
        return newBox.info(self)
    
    def info(self): #Infos zum testen
        return self.boxAmount, self.BoxInv;