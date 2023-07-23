import time
import tkinter as tk
##import sys
import time
from tkinter.messagebox import showinfo
from tkinter import messagebox
import playsound
from playsound import playsound
from tkinter import END
from PIL import ImageTk
import threading
import os
import sys
import pkg_resources

r = 0
key = 0
label7 = 0

def muz():
##        audiofile="C:\\na.wav"
##        playsound(audiofile)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        wav_file = os.path.join(script_dir, '1na.wav')
        audiofile = wav_file
        playsound(audiofile)

def muz3():
##        audiofile="C:\\vzr3.wav"
##        playsound(audiofile)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        wav_file = os.path.join(script_dir, 'vzr3.wav')
        audiofile = wav_file
        playsound(audiofile)
def vzr2():
         script_dir = os.path.dirname(os.path.abspath(__file__))
         wav_file = os.path.join(script_dir, 'vzr2.wav')
         audiofile = wav_file
         playsound(audiofile)
def ser():
         script_dir = os.path.dirname(os.path.abspath(__file__))
         wav_file = os.path.join(script_dir, '3s.wav')
         audiofile = wav_file
         playsound(audiofile)
def vzr1():
         script_dir = os.path.dirname(os.path.abspath(__file__))
         wav_file = os.path.join(script_dir, 'vzr1.wav')
         audiofile = wav_file
         playsound(audiofile)

def rty2():
        root2 = tk.Tk()
        root2.title('Сапер')
        root2.geometry('700x150')
        root2.resizable(width=False, height=False)
        muz3()
        label1 = tk.Label(root2, text='   Вы отлично разминировали все предложения.\n Из Вас выйдет хороший сапер, ждите звонка из ВК ', font=("Helvetica", 20),  fg="red")
        label1.place(relx=0, rely=0.1)
        root2.after(10000, root2.destroy)
        root.after(10100, root.destroy)



def rty():
        root1 = tk.Tk()
        root1.title('Сапер')
        root1.geometry('700x150')
        root1.resizable(width=False, height=False)
        label1 = tk.Label(root1, text='   ВЫ НАСТУПИЛИ НА ЗАМИНИРОВАННОЕ СЛОВО ', font=("Helvetica", 20),  fg="red")
        label1.place(relx=0, rely=0.1)
        root1.after(10000, root1.destroy)

def keyw3(Event):
        global key
        global r
##        audio_file="C:\\vzr2.wav"
        key = entry3.get()
        if key in('сбежать', 'уплыть'):
         rty()
         vzr2()
##         playsound(audio_file)
         
         root.destroy()
        if key in ('увернуться','спрятяться','обмануть','избежать','смыться','испариться','изчезнуть','укрыться','скрыться', 'свалить'):
         entered_text = entry3.get()
         entry3.delete(0, END)  # очистить поле ввода
         entry3.insert(0, key)  # вставить введенный текст
         entry3.config(foreground="green")  # изменить цвет текста на зеленый
         ser()
         r += 1 
         
         if r == 3:
          rty2()
##r = keyw3(Event)

def keyw2(Event):
        global key
        global r
##        audio_file="C:\\vzr2.wav"
        key = entry2.get()
        if key == 'хищник':
         rty()
         vzr2()
         root.destroy()
        if key in ('щука','рыбак','невод','сети','холод','жар','вирус','болезнь', 'рыбаки','среда','акула','кит',',бактерии'):
          entered_text = entry2.get()
          entry2.delete(0, END)  # очистить поле ввода
          entry2.insert(0, key)  # вставить введенный текст
          entry2.config(foreground="green")  # изменить цвет текста на зеленый
          ser()
          r += 1       
        if r == 3:
          rty2()

def keyw(Event):           
        global key
        global r
        key = entry.get()
        if key == 'хвост':
         rty()        
##         audio_file = "C:\\vzr1.wav"
         vzr1()
         root.destroy()
        if key in ('глаз','глаза','плавник','плавники','чешуя','рот','мозги'):
         
         entered_text = entry2.get()
         entry.delete(0, END)  # очистить поле ввода
         entry.insert(0, key)  # вставить введенный текст
         entry.config(foreground="green")  # изменить цвет текста на зеленый
##         playsound(audio_file2)
         ser()
         r += 1
         
         if r == 3:
          rty2()
                                 

root = tk.Tk()
root.title('Сапер')
root.geometry('630x450')
root.resizable(width=False, height=False)
              

labe7 = tk.Label(text='Спонсор разработки сайт: Stoptut.ru ♥ ', font=("Times New Roman", 10),foreground='Blue')
labe7.pack(anchor="n")

label5 = tk.Label(root, text='   Для разминирования предложений необходимо перебирать подходящие по смыслу\n слово, подтверждая выбор кнопкой <Enter>. Однако, следует знать, \n что самые из них первые, приходящие в голову  могут быть заминированы☭', font=("Helvetica", 12))
label5.place(relx=0, rely=0.3)

label1 = tk.Label(root, text='   У рыбы есть  ', font=("Helvetica", 12))
label1.place(relx=0, rely=0.5)

##entry = tk.Entry(root, font="Arial", 12, justify=CENTER, width=6)
entry = tk.Entry(root, font="Arial", justify="center", width=8)
entry.place(relx=0.19, rely=0.5)


label2 = tk.Label(root, text='без этого ей будет плохо, потому что', font=("Helvetica", 12))
label2.place(relx=0.37, rely=0.5)

entry2 = tk.Entry(root, font="Arial", justify="center", width=8)
entry2.place(relx=0.81, rely=0.5)

label3 = tk.Label(root, text='   может  стать  причиной  ее  конца, если  она  не  увидит опасность, не  сможет', font=("Helvetica", 12))
label3.place(relx=0, rely=0.56)

entry3 = tk.Entry(root, font="Arial", justify="center", width=8)
entry3.place(relx=0.2, rely=0.62)

label4 = tk.Label(root, text='  что бы избежать гибели', font=("Helvetica", 12))
label4.place(relx=0.36, rely=0.62)

music_thread = threading.Thread(target=muz)
music_thread.start()






root.bind_all('<Return>', lambda event: None)
entry.bind('<Return>', keyw)
entry2.bind('<Return>', keyw2)
entry3.bind('<Return>', keyw3)



root.mainloop()






