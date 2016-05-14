from tkinter import *
from random import *
from time import *
import random

def Main():
    Launcher.destroy() #Quand on clique, le bouton disparait
    Chat.config(state = NORMAL)
    Ligne = float(Chat.index('end'))-1.0
    Chat.insert(END, "Le jeu commence ! \n \n")
    Chat.tag_add("start", Ligne, Ligne + 0.17)
    Chat.tag_config("start", foreground="#008000", font=("Arial", 20)) #, "bold"

    PlayerBox.config(state = NORMAL)
    PlayerBox.insert("0.0", texte, "texte")
    PlayerBox.config(state = DISABLED)

    

    if Joueur == 'LoupGarou':
        PictureBox.create_image(75, 75, image=ImgLoupGarou)
        Chat.insert(END, RoleLG + '\n')
        Chat.insert(END, "Utilisez la commande '.kill + nom', pour éliminer un joueur." + '\n')
    elif Joueur == 'Chasseur':
        PictureBox.create_image(75, 75, image=ImgChasseur)
        Chat.insert(END, RoleChassou + '\n')
        Chat.insert(END, """Utilisez la commande '.revenge + nom', pour éliminer quelqu'un lorsque
vous mourrez.""" + '\n')
    elif Joueur == 'Salvateur':
        PictureBox.create_image(75, 75, image=ImgSalvateur)
        Chat.insert(END, RoleSalva + '\n')
        Chat.insert(END, "Utilisez la commande '.protect + nom' pour vous unir avec un joueur." + '\n')
    elif Joueur == 'Sorciere':
        PictureBox.create_image(75, 75, image=ImgSorciere)
        Chat.insert(END, RoleSoso + '\n')
        Chat.insert(END, "Utilisez la commande '.poison + nom' pour éliminer un joueur." + '\n')
    else:
        PictureBox.create_image(75, 75, image=ImgCorbeau)
        Chat.insert(END, RoleCorbac + '\n')
        Chat.insert(END, "Utilisez la commande '.curse + nom' pour éliminer un joueur." + '\n')

    Chat.insert(END, "--------------------------------------------------------------------------------------------------------------" + '\n')
    Chat.insert(END, Night + '\n')
    Chat.config(state = DISABLED)
    TimerNuit()

        
    
def TimerNuit():
    global texte, secNuit, isNuit, CanPlayLG, CanPlaySoso, CanPlaySalva, CanPlayCorbac, CanPlayChassou, AlreadyPlayedSalva, AlreadyPlayedCorbac, AlreadyPlayedSoso, AlreadyPlayedChassou, finish
    BackGround.create_image(400, 230, image=FondNuit)
    
    if secNuit == 55:
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
            print("Salva:",Chosen)
            Shield(Chosen)
            AlreadyPlayedSalva = True

        Chat.yview()
        Chat.config(state = DISABLED)

    if secNuit == 40:
        Chat.config(state = NORMAL)
        Ligne = float(Chat.index('end'))-1.0
        Chat.insert(END, ActionLG + '\n')
        Chat.tag_add("LGText", Ligne, Ligne + 0.47)
        Chat.tag_config("LGText", foreground="#FF8000", font=("Arial", 12, "bold")) 
        if Joueur == 'LoupGarou':
            CanPlayLG = True
            Chat.insert(END, 'Vous disposez de 10 secondes pour entrer votre commande.' + '\n')
        else:
            while finish is False:
                random.shuffle(PlayerList)
                Victime = random.choice(PlayerList)
                if Victime != 'LoupGarou':
                    Kill(Victime)
                    AlreadyPlayedLG = True
                    finish = True
                else:
                    finish = False

        finish = False
        Chat.yview()
        Chat.config(state = DISABLED)
        

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
            

    if secNuit == 15:
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
            AlreadyPlayedCorbac = True

        Chat.yview()
        Chat.config(state = DISABLED)
            
        
    

    # Ordre : ActionSalva / ActionLG / ActionSoso / ActionCorbeau
    if secNuit != 0:
        isNuit = True
        secNuit -= 1
        TimerBox['text'] = 'Nuit :\n' + 'Temps restant : ' + str(secNuit)
        TimerBox.after(1000, TimerNuit)
        
    elif secNuit == 0:
        AlreadyPlayedLG = False
        AlreadyPlayedSalva = False
        AlreadyPlayedCorbac = False
        
        Chat.config(state = NORMAL)
        Chat.insert(END, DeadList)
        if Joueur not in PlayerList:
            Chat.insert(END, "- Joueur" + "(" + Joueur + ")" +'\n' +'\n')
            PlayerBox.config(state = NORMAL)
            texte -= J1
            PlayerBox.insert("0.0", texte, "texte")
            PlayerBox.config(state = DISABLED)
            
        if ordi1 not in PlayerList:
            Chat.insert(END, "- Ordi1" + "(" + ordi1 + ")" + '\n' +'\n')
            PlayerBox.config(state = NORMAL)
            texte -= O1
            PlayerBox.insert("0.0", texte, "texte")
            PlayerBox.config(state = DISABLED)
            
        if ordi2 not in PlayerList:
            Chat.insert(END, "- Ordi2" + "(" + ordi2 + ")" + '\n' +'\n')
            PlayerBox.config(state = NORMAL)
            texte -= O2
            PlayerBox.insert("0.0", texte, "texte")
            PlayerBox.config(state = DISABLED)
            
        if ordi3 not in PlayerList:
            Chat.insert(END, "- Ordi3" + "(" + ordi3 + ")" + '\n' +'\n')
            PlayerBox.config(state = NORMAL)
            texte -= O3
            PlayerBox.insert("0.0", texte, "texte")
            PlayerBox.config(state = DISABLED)
            
        if ordi4 not in PlayerList:
            Chat.insert(END, "- Ordi4" + "(" + ordi4 + ")" + '\n' +'\n')
            PlayerBox.config(state = NORMAL)
            texte -= O4
            PlayerBox.insert("0.0", texte, "texte")
            PlayerBox.config(state = DISABLED)
            
        if ordi5 not in PlayerList:
            Chat.insert(END, "- Ordi5" + "(" + ordi5 + ")" + '\n' +'\n')
            PlayerBox.config(state = NORMAL)
            texte -= O5
            PlayerBox.insert("0.0", texte, "texte")
            PlayerBox.config(state = DISABLED)



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
                    random.shuffle(PlayerList)
                    Killed = random.choice(PlayerList)
                    Kill(Killed)
                    Ligne = float(Chat.index('end'))-1.0
                    if Killed == Joueur:
                        Chat.insert(END, "PAN ! Joueur"+"("+ Killed +") a été tué par le chasseur." + '\n')

                    elif Killed == ordi1:
                        Chat.insert(END, "PAN ! Ordi1"+"("+ Killed +") a été tué par le chasseur." + '\n')

                    elif Killed == ordi2:
                        Chat.insert(END, "PAN ! Ordi2"+"("+ Killed +") a été tué par le chasseur." + '\n')

                    elif Killed == ordi3:
                        Chat.insert(END, "PAN ! Ordi3"+"("+ Killed +") a été tué par le chasseur." + '\n')

                    elif Killed == ordi4:
                        Chat.insert(END, "PAN ! Ordi4"+"("+ Killed +") a été tué par le chasseur." + '\n')

                    else:
                        Chat.insert(END, "PAN ! Ordi5"+"("+ Killed +") a été tué par le chasseur." + '\n')
                    Chat.tag_add("ChassouText", Ligne, Ligne + 0.61)
                    Chat.tag_config("ChassouText", foreground="#008000", font=("Arial", 14, "bold")) 
                AlreadyPlayedChassou = True
            


        Chat.insert(END, InfoVote + '\n' + '\n')
        
        if ordi1 in PlayerList:
            Choix = random.choice(PlayerList)
            print(Choix)
            Vote(Choix)
        if ordi2 in PlayerList:
            Choix = random.choice(PlayerList)
            print(Choix)
            Vote(Choix)
        if ordi3 in PlayerList:
            Choice = random.choice(PlayerList)
            print(Choice)
            Vote(Choice)
        if ordi4 in PlayerList:
            Choice = random.choice(PlayerList)
            print(Choice)
            Vote(Choice)
        if ordi5 in PlayerList:
            Choice = random.choice(PlayerList)
            print(Choice)
            Vote(Choice)



        Chat.config(state = DISABLED)
        Chat.yview(END)

            
        TimerBox['text'] = ''
        isNuit = False
        TimerJour()
        secNuit += 60
        

def TimerJour():
    global secJour, isJour
    BackGround.create_image(400, 230, image=FondJour)
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
            Chat.insert(END, "Le village a décidé d'éliminer Joueur qui était " + Joueur + ".\n")
        elif Ordi1IsVoted > JoueurIsVoted and Ordi1IsVoted > Ordi2IsVoted and Ordi1IsVoted > Ordi3IsVoted and Ordi1IsVoted > Ordi4IsVoted and Ordi1IsVoted > Ordi5IsVoted:
            PlayerList.remove(ordi1)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi1 qui était " + ordi1 + ".\n")

        elif Ordi2IsVoted > JoueurIsVoted and Ordi2IsVoted > Ordi1IsVoted and Ordi2IsVoted > Ordi3IsVoted and Ordi2IsVoted > Ordi4IsVoted and Ordi2IsVoted > Ordi5IsVoted:
            PlayerList.remove(ordi2)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi2 qui était " + ordi2 + ".\n")

        elif Ordi3IsVoted > JoueurIsVoted and Ordi3IsVoted > Ordi1IsVoted and Ordi3IsVoted > Ordi2IsVoted and Ordi3IsVoted > Ordi4IsVoted and Ordi3IsVoted > Ordi5IsVoted:
            PlayerList.remove(ordi3)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi3 qui était " + ordi3 + ".\n")

        elif Ordi4IsVoted > JoueurIsVoted and Ordi4IsVoted > Ordi1IsVoted and Ordi4IsVoted > Ordi2IsVoted and Ordi4IsVoted > Ordi3IsVoted and Ordi4IsVoted > Ordi5IsVoted:
            PlayerList.remove(ordi4)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi4 qui était " + ordi4 + ".\n")

        elif Ordi5IsVoted > JoueurIsVoted and Ordi5IsVoted > Ordi1IsVoted and Ordi5IsVoted > Ordi2IsVoted and Ordi5IsVoted > Ordi3IsVoted and Ordi5IsVoted > Ordi4IsVoted:
            PlayerList.remove(ordi5)
            Chat.insert(END, "Le village a décidé d'éliminer Ordi5 qui était " + ordi5 + ".\n")

        else:
           Chat.insert(END, "Le village n'arrivant pas à se décider, la nuit tombe sur Thiercelieux." + '\n')

        
            
        TimerBox['text'] = ''
        isJour = False
        Chat.insert(END, "--------------------------------------------------------------------------------------------------------------" + '\n')
        Chat.insert(END, Night + '\n')
        Chat.config(state = DISABLED)
        TimerNuit()
        secJour += 60


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


#A simplifier
def Filtration(EntryText): #Permet de filtrer les messages (EntryText)
    DoneFilter = '' #On initialise la variable qu'on va renvoyer
    for i in range(len(EntryText)-1,-1,-1): #On va regarder dans notre message (step = -1)
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
    #FinalMessage(Chat, EntryText)
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
    if EntryText != None: #Si le texte n'est vide
        if EntryText[0] == '.': #Si le texte commence par un point, on le considère comme une commande (si elle existe)
            #Début des commandes#
            
            if EntryText[:6] == '.vote ':#Commande .vote
                if isNuit == True:
                    EntryText = ''
                EntryText = EntryText.replace("\n", '') #On enlève le retour à la ligne (fixage de bugs)
                EntryText = EntryText.replace(".vote ", '') #On enlève le '.vote ' pour ne reccuperer que le pseudo
                if EntryText in PlayerList: #Si le pseudo fait partie de la liste de Joueurs
                    Vote(EntryText)
                    
            #Début du message Chat
                    VotedMessage = "Vous avez voté contre " + EntryText + '.' #Le message à envoyer
                    Chat.config(state=NORMAL) # On 'ouvre' le chat
                    if Chat.index('end') != None:
                        Ligne = float(Chat.index('end'))-1.0 # On définit la position du message
                        Chat.insert(END, VotedMessage + '\n') #On l'insert dans le Chat
                        Chat.tag_add('Start', Ligne, Ligne + 1.100) #On le repère avec Ligne (position)
                        Chat.tag_config('Start', foreground="#713070", font=("Arial", 15, "bold")) #On lui donne une couleur, taille
                        Chat.config(state=DISABLED)#Et on 'ferme' le chat
                        Chat.yview(END)
            #Fin du Message Chat

                else: #Sinon, on ne revoie rien
                    EntryText = ''

            elif EntryText[:6] == '.kill ':#Commande .kill
                if Joueur == 'LoupGarou':
                    if isJour == True:
                        EntryText = ''
                    if CanPlayLG == False:
                        EntryText = ''

                    if Joueur not in PlayerList:
                        EntryText = EntryText.replace("\n", '') 
                        EntryText = EntryText.replace(".kill ", '')
                        if EntryText in PlayerList:
                            if AlreadyPlayedLG != True:
                                Kill(EntryText)

                                KillMessage = "Vous avez décidé de tuer " + EntryText + '.\n Il ne se reveillera pas demain. \n'
                                Chat.config(state=NORMAL)
                                if Chat.index('end') != None:
                                    Ligne = float(Chat.index('end'))-1.0 # On définit la position du message
                                    Chat.insert(END, KillMessage + '\n') #On l'insert dans le Chat
                                    Chat.tag_add('Start', Ligne, Ligne + 1.100) #On le repère avec Ligne (position)
                                    Chat.tag_config('Start', foreground="#ED0000", font=("Arial", 12, "bold")) #On lui donne une couleur, taille
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
                    if EntryText in PlayerList:
                        Kill(EntryText)

                        RevengeMessage = "Dans un élan d'éffort, vous tirez sur " + EntryText + '.'
                        Chat.config(state=NORMAL)
                        if Chat.index('end') != None:
                            Ligne = float(Chat.index('end'))-1.0 # On définit la position de la première lettre
                            Chat.insert(END, RevengeMessage + '\n') #On l'insere dans le Chat
                            Chat.tag_add('Start', Ligne, Ligne + 1.100) #On le repère avec Ligne (position)
                            Chat.tag_config('Start', font=("Arial", 12, "bold")) #On lui donne une couleur, taille
                            Chat.config(state=DISABLED)#Et on 'ferme' le chat
                            Chat.yview(END)
                    else:
                        EntryText = ''
                else:
                    EntryText = ''
                    

            elif EntryText[:7] == '.curse ':
                if Joueur == 'Corbeau':
                    if isJour == True:
                        EntryText = ''
                    if CanPlayCorbac == False:
                        EntryText = ''
                    if Joueur in PlayerList:
                        EntryText = EntryText.replace("\n", '') 
                        EntryText = EntryText.replace(".curse ", '')
                        if EntryText in PlayerList:
                            Vote(EntryText)

                        else:
                            EntryText = ''
                    else:
                        EntryText = ''
                else:
                    EntryText = ''


            elif EntryText[:9] == '.protect ':
                if Joueur == 'Salvateur':
                    if isJour == True:
                        EntryText = ''
                    if CanPlaySalva == False:
                        EntryText = ''
                    if Joueur in PlayerList:
                        EntryText = EntryText.replace("\n", '') 
                        EntryText = EntryText.replace(".protect ", '')
                        if EntryText in PlayerList:
                            Shield(EntryText)

                        else:
                            EntryText = ''
                    else:
                        EntryText = ''
                else:
                    EntryText = ''
                    

            elif EntryText[:8] == '.poison ':
                if Joueur == 'Sorciere':
                    if isJour == True:
                        EntryText = ''
                    if CanPlaySoso == False:
                        EntryText = ''
                    if Joueur in PlayerList:
                        EntryText = EntryText.replace("\n", '') 
                        EntryText = EntryText.replace(".poison ", '')
                        if EntryText in PlayerList:
                            if AlreadyPlayedSoso != True:
                                Kill(EntryText)

                        else:
                            EntryText = ''
                    else:
                        EntryText = ''
                else:
                    EntryText = ''
                    
                


            if EntryText[:5] == '.info':
                Chat.config(state = NORMAL)
                Chat.insert(END, PlayerList)
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
    if Target == Joueur:
        JoueurIsProtect = True
    elif Target == ordi1:
        Ordi1IsProtect = True
    elif Target == ordi2:
        Ordi2IsProtect = True
    elif Target == ordi3:
        Ordi3IsProtect = True
    elif Target == ordi4:
        Ordi4IsProtect = True
    elif Target == ordi5:
        Ordi5IsProtect = True
    

def Vote(Target):
    global JoueurIsVoted,Ordi1IsVoted,Ordi2IsVoted,Ordi3IsVoted,Ordi4IsVoted, Ordi5IsVoted
    if Target == Joueur:
        JoueurIsVoted += 1
    elif Target == ordi1:
        Ordi1IsVoted += 1
    elif Target == ordi2:
        Ordi2IsVoted += 1
    elif Target == ordi3:
        Ordi3IsVoted += 1
    elif Target == ordi4:
        Ordi4IsVoted += 1
    elif Target == ordi5:
        Ordi5IsVoted += 1


def Kill(Target):
    global JoueurIsProtect, Ordi1IsProtect, Ordi2IsProtect, Ordi3IsProtect, Ordi4IsProtect, Ordi5IsProtect
    print(Target)
    if Target in PlayerList:
        if Target == Joueur:
            if JoueurIsProtect != True:
                PlayerList.remove(Target)

        elif Target == ordi1:
            if Ordi1IsProtect != True:
                PlayerList.remove(Target)

        elif Target == ordi2:
            if Ordi2IsProtect != True:
                PlayerList.remove(Target)

        elif Target == ordi3:
            if Ordi3IsProtect != True:
                PlayerList.remove(Target)

        elif Target == ordi4:
            if Ordi4IsProtect != True:
                PlayerList.remove(Target)

        elif Target == ordi5:
            if Ordi5IsProtect != True:
                PlayerList.remove(Target)



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
Chat.insert(END, "Bienvenue à cette partie de Loup Garous !\n") #On insère du texte
Chat.config(state=DISABLED) #Une fenêtre où ne peut pas écrire, sinon wtf

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
texte = """Joueurs restants :\n\n""" + J1 + O1 + O2 + O3 + O4 + O5
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


#Images
ImgLoupGarou = PhotoImage(file ='lg.gif')
ImgSalvateur = PhotoImage(file ='salva.gif')
ImgCorbeau = PhotoImage(file ='corbac.gif')
ImgChasseur = PhotoImage(file ='chassou.gif')
ImgSorciere = PhotoImage(file ='soso.gif')
FondJour = PhotoImage(file ='FondJour.gif')
FondNuit = PhotoImage(file ='FondNuit.gif')


#---------------------------------------------------#
#----------------GESTION DES DONNEES----------------#
#---------------------------------------------------#

RoleList = ['LoupGarou','LoupGarou','Salvateur','Sorciere','Chasseur', 'Corbeau']

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
CanPlayCupi = False
CanPlayChassou = False
CanPlaySalva = False
CanPlayCorbac = False

AlreadyPlayedLG = False
AlreadyPlayedSoso = False
AlreadyPlayedCupi = False
AlreadyPlayedChassou = False
AlreadyPlayedSalva = False
AlreadyPlayedCorbac = False
finish = False
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


Death = "[Privé] Vous êtes mort."


ActionLG = "Les loups vont décider d'une victime à éliminer."
VictimeLG = "Les loups on décidé d'éliminer [Joueur]"

ActionCorbac = "Le corbeau va pouvoir désigner un suspect."

ActionSalva = "Le Salvateur va pouvoir protéger quelqu'un."


ActionSoso = "La sorcière va pouvoir utiliser ses potions."
VictimeSoso = "[Privé] Avec vos subtiles potions vous arrivez à empoisonner [Joueur]. Il ne se reveillera pas demain..."

ChoixChassou = "Le chasseur dispose de 30 secondes pour éliminer sa cible !"

InfoVote = """Une fois par jour, le village décide d'éliminer un joueur qu'il croit Loup-Garou.
Pour voter contre quelqu'un, vous devez utiliser la commande '.vote ' + nom."""


Night = "La nuit tombe sur le village de Thiercelieux..."

RipAll = "Tout le monde est mort !"
GgLg = "Les LOUPS-GAROUS ont gagné !"
GgVillage = "Les VILLAGEOIS ont gagné !"
