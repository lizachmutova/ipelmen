from tkinter import * 
import random 
 
 
window = Tk() 
window.geometry('590x590') 
window.title('Калькулятор') 
window['bg'] = 'black'

all_rezult = 0
rezult_1 = 0
rezult_2 = 0
rezult_3 = 0
rezult_4 = 0
rezult_5 = 0
rezult_6 = 0
rezult_7 = 0
rezult_8 = 0
rezult_9 = 0
rezult_10 = 0
rezult_11 = 0


def check_knopka():
    global all_rezult
    global rezult_1
    all_rezult += 1
    rezult_1 += 1 
    label['text'] = all_rezult

def check_knopka_2():
    global all_rezult
    global rezult_2
    all_rezult += 2
    rezult_2 += 2
    label['text'] = all_rezult

def check_knopka_3():
    global all_rezult
    global rezult_3
    all_rezult += 5
    rezult_3 += 5
    label['text'] = all_rezult

def check_knopka_4():
    global all_rezult
    global rezult_4
    all_rezult += 10
    rezult_4 += 10
    label['text'] = all_rezult
def check_knopka_5():
    global all_rezult
    global rezult_5
    all_rezult += 50
    rezult_5 += 50
    label['text'] = all_rezult
def check_knopka_6():
    global all_rezult
    global rezult_6
    all_rezult += 100
    rezult_6 += 100 
    label['text'] = all_rezult
def check_knopka_7():
    global all_rezult
    global rezult_7
    all_rezult += 200
    rezult_7 += 200 
    label['text'] = all_rezult
def check_knopka_8():
    global all_rezult
    global rezult_8
    all_rezult += 500
    rezult_8+= 500
    label['text'] = all_rezult
def check_knopka_9():
    global all_rezult
    global rezult_9
    all_rezult += 1000
    rezult_9 += 1000
    label['text'] = all_rezult
def check_knopka_10():
    global all_rezult
    global rezult_10
    all_rezult += 2000
    rezult_10 += 2000 
    label['text'] = all_rezult
def check_knopka_11():
    global all_rezult
    global rezult_11
    all_rezult += 5000
    rezult_11 += 5000
    label['text'] = all_rezult

fact = [
        'В среднем купюры за свой жизненный срок проходят через руки 30.000-50.000 людей.',
        'Самой распространённой в мире купюрой является банкнота в 100 американских долларов.',
        'В США на деньгах изображают портреты только уже умерших людей.',
        'В середине XIX века в США до 30% всех бывших в обиходе долларов были фальшивыми.',
        'Впервые в истории массовый выпуск круглых монет был налажен в Древнем Риме.',
        'Миллион американских долларов 100-долларовыми купюрами весит около 10 кг.',
        'Русское слово “деньги” произошло, вероятно, от тюркского “тенге”.',
        'Первые монеты на Руси были отчеканены князем Владимиром.',
        'В настоящее время название “рубль” носят валюты двух стран, России и Беларуси.',
        'Древнейшие чеканные монеты появились на Земле около 2700 лет назад.',
        'Игрушечных денег для “Монополии” ежегодно печатается больше, чем настоящих.'
        ]
r_fact = random.choice(fact)
rand_fact = random.choice(fact)
def new():
    facts['text'] = rand_fact
    new_fact.destroy()
    
knopka = Button(text='  1р  ', font=('Arial', 47), fg='SpringGreen2', bg='black',command = check_knopka) 
knopka.place(x=0, y=483) 
knopka_2 = Button(text='  2р  ', font=('Arial', 47), fg='SpringGreen2', bg='black',command = check_knopka_2) 
knopka_2.place(x=197, y=483) 
knopka_3 = Button(text = '  5р  ',font = ('Arial',47),fg = 'SpringGreen2',bg = 'black',command = check_knopka_3)
knopka_3.place(x = 394,y = 483)
knopka_4 = Button(text = '10р',font = ('Arial',40),fg = 'SpringGreen2',bg = 'black',command = check_knopka_4)
knopka_4.place(x = 457,y = 379)
knopka_5 = Button(text = '50р',font = ('Arial',40),fg = 'SpringGreen2', bg = 'black',command = check_knopka_5)
knopka_5.place(x = 324,y = 379)
knopka_0 = Button(text = '200р',font = ('Arial',40),fg = 'SpringGreen2',bg = 'black',command = check_knopka_7)
knopka_0.place(x =162,y = 379 )
knopka_100 = Button(text='100р', font=('Arial', 40), fg='SpringGreen2', bg='black',command = check_knopka_6) 
knopka_100.place(x = 0,y= 379)
knopka_6 = Button(text = '    500р    ',font = ('Arial',40),fg = 'SpringGreen2',bg = 'black',command= check_knopka_8)
knopka_6.place(x =310,y= 275 )
knopka_7 = Button(text = '    1000р    ',font = ('Arial',40),fg = 'SpringGreen2',bg = 'black',command = check_knopka_9)
knopka_7.place(x = 0,y = 275)
knopka_8 = Button(text = '    2000р    ',font = ('Arial',40),fg = 'SpringGreen2',bg = 'black',command = check_knopka_10)
knopka_8.place(x = 0,y = 175)
knopka_9 = Button(text = '    5000р    ',font = ('Arial',40),fg = 'SpringGreen2',bg = 'black',command = check_knopka_11)
knopka_9.place(x = 310,y = 175)
label = Label(text= all_rezult,font = ('Arial',46),fg = 'SpringGreen2',bg = 'black')
label.place(x = 230,y = 100)
facts = Label(text= r_fact,font = ('Arial',10),fg = 'purple1',bg = 'black')
facts.place(x = 6,y = 30)
lbl = Label(text= 'Считай и узнавай:',font = ('Arial',12),fg = 'purple1',bg = 'black')
lbl.place(x = 200,y = 2)
bord = Label(text= '__________________________________________________________',font = ('Arial',20),fg = 'purple4',bg = 'black')
bord.place(x = 0,y = 49)
new_fact= Button(text = 'Новый факт',font = ('Arial',10),fg = 'purple1',bg = 'black',command = new )
new_fact.place(x = 10,y =5 )

 
window.mainloop()