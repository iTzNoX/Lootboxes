import random
import json
import os

class PlayerAccount():
    
    PlayerIDS = []
    
    def __init__(self):
        
        name = input("Wie Soll dein Account heißen?")
        age = input("Wie alt bist du?")

        ID = random.randint(0, 999999999)       #------------------
        while ID in PlayerAccount.PlayerIDS:    #Erstellt für jeden neu erstellten Account eine
            ID = random.randint(0, 999999999)   #eindeutige Player ID
        PlayerAccount.PlayerIDS.append(ID)      #------------------
        
        self.name = name #Name des Spielers
        self.age = age #Alter des Spielers
        self.ID = ID #Eindeutige ID für jeden benutzer (Keine verwendung)
        self.konto = 100
        
        self.skinInventory = {}
        self._resetSkinInv()
        self.BoxInventory = {} #{BoxName:AnzahlDerBox, ...}
        self._resetInv()
        
    def play_moneygame(self): #Kleines (Mathe)spiel um Geld zu verdienen
        
        x = random.randint(1,100)
        y = random.randint(1,100)
        z = random.randint(1,100)
         
        answer = int(input(f"was ergibt{x} + {y} + {z} ?"))
        
        if answer == x + y + z:
            money = random.randint(5,15)
            self.konto = self.konto + money
            print(f"Hervorragend! Deinem Konto wurden {money}$ gutgeschrieben")
            print(f"Dein neuer Kontostand lautet{self.konto}")
            
        else:
            print("Falsch, verusche es erneut!")
            print(f"Die Lösung war {x+y+z}")
            
    def sell_skins(self): #Option Skins zu verkaufen um geld zu bekommen
        
        filename = "BoxList.json"
        
        print(self.skinInventory)
        skinname = input("Welchen Skin möchtest du verkaufen?")
        
        if skinname in self.skinInventory and self.skinInventory[skinname] >= 1: 
            with open(filename, "r") as file:
                data = json.load(file)
            
            for box in data: #Sucht nach dem Skinnamen
                if isinstance(data[box], dict):
                    skins = list(data[box].keys())

                    if skinname in skins: #Aktuallisiert das Inventar und gibt dem Spieler das Geld
                        skinValue = data[box][skinname]
                        self.skinInventory[skinname] -= 1
                        self.konto += skinValue
                        print(f"Dein neuer Kontostand lautet {self.konto}")
                        return
            
        else:
            print("Du besitzt diesen Skin nicht")
        
    def _resetInv(self): #Aktuallisiert das Inventar des Spielers beim erstellen. Setzt jede Kiste auf 0
        filename = "BoxList.json"
        data = {}
        
        with open(filename) as file:
            data = json.load(file)
        
        keys = list(data.keys())
        for i in range(0, len(keys), 3): #Geht durch die Anzahl der Boxnamen und erstellt für diese das Inventar
            key = keys[i]
            self.BoxInventory[key] = 0
        
    def info(self):
        return self.name, self.age, self.skinInventory, self.BoxInventory, self.konto
    
    def buy_box(self): #Kauft eine Box
        filename = "BoxList.json"
        
        if os.path.exists(filename):
                
            print(self.BoxInventory)
                    
            boxname = input("Welche Box willst du Kaufen?")
            boxname = boxname.lower()
            
            with open(filename) as file:
                data = json.load(file)
                
            boxvalue = (data[f"{boxname}Value"])
            
            if self.konto >= boxvalue:
                newBoxAmount = data[f"{boxname}Amount"] - 1
                
                if data[f"{boxname}Amount"] >= 0:
                
                    for i in data: #Aktuallisiert die Menge der verbleibenden Boxen
                        data[f"{boxname}Amount"] = newBoxAmount
     
                    with open(filename, "w") as file:
                        json.dump(data, file, indent=4)

                    self.konto = self.konto - boxvalue #Konto wird der Kistenpreis abgezogen
                    
                    self.BoxInventory[f"{boxname}"] += 1 #anzahl der kisten im inventar wird um 1 erhöht
                    
                    print(self.BoxInventory)
                    
                else:
                    print("es gibt keine Boxen dieser Reihe mehr zu kaufen")
   
            else:
                print("Du hast nicht genügend Geld auf dem Konto. Spiele das MoneyGame!")
                
        else:
            print("Erstelle zuerst eine SkinBox!")
    
    def sell_box(self): #Verkauft Boxen bei einem Fehlkauf
        
        filename = "BoxList.json"
        
        print(self.BoxInventory)
        boxname = input("Welche Box möchtest du verkaufen?")
        
        if boxname in self.BoxInventory and self.BoxInventory[boxname] >= 1: 
            with open(filename, "r") as file:
                data = json.load(file)
            
            if boxname in data:  
                
                boxValue = data[f"{boxname}Value"]
                self.BoxInventory[boxname] -= 1
                self.konto += boxValue
                print(f"Dein neuer Kontostand lautet {self.konto}")
    
    def open_box(self): #Öffnet eine box und gibt dem Spieler den Inhalt
        
        filename = "BoxList.json"
        
        print(self.BoxInventory)
        boxname = input("Welche Box möchtest du öffnen?")
        
        if self.BoxInventory[boxname] >= 1:
            self.BoxInventory[boxname] -= 1
            
            with open(filename) as file:
                data = json.load(file)
            
            skins = data[boxname]
            skinNames = list(skins.keys())
            skin = random.choice(skinNames)
            
            self.skinInventory[skin] += 1
            
            print(f"du hast {skin} gezogen")
                        
        
    def _resetSkinInv(self): #Gibt dem Inv beim erstellen seinen Inhalt
        filename = "BoxList.json"
        
        with open(filename) as file:
            data = json.load(file)
            
        for key, value in data.items(): #Iteriert über die Schlüssel/Wert Paare der JSON Datei
            if isinstance(value, dict): #Überprüft, ob der Wert ein Dictionary ist
                for sub_key, sub_value in value.items(): #Iteriert über die unteren Schlüssel/Wert Paare der JSON Datei um an die Skinnamen zu kommen
                    if isinstance(sub_value, float): #Überprüft, ob der Wert eine Ganzzahl ist
                        self.skinInventory[sub_key] = 0
            
        print(self.skinInventory)
