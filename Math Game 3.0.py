#***************     Eric       *********************#
#****Python Tkinter Program for Simple Maths Game****#

from tkinter import *
import random
import tkinter.messagebox as tm

#Global Values for functions
n_number = 0
n_answer = 0
n = 0
m = 0

#Quit Function for exiting window
def quit():
    window.destroy()

#Reset Function for reseting all displayed functions such as text: Reseting the game, in case user doesn't know question
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
    global x, y, num
    x = 80
    y += 80
    num = random.randint(1,9)

#Start Function for starting Math Game with random numbers and text displays
def start():
    global x, y, num, n, m
    x = 80
    y = 80

    #When start button is activated, start button is disabled until reset
    startbutton = (Button(window, text="Start", width=5, bg="turquoise", fg="white",command=start, state=DISABLED))
    canvas.create_window(200, 20, width=100, window=startbutton)
  
    #Number Lables created from start function
    label_generate()

    if age >= str(2) and age <= str(3):
        equation_function1()

    if age >= str(4) and age <= str(5):
        equation_function2()

    if age == str(6):
        equation_function3()

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
        n_number = pressed

    #If number box is correct initiate next question
    n1_answer = n + m
    if n_number == n1_answer:
        equation_function1()

    #If number box is correct initiate next question
    n2_answer = n - m
    if n_number == n2_answer:
        equation_function2()

    #If number box is correct initiate next question
    n3_answer = n * m
    if n_number == n3_answer:
        equation_function3()

#For reseting equation generating, to make new question if answer is correct
def equation_function1():
    global n, m
    n = random.randint(1,5)
    m = random.randint(1,4)
    question1_text = StringVar()
    question1_text.set("{} + {} = ?".format(n,m))
    question1_label = (Label(window, bg= "white",textvariable=question1_text))
    canvas.create_window(200, 50, width=120, height=10,window=question1_label)

def equation_function2():
    global n, m
    n = random.randint(5,9)
    m = random.randint(1,4)
    question2_text = StringVar()
    question2_text.set("{} - {} = ?".format(n,m))
    question2_label = (Label(window, bg= "white",textvariable=question2_text))
    canvas.create_window(200, 50, width=120, height=10,window=question2_label)

def equation_function3():
    global n, m
    n = random.randint(1,3)
    m = random.randint(1,3)
    question3_text = StringVar()
    question3_text.set("{} * {} = ?".format(n,m))
    question3_label = (Label(window, bg= "white",textvariable=question3_text))
    canvas.create_window(200, 50, width=120, height=10,window=question3_label)

#Main Function used for the initial program and conjoins everything for the user
def main():
    global window, tkinter, canvas, message_label

    #Canvas Setup window
    window = Tk()
    window.title("Math Game 2.0")
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
    canvas.create_rectangle(40, 40, 360, 65, fill="white", outline="salmon")
    canvas.create_rectangle(40, 70, 360, 310, fill="salmon", outline="white")
    message_label = (Label(window, bg= "white",text= "Press the Start Button!"))
    message_label.place(relx=0.35, rely=0.13)
    
#Generate position of text
def label_generate():
    global label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, label_9, question_label
    label_1 = (Label(window, bg="turquoise", fg="white", text="1", font="Arial 20"))
    label_1.place(relx=0.25, rely=0.28)
    label_2 = (Label(window, bg="turquoise", fg="white", text="2", font="Arial 20"))
    label_2.place(relx=0.45, rely=0.28)
    label_3 = (Label(window, bg="turquoise", fg="white", text="3", font="Arial 20"))
    label_3.place(relx=0.65, rely=0.28)
    label_4 = (Label(window, bg="turquoise", fg="white", text="4", font="Arial 20"))
    label_4.place(relx=0.25, rely=0.53)
    label_5 = (Label(window, bg="turquoise", fg="white", text="5", font="Arial 20"))
    label_5.place(relx=0.45, rely=0.53)
    label_6 = (Label(window, bg="turquoise", fg="white", text="6", font="Arial 20"))
    label_6.place(relx=0.65, rely=0.53)
    label_7 = (Label(window, bg="turquoise", fg="white", text="7", font="Arial 20"))
    label_7.place(relx=0.25, rely=0.78)
    label_8 = (Label(window, bg="turquoise", fg="white", text="8", font="Arial 20"))
    label_8.place(relx=0.45, rely=0.78)
    label_9 = (Label(window, bg="turquoise", fg="white", text="9", font="Arial 20"))
    label_9.place(relx=0.65, rely=0.78)
    question_label = (Label(window, bg="white",text="What is: "))
    question_label.place(relx=0.2, rely=0.125)
    message_label.place_forget()
    
#To forget the labels generated from start
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
    question_label.place_forget()

#Login Form which is launched at start
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        #Labels and positions on the login form for Name and Age
        self.label_1 = Label(self, text="Name", bg="turquoise", fg="white", padx=9)
        self.label_2 = Label(self, text="Age ", bg="turquoise", fg="white", padx=13)
        self.info = Label(self, text="Math Game 2.0", bg="turquoise", fg="white", padx=50, pady=5, font="Arial 10")
        self.info2 = Label(self, text="2-6 Years", bg="salmon", fg="white", padx=72, font="Arial 7")
        self.entry_1 = Entry(self, bg="salmon", fg="white")
        self.entry_2 = Entry(self, bg="salmon", fg="white")
        
        self.label_1.grid(row=2, sticky=E)
        self.label_2.grid(row=3, sticky=E)
        self.info.grid(row=0, columnspan=2, sticky=E)
        self.info2.grid(row=1, columnspan=2, sticky=E)
        self.entry_1.grid(row=2, column=1, pady=2, padx=3)
        self.entry_2.grid(row=3, column=1, pady=2, padx=3)
        root.title("")

        #Login Buttons and packing Login window
        self.loginbutton = Button(self, text="Login",bg="turquoise", fg="white", command=self.loginbutton_clicked)
        self.loginbutton.grid(columnspan=2, sticky=E, padx=6, pady=2)
        self.pack()
    
    #Exceptions to when login button is clicked on
    def loginbutton_clicked(self):
        global age
        
        #print if clicked on
        name = self.entry_1.get()
        age = self.entry_2.get()

        #print name and age and the exceptions   
        if name == "" or age == "" or age <= str(1) or age >= str(7)or name.isdigit() or age.isalpha(): 
            tm.showinfo("!Error!", "Input correct Name and/or Age!")

        elif name.isalpha() and age.isdigit() and age >= str(2):
            tm.showinfo("!Welcoime!", "Lets goooo!")
            root.destroy()
            main()

#Baseline of running root tkinter GUI (login)
root = Tk()
lf = LoginFrame(root)
root.mainloop()




