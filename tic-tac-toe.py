import tkinter.messagebox
from tkinter import *
from tkinter import ttk



win = Tk()
win.title("TIC-TAC-TOE")
win.geometry("471x445")
win.resizable(0,0)

b1 = ttk.Button(win,text=" ")
b1.grid(row =0,column =0,sticky='snew',ipadx=40,ipady=40)
b1.config(command=lambda:buttonclick(1))


b2 = ttk.Button(win,text=" ")
b2.grid(row =0,column =1,sticky='snew',ipadx=40,ipady=40)
b2.config(command=lambda:buttonclick(2))

b3 = ttk.Button(win,text=" ")
b3.grid(row =0,column =2,sticky='snew',ipadx=40,ipady=40)
b3.config(command=lambda:buttonclick(3))

b4 = ttk.Button(win,text=" ")
b4.grid(row =1,column =0,sticky='snew',ipadx=40,ipady=40)
b4.config(command=lambda:buttonclick(4))

b5 = ttk.Button(win,text=" ")
b5.grid(row =1,column =1,sticky='snew',ipadx=40,ipady=40)
b5.config(command=lambda:buttonclick(5))

b6 = ttk.Button(win,text=" ")
b6.grid(row =1,column =2,sticky='snew',ipadx=40,ipady=40)
b6.config(command=lambda:buttonclick(6))

b7 = ttk.Button(win,text=" ")
b7.grid(row =2,column =0,sticky='snew',ipadx=40,ipady=40)
b7.config(command=lambda:buttonclick(7))

b8 = ttk.Button(win,text=" ")
b8.grid(row =2,column =1,sticky='snew',ipadx=40,ipady=40)
b8.config(command=lambda:buttonclick(8))

b9 = ttk.Button(win,text=" ")
b9.grid(row =2,column =2,sticky='snew',ipadx=40,ipady=40)
b9.config(command=lambda:buttonclick(9))

playerturn = ttk.Label(win,text="  Player 1 turn!")
playerturn.grid(row =3,column =0,sticky='snew',ipadx=40,ipady=40)

playerdetails = ttk.Label(win,text="Player 1 is X \n\n player 2 is O")
playerdetails.grid(row=3,column =2,sticky='snew',ipadx=40,ipady=40)

res = ttk.Button(win,text = "Restart")
res.grid(row =3,column =1,sticky='snew',ipadx=40,ipady=40)
res.config(command = lambda :restartbutton())


a = 1
b = 0
c = 0

def restartbutton():
    global a,b,c
    a = 1
    b = 0
    c = 0
    playerturn["text"]="Player 1 turn!"
    b1["text"] = " "
    b2["text"] = " "
    b3["text"] = " "
    b4["text"] = " "
    b5["text"] = " "
    b6["text"] = " "
    b7["text"] = " "
    b8["text"] = " "
    b9["text"] = " "

    b1.state(['!disabled'])
    b2.state(['!disabled'])
    b3.state(['!disabled'])
    b4.state(['!disabled'])
    b5.state(['!disabled'])
    b6.state(['!disabled'])
    b7.state(['!disabled'])
    b7.state(['!disabled'])
    b8.state(['!disabled'])
    b9.state(['!disabled'])


# after getting the result (win,lose or draw)

def disablebutton():
    b1.state(['disabled'])
    b2.state(['disabled'])
    b3.state(['disabled'])
    b4.state(['disabled'])
    b5.state(['disabled'])
    b6.state(['disabled'])
    b7.state(['disabled'])
    b8.state(['disabled'])
    b9.state(['disabled'])


def buttonclick(id):
    global  a,b,c
    print("ID :{}".format(id))

    #for player 1 turn
    if id == 1 and b1["text"] == " " and a == 1:
        b1["text"] = "X"
        a = 0
        b +=1
    if id == 2 and b2["text"] == " " and a == 1:
        b2["text"] = "X"
        a = 0
        b +=1
    if id == 3 and b3["text"] == " " and a == 1:
        b3["text"] = "X"
        a = 0
        b +=1
    if id == 4 and b4["text"] == " " and a == 1:
        b4["text"] = "X"
        a = 0
        b +=1
    if id == 5 and b5["text"] == " " and a == 1:
        b5["text"] = "X"
        a = 0
        b +=1
    if id == 6 and b6["text"] == " " and a == 1:
        b6["text"] = "X"
        a = 0
        b +=1
    if id == 7 and b7["text"] == " " and a == 1:
        b7["text"] = "X"
        a = 0
        b +=1
    if id == 8 and b8["text"] == " " and a == 1:
        b8["text"] = "X"
        a = 0
        b +=1
    if id == 9 and b9["text"] == " " and a == 1:
        b9["text"] = "X"
        a = 0
        b +=1

    # fro player 2 turn
    if id == 1 and b1["text"] == " " and a == 0:
        b1["text"] = "O"
        a = 1
        b +=1
    if id == 2 and b2["text"] == " " and a == 0:
        b2["text"] = "O"
        a = 1
        b +=1
    if id == 3 and b3["text"] == " " and a == 0:
        b3["text"] = "O"
        a = 1
        b += 1
    if id == 4 and b4["text"] == " " and a == 0:
        b4["text"] = "O"
        a = 1
        b += 1
    if id == 5 and b5["text"] == " " and a == 0:
        b5['text'] = "O"
        a = 1
        b += 1
    if id == 6 and b6["text"] == " " and a == 0:
        b6["text"] = "O"
        a = 1
        b += 1
    if id == 7 and b7["text"] == " " and a == 0:
        b7["text"] = "O"
        a = 1
        b += 1
    if id == 8 and b8["text"] == " " and a == 0:
        b8["text"] = "O"
        a = 1
        b += 1
    if id == 9 and b9["text"] == " " and a == 0:
        b9["text"] = "O"
        a = 1
        b += 1

    # checking for the winner

    #checking for player 1
    if( b1['text']=='X' and b2['text'] == "X" and b3['text'] == "X" or
        b4["text"] == 'X' and b5["text"] == "X" and b6["text"] == "X" or
        b7["text"] == 'X' and b8["text"] == "X" and b9["text"] == "X" or
        b1["text"] == 'X' and b4["text"] == "X" and b7["text"] == "X" or
        b2["text"] == 'X' and b5["text"] == "X" and b8["text"] == "X" or
        b3["text"] == 'X' and b6["text"] == "X" and b9["text"] == "X" or
        b1["text"] == 'X' and b5["text"] == "X" and b9["text"] == "X" or
        b3["text"] == 'X' and b5["text"] == "X" and b7["text"] == "X" ):
        disablebutton()
        c = 1
        tkinter.messagebox.showinfo("TIC-TAC-TOE :","WINNER IS PLAYERR 1")

        #checking for player 2
    elif (b1["text"] == 'O' and b2["text"] == "O" and b3["text"] == "O" or
            b4["text"] == 'O' and b5["text"] == "O" and b6["text"] == "O" or
            b7["text"] == 'O' and b8["text"] == "O" and b9["text"] == "O" or
            b1["text"] == 'O' and b4["text"] == "O" and b7["text"] == "O" or
            b2["text"] == 'O' and b5["text"] == "O"  and b8["text"] == "O" or
            b3["text"] == 'O' and b6["text"] == "O" and b9["text"] == "O" or
            b1["text"] == 'O' and b5["text"] == "O" and b9["text"] == "O" or
            b3["text"] == 'O' and b5["text"] == "O" and b7["text"] == "O" ):
        disablebutton()
        c = 1
        tkinter.messagebox.showinfo("TIC-TAC-TOE :","WINNER IS PLAYERR 2")
    elif b == 9:
        disablebutton()
        r = tkinter.messagebox.askyesno("TIC-TAC-TOE","Do you want to play again")


        c = 1
        tkinter.messagebox.showinfo("TIC-TAC-TOE","MATCH DRAW")
    if a==1 and c == 0:
        playerturn["text"] = "  Player 1 turn!"
    elif a == 0 and c==0:
        playerturn["text"] = "  Player 2 turn!"

win.mainloop()