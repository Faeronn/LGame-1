from tkinter import *
from random import *
from time import *
import random

def Main():
    Launcher.destroy() #Quand on clique, le bouton disparait
    Chat.config(state = NORMAL)
    Chat.delete('0.0', END)
    Ligne = float(Chat.index('end'))-1.0
    Chat.insert(END, "Le jeu commence ! \n \n")
    Chat.tag_add("start", Ligne, Ligne + 0.17)
    Chat.tag_config("start", foreground="#008000", font=("Arial", 20)) #, "bold"

    PlayerBox.config(state = NORMAL)
    PlayerBox.insert("1.0", texte, "texte")
    
    PlayerBox.config(state = DISABLED)

    
    #Message si le joueur est Loup Garou
    if Joueur == 'LoupGarou1' or Joueur == 'LoupGarou2':
        Chat.insert(END, RoleLG + '\n')
        Chat.insert(END, "Utilisez la commande '.kill + nom', pour éliminer un joueur." + '\n')
        Ligne = float(Chat.index('end'))-1.0
        if ordi1 =='LoupGarou1' or ordi1 == 'LoupGarou2':
            Chat.insert(END, "Dans cette partie vous faites équipe avec Ordi1(LoupGarou)." + '\n')
            Chat.tag_add("LgFriend", Ligne, Ligne + 0.77)
            Chat.tag_config("LgFriend", foreground="#0000ff", font=("Arial", 12))
        if ordi2 =='LoupGarou1' or ordi2 == 'LoupGarou2':
            Chat.insert(END, "Dans cette partie vous faites équipe avec Ordi2(LoupGarou)." + '\n')
            Chat.tag_add("LgFriend", Ligne, Ligne + 0.77)
            Chat.tag_config("LgFriend", foreground="#0000ff", font=("Arial", 12))
        if ordi3 =='LoupGarou1' or ordi3 == 'LoupGarou2':
            Chat.insert(END, "Dans cette partie vous faites équipe avec Ordi3(LoupGarou)." + '\n')
            Chat.tag_add("LgFriend", Ligne, Ligne + 0.77)
            Chat.tag_config("LgFriend", foreground="#0000ff", font=("Arial", 12))
        if ordi4 =='LoupGarou1' or ordi4 == 'LoupGarou2':
            Chat.insert(END, "Dans cette partie vous faites équipe avec Ordi4(LoupGarou)." + '\n')
            Chat.tag_add("LgFriend", Ligne, Ligne + 0.77)
            Chat.tag_config("LgFriend", foreground="#0000ff", font=("Arial", 12))
        if ordi5 =='LoupGarou1' or ordi5 == 'LoupGarou2':
            Chat.insert(END, "Dans cette partie vous faites équipe avec Ordi5(LoupGarou)." + '\n')
            Chat.tag_add("LgFriend", Ligne, Ligne + 0.77)
            Chat.tag_config("LgFriend", foreground="#0000ff", font=("Arial", 12))

    #Atribution de l'image en fonction du Role (+ des explications sur les commandes)
    elif Joueur == 'Chasseur':
        Chat.insert(END, RoleChassou + '\n')
        Chat.insert(END, """Utilisez la commande '.revenge + nom', pour éliminer quelqu'un lorsque
vous mourrez.""" + '\n')
    elif Joueur == 'Salvateur':
        Chat.insert(END, RoleSalva + '\n')
        Chat.insert(END, "Utilisez la commande '.protect + nom' pour proteger un joueur." + '\n')
    elif Joueur == 'Sorciere':
        Chat.insert(END, RoleSoso + '\n')
        Chat.insert(END, "Utilisez la commande '.poison + nom' pour éliminer un joueur." + '\n')
    else:
        Chat.insert(END, RoleCorbac + '\n')
        Chat.insert(END, "Utilisez la commande '.curse + nom' pour maudire un joueur." + '\n')

    Chat.insert(END, "--------------------------------------------------------------------------------------------------------------" + '\n')
    Chat.insert(END, Night + '\n')
    Chat.config(state = DISABLED)
    TimerNuit()

        
    
def TimerNuit():
    global AlreadyVoted, InfoCursed, JoueurIsProtect, Ordi1IsProtect, Ordi2IsProtect, Ordi3IsProtect, Ordi4IsProtect, Ordi5IsProtect, texte, secNuit, isNuit, CanPlayLG, CanPlaySoso, CanPlaySalva, CanPlayCorbac, CanPlayChassou, AlreadyPlayedSalva, AlreadyPlayedCorbac, AlreadyPlayedSoso, AlreadyPlayedChassou, finish

    #Gestion des messages la nuit + roles ordinateurs
    #Salvateur
    if secNuit == 55:
        if 'Salvateur' in PlayerList:
            Chat.config(state = NORMAL)
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, ActionSalva + '\n')
            Chat.tag_add("SalvaText", Ligne, Ligne + 0.42)
            Chat.tag_config("SalvaText", foreground="#FF8000", font=("Arial", 12, "bold")) 
            if Joueur == 'Salvateur':
                CanPlaySalva = True
                Chat.insert(END, 'Vous disposez de 10 secondes pour entrer votre commande.' + '\n')
            else:
                random.shuffle(PlayerList)
                Chosen = random.choice(PlayerList)
                Shield(Chosen)
                AlreadyPlayedSalva = True

            Chat.yview()
            Chat.config(state = DISABLED)

    #Loups
    if secNuit == 40:
        Chat.config(state = NORMAL)
        Ligne = float(Chat.index('end'))-1.0
        Chat.insert(END, ActionLG + '\n')
        Chat.tag_add("LGText", Ligne, Ligne + 0.47)
        Chat.tag_config("LGText", foreground="#FF8000", font=("Arial", 12, "bold")) 
        if Joueur == 'LoupGarou1' or Joueur == 'LoupGarou2':
            CanPlayLG = True
            Chat.insert(END, 'Vous disposez de 10 secondes pour entrer votre commande.' + '\n')
        else:
            while finish is False:
                random.shuffle(PlayerList)
                Victime = random.choice(PlayerList)
                if Victime != 'LoupGarou1' and Victime != 'LoupGarou2':
                    Kill(Victime)
                    AlreadyPlayedLG = True
                    finish = True
                else:
                    finish = False
    
            finish = False
        Chat.yview()
        Chat.config(state = DISABLED)
        
    #Sorciere
    if secNuit == 30:
        if AlreadyPlayedSoso != True:
            Chat.config(state = NORMAL)
            
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, ActionSoso + '\n')
            Chat.tag_add("SosoText", Ligne, Ligne + 0.43)
            Chat.tag_config("SosoText", foreground="#FF8000", font=("Arial", 12, "bold")) 
            if Joueur == 'Sorciere':
                CanPlaySoso = True
                Chat.insert(END, 'Vous disposez de 10 secondes pour entrer votre commande.' + '\n')
            else:
                while finish is False:
                    random.shuffle(PlayerList)
                    Poisonned = random.choice(PlayerList)
                    if Poisonned != 'Sorciere':
                        Kill(Poisonned)
                        AlreadyPlayedSoso = True
                        finish = True
                    else:
                        finish = False
                    
            finish = False
            Chat.yview()
            Chat.config(state = DISABLED)
            
    #Corbeau
    if secNuit == 15:
        if 'Corbeau' in PlayerList:
            Chat.config(state = NORMAL)
            
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, ActionCorbac + '\n')
            Chat.tag_add("CorbacText", Ligne, Ligne + 0.42)
            Chat.tag_config("CorbacText", foreground="#FF8000", font=("Arial", 12, "bold")) 
            if Joueur == 'Corbeau':
                CanPlayCorbac = True
                Chat.insert(END, 'Vous disposez de 10 secondes pour entrer votre commande.' + '\n')
            else:
                random.shuffle(PlayerList)
                Cursed = random.choice(PlayerList)
                Vote(Cursed)
                if Joueur == Cursed:
                    InfoCursed = 'Joueur'
                elif ordi1 == Cursed:
                    InfoCursed = 'Ordi1'
                elif ordi2 == Cursed:
                    InfoCursed = 'Ordi2'
                elif ordi3 == Cursed:
                    InfoCursed = 'Ordi3'
                elif ordi4 == Cursed:
                    InfoCursed = 'Ordi4'
                elif ordi5 == Cursed:
                   InfoCursed = 'Ordi5'
    
                
                AlreadyPlayedCorbac = True

            Chat.yview()
            Chat.config(state = DISABLED)
            
        
    

    # Ordre : ActionSalva / ActionLG / ActionSoso / ActionCorbeau
    #Ici le timer relance la fonction chaque 1000 ms (1sec)
    if secNuit != 0:
        isNuit = True
        secNuit -= 1
        TimerBox['text'] = 'Nuit :\n' + 'Temps restant : ' + str(secNuit)
        TimerBox.after(1000, TimerNuit)
        
    elif secNuit == 0:
        #On reinitialise toutes les variables 
        AlreadyPlayedLG = False
        AlreadyPlayedSalva = False
        AlreadyPlayedCorbac = False
        AlreadyVoted = False

        JoueurIsProtect = False
        Ordi1IsProtect = False
        Ordi2IsProtect = False
        Ordi3IsProtect = False
        Ordi4IsProtect = False
        Ordi5IsProtect = False
        
        Chat.config(state = NORMAL)
        Chat.insert(END, "--------------------------------------------------------------------------------------------------------------" + '\n')
        Chat.insert(END, "Le jour se lève sur le village de Thiercelieux..."+ '\n')
        #Message de malediction du corbeau
        if 'Corbeau' in PlayerList:
            if InfoCursed != '':
                Ligne = float(Chat.index('end'))-1.0
                Chat.insert(END, "Le corbeau a posé sa malédiction sur "+ InfoCursed +"..."+ '\n' + '\n')
                Chat.tag_add("CorbeauCurse", Ligne, Ligne + 0.44)
                Chat.tag_config("CorbeauCurse", foreground="#0000ff", font=("Arial", 12, "bold")) 
        
        
        #Affichage des morts
        Chat.insert(END, DeadList)
        if Joueur not in PlayerList:
            Chat.insert(END, "- Joueur" + "(" + Joueur + ")" +'\n' +'\n')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("2.0", "2.11")
            PlayerBox.config(state = DISABLED)
            
        if ordi1 not in PlayerList:
            Chat.insert(END, "- Ordi1" + "(" + ordi1 + ")" + '\n' +'\n')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("3.0", "3.11")
            PlayerBox.config(state = DISABLED)
            
        if ordi2 not in PlayerList:
            Chat.insert(END, "- Ordi2" + "(" + ordi2 + ")" + '\n' +'\n')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("4.0", "4.11")
            PlayerBox.config(state = DISABLED)
            
        if ordi3 not in PlayerList:
            Chat.insert(END, "- Ordi3" + "(" + ordi3 + ")" + '\n' +'\n')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("5.0", "5.11")
            PlayerBox.config(state = DISABLED)
            
        if ordi4 not in PlayerList:
            Chat.insert(END, "- Ordi4" + "(" + ordi4 + ")" + '\n' +'\n')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("6.0", "6.11")
            PlayerBox.config(state = DISABLED)
            
        if ordi5 not in PlayerList:
            Chat.insert(END, "- Ordi5" + "(" + ordi5 + ")" + '\n' +'\n')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("7.0", "7.11")
            PlayerBox.config(state = DISABLED)

        if Joueur in PlayerList and ordi1 in PlayerList and ordi2 in PlayerList and ordi3 in PlayerList and ordi4 in PlayerList and ordi5 in PlayerList :
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, "Personne n'est mort !" + '\n' +'\n')
            Chat.tag_add("NobodyDied", Ligne, Ligne + 0.31)
            Chat.tag_config("NobodyDied", foreground="#008000", font=("Arial", 14, "bold")) 

        #Message si le joueur meurt.
        if Joueur not in PlayerList:
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, Death +'\n')
            Chat.tag_add("JoueurDied", Ligne, Ligne + 0.99)
            Chat.tag_config("JoueurDied", foreground="#0000ff", font=("Arial", 12, "bold")) 
            
        #Si le Chasseur est mort, on lui permet de tuer quelqu'un
        if 'Chasseur' not in PlayerList:
            if AlreadyPlayedChassou != True:
                Chat.config(state = NORMAL)
            
                Ligne = float(Chat.index('end'))-1.0
                Chat.insert(END, ChoixChassou + '\n')
                Chat.tag_add("ChassouText", Ligne, Ligne + 0.61)
                Chat.tag_config("ChassouText", foreground="#008000", font=("Arial", 12, "bold")) 
                if Joueur == 'Chasseur':
                    CanPlayChassou = True
                    Chat.insert(END, '[Privé] Vous disposez de 10 secondes pour entrer votre commande.' + '\n')
                else:
                    #Automatisme (si le joueur n'est pas un chasseur, l'ordi s'en charge)
                    random.shuffle(PlayerList)
                    Killed = random.choice(PlayerList)
                    Kill(Killed)
                    Ligne = float(Chat.index('end'))-1.0
                    if Killed == Joueur:
                        Chat.insert(END, "PAN ! Joueur"+"("+ Killed +") a été tué par le chasseur." + '\n')
                        PlayerBox.config(state = NORMAL)
                        PlayerBox.delete("2.0", "2.11")
                        PlayerBox.config(state = DISABLED)

                    elif Killed == ordi1:
                        Chat.insert(END, "PAN ! Ordi1"+"("+ Killed +") a été tué par le chasseur." + '\n')
                        PlayerBox.config(state = NORMAL)
                        PlayerBox.delete("3.0", "3.11")
                        PlayerBox.config(state = DISABLED)

                    elif Killed == ordi2:
                        Chat.insert(END, "PAN ! Ordi2"+"("+ Killed +") a été tué par le chasseur." + '\n')
                        PlayerBox.config(state = NORMAL)
                        PlayerBox.delete("4.0", "4.11")
                        PlayerBox.config(state = DISABLED)

                    elif Killed == ordi3:
                        Chat.insert(END, "PAN ! Ordi3"+"("+ Killed +") a été tué par le chasseur." + '\n')
                        PlayerBox.config(state = NORMAL)
                        PlayerBox.delete("5.0", "5.11")
                        PlayerBox.config(state = DISABLED)

                    elif Killed == ordi4:
                        Chat.insert(END, "PAN ! Ordi4"+"("+ Killed +") a été tué par le chasseur." + '\n')
                        PlayerBox.config(state = NORMAL)
                        PlayerBox.delete("6.0", "6.11")
                        PlayerBox.config(state = DISABLED)

                    else:
                        Chat.insert(END, "PAN ! Ordi5"+"("+ Killed +") a été tué par le chasseur." + '\n')
                        PlayerBox.config(state = NORMAL)
                        PlayerBox.delete("7.0", "7.11")
                        PlayerBox.config(state = DISABLED)
                        
                    Chat.tag_add("ChassouText", Ligne, Ligne + 0.61)
                    Chat.tag_config("ChassouText", foreground="#008000", font=("Arial", 14, "bold"))
                AlreadyPlayedChassou = True


        #Gestion des messages de fin de jeu :
        #Tout le monde est mort
        if 'Chasseur' not in PlayerList and 'Salvateur' not in PlayerList and 'Sorciere' not in PlayerList and 'Corbeau' not in PlayerList and 'LoupGarou1' not in PlayerList and 'LoupGarou2' not in PlayerList:
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, RipAll + "\n")
            Chat.tag_add("RipAlle", Ligne, Ligne + 0.77)
            Chat.tag_config("RipAlle", foreground="#008000", font=("Arial", 20, "bold"))
            Chat.insert(END, "Vous pouvez relancer une partie en redémarrant le programme." + "\n")
            return ''

        #Les villageois ont gagné
        elif 'LoupGarou1' not in PlayerList and 'LoupGarou2' not in PlayerList:
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, GgVillage + "\n")
            Chat.tag_add("GgVillaj", Ligne, Ligne + 0.77)
            Chat.tag_config("GgVillaj", foreground="#008000", font=("Arial", 20, "bold"))
            Chat.insert(END, "Vous pouvez relancer une partie en redémarrant le programme." + "\n")
            return ''

        #Les loups ont gagné
        elif 'Chasseur' not in PlayerList and 'Salvateur' not in PlayerList and 'Sorciere' not in PlayerList and 'Corbeau' not in PlayerList:
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, GgLg + "\n")
            Chat.tag_add("GgLge", Ligne, Ligne + 0.77)
            Chat.tag_config("GgLge", foreground="#008000", font=("Arial", 20, "bold"))
            Chat.insert(END, "Vous pouvez relancer une partie en redémarrant le programme." + "\n")
            return ''
        

        

        Chat.insert(END, InfoVote + '\n' + '\n')
        #Gestion des votes automatiques par les ordis
        if ordi1 in PlayerList:
            Choix1 = ordi1
            while Choix1 == ordi1:
                Choix1 = random.choice(PlayerList)
            if Choix1 == Joueur:
                ResultVote1 = 'Joueur'
            elif Choix1 == ordi1:
                ResultVote1 = 'Ordi1'
            elif Choix1 == ordi2:
                ResultVote1 = 'Ordi2'
            elif Choix1 == ordi3:
                ResultVote1 = 'Ordi3'
            elif Choix1 == ordi4:
                ResultVote1 = 'Ordi4'
            elif Choix1 == ordi5:
                ResultVote1 = 'Ordi5'
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, "Ordi1 : Je vote contre " +ResultVote1+", il me semble louche...\n")
            Chat.tag_add("Ordi1", Ligne, Ligne + 0.7)
            Chat.tag_config("Ordi1", foreground="#FF8000", font=("Arial", 12, "bold")) 
            Vote(Choix1)
            Chat.insert(END, "Ordi1 vote contre "+ResultVote1+"\n\n")
            Chat.yview()
            
        if ordi2 in PlayerList:
            Choix2 = ordi2
            while Choix2 == ordi2:
                Choix2 = random.choice(PlayerList)
            
            if Choix2 == Joueur:
                ResultVote2 = 'Joueur'
            elif Choix2 == ordi1:
                ResultVote2 = 'Ordi1'
            elif Choix2 == ordi2:
                ResultVote2 = 'Ordi2'
            elif Choix2 == ordi3:
                ResultVote2 = 'Ordi3'
            elif Choix2 == ordi4:
                ResultVote2 = 'Ordi4'
            elif Choix2 == ordi5:
                ResultVote2 = 'Ordi5'
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, "Ordi2 : Je vote contre toi " +ResultVote2+", je sais que tu es un Loup !!!\n")
            Chat.tag_add("Ordi2", Ligne, Ligne + 0.7)
            Chat.tag_config("Ordi2", foreground="#FF8000", font=("Arial", 12, "bold")) 
            Vote(Choix2)
            Chat.insert(END, "Ordi2 vote contre "+ResultVote2+".\n\n")
            Chat.yview()
            
        if ordi3 in PlayerList:
            Choix3 = ordi3
            while Choix3 == ordi3:
                Choix3 = random.choice(PlayerList)
                
            if Choix3 == Joueur:
                ResultVote3 = 'Joueur'
            elif Choix3 == ordi1:
                ResultVote3 = 'Ordi1'
            elif Choix3 == ordi2:
                ResultVote3 = 'Ordi2'
            elif Choix3 == ordi3:
                ResultVote3 = 'Ordi3'
            elif Choix3 == ordi4:
                ResultVote3 = 'Ordi4'
            elif Choix3== ordi5:
                ResultVote3 = 'Ordi5'
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, "Ordi3 : J'ai des gros doutes. Je te vote " +ResultVote3+".\n")
            Chat.tag_add("Ordi3", Ligne, Ligne + 0.7)
            Chat.tag_config("Ordi3", foreground="#FF8000", font=("Arial", 12, "bold")) 
            Vote(Choix3)
            Chat.insert(END, "Ordi3 vote contre "+ResultVote3+".\n\n")
            Chat.yview()
            
        if ordi4 in PlayerList:
            Choix4 = ordi4
            while Choix4 == ordi4:
                Choix4 = random.choice(PlayerList)
                
            if Choix4 == Joueur:
                ResultVote4 = 'Joueur'
            elif Choix4 == ordi1:
                ResultVote4 = 'Ordi1'
            elif Choix4 == ordi2:
                ResultVote4 = 'Ordi2'
            elif Choix4 == ordi3:
                ResultVote4 = 'Ordi3'
            elif Choix4 == ordi4:
                ResultVote4 = 'Ordi4'
            elif Choix4 == ordi5:
                ResultVote4 = 'Ordi5'
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, "Ordi4 : Votez " +ResultVote4+", il est très suspect !!!!\n")
            Chat.tag_add("Ordi4", Ligne, Ligne + 0.7)
            Chat.tag_config("Ordi4", foreground="#FF8000", font=("Arial", 12, "bold")) 
            Vote(Choix4)
            Chat.insert(END, "Ordi4 vote contre "+ResultVote4+".\n\n")
            Chat.yview()
            
        if ordi5 in PlayerList:
            Choix5 = ordi5
            while Choix5 == ordi5:
                Choix5 = random.choice(PlayerList)
                
            if Choix5 == Joueur:
                ResultVote5 = 'Joueur'
            elif Choix5 == ordi1:
                ResultVote5 = 'Ordi1'
            elif Choix5 == ordi2:
                ResultVote5 = 'Ordi2'
            elif Choix5 == ordi3:
                ResultVote5 = 'Ordi3'
            elif Choix5 == ordi4:
                ResultVote5 = 'Ordi4'
            elif Choix5 == ordi5:
                ResultVote5 = 'Ordi5'
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, "Ordi5 : C'est obligé que " +ResultVote5+", est un Loup...\n")
            Chat.tag_add("Ordi5", Ligne, Ligne + 0.7)
            Chat.tag_config("Ordi5", foreground="#FF8000", font=("Arial", 12, "bold")) 
            Vote(Choix5)
            Chat.insert(END, "Ordi5 vote contre "+ResultVote5+".\n\n")
            Chat.yview()



        Chat.config(state = DISABLED)
        Chat.yview(END)

        #On lance TimerJour
        TimerBox['text'] = ''
        isNuit = False
        TimerJour()
        secNuit += 60
        

def TimerJour():
    global secJour, isJour, JoueurIsVoted, Ordi1IsVoted, Ordi2IsVoted, Ordi3IsVoted, Ordi4IsVoted, Ordi5IsVoted
    if secJour != 0:
        isJour = True
        secJour -= 1
        TimerBox['text'] = 'Jour :\n' +'Temps restant : ' + str(secJour)
        TimerBox.after(1000, TimerJour)
    else:
        #Gestion de la mort du voté ici
        Chat.config(state = NORMAL)
        if JoueurIsVoted > Ordi1IsVoted and JoueurIsVoted > Ordi2IsVoted and JoueurIsVoted > Ordi3IsVoted and JoueurIsVoted > Ordi4IsVoted and JoueurIsVoted > Ordi5IsVoted:
            PlayerList.remove(Joueur)
            InfoList.remove('Joueur')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("2.0", "2.11")
            PlayerBox.config(state = DISABLED)
            Chat.insert(END, "Le village a décidé d'éliminer Joueur qui était " + Joueur + ".\n")
        elif Ordi1IsVoted > JoueurIsVoted and Ordi1IsVoted > Ordi2IsVoted and Ordi1IsVoted > Ordi3IsVoted and Ordi1IsVoted > Ordi4IsVoted and Ordi1IsVoted > Ordi5IsVoted:
            PlayerList.remove(ordi1)
            InfoList.remove('ordi1')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("3.0", "3.11")
            PlayerBox.config(state = DISABLED)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi1 qui était " + ordi1 + ".\n")

        elif Ordi2IsVoted > JoueurIsVoted and Ordi2IsVoted > Ordi1IsVoted and Ordi2IsVoted > Ordi3IsVoted and Ordi2IsVoted > Ordi4IsVoted and Ordi2IsVoted > Ordi5IsVoted:
            PlayerList.remove(ordi2)
            InfoList.remove('ordi2')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("4.0", "4.11")
            PlayerBox.config(state = DISABLED)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi2 qui était " + ordi2 + ".\n")

        elif Ordi3IsVoted > JoueurIsVoted and Ordi3IsVoted > Ordi1IsVoted and Ordi3IsVoted > Ordi2IsVoted and Ordi3IsVoted > Ordi4IsVoted and Ordi3IsVoted > Ordi5IsVoted:
            PlayerList.remove(ordi3)
            InfoList.remove('ordi3')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("5.0", "5.11")
            PlayerBox.config(state = DISABLED)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi3 qui était " + ordi3 + ".\n")

        elif Ordi4IsVoted > JoueurIsVoted and Ordi4IsVoted > Ordi1IsVoted and Ordi4IsVoted > Ordi2IsVoted and Ordi4IsVoted > Ordi3IsVoted and Ordi4IsVoted > Ordi5IsVoted:
            PlayerList.remove(ordi4)
            InfoList.remove('ordi4')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("6.0", "6.11")
            PlayerBox.config(state = DISABLED)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi4 qui était " + ordi4 + ".\n")

        elif Ordi5IsVoted > JoueurIsVoted and Ordi5IsVoted > Ordi1IsVoted and Ordi5IsVoted > Ordi2IsVoted and Ordi5IsVoted > Ordi3IsVoted and Ordi5IsVoted > Ordi4IsVoted:
            PlayerList.remove(ordi5)
            InfoList.remove('ordi5')
            PlayerBox.config(state = NORMAL)
            PlayerBox.delete("7.0", "7.11")
            PlayerBox.config(state = DISABLED)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi5 qui était " + ordi5 + ".\n")

        else:
           Chat.insert(END, "Le village n'arrivant pas à se décider, la nuit tombe sur Thiercelieux." + '\n')

        
        #Gestion des fins possibles
        if 'Chasseur' not in PlayerList and 'Salvateur' not in PlayerList and 'Sorciere' not in PlayerList and 'Corbeau' not in PlayerList:
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, GgLg + "\n")
            Chat.tag_add("LgEnd", Ligne, Ligne + 0.77)
            Chat.tag_config("LgEnd", foreground="#008000", font=("Arial", 20, "bold"))
            Chat.insert(END, "Vous pouvez relancer une partie en redémarrant le programme." + "\n")
            return ''
            
        elif 'LoupGarou1' not in PlayerList and 'LoupGarou2' not in PlayerList:
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, GgVillage + "\n")
            Chat.tag_add("VillageEnd", Ligne, Ligne + 0.77)
            Chat.tag_config("VillageEnd", foreground="#008000", font=("Arial", 20, "bold"))
            Chat.insert(END, "Vous pouvez relancer une partie en redémarrant le programme." + "\n")
            return ''

        #On reinitialise les votes
        JoueurIsVoted = 0
        Ordi1IsVoted = 0
        Ordi2IsVoted = 0
        Ordi3IsVoted = 0
        Ordi4IsVoted = 0
        Ordi5IsVoted = 0
                
        TimerBox['text'] = ''
        isJour = False
        Chat.insert(END, "--------------------------------------------------------------------------------------------------------------" + '\n')
        Chat.insert(END, Night + '\n')
        Chat.config(state = DISABLED)
        TimerNuit()
        secJour += 60


#Permet d'ajouter "Vous:" en couleur devant le message envoyé
def FinalMessage(Chat, EntryText):
    if EntryText != '':
        Chat.config(state=NORMAL)
        if Chat.index('end') != None:
            Ligne = float(Chat.index('end'))-1.0
            Chat.insert(END, "Vous: " + EntryText)
            Chat.tag_add("Vous", Ligne, Ligne+0.4)
            Chat.tag_config("Vous", foreground="#FF8000", font=("Arial", 12, "bold")) #Police, couleur...
            Chat.config(state=DISABLED)
            Chat.yview(END)


#Permet de filtrer les messages (EntryText)
def Filtration(EntryText): 
    DoneFilter = '' #On initialise la variable qu'on va renvoyer
    for i in range(len(EntryText)-1,-1,-1): #On va regarder dans notre message 
        if EntryText[i]!='\n': #Si le message n'est pas "vide"
            DoneFilter = EntryText[0:i+1] #On remplit la varible avec le message (i+1 = limite du message)
            break #Et on sort de la boucle for
    for i in range(0,len(DoneFilter), 1): #On va regarder notre message "filtré"
        if DoneFilter[i] != "\n": #Si il n'est pas "vide"
            return DoneFilter[i:]+'\n' #On le 'renvoie', avec un '\n' pour sauter une ligne
        return '' #Si le message est vide, on ne 'renvoie' rien

def ClicAction():
    #On envoie le texte dans le fonction Filtration
    EntryText = Filtration(ChatBox.get("0.0",END))
    #Puis on l'envoie dans la fonction Command, pour regarder si il y a une éventuelle commande
    Command(EntryText)
    #Scroll du message
    Chat.yview(END)
    #Supprimer le message de la ChatBox après envoi
    ChatBox.delete("0.0",END)

def ReleaseEnter(event):
    ChatBox.config(state=NORMAL) #Après avoir relaché ENTER, on re-initialise la ChatBox (de nouveau dispo)
    ClicAction() #Et on utilise la fonction ClicAction

def StopChat(event):
    #Permet de désactiver le chat quand on appuie sur ENTER (pour eviter de sauter un espace en écrivant)
    ChatBox.config(state=DISABLED)




#---------------------------------------------------#
#---------------GESTION DES COMMANDES---------------#
#---------------------------------------------------#

def Command(EntryText):
    global Cursed, AlreadyVoted, CanPlayLG, CanPlayChassou, CanPlaySoso, CanPlaySalva, CanPlayCorbac
    if EntryText != None: #Si le texte n'est vide
        if EntryText[0] == '.': #Si le texte commence par un point, on le considère comme une commande (si elle existe)
            
            #Début des commandes#
            if EntryText[:6] == '.vote ':#Commande .vote
                if AlreadyVoted == True:
                    EntryText = ''
                if isNuit == True:
                    EntryText = ''
                if Joueur in PlayerList:
                    EntryText = EntryText.replace("\n", '') #On enlève le retour à la ligne (fixage de bugs)
                    EntryText = EntryText.replace(".vote ", '') #On enlève le '.vote ' pour ne reccuperer que le pseudo
                    if EntryText in InfoList: #Si le pseudo fait partie de la liste de Joueurs
                        Vote(EntryText)
                        AlreadyVoted = True
                    
                #Début du message Chat
                        VotedMessage = "Vous avez voté contre " + EntryText + '. \n' #Le message à envoyer
                        Chat.config(state=NORMAL) # On 'ouvre' le chat
                        if Chat.index('end') != None:
                            Ligne = float(Chat.index('end'))-1.0 # On définit la position du message
                            Chat.insert(END, VotedMessage + '\n') #On l'insert dans le Chat
                            Chat.tag_add('Voted', Ligne, Ligne + 0.77) #On le repère avec Ligne (position)
                            Chat.tag_config('Voted', foreground="#713070", font=("Arial", 15, "bold")) #On lui donne une couleur, taille
                            Chat.config(state=DISABLED)#Et on 'ferme' le chat
                            Chat.yview(END)
                            EntryText = ''
                   #Fin du Message Chat

                    else: #Sinon, on ne revoie rien
                        EntryText = ''
                else: #Sinon, on ne revoie rien
                    EntryText = ''

            elif EntryText[:6] == '.kill ':#Commande .kill
                if Joueur == 'LoupGarou1' or Joueur == 'LoupGarou2':

                    if isJour == True:
                        EntryText = ''
                    if CanPlayLG == False:
                        EntryText = ''

                    if Joueur in PlayerList:
                        EntryText = EntryText.replace("\n", '') 
                        EntryText = EntryText.replace(".kill ", '')
                        if EntryText in InfoList:
                            if AlreadyPlayedLG != True:
                                Kill(EntryText)
                                CanPlayLG = False

                                KillMessage = "Vous avez décidé de tuer " + EntryText + '.\n'+'Il ne se reveillera pas demain. \n'
                                Chat.config(state=NORMAL)
                                if Chat.index('end') != None:
                                    Ligne = float(Chat.index('end'))-1.0 # On définit la position du message
                                    Chat.insert(END, KillMessage + '\n') #On l'insert dans le Chat
                                    Chat.tag_add('Killed', Ligne, Ligne + 0.99) #On le repère avec Ligne (position)
                                    Chat.tag_config('Killed', foreground="#ED0000", font=("Arial", 12, "bold")) #On lui donne une couleur, taille
                                    Chat.config(state=DISABLED)#Et on 'ferme' le chat
                                    Chat.yview(END)
                            
                        else:
                            EntryText = ''
                    else:
                        EntryText = ''

            elif EntryText[:9] == '.revenge ':#Commande .revenge (chasseur)
                if Joueur == 'Chasseur':
                    if isJour == False:
                        EntryText = ''
                    if Joueur in PlayerList:
                        EntryText = ''
                    if CanPlayChassou == False:
                        EntryText = ''
                    EntryText = EntryText.replace("\n", '') 
                    EntryText = EntryText.replace(".revenge ", '')
                    if EntryText in InfoList:
                        Kill(EntryText)
                        CanPlayChassou = False

                        RevengeMessage = "Dans un élan d'éffort, vous tirez sur " + EntryText + '.'
                        Chat.config(state=NORMAL)
                        if Chat.index('end') != None:
                            Ligne = float(Chat.index('end'))-1.0 # On définit la position de la première lettre
                            Chat.insert(END, RevengeMessage + '\n') #On l'insere dans le Chat
                            Chat.tag_add('Revenged', Ligne, Ligne + 0.99) #On le repère avec Ligne (position)
                            Chat.tag_config('Revenged',foreground="#0000ff", font=("Arial", 12, "bold")) #On lui donne une couleur, taille
                            Chat.config(state=DISABLED)#Et on 'ferme' le chat
                            Chat.yview(END)
                            EntryText = ''
                    else:
                        EntryText = ''
                else:
                    EntryText = ''
                    

            elif EntryText[:7] == '.curse ': #Commande Curse (corbeau)
                if Joueur == 'Corbeau':
                    if isJour == True:
                        EntryText = ''
                    if CanPlayCorbac == False:
                        EntryText = ''
                    if Joueur in PlayerList:
                        EntryText = EntryText.replace("\n", '') 
                        EntryText = EntryText.replace(".curse ", '')
                        if EntryText in InfoList:
                            Vote(EntryText)
                            Cursed = EntryText
                            CanPlayCorbac = False

                            CurseMessage = "Vous maudissez " + EntryText+ ', il aura 1 vote au levé du jour.'
                            Chat.config(state=NORMAL)
                            if Chat.index('end') != None:
                                Ligne = float(Chat.index('end'))-1.0 # On définit la position de la première lettre
                                Chat.insert(END, CurseMessage + '\n') #On l'insere dans le Chat
                                Chat.tag_add('Cursed', Ligne, Ligne + 0.99) #On le repère avec Ligne (position)
                                Chat.tag_config('Cursed', foreground="#0000ff",font=("Arial", 12, "bold")) #On lui donne une couleur, taille
                                Chat.config(state=DISABLED)#Et on 'ferme' le chat
                                Chat.yview(END)

                        else:
                            EntryText = ''
                    else:
                        EntryText = ''
                else:
                    EntryText = ''


            elif EntryText[:9] == '.protect ':# Commande Protect(Salva)
                if Joueur == 'Salvateur':
                    if isJour == True:
                        EntryText = ''
                    if CanPlaySalva == False:
                        EntryText = ''
                    if Joueur in PlayerList:
                        EntryText = EntryText.replace("\n", '') 
                        EntryText = EntryText.replace(".protect ", '')
                        if EntryText in InfoList:
                            Shield(EntryText)
                            CanPlaySalva = False

                            ProtectMessage = "Vous protégez " + EntryText+ ", il sera protégé de l'assaut des Loups-Garous."
                            Chat.config(state=NORMAL)
                            if Chat.index('end') != None:
                                Ligne = float(Chat.index('end'))-1.0 # On définit la position de la première lettre
                                Chat.insert(END, ProtectMessage + '\n') #On l'insere dans le Chat
                                Chat.tag_add('Protected', Ligne, Ligne + 0.99) #On le repère avec Ligne (position)
                                Chat.tag_config('Protected',foreground="#0000ff", font=("Arial", 12, "bold")) #On lui donne une couleur, taille
                                Chat.config(state=DISABLED)#Et on 'ferme' le chat
                                Chat.yview(END)

                        else:
                            EntryText = ''
                    else:
                        EntryText = ''
                else:
                    EntryText = ''
                    

            elif EntryText[:8] == '.poison ': # Commande Poison(Sorciere)
                if Joueur == 'Sorciere':
                    if isJour == True:
                        EntryText = ''
                    if CanPlaySoso == False:
                        EntryText = ''
                    if Joueur in PlayerList:
                        EntryText = EntryText.replace("\n", '') 
                        EntryText = EntryText.replace(".poison ", '')
                        if EntryText in InfoList:
                            if AlreadyPlayedSoso != True:
                                Kill(EntryText)
                                CanPlaySoso = False

                                PoisonMessage = "Vous empoisonnez " + EntryText + ", il ne se reveillera pas le lendemain."
                                Chat.config(state=NORMAL)
                                if Chat.index('end') != None:
                                    Ligne = float(Chat.index('end'))-1.0 # On définit la position de la première lettre
                                    Chat.insert(END, PoisonMessage + '\n') #On l'insere dans le Chat
                                    Chat.tag_add('Start', Ligne, Ligne + 0.99) #On le repère avec Ligne (position)
                                    Chat.tag_config('Start', foreground="#0000ff",font=("Arial", 12, "bold")) #On lui donne une couleur, taille
                                    Chat.config(state=DISABLED)#Et on 'ferme' le chat
                                    Chat.yview(END)

                        else:
                            EntryText = ''
                    else:
                        EntryText = ''
                else:
                    EntryText = ''
                    
                

            #Commande info, pour afficher la liste des joueurs (Developpeurs)
            if EntryText[:5] == '.info':
                Chat.config(state = NORMAL)
                Chat.insert(END, InfoList)
                Chat.insert(END, '\n')
                Chat.config(state = DISABLED)
                        
            else:
                if isNuit == True:
                    EntryText = ''
                else:
                    FinalMessage(Chat, EntryText) #Si ce n'est pas une commande connue, on envoie le message tel quel
        else:
            if isNuit == True:
                EntryText = ''
            else:
                FinalMessage(Chat, EntryText) # Si le message ne commence pas par un point, on l'envoie normalement


def Shield(Target):
    global JoueurIsProtect, Ordi1IsProtect, Ordi2IsProtect, Ordi3IsProtect, Ordi4IsProtect, Ordi5IsProtect
    if Target == Joueur or Target == 'Joueur':
        JoueurIsProtect = True
    elif Target == ordi1 or Target == 'ordi1':
        Ordi1IsProtect = True
    elif Target == ordi2 or Target == 'ordi2':
        Ordi2IsProtect = True
    elif Target == ordi3 or Target == 'ordi3':
        Ordi3IsProtect = True
    elif Target == ordi4 or Target == 'ordi4':
        Ordi4IsProtect = True
    elif Target == ordi5 or Target == 'ordi5':
        Ordi5IsProtect = True
    

def Vote(Target):
    global JoueurIsVoted,Ordi1IsVoted,Ordi2IsVoted,Ordi3IsVoted,Ordi4IsVoted, Ordi5IsVoted
    if Target == Joueur or Target == 'Joueur':
        JoueurIsVoted += 1
    elif Target == ordi1 or Target == 'ordi1':
        Ordi1IsVoted += 1
    elif Target == ordi2 or Target == 'ordi2':
        Ordi2IsVoted += 1
    elif Target == ordi3 or Target == 'ordi3':
        Ordi3IsVoted += 1
    elif Target == ordi4 or Target == 'ordi4':
        Ordi4IsVoted += 1
    elif Target == ordi5 or Target == 'ordi5':
        Ordi5IsVoted += 1


def Kill(Target):
    global JoueurIsProtect, Ordi1IsProtect, Ordi2IsProtect, Ordi3IsProtect, Ordi4IsProtect, Ordi5IsProtect
    if Target in PlayerList or Target in InfoList :
        if Target == Joueur or Target == 'Joueur':
            if JoueurIsProtect != True:
                PlayerList.remove(Joueur)
                InfoList.remove('Joueur')

        elif Target == ordi1 or Target == 'ordi1':
            if Ordi1IsProtect != True:
                PlayerList.remove(ordi1)
                InfoList.remove('ordi1')

        elif Target == ordi2 or Target == 'ordi2':
            if Ordi2IsProtect != True:
                PlayerList.remove(ordi2)
                InfoList.remove('ordi2')

        elif Target == ordi3 or Target == 'ordi3':
            if Ordi3IsProtect != True:
                PlayerList.remove(ordi3)
                InfoList.remove('ordi3')

        elif Target == ordi4 or Target == 'ordi4':
            if Ordi4IsProtect != True:
                PlayerList.remove(ordi4)
                InfoList.remove('ordi4')

        elif Target == ordi5 or Target == 'ordi5':
            if Ordi5IsProtect != True:
                PlayerList.remove(ordi5)
                InfoList.remove('ordi5')



#---------------------------------------------------#
#----------------GESTION DU GRAPHISME---------------#
#---------------------------------------------------#

root = Tk() #On définit notre fenêtre
root.title('LGame') #On définit notre nom, ici LGame
root.geometry("800x460") # On définit sa taille
root.resizable(width=FALSE, height=FALSE) # On dit que la fenêtre ne peut pas être redimensionnée

BackGround = Canvas(root, width=800, height=460)
BackGround.pack()

#Fenêtre du Chat
Chat = Text(root, bd=0, bg="white", height="8", width="50", font="Arial") #Customisation de la fenêtre de chat
Chat.insert(END, "Bienvenue à cette partie de Loup Garous !\n")
Ligne = float(Chat.index('end'))-1.0 
Chat.insert(END, """Quelques informations :
- Le jeu se passe rapidement, il faut lire les informations données et donc réagir
pour entrer une commande.

- Pour rentrer une commande telle que " .vote nom " le nom de la personne doit etre
tout en minuscule (ex : .vote ordi2).

- A savoir sur les règles :
    Le corbeau peut 'maudire' une personne en lui attribuant un vote d'office
    avec la commande '.curse + nom'.
    
    La Sorcière peut utiliser sa potion de mort pour éliminer une personne,
    avec la commande '.poison + nom'.
    
    Le Salvateur peut proteger une personne pendant une nuit
    avec la commande '.protect + nom'
    
    Les Loups Garous peuvent tuer une personne par nuit
    avec la commande '.kill + nom'.
    
    Le Chasseur peut se venger et tuer une personne si il a été tué
    la nuit précédente, avec la commande '.revenge + nom'.

Bonne chance pour survivre et faire gagner votre camp,
et puisse la chance vous etre favorable !""")
Chat.tag_add('Voted', Ligne, Ligne + 99.77) 
Chat.tag_config('Voted', foreground="#008000", font=("Arial", 10, "bold")) 
Chat.config(state=DISABLED) 

#Fenetre Image
PictureBox = Canvas(root, width=200, height=200)

#Fenetre Joueurs
PlayerBox = Text(root, bd=0, height="8", width = "25", font = 'Arial')
J1 = "- Joueur\n"
O1 = "- Ordi1\n"
O2 = "- Ordi2\n"
O3 = "- Ordi3\n"
O4 = "- Ordi4\n"
O5 = "- Ordi5\n"

texte = """Joueurs restants :\n""" + J1 +O1 + O2 + O3 + O4 + O5
PlayerBox.config(state = DISABLED)


#Fenetre timer
TimerBox = Label(root)

#Barre de Scrolling
scrollbar = Scrollbar(root, command=Chat.yview)
Chat['yscrollcommand'] = scrollbar.set

#Le Bouton "Envoyer"
BoutonEnvoi = Button(root, font=30, text="Envoyer", width='12', height='5', #Customisation du Bouton
bd=0, bg="#FFBF00", activebackground="#FACC2E", #Customisation du Bouton
command=ClicAction) #Quand on clique, ça lance la fonction "ClicAction"

#Le Bouton "Lancer la partie"
Launcher = Button(root, font=30, text="Lancer la partie", width='12', height='5',
bd=0, bg="#FFBF00", activebackground="#FACC2E",
command=Main)

#L'espace où taper son message
ChatBox = Text(root, bd=0, bg="white",width='29', height='5', font="Arial") # Customisation de la ChatBox (Taille/police/fond)
ChatBox.bind("<Return>", StopChat) #Quand on appuie sur Enter, Utiliser la fonction StopChat
ChatBox.bind("<KeyRelease-Return>", ReleaseEnter) #Quand on relache Enter, Utiliser la fonction ReleaseEnter

#Placer les différents tools sur l'interface
scrollbar.place(x=559,y=6, height=386) #La Barre de Scroll
Chat.place(x=6,y=6, height=386, width=570) #Le cadre du Chat
ChatBox.place(x=128, y=401, height=50, width=500) #Le cadre de la boite à message (lol)
BoutonEnvoi.place(x=6, y=401, height=50) #Le cadre du bouton
Launcher.place(x=650, y=401, height=50 ) #Le cadre du bouton
PictureBox.place(x=645, y=5)
PlayerBox.place(x= 645, y= 215)
TimerBox.place(x= 655, y= 165)


#---------------------------------------------------#
#----------------GESTION DES DONNEES----------------#
#---------------------------------------------------#

RoleList = ['LoupGarou1','LoupGarou2','Salvateur','Sorciere','Chasseur', 'Corbeau']
InfoList = ['Joueur', 'ordi1', 'ordi2', 'ordi3', 'ordi4','ordi5']

Joueur = random.choice(RoleList)
RoleList.remove(Joueur)
    #------------#
ordi1 = random.choice(RoleList)
RoleList.remove(ordi1)
    #------------#
ordi2 = random.choice(RoleList)
RoleList.remove(ordi2)
    #------------#
ordi3 = random.choice(RoleList)
RoleList.remove(ordi3)
    #------------#
ordi4 = random.choice(RoleList)
RoleList.remove(ordi4)

ordi5 = random.choice(RoleList)
RoleList.remove(ordi5)

PlayerList = [Joueur, ordi1, ordi2, ordi3, ordi4, ordi5]

secNuit = 60
isNuit = False
secJour = 60
isJour = False


JoueurIsVoted = 0
Ordi1IsVoted = 0
Ordi2IsVoted = 0
Ordi3IsVoted = 0
Ordi4IsVoted = 0
Ordi5IsVoted = 0


JoueurIsProtect = False
Ordi1IsProtect = False
Ordi2IsProtect = False
Ordi3IsProtect = False
Ordi4IsProtect = False
Ordi5IsProtect = False

CanPlayLG = False
CanPlaySoso = False
CanPlayChassou = False
CanPlaySalva = False
CanPlayCorbac = False

AlreadyPlayedLG = False
AlreadyPlayedSoso = False
AlreadyPlayedChassou = False
AlreadyPlayedSalva = False
AlreadyPlayedCorbac = False
AlreadyVoted = False
finish = False
InfoCursed = ''
#---------------------------------------------------#
#----------------     DIALOGUES     ----------------#
#---------------------------------------------------#

DeadList = "Liste des morts : \n"

RoleLG = """[Privé] Vous êtes Loup-Garou. Votre objectif est d'éliminer tous les innocents.
Chaque nuit, vous vous réunissez entre Loups pour décider d'une victime
à éliminer... Bon jeu et... Bonne chance !"""

RoleSoso = """[Privé] Vous êtes Sorcière. Votre objectif est d'éliminer tous les Loups-Garous.
Vous disposez d'une potion de mort pour assassiner quelqu'un...
Bon jeu et... Bonne chance !"""

RoleChassou = """[Privé] Vous êtes Chasseur. Votre objectif est d'éliminer tous les Loups-Garous.
A votre mort, vous pourrez éliminer un joueur en utilisant votre dernier souffle...
Bon jeu et... Bonne chance !"""

RoleSalva = """[Privé] Vous êtes Salvateur. Votre objectif est d'éliminer tous les Loups-Garous.
Chaque nuit, vous pouvez proteger une personne de l'assaut des Loups-Garous.
Bon jeu et... Bonne chance !"""

RoleCorbac = """[Privé] Vous êtes Corbeau. Votre objectif est d'éliminer tous les Loups-Garous.
Chaque nuit, vous pouvez maudire une personne, ainsi, elle aura d'emblée
un vote au levé du jour.
Bon jeu et... Bonne chance !"""


Death = "[Privé] Vous êtes mort, vous pouvez toujours observer la fin de la partie."


ActionLG = "Les loups vont décider d'une victime à éliminer."
VictimeLG = "Les loups on décidé d'éliminer [Joueur]"

ActionCorbac = "Le corbeau va pouvoir désigner un suspect."

ActionSalva = "Le Salvateur va pouvoir protéger quelqu'un."


ActionSoso = "La sorcière va pouvoir utiliser ses potions."
VictimeSoso = "[Privé] Avec vos subtiles potions vous arrivez à empoisonner [Joueur]. Il ne se reveillera pas demain..."

ChoixChassou = "Le chasseur dispose de 30 secondes pour éliminer sa cible !"
Pan = "PAN ! [Joueur]([Rôle]) a été tué par le chasseur."

InfoVote = """Une fois par jour, le village décide d'éliminer un joueur qu'il croit Loup-Garou.
Pour voter contre quelqu'un, vous devez utiliser la commande '.vote ' + nom."""


Night = "La nuit tombe sur le village de Thiercelieux..."

RipAll = "Tout le monde est mort !"
GgLg = "Les LOUPS-GAROUS ont gagné !"
GgVillage = "Les VILLAGEOIS ont gagné !"

root.mainloop()
