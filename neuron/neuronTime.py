import datetime
from src.srcSix import*
from objet.Horloge.AppHorloge import*
from objet.date.objetdate import*
from function.calendar import *
from function.fenetrePygame import*

def neuronTime(var,genre,user,name,root,police):
    fenetre = pygameFond(root,police,genre)
    if "heure" in var :
        hour = str(datetime.datetime.now().hour)
        minute = str(datetime.datetime.now().minute)
        SIXsrc(root,police).speak("Il es "+hour+" heure " +minute)
        return 1
    else : 
        if "date" in var :
            jour = dateToday().jour()
            mois = dateToday().moisSTR()
            annees = dateToday().annes()
            SIXsrc(root,police).speak("Aujourd'hui on es le "+jour+" "+mois+" "+annees)
            return 1
        else : 
            if "horloge" in var :
                fenetre.OuvertureTK("Ok je vous ouvre l'application horloge "+genre+" "+user)
                AppHorloge("#3c0f14","white","Six : Horloge","acceuil")
                fenetre.FermetureTK()
                return 1
            else :
                if "chronomètre" in var or "chrono" in var :
                    fenetre.OuvertureTK("Ok je vous ouvre le chronomètre "+genre+" "+user)
                    AppHorloge("#3c0f14","white","Six : Horloge","chronometre")
                    fenetre.FermetureTK()
                    return 1
                else :
                    if "minuteur" in var :
                        fenetre.OuvertureTK("Ok je vous ouvre le minuteur "+genre+" "+user)
                        AppHorloge("#3c0f14","white","Six : Horloge","minuteur")
                        fenetre.FermetureTK()
                        return 1
                    else :
                        if "agenda" in var :
                            if "ouvre" in var :
                                fenetre.OuvertureTK("Je vous ouvre mon calendrier")
                                SixCalendar()
                                fenetre.FermetureTK()
                            else :
                                texte = SortieEvenementTexte()
                                SIXsrc(root,police).speak(texte)
                            return 1
                        else :
                            return 0