from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot=ChatBot('BOT')

trainer = ListTrainer(bot)

convo=[
        
    "Hi there!","hi","Hello",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.","In which city you live?","I live in INDORE",
    "who created you?",
    " ANKIT CHIMANIYA",
    "You're welcome.",
    "What is your name","My name is Bot",
    "How is the weathere?","Too cold here ","awesome"
    
    "Bye",
    "Bye and have a good day !!"
]
trainer.train(convo)
"""
while True: 
    query=input()
    if query=='exit':
        break;
    answer= bot.get_response(query)
    print('bot:',answer)   
"""
main = Tk() 

main.geometry("500x750")
    
main.title("My Chat bot")

img = PhotoImage(file="bot1.png")

photoL = Label(main, image = img)

photoL.pack(pady=5)
def submit():
    querry=textF.get()
    answer=bot.get_response(querry)
    
    msg.insert( END,"you : "+querry)
    msg.insert( END,"Bot : "+str(answer))
    textF.delete(0, END)



frame = Frame(main)
sc = Scrollbar(frame)
msg = Listbox(frame,width=80, height=20)
 
sc.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH,pady=10) 

frame.pack()  
#creating textfield

textF=Entry(main,font=("verdana",20))
textF.pack(fill=X,pady=10)
 
btn=Button(main,text="submit",font=("Verdana", 20),command=submit)
btn.pack() 


main.mainloop()            