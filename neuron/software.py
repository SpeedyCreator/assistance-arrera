from software.YoutubeDownlaod import *
from src.voice import*

def Software(var,genre,user,name):
    if "enregistre de la musique" in var or "enregistrement de la musique" in var or "enregistre moi des vidéos" in var or "enregistre-moi une vidéo" in var:
        speak("Ok "+genre+" je vous ouvre le téléchargeur de video Youtube.")
        YoutubeDownload()
        return 1
    else :
        if "ouvre l'explorateur de fichier" in var or "ouvre les fichiers" in var or "montre-moi mes fichiers" in var :
            speak("ok je vous ouvre l'explorateur de fichier "+var+".")
            os.popen("start explorer")
            return 1
        else :
            return 0