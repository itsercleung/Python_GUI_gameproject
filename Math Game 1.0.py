#Eric
#Python Tkinter Program for Simple Maths Game

from tkinter import *
import random

#Global Values for functions: Some variables change within subroutine, so use of global would easily reset
n_number = 0
n_answer = 0
n = 0
m = 0

#Quit Function for exiting window
def quit():
    window.destroy()

#Reset Function for reseting all displayed functions such as text
def reset():

    #Reset of labels that function start() changed
    message_label = (Label(window, bg= "white",text= "Press the Start Button!"))
    canvas.create_window(200, 50, width=300, height=13,window=message_label)
    canvas.create_rectangle(40, 70, 360, 310, fill="salmon", outline="white")
    label_forget()

    #Reset of startbutton which was disabled from start()
    startbutton = (Button(window, text="Start", width=5, bg="turquoise", fg="white",command=start, state=NORMAL))
    canvas.create_window(200, 20, width=100, window=startbutton)
    
#Fixture towards positioning text and box generated values
def new_start():
    global x
    global y
    global num
    x = 80
    y += 80
    num = random.randint(1,9)

#Start Function for starting Math Game with random numbers and text displays
def start():
    global x
    global y
    global num
    global n
    global m
    global question_text
    x = 80
    y = 80

    #When start button is activated, start button is disabled until reset
    startbutton = (Button(window, text="Start", width=5, bg="turquoise", fg="white",command=start, state=DISABLED))
    canvas.create_window(200, 20, width=100, window=startbutton)
  
    #Number Lables created from start function
    label_generate()
  
    #Label Function to display randomized question values and to generate message
    n = random.randint(4,6)
    m = random.randint(0,3)
    question_text = StringVar()
    question_text.set("{} + {} = ?".format(n,m))
    question_label = (Label(window, bg= "white",textvariable= question_text))
    canvas.create_window(200, 50, width=120, height=9,window=question_label)
  
    message_label = (Label(window, bg= "white",text= "Question 1:"))
    canvas.create_window(100, 50, width=110, height=13,window=message_label)

    #Number Function to display randomized number values for the boxes for variety
    for i in range(3):
        for i in range(3):
            canvas.create_rectangle(x, y, x+60, y+60, fill="turquoise", outline="white")
            x += 80
        new_start()

#Button Click Function used for when mouse clicks on squares to make a command
def buttonclick(event):
    global n_number
    
    #Button Clicking event for 0-9
    if event.x >80 and event.x < 140 and event.y > 80 and event.y < 140 : pressed = 1
    if event.x >160 and event.x < 220 and event.y > 80 and event.y < 140 : pressed = 2
    if event.x >240 and event.x < 300 and event.y > 80 and event.y < 140 : pressed = 3
    if event.x >80 and event.x < 140 and event.y > 160 and event.y < 220 : pressed = 4
    if event.x >160 and event.x < 220 and event.y > 160 and event.y < 220 : pressed = 5
    if event.x >240 and event.x < 300 and event.y > 160 and event.y < 220 : pressed = 6
    if event.x >80 and event.x < 140 and event.y > 240 and event.y < 300 : pressed = 7
    if event.x >160 and event.x < 220 and event.y > 240 and event.y < 300 : pressed = 8
    if event.x >240 and event.x < 300 and event.y > 240 and event.y < 300 : pressed = 9

    #If certain boxes a pressed then assign number to what is pressed
    if pressed == 0 or pressed == 1 or pressed == 2 or pressed == 3 or pressed == 4 or pressed == 5 or pressed == 6 or pressed == 7 or pressed == 8 or pressed == 9 :
        print("Hey its working")
        n_number = pressed

    #If number box is correct initiate next question
    n1_answer = n + m
    if n_number == n1_answer:
        print("You're correct!")
        message_label = (Label(window, bg= "white",text= "Question 2:"))
        canvas.create_window(100, 50, width=110, height=13,window=message_label)
        equation_function()

    #If number box is correct initiate next question
    n2_answer = p + q
    if n_number == n2_answer:
        print("You're correct!")
        message_label = (Label(window, bg= "white",text= "Question 3:"))
        canvas.create_window(100, 50, width=110, height=13,window=message_label)
        equation_function()


#For reseting equation generating, to make new question if answer is correct
def equation_function():
    global p
    global q
    p = random.randint(4,6)
    q = random.randint(0,3)
    question_text = StringVar()
    question_text.set("{} + {} = ?".format(p,q))
    question_label = (Label(window, bg= "white",textvariable= question_text))
    canvas.create_window(200, 50, width=120, height=9,window=question_label)


#Main Function used for the initial program and conjoins everything for the user
def main():
    global window
    global tkinter
    global canvas

    #Canvas Setup window
    window = Tk()
    window.title("Stupid Math Game 1.0")
    canvas = Canvas(window, width=395, height= 320, bg = 'beige')
    canvas.bind("<Button-1>", buttonclick)

    #Button Setup for Quit, Start and Reset
    quitbutton = (Button(window, text="Quit", width=5, bg="salmon", fg="white",command=quit))
    canvas.create_window(90, 20, width=100, window=quitbutton)
    startbutton = (Button(window, text="Start", width=5, bg="turquoise", fg="white",command=start))
    canvas.create_window(200, 20, width=100, window=startbutton)
    resetbutton = (Button(window, text="Reset", width=5, bg="turquoise", fg="white",command=reset))
    canvas.create_window(310, 20, width=100, window=resetbutton)
    canvas.grid()

    #Display Setup
    canvas.create_rectangle(40, 40, 360, 60, fill="white", outline="salmon")
    canvas.create_rectangle(40, 70, 360, 310, fill="salmon", outline="white")
    message_label = (Label(window, bg= "white",text= "Press the Start Button!"))
    canvas.create_window(200, 50, width=300, height=13,window=message_label)

##Generate position of text
def label_generate():
    global label_1
    global label_2
    global label_3
    global label_4
    global label_5
    global label_6
    global label_7
    global label_8
    global label_9
    label_1 = (Label(window, bg= "turquoise", fg="white", text= "1", font= "Arial 20"))
    label_1.place(relx=0.25, rely=0.28)
    label_2 = (Label(window, bg= "turquoise", fg="white", text= "2", font= "Arial 20"))
    label_2.place(relx=0.45, rely=0.28)
    label_3 = (Label(window, bg= "turquoise", fg="white", text= "3", font= "Arial 20"))
    label_3.place(relx=0.65, rely=0.28)
    label_4 = (Label(window, bg= "turquoise", fg="white", text= "4", font= "Arial 20"))
    label_4.place(relx=0.25, rely=0.53)
    label_5 = (Label(window, bg= "turquoise", fg="white", text= "5", font= "Arial 20"))
    label_5.place(relx=0.45, rely=0.53)
    label_6 = (Label(window, bg= "turquoise", fg="white", text= "6", font= "Arial 20"))
    label_6.place(relx=0.65, rely=0.53)
    label_7 = (Label(window, bg= "turquoise", fg="white", text= "7", font= "Arial 20"))
    label_7.place(relx=0.25, rely=0.78)
    label_8 = (Label(window, bg= "turquoise", fg="white", text= "8", font= "Arial 20"))
    label_8.place(relx=0.45, rely=0.78)
    label_9 = (Label(window, bg= "turquoise", fg="white", text= "9", font= "Arial 20"))
    label_9.place(relx=0.65, rely=0.78)

##To forget the labels generated from start
def label_forget():
    label_1.place_forget()
    label_2.place_forget()
    label_3.place_forget()
    label_4.place_forget()
    label_5.place_forget()
    label_6.place_forget()
    label_7.place_forget()
    label_8.place_forget()
    label_9.place_forget()
    
main()
