#***************    Eric        *********************#
#****Python Tkinter Program for Simple Maths Game****#

from tkinter import *
import random
import tkinter.messagebox as tm

#Global Values for functions in subroutines: equation_function1, equation_function2, equation_function3 and the button_click event

##button click (event)
n_number = 0
n_answer = 0

##equation function 1
n = 0
m = 0

##equation function 2
q = 0
p = 0
r = 0

##equation function 3
s = 0
w = 0
c = 0

#Quit Function for exiting window
def quit():
    window.destroy()

#Reset Function for reseting all displayed functions such as text
def reset():

    #Reset of labels that function start() changed
    message_label = (Label(window, bg= "white",text= "Press the Start Button!"))
    canvas.create_window(200, 50, width=300, height=13,window=message_label)

    #Reset of startbutton which was disabled from start()
    startbutton = (Button(window, text="Start", width=5, bg="turquoise", fg="white",command=start, state=NORMAL))
    canvas.create_window(200, 20, width=100, window=startbutton)

#Start Function for starting Math Game with random numbers and text displays
def start():

    #When start button is activated, start button is disabled until reset
    startbutton = (Button(window, text="Start", width=5, bg="turquoise", fg="white",command=start, state=DISABLED))
    canvas.create_window(200, 20, width=100, window=startbutton)
  
    #Number Lables created from start function
    label_generate()

    #If age equals to 6, then run subroutine "equation_function3"
    if age >= str(2) and age <= str(3):
        equation_function1()

    #If age equals to 6, then run subroutine "equation_function3"
    if age >= str(4) and age <= str(5):
        equation_function2()

    #If age equals to 6, then run subroutine "equation_function3"
    if age == str(6):
        equation_function3()

#Generate position of text within the white bar in program
def label_generate():
    global question_label

    #This is a list because I wanted to be able to change the question output whenever I can, and also have suggestions up at the same time
    question_list = ["Find: ", "What is: ", "Question: "]
    question_list.append("Solve: ")
    question_label = (Label(window, bg="white",text="{}".format(question_list[3])))
    question_label.place(relx=0.2, rely=0.125)

    #When label_generate is run, then the initial message_label from "main" subroutine disappears
    message_label.place_forget()

#Button Click Function used for when mouse clicks on squares to make a command
def buttonclick(event):
    global n_number
    
    #Button Clicking event for 1-9; if mouse_1 clicks these certain positions then pressed = x
    if event.x >80 and event.x < 140 and event.y > 80 and event.y < 140 : pressed = 1
    if event.x >170 and event.x < 230 and event.y > 80 and event.y < 140 : pressed = 2
    if event.x >260 and event.x < 320 and event.y > 80 and event.y < 140 : pressed = 3
    if event.x >80 and event.x < 140 and event.y > 160 and event.y < 220 : pressed = 4
    if event.x >170 and event.x < 230 and event.y > 160 and event.y < 220 : pressed = 5
    if event.x >260 and event.x < 320 and event.y > 160 and event.y < 220 : pressed = 6
    if event.x >80 and event.x < 140 and event.y > 240 and event.y < 300 : pressed = 7
    if event.x >170 and event.x < 230 and event.y > 240 and event.y < 300 : pressed = 8
    if event.x >260 and event.x < 320 and event.y > 240 and event.y < 300 : pressed = 9

    #If certain boxes a pressed then assign number to what is pressed; so n_number = pressed
    if pressed == 1 or pressed == 2 or pressed == 3 or pressed == 4 or pressed == 5 or pressed == 6 or pressed == 7 or pressed == 8 or pressed == 9 :
        n_number = pressed

    #If number box is correct initiate next question and if incorrect do not initiate
    n1_answer = n + m
    if n_number == n1_answer:
        tm.showinfo("Note" ,"Correct!")
        equation_function1()

    #If number box is correct initiate next question and if incorrect do not initiate
    n2_answer = q - p + w
    if n_number == n2_answer:
        tm.showinfo("Note" ,"Correct!")
        equation_function2()

    #If number box is correct initiate next question and if incorrect do not initiate
    n3_answer = r * s - c
    if n_number == n3_answer:
        tm.showinfo("Note" ,"Correct!")
        equation_function3()

    #If number does not equal to the n_answers (3 of them) then display window "Incorrect"
    if n_number != n1_answer and n_number != n2_answer and n_number != n3_answer:
        tm.showinfo("Note","Incorrect!")

#For reseting equation generating, to make new question if answer is correct
def equation_function1():
    global n, m

    #Make n and m only randomize between these numbers
    n = random.randint(0,2)
    m = random.randint(3,7)

    #Function for question1 randomly generates "n + m" and is displayed in game
    question1_text = StringVar()
    question1_text.set("{} + {} = ?".format(n,m))
    question1_label = (Label(window, bg= "white",textvariable=question1_text))
    canvas.create_window(200, 50, width=120, height=10,window=question1_label)

#For reseting equation generating, to make new question if answer is correct
def equation_function2():
    global q, p, w

    #Make q, p and w only randomize between these numbers
    q = random.randint(1,7)
    p = random.randint(1,3)
    w = random.randint(0,2)

    #Function for question2 randomly generates "(q - p) + w" and is displayed in game
    question2_text = StringVar()
    question2_text.set("({} - {}) + {} = ?".format(q,p,w))
    question2_label = (Label(window, bg= "white",textvariable=question2_text))
    canvas.create_window(200, 50, width=120, height=10,window=question2_label)

#For reseting equation generating, to make new question if answer is correct
def equation_function3():
    global r, s, c

    #Make r, s and c only randomize between these numbers
    r = random.randint(1,3)
    s = random.randint(2,4)
    c = random.randint(0,3)

    #Function for question3 randomly generates "r * s - c" and is displayed in game
    question3_text = StringVar()
    question3_text.set("{} * {} - {} = ?".format(r,s,c))
    question3_label = (Label(window, bg= "white",textvariable=question3_text))
    canvas.create_window(200, 50, width=120, height=10,window=question3_label)

#Main Function used for the initial program and conjoins everything for the user
def main():
    global window, tkinter, canvas, message_label

    #Canvas Setup window: including title, width and setting up mouse click to button-1
    window = Tk()
    window.title("Math Game 4.0")
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

    #Display Setup (Canvas, rectangles and labels for 3x3 input GUI)
    canvas.create_rectangle(40, 40, 360, 65, fill="white", outline="salmon")
    canvas.create_rectangle(40, 70, 360, 310, fill="salmon", outline="white")
    message_label = (Label(window, bg= "white",text= "Press the Start Button!"))
    message_label.place(relx=0.35, rely=0.13)

    ##Rectangle (Squares) Setup
    canvas.create_rectangle(80, 80, 140, 140, fill="turquoise", outline="white")
    canvas.create_rectangle(170, 80, 230, 140, fill="turquoise", outline="white")
    canvas.create_rectangle(260, 80, 320, 140, fill="turquoise", outline="white")
    canvas.create_rectangle(80, 160, 140, 220, fill="turquoise", outline="white")
    canvas.create_rectangle(170, 160, 230, 220, fill="turquoise", outline="white")
    canvas.create_rectangle(260, 160, 320, 220, fill="turquoise", outline="white")
    canvas.create_rectangle(80, 240, 140, 300, fill="turquoise", outline="white")
    canvas.create_rectangle(170, 240, 230, 300, fill="turquoise", outline="white")
    canvas.create_rectangle(260, 240, 320, 300, fill="turquoise", outline="white")

    ##Text number Setup
    canvas.create_text(110, 110, text="1", fill="white", font="Arial 20")
    canvas.create_text(200, 110, text="2", fill="white", font="Arial 20")
    canvas.create_text(290, 110, text="3", fill="white", font="Arial 20")
    canvas.create_text(110, 190, text="4", fill="white", font="Arial 20")
    canvas.create_text(200, 190, text="5", fill="white", font="Arial 20")
    canvas.create_text(290, 190, text="6", fill="white", font="Arial 20")
    canvas.create_text(110, 270, text="7", fill="white", font="Arial 20")
    canvas.create_text(200, 270, text="8", fill="white", font="Arial 20")
    canvas.create_text(290, 270, text="9", fill="white", font="Arial 20")
    
#Login Form which is launched at start
class LoginFrame(Frame):
    def __init__(self, master):
        #Python will immediately call its __init__ method before it gives the new object back to whoever made it.
        super().__init__(master)

        #Labels and positions on the login form for Name and Age and display Titles
        self.label_1 = Label(self, text="Name", bg="turquoise", fg="white", padx=9)
        self.label_2 = Label(self, text="Age ", bg="turquoise", fg="white", padx=13)
        self.info = Label(self, text="Math Game 4.0", bg="turquoise", fg="white", padx=50, pady=5, font="Arial 10")
        self.info2 = Label(self, text="2-6 Years", bg="salmon", fg="white", padx=70, font="Arial 8")
        self.entry_1 = Entry(self, bg="salmon", fg="white")
        self.entry_2 = Entry(self, bg="salmon", fg="white")

        #Position fixing on login form for labels and entry input
        self.label_1.grid(row=2, sticky=E)
        self.label_2.grid(row=3, sticky=E)
        self.info.grid(row=0, columnspan=2, sticky=E)
        self.info2.grid(row=1, columnspan=2, sticky=E)
        self.entry_1.grid(row=2, column=1, pady=2, padx=3)
        self.entry_2.grid(row=3, column=1, pady=2, padx=3)

        #Login Buttons and packing Login window
        self.loginbutton = Button(self, text="Login",bg="turquoise", fg="white", command=self.loginbutton_clicked)
        self.loginbutton.grid(columnspan=2, sticky=E, padx=6, pady=2)
        root.title("")
        self.pack()
    
    #Exceptions to when login button is clicked on
    def loginbutton_clicked(self):
        global age
        
        #Print if clicked on
        name = self.entry_1.get()
        age = self.entry_2.get()
        count = 0

        #Print name and age and the exceptions 
        if name == "" or age == "" or  str(1) >= age or str(7) <= age or name.isdigit() or age.isalpha(): 
            tm.showinfo("!Error!", "Input correct Name and/or Age!")

        ## If age in between 2 to 3 then display message for level 1 and run main
        if name.isalpha() and age.isdigit() and str(2) <= age <= str(3):
            tm.showinfo("Note", "[Level 1]: Hello {}!".format(name))
            root.destroy()
            main() 

        ## If age in between 4 to 5 then display message for level 2 and run main
        if name.isalpha() and age.isdigit() and str(4) <= age <= str(5):
            tm.showinfo("Note", "[Level 2]: Hello {}!".format(name))
            root.destroy()
            main()

        ## If age input is 6 then display message for level 3 and run main
        if name.isalpha() and age.isdigit() and str(6) == age:
            tm.showinfo("Note", "[Level 3]: Hello {}!".format(name))
            root.destroy()
            main()

        #Counting towards starting game if exceptions have been met (loading up to 99% to run)
        while (count < 100) and name.isalpha() and age.isdigit() and(str(6) == age or str(4) <= age <= str(5) or str(2) <= age <= str(3)):
            print (count, '%')
            print ("Loading..")
            count = count + 1
            

#Baseline of running root tkinter GUI (login)
root = Tk()
lf = LoginFrame(root)
root.mainloop()
