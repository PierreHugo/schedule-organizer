#--------------------------------------------------------------------------
#APPELS
#--------------------------------------------------------------------------
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox

import tkinter as tk

from PIL import Image, ImageTk
import matplotlib.pyplot as plt

import webbrowser

import smtplib

import numpy



#--------------------------------------------------------------------------
#DEF
#--------------------------------------------------------------------------
def maj():
    im = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
    F=open("fichier.csv","w")
    F.write("Lundi"+";"+"1er cours"+";"+cours(im,245,346,358,399))
    F.write(";"+"2eme cours"+";"+cours(im,245,507,358,560))
    F.write(";"+"3eme cours"+";"+cours(im,245,746,358,799))
    F.write(";"+"4eme cours"+";"+cours(im,245,907,358,960)+";")
    
    F.write("Mardi"+";"+"1er cours"+";"+cours(im,523,346,636,399))
    F.write(";"+"2eme cours"+";"+cours(im,523,507,636,560))
    F.write(";"+"3eme cours"+";"+cours(im,523,746,636,799))
    F.write(";"+"4eme cours"+";"+cours(im,523,907,636,960)+";")
    
    F.write("Mercredi"+";"+"1er cours"+";"+cours(im,800,346,913,399))
    F.write(";"+"2eme cours"+";"+cours(im,800,507,913,560))
    F.write(";"+"3eme cours"+";"+cours(im,800,746,913,799))
    F.write(";"+"4eme cours"+";"+cours(im,800,907,913,960)+";")
    
    F.write("Jeudi"+";"+"1er cours"+";"+cours(im,1077,346,1190,399))
    F.write(";"+"2eme cours"+";"+cours(im,1077,507,1190,560)+";")
    
    F.write("Vendredi"+";"+"1er cours"+";"+cours(im,1354,346,1467,399))
    F.write(";"+"2eme cours"+";"+cours(im,1354,507,1467,560))
    F.write(";"+"3eme cours"+";"+cours(im,1354,746,1467,799))
    F.write(";"+"4eme cours"+";"+cours(im,1354,907,1467,960)+";")
    
    F.write("Samedi"+";"+"1er cours"+";"+cours(im,1633,346,1746,399))
    F.write(";"+"2eme cours"+";"+cours(im,1633,507,1746,560))

    F.close()
    messagebox.showinfo("Information", "Emploi du temps mis à jour !")


def cours (image,x,y,x2,y2):
    C = Image.open(image)
    r,g,b,a = C.getpixel( (x,y) )
    r2,g2,b2,a2 = C.getpixel( (x2,y2) )
    if r == 250 and g == 88 and b == 130:
       c="Genie electrique"
    elif r == 72 and g == 201 and b == 176:
        c="Programmation"
    elif r == 153 and g == 255 and b == 204:
        c="Mathematiques"
    elif r == 255 and g == 204 and b == 153:
        c="Anglais"
    elif r == 102 and g == 204 and b == 255:
        c="Physique"
    elif r == 0 and g == 102 and b == 255:
        c="Electronique"
    elif r == 84 and g == 114 and b == 174:
        c="Techniques d'expression et de communication"
    elif r == 246 and g == 108 and b == 177:
        c="Projet informatique"
    elif r == 255 and g == 255 and b == 255 and r2 == 0 and g2 == 0 and b2 == 0:
        c="Introduction au monde aeronautique et spatial"
    elif r == 255 and g == 255 and b == 255 and r2 == 255 and g2 == 255 and b2 == 255:
        c="---"
    elif r == 242 and g == 226 and b == 128:
        c="Algorithmique"
    elif r == 243 and g == 214 and b == 23:
        c="Piscine d'anglais"
    elif r == 224 and g == 197 and b == 247:
        c="Projet electronique"
    else:
        c="---"
    return(c)

def GoUrl():
        webbrowser.open("https://ipsa-etud.helvetius.net/pegasus/index.php#")

def email_lundi(mail):

    
    F=open("fichier.csv","r")
    for l in F.readlines():
        L=l.split(";")
        
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "pierrehugo.herran@gmail.com"
    SMTP_PASSWORD = "Akewra-91790"
    EMAIL_FROM = "pierrehugo.herran@gmail.com"
    EMAIL_TO = mail
    EMAIL_SUBJECT = "Emploi du temps de lundi"
    EMAIL_MESSAGE = "Voici vos cours d'aujourd'hui :"+"\n"+L[0]+" :\n"+L[1]+" : "+L[2]+"\n"+L[3]+" : "+L[4]+"\n"+L[5]+" : "+L[6]+"\n"+L[7]+" : "+L[8]

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.starttls()
    s.login(SMTP_USERNAME, SMTP_PASSWORD)
    message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)
    s.sendmail(EMAIL_FROM, EMAIL_TO, message)
    s.quit()

    F.close()
    messagebox.showinfo("Information", "E-mail envoyé avec succès !")

    
    

def email_mardi(mail):
    
    F=open("fichier.csv","r")
    for l in F.readlines():
        L=l.split(";")
        
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "pierrehugo.herran@gmail.com"
    SMTP_PASSWORD = "Akewra-91790"
    EMAIL_FROM = "pierrehugo.herran@gmail.com"
    EMAIL_TO = mail
    EMAIL_SUBJECT = "Emploi du temps de mardi"
    EMAIL_MESSAGE = "Voici vos cours d'aujourd'hui :"+"\n"+L[9]+" :\n"+L[10]+" : "+L[11]+"\n"+L[12]+" : "+L[13]+"\n"+L[14]+" : "+L[15]+"\n"+L[16]+" : "+L[17]

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.starttls()
    s.login(SMTP_USERNAME, SMTP_PASSWORD)
    message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)
    s.sendmail(EMAIL_FROM, EMAIL_TO, message)
    s.quit()

    F.close()
    messagebox.showinfo("Information", "E-mail envoyé avec succès !")


def email_mercredi(mail):
    
    F=open("fichier.csv","r")
    for l in F.readlines():
        L=l.split(";")
        
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "pierrehugo.herran@gmail.com"
    SMTP_PASSWORD = "Akewra-91790"
    EMAIL_FROM = "pierrehugo.herran@gmail.com"
    EMAIL_TO = mail
    EMAIL_SUBJECT = "Emploi du temps de mercredi"
    EMAIL_MESSAGE = "Voici vos cours d'aujourd'hui :"+"\n"+L[18]+" :\n"+L[19]+" : "+L[20]+"\n"+L[21]+" : "+L[22]+"\n"+L[23]+" : "+L[24]+"\n"+L[25]+" : "+L[26]

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.starttls()
    s.login(SMTP_USERNAME, SMTP_PASSWORD)
    message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)
    s.sendmail(EMAIL_FROM, EMAIL_TO, message)
    s.quit()

    F.close()
    messagebox.showinfo("Information", "E-mail envoyé avec succès !")


def email_jeudi(mail):
    
    F=open("fichier.csv","r")
    for l in F.readlines():
        L=l.split(";")
        
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "pierrehugo.herran@gmail.com"
    SMTP_PASSWORD = "Akewra-91790"
    EMAIL_FROM = "pierrehugo.herran@gmail.com"
    EMAIL_TO = mail
    EMAIL_SUBJECT = "Emploi du temps de jeudi"
    EMAIL_MESSAGE = "Voici vos cours d'aujourd'hui :"+"\n"+L[27]+" :\n"+L[28]+" : "+L[29]+"\n"+L[30]+" : "+L[31]

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.starttls()
    s.login(SMTP_USERNAME, SMTP_PASSWORD)
    message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)
    s.sendmail(EMAIL_FROM, EMAIL_TO, message)
    s.quit()

    F.close()
    messagebox.showinfo("Information", "E-mail envoyé avec succès !")


def email_vendredi(mail):
    
    F=open("fichier.csv","r")
    for l in F.readlines():
        L=l.split(";")
        
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "pierrehugo.herran@gmail.com"
    SMTP_PASSWORD = "Akewra-91790"
    EMAIL_FROM = "pierrehugo.herran@gmail.com"
    EMAIL_TO = mail
    EMAIL_SUBJECT = "Emploi du temps de vendredi"
    EMAIL_MESSAGE = "Voici vos cours d'aujourd'hui :"+"\n"+L[32]+" :\n"+L[33]+" : "+L[34]+"\n"+L[35]+" : "+L[36]+"\n"+L[37]+" : "+L[38]+"\n"+L[39]+" : "+L[40]

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.starttls()
    s.login(SMTP_USERNAME, SMTP_PASSWORD)
    message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)
    s.sendmail(EMAIL_FROM, EMAIL_TO, message)
    s.quit()

    F.close()
    messagebox.showinfo("Information", "E-mail envoyé avec succès !")


def email_samedi(mail):
    
    F=open("fichier.csv","r")
    for l in F.readlines():
        L=l.split(";")
        
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "pierrehugo.herran@gmail.com"
    SMTP_PASSWORD = "Akewra-91790"
    EMAIL_FROM = "pierrehugo.herran@gmail.com"
    EMAIL_TO = mail
    EMAIL_SUBJECT = "Emploi du temps de samedi"
    EMAIL_MESSAGE = "Voici vos cours d'aujourd'hui :"+"\n"+L[41]+" :\n"+L[42]+" : "+L[43]+"\n"+L[44]+" : "+L[45]

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.starttls()
    s.login(SMTP_USERNAME, SMTP_PASSWORD)
    message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)
    s.sendmail(EMAIL_FROM, EMAIL_TO, message)
    s.quit()

    F.close()
    messagebox.showinfo("Information", "E-mail envoyé avec succès !")

def email_semaine(mail):
    
    F=open("fichier.csv","r")
    for l in F.readlines():
        L=l.split(";")
        
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "pierrehugo.herran@gmail.com"
    SMTP_PASSWORD = "Akewra-91790"
    EMAIL_FROM = "pierrehugo.herran@gmail.com"
    EMAIL_TO = mail
    EMAIL_SUBJECT = "Emploi du temps de la semaine"
    EMAIL_MESSAGE = "Voici vos cours de cette semaine :"+"\n"+L[0]+" :\n"+L[1]+" : "+L[2]+"\n"+L[3]+" : "+L[4]+"\n"+L[5]+" : "+L[6]+"\n"+L[7]+" : "+L[8]+"\n"+L[9]+" :\n"+L[10]+" : "+L[11]+"\n"+L[12]+" : "+L[13]+"\n"+L[14]+" : "+L[15]+"\n"+L[16]+" : "+L[17]+"\n"+L[18]+" :\n"+L[19]+" : "+L[20]+"\n"+L[21]+" : "+L[22]+"\n"+L[23]+" : "+L[24]+"\n"+L[25]+" : "+L[26]+"\n"+L[27]+" :\n"+L[28]+" : "+L[29]+"\n"+L[30]+" : "+L[31]+"\n"+L[32]+" :\n"+L[33]+" : "+L[34]+"\n"+L[35]+" : "+L[36]+"\n"+L[37]+" : "+L[38]+"\n"+L[39]+" : "+L[40]+"\n"+L[41]+" :\n"+L[42]+" : "+L[43]+"\n"+L[44]+" : "+L[45]

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.starttls()
    s.login(SMTP_USERNAME, SMTP_PASSWORD)
    message = 'Subject: {}\n\n{}'.format(EMAIL_SUBJECT, EMAIL_MESSAGE)
    s.sendmail(EMAIL_FROM, EMAIL_TO, message)
    s.quit()

    F.close()
    messagebox.showinfo("Information", "E-mail envoyé avec succès !")


def notif():
    top = tk.Toplevel(fenêtre)
    top.title("Notifications")
    top.geometry("800x650")
    top.configure(bg="lightblue")

    l2=Label(top,text="Recevoir quel emploi du temps ?",font=('Bahnschrift',30),bg="lightblue",fg="black")
    l2.pack(side=TOP,pady=30)
    
    b7=Button(top,text="Lundi",font=('Bahnschrift',20),width = 15,bg="white",fg="black",command=con_lundi)
    b7.pack(side=TOP,pady=5)

    b8=Button(top,text="Mardi",font=('Bahnschrift',20),width = 15,bg="white",fg="black",command=con_mardi)
    b8.pack(side=TOP,pady=5)

    b9=Button(top,text="Mercredi",font=('Bahnschrift',20),width = 15,bg="white",fg="black",command=con_mercredi)
    b9.pack(side=TOP,pady=5)

    b10=Button(top,text="Jeudi",font=('Bahnschrift',20),width = 15,bg="white",fg="black",command=con_jeudi)
    b10.pack(side=TOP,pady=5)

    b11=Button(top,text="Vendredi",font=('Bahnschrift',20),width = 15,bg="white",fg="black",command=con_vendredi)
    b11.pack(side=TOP,pady=5)

    b12=Button(top,text="Samedi",font=('Bahnschrift',20),width = 15,bg="white",fg="black",command=con_samedi)
    b12.pack(side=TOP,pady=5)

    b13=Button(top,text="Semaine complète",font=('Bahnschrift',20),width = 15,bg="white",fg="black",command=con_semaine)
    b13.pack(side=TOP,pady=5)

    btn2 = Button(top, text ="Fermer", font=('Bahnschrift',15),command = top.destroy) 
    btn2.pack(side=RIGHT,padx = 10,pady = 10)

def con_lundi():
    con = tk.Toplevel(fenêtre)
    con.title("Connexion")
    con.geometry("600x300")
    con.configure(bg="lightblue")

    def getEntry():
        res = e1.get()
        email_lundi(res)

    l3=Label(con,text="Veuillez entrer votre adresse email :",font=('Bahnschrift',25),bg="lightblue",fg="black")
    l3.pack(side=TOP,pady=30)
    
    e1=Entry(con,width=30,font=('Bahnschrift',25),bg="white",fg="black")
    e1.pack(side=TOP,pady=5)
    
    btn = tk.Button(con, height=1, width=10, text="Valider",font=('Bahnschrift',15),bg="white",fg="black",command=getEntry)
    btn.pack(side=TOP,pady=20)

    btn2 = Button(con, text ="Fermer", font=('Bahnschrift',15),command = con.destroy) 
    btn2.pack(side=RIGHT,padx = 10,pady = 10)

    

def con_mardi():
    con = tk.Toplevel(fenêtre)
    con.title("Connexion")
    con.geometry("600x300")
    con.configure(bg="lightblue")

    def getEntry():
        res = e1.get()
        email_mardi(res)

    l3=Label(con,text="Veuillez entrer votre adresse email :",font=('Bahnschrift',25),bg="lightblue",fg="black")
    l3.pack(side=TOP,pady=30)
    
    e1=Entry(con,width=30,font=('Bahnschrift',25),bg="white",fg="black")
    e1.pack(side=TOP,pady=5)
    
    btn = tk.Button(con, height=1, width=10, text="Valider",font=('Bahnschrift',15),bg="white",fg="black",command=getEntry)
    btn.pack(side=TOP,pady=20)

    btn2 = Button(con, text ="Fermer", font=('Bahnschrift',15),command = con.destroy) 
    btn2.pack(side=RIGHT,padx = 10,pady = 10)



def con_mercredi():
    con = tk.Toplevel(fenêtre)
    con.title("Connexion")
    con.geometry("600x300")
    con.configure(bg="lightblue")

    def getEntry():
        res = e1.get()
        email_mercredi(res)

    l3=Label(con,text="Veuillez entrer votre adresse email :",font=('Bahnschrift',25),bg="lightblue",fg="black")
    l3.pack(side=TOP,pady=30)
    
    e1=Entry(con,width=30,font=('Bahnschrift',25),bg="white",fg="black")
    e1.pack(side=TOP,pady=5)
    
    btn = tk.Button(con, height=1, width=10, text="Valider",font=('Bahnschrift',15),bg="white",fg="black",command=getEntry)
    btn.pack(side=TOP,pady=20)

    btn2 = Button(con, text ="Fermer", font=('Bahnschrift',15),command = con.destroy) 
    btn2.pack(side=RIGHT,padx = 10,pady = 10) 



def con_jeudi():
    con = tk.Toplevel(fenêtre)
    con.title("Connexion")
    con.geometry("600x300")
    con.configure(bg="lightblue")

    def getEntry():
        res = e1.get()
        email_jeudi(res)

    l3=Label(con,text="Veuillez entrer votre adresse email :",font=('Bahnschrift',25),bg="lightblue",fg="black")
    l3.pack(side=TOP,pady=30)
    
    e1=Entry(con,width=30,font=('Bahnschrift',25),bg="white",fg="black")
    e1.pack(side=TOP,pady=5)
    
    btn = tk.Button(con, height=1, width=10, text="Valider",font=('Bahnschrift',15),bg="white",fg="black",command=getEntry)
    btn.pack(side=TOP,pady=20)

    btn2 = Button(con, text ="Fermer", font=('Bahnschrift',15),command = con.destroy) 
    btn2.pack(side=RIGHT,padx = 10,pady = 10)


def con_vendredi():
    con = tk.Toplevel(fenêtre)
    con.title("Connexion")
    con.geometry("600x300")
    con.configure(bg="lightblue")

    def getEntry():
        res = e1.get()
        email_vendredi(res)

    l3=Label(con,text="Veuillez entrer votre adresse email :",font=('Bahnschrift',25),bg="lightblue",fg="black")
    l3.pack(side=TOP,pady=30)
    
    e1=Entry(con,width=30,font=('Bahnschrift',25),bg="white",fg="black")
    e1.pack(side=TOP,pady=5)
    
    btn = tk.Button(con, height=1, width=10, text="Valider",font=('Bahnschrift',15),bg="white",fg="black",command=getEntry)
    btn.pack(side=TOP,pady=20)

    btn2 = Button(con, text ="Fermer", font=('Bahnschrift',15),command = con.destroy) 
    btn2.pack(side=RIGHT,padx = 10,pady = 10)



def con_samedi():
    con = tk.Toplevel(fenêtre)
    con.title("Connexion")
    con.geometry("600x300")
    con.configure(bg="lightblue")

    def getEntry():
        res = e1.get()
        email_samedi(res)

    l3=Label(con,text="Veuillez entrer votre adresse email :",font=('Bahnschrift',25),bg="lightblue",fg="black")
    l3.pack(side=TOP,pady=30)
    
    e1=Entry(con,width=30,font=('Bahnschrift',25),bg="white",fg="black")
    e1.pack(side=TOP,pady=5)
    
    btn = tk.Button(con, height=1, width=10, text="Valider",font=('Bahnschrift',15),bg="white",fg="black",command=getEntry)
    btn.pack(side=TOP,pady=20)

    btn2 = Button(con, text ="Fermer", font=('Bahnschrift',15),command = con.destroy) 
    btn2.pack(side=RIGHT,padx = 10,pady = 10)



def con_semaine():
    con = tk.Toplevel(fenêtre)
    con.title("Connexion")
    con.geometry("600x300")
    con.configure(bg="lightblue")

    def getEntry():
        res = e1.get()
        email_semaine(res)

    l3=Label(con,text="Veuillez entrer votre adresse email :",font=('Bahnschrift',25),bg="lightblue",fg="black")
    l3.pack(side=TOP,pady=30)
    
    e1=Entry(con,width=30,font=('Bahnschrift',25),bg="white",fg="black")
    e1.pack(side=TOP,pady=5)
    
    btn = tk.Button(con, height=1, width=10, text="Valider",font=('Bahnschrift',15),bg="white",fg="black",command=getEntry)
    btn.pack(side=TOP,pady=20)

    btn2 = Button(con, text ="Fermer", font=('Bahnschrift',15),command = con.destroy) 
    btn2.pack(side=RIGHT,padx = 10,pady = 10)


def stats():
    stats = tk.Toplevel(fenêtre)
    stats.title("Statistiques")
    stats.geometry("500x270")
    stats.configure(bg="lightblue")

    b12=Button(stats,text="Matières",font=('Bahnschrift',20),width = 15,bg="white",fg="black",command=stat_mat)
    b12.pack(side=TOP,pady=5)

    b13=Button(stats,text="Temps de travail",font=('Bahnschrift',20),width = 15,bg="white",fg="black",command=stat_trav)
    b13.pack(side=TOP,pady=5)

    b3=Button(stats,text="Pôles",font=('Bahnschrift',20),width = 15,bg="white",fg="black",command=stat_pole)
    b3.pack(side=TOP,pady=5)

    btn2 = Button(stats, text ="Fermer", font=('Bahnschrift',15),command = stats.destroy) 
    btn2.pack(side=RIGHT,padx = 10,pady = 10)


def aide():
    aide = tk.Toplevel(fenêtre)
    aide.title("Aide")
    aide.geometry("900x600")
    aide.configure(bg="lightblue")

    l1=Label(aide,text="Ce logiciel a pour but de vous aider à planifier votre journée en tant qu'étudiant à l'IPSA"+"\n"+"Voici comment l'utiliser :",font=('Bahnschrift',16),bg="white",fg="black")
    l1.place(x=10, y=10)

    b1=Button(aide,text="Pegasus",font=('Bahnschrift',15),bg="white",fg="black")
    b1.place(x=10, y=100)

    l2=Label(aide,justify=LEFT,text="vous redirige vers Pegasus. Il vous faut prendre une capture d'écran"+"\n"+"de votre emploi du temps en respectant ces paramètres :"+"\n"+"- Google Chrome"+"\n"+"- Mode plein écran"+"\n"+"- Zoom 80%"+"\n"+"- se placer en haut de la page"+"\n"+"- outil capture d'écran Windows en mode fenêtre"+"\n",font=('Bahnschrift',15),bg="lightblue",fg="black")
    l2.place(x=120,y=100)

    b2=Button(aide,text="Mise à jour",font=('Bahnschrift',15),bg="white",fg="black")
    b2.place(x=10, y=310)

    l3=Label(aide,text="vous permet de sélectionner votre capture d'écran.",font=('Bahnschrift',15),bg="lightblue",fg="black")
    l3.place(x=135,y=310)

    b3=Button(aide,text="Notifications",font=('Bahnschrift',15),bg="white",fg="black")
    b3.place(x=10, y=390)

    l4=Label(aide,justify=LEFT,text="vous permet de vous connecter avec votre adresse email ainsi que de choisir"+"\n"+"l'emploi du temps que vous voulez recevoir.",font=('Bahnschrift',15),bg="lightblue",fg="black")
    l4.place(x=150,y=390)

    b4=Button(aide,text="Statistiques",font=('Bahnschrift',15),bg="white",fg="black")
    b4.place(x=10, y=480)

    l5=Label(aide,text="vous affiche quelques statistiques sur votre semaine.",font=('Bahnschrift',15),bg="lightblue",fg="black")
    l5.place(x=145,y=480)
    
    b5 = Button(aide, text ="Fermer", font=('Bahnschrift',15),command = aide.destroy) 
    b5.place(x=805,y=550)



def stat_mat():
    F=open("fichier.csv","r")
    for l in F.readlines():
        L=l.split(";")
    F.close()

    GE = L.count("Genie electrique")
    PR = L.count("Programmation")
    MA = L.count("Mathematiques")
    AN = L.count("Anglais")
    PH = L.count("Physique")
    EL = L.count("Electronique")
    TE = L.count("Techniques d'expression et de communication")
    IN = L.count("Projet informatique")
    AE = L.count("Introduction au monde aeronautique et spatial")
    AL = L.count("Algorithmique")
    PI = L.count("Piscine d'anglais")
    PE = L.count("Projet electronique")
    
    labels = 'Génie électrique', 'Programmation','Mathématiques','Anglais','Physique','Electronique','Techniques dexpression et de communication','Projet informatique','Introduction au monde aéronautique et spatial','Algorithmique','Piscine danglais','Projet electronique'
    sizes = numpy.array([GE*2,PR*2,MA*2,AN*2,PH*2,EL*2,TE*2,IN*2,AE*2,AL*2,PI*2,PE*2])
    colors = ['green', 'red','yellow','lightblue','darkblue','purple','orange','pink','grey','brown','lime','magenta']

    def absolute_value(val):
        a  = numpy.round(val/100.*sizes.sum())
        return a

    plt.pie(sizes, labels=labels, colors=colors,
        autopct=absolute_value)
    
    plt.axis('equal')
    plt.title("Matières")
    plt.savefig("matieres.pdf")
    plt.show()


def stat_pole():
    F=open("fichier.csv","r")
    for l in F.readlines():
        L=l.split(";")
    F.close()

    #GE = L.count("Genie electrique")
    #PR = L.count("Programmation")
    #MA = L.count("Mathematiques")
    #AN = L.count("Anglais")
    #PH = L.count("Physique")
    #EL = L.count("Electronique")
    #TE = L.count("Techniques d'expression et de communication")
    #IN = L.count("Projet informatique")
    #AE = L.count("Introduction au monde aeronautique et spatial")
    #AL = L.count("Algorithmique")
    #PI = L.count("Piscine d'anglais")
    #PE = L.count("Projet electronique")

    SF = L.count("Mathematiques")+L.count("Physique")
    PI = L.count("Programmation")+L.count("Projet informatique")+L.count("Algorithmique")
    PE = L.count("Genie electrique")+L.count("Electronique")+L.count("Projet electronique")
    PL = L.count("Anglais")+L.count("Techniques d'expression et de communication")+L.count("Piscine d'anglais")
    SA = L.count("Introduction au monde aeronautique et spatial")
    
    labels = 'Sciences fondamentales', 'Pôle informatique','Pôle électricité','Pôle langage','Sciences appliquées'
    sizes = numpy.array([SF*2,PI*2,PE*2,PL*2,SA*2])
    colors = ['green','yellow','lightblue','orange','lime']

    def absolute_value(val):
        a  = numpy.round(val/100.*sizes.sum())
        return a

    plt.pie(sizes, labels=labels, colors=colors,
        autopct=absolute_value)
    
    plt.axis('equal')
    plt.title("Pôles")
    plt.savefig("poles.pdf")
    plt.show()

    

def stat_trav():
   

    F=open("fichier.csv","r")
    for l in F.readlines():
        L=l.split(";")
    F.close()

    PC = L.count("---")
    YC = 20-PC
    
    labels = 'Pas cours', 'Cours'
    sizes = numpy.array([PC*2,YC*2])
    colors = ['red', 'green']

    def absolute_value(val):
        a  = numpy.round(val/100.*sizes.sum())
        return a

    plt.pie(sizes, labels=labels, colors=colors,
        autopct=absolute_value)

    plt.axis('equal')
    plt.title("Temps de travail")
    plt.savefig("temps_de_travail.pdf")
    plt.show()
    


    

#--------------------------------------------------------------------------
#PP
#--------------------------------------------------------------------------

fenêtre=tk.Tk()

fenêtre.title("Assistant d'organisation")
fenêtre.attributes('-fullscreen', True)
fenêtre.bind('<Escape>',lambda e: fenêtre.destroy())
fenêtre.configure(bg="lightblue")

l1=Label(fenêtre,text="ASSISTANT D'ORGANISATION",font=('Bahnschrift',60),bg="lightblue",fg="black")
l1.pack(side=TOP,pady=60)

b1=Button(fenêtre,text="Pegasus",font=('Bahnschrift',25),bg="white",fg="black",command=GoUrl)
b1.pack(side=TOP,pady=30)

b2=Button(fenêtre,text="Mise à jour",font=('Bahnschrift',25),bg="white",fg="black",command=maj)
b2.pack(side=TOP,pady=30)

b3=Button(fenêtre, text="Notifications",font=('Bahnschrift',25),bg="white",fg="black",command=notif)
b3.pack(side=TOP,pady=30)

b4=Button(fenêtre,text="Quitter",font=('Bahnschrift',25),bg="white",fg="black",command=fenêtre.destroy)
b4.place(x=10,y=783)

b5=Button(fenêtre,text="Aide",font=('Bahnschrift',25),bg="white",fg="black",command=aide)
b5.pack(side=BOTTOM,pady=10)

b6=Button(fenêtre,text="Statistiques",font=('Bahnschrift',25),bg="white",fg="black",command=stats)
b6.place(x=1325,y=783)

fenêtre.mainloop()
