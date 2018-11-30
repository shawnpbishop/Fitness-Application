#This program is written by Shawn Bishop

from random import randint
from datetime import datetime
from tkinter import *

class ExerciseApplication:
    def __init__(self):
        window = Tk()
        window.title("The Key To Gains Workout Tracker")

        self.canvas = Canvas(window, width = 500, height = 500, bg = "green")
        self.canvas.pack()
        self.canvas.create_text(250,50, text = "Welcome to The Key to Gains Workout Tracker!",
                                font = "Times 10 bold underline", tags = "welcome")
        keyImage = PhotoImage(file = "key.gif")
        self.canvas.create_image(250,200, image = keyImage, tags = "key")
        self.canvas.create_text(250,400, text = "If this is your first time, click File, First Workout.", tags = "welcome")
        self.canvas.create_text(250,450, text = "Otherwise, click File, Functional Workout or Strength Training.", tags = "welcome")
        self.frame = Frame(window)
        self.frame.pack()
        menubar = Menu(window)
        window.config(menu = menubar)
        fileMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu = fileMenu)
        fileMenu.add_command(label = "First Workout",
                             command = self.displayFirstWorkout)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Functional Workout",
                             command = self.functional)
        fileMenu.add_command(label = "Strength Training",
                             command = self.strength)

        viewMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "View Results", menu = viewMenu)
        viewMenu.add_command(label = "Strength Tracker",
                             command = self.total)


        window.mainloop()

    def displayFirstWorkout(self):
        self.canvas.delete("welcome", "new", "exercise", "strength", "functional", "first", "complete", "total", "key", "quit")
        self.canvas.create_text(250, 200, text = "If you are a new user, right click to open a new workout file.", tags = "new")
        self.canvas.create_text(250, 250, text = "Warning!", tags = "new")
        self.canvas.create_text(250, 300, text = "It will erase any previous workout files.", tags = "new")
        self.canvas.bind("<Button-3>", self.firstWorkout)

        
    def firstWorkout(self, event):
        import tkinter.simpledialog
        
        self.canvas.delete("welcome", "new", "exercise", "strength", "functional", "first", "complete", "total", "key", "quit")
        outfile = open("myWorkout.txt", "w")
        name = tkinter.simpledialog.askstring(
                "Name", "Enter Name:")
        outfile.write(name)
        outfile.write("\n")
        date = datetime.now()
        outfile.write(str(date.month))
        outfile.write("/")
        outfile.write(str(date.day))
        outfile.write("/")
        outfile.write(str(date.year))
        outfile.write("\n")
        outfile.write("Starting weight is ")
        weight = tkinter.simpledialog.askinteger(
                "Weight", "Enter Current Weight:")
        outfile.write(str(weight))
        outfile.write("\n")
        outfile.write("\n")
        outfile.close()
        self.canvas.create_text(250, 250, text = "Workout file is created.", tags = "first")
        self.canvas.create_text(250, 300, text = "Choose either Functional Workout or Strength Training in File Menu.", tags = "first")

    def functional(self):
        global count 
        count = 0 
        self.canvas.delete("welcome", "new", "exercise", "strength", "complete", "first", "total", "key", "quit")
        self.canvas.create_text(250, 200, text = "This functional workout is designed with random bodyweight exercises.", tags = "functional")
        self.canvas.create_text(250, 250, text = "The goal is to limit rest periods after exercises to under 60 seconds.", tags = "functional")
        self.canvas.create_text(250, 300, text = "A beginner should attempt to do 8-12 exercises.", tags = "functional")
        self.canvas.create_text(250, 350, text = "Click the Exercise button to begin.", tags = "functional")
        self.btExercise = Button(self.frame, text = "Exercise",
                                     command = self.displayExercise)
        self.btExercise.pack(side = LEFT)
        self.btComplete = Button(self.frame, text = "Complete Workout",
                                 command = self.complete)
        self.btComplete.pack(side = LEFT)

    def complete(self):
        self.canvas.delete("welcome", "new", "exercise", "strength", "functional", "first", "total", "key", "quit")
        self.canvas.create_text(250, 150, text = "Great job!", font = "Times 16 bold", tags = "complete")
        self.canvas.create_text(250, 200, text = "Exercises completed:", tags = "complete")
        self.canvas.create_text(250, 250, text = str(count), font = "Times 10 bold underline", tags = "complete")
        repsCompleted = count * 20
        self.canvas.create_text(250, 300, text = "Repetitions completed:", tags = "complete")
        self.canvas.create_text(250, 350, text = str(repsCompleted), font = "Times 10 bold underline", tags = "complete")
        

    def displayExercise(self):
        self.deck = ["Lunges", "Squats", "Calf Raises", "Reverse Lunges",
                     "Pushups", "Crunches", "Slow Bicycles",
                     "Leg Raises", "Russian Twists", "Jumping Jacks"]

        lunge1 = PhotoImage(file = "lunge1.gif")
        lunge2 = PhotoImage(file = "lunge2.gif")
        squat1 = PhotoImage(file = "squat1.gif")
        squat2 = PhotoImage(file = "squat2.gif")
        calfraise1 = PhotoImage(file = "calfraise1.gif")
        calfraise2 = PhotoImage(file = "calfraise2.gif")
        reverselunge1 = PhotoImage(file = "reverselunge1.gif")
        reverselunge2 = PhotoImage(file = "reverselunge2.gif")
        pushup1 = PhotoImage(file = "pushup1.gif")
        pushup2 = PhotoImage(file = "pushup2.gif")
        crunch1 = PhotoImage(file = "crunch1.gif")
        crunch2 = PhotoImage(file = "crunch2.gif")
        slowbicycle1 = PhotoImage(file = "slowbicycle1.gif")
        slowbicycle2 = PhotoImage(file = "slowbicycle2.gif")
        legraise1 = PhotoImage(file = "legraise1.gif")
        legraise2 = PhotoImage(file = "legraise2.gif")
        russiantwist1 = PhotoImage(file = "russiantwist1.gif")
        russiantwist2 = PhotoImage(file = "russiantwist2.gif")
        jumpingjack1 = PhotoImage(file = "jumpingjack1.gif")
        jumpingjack2 = PhotoImage(file = "jumpingjack2.gif")

        self.pic1 = [lunge1, squat1, calfraise1, reverselunge1,
                     pushup1, crunch1, slowbicycle1,
                     legraise1, russiantwist1, jumpingjack1]
        self.pic2 = [lunge2, squat2, calfraise2, reverselunge2,
                     pushup2, crunch2, slowbicycle2,
                     legraise2, russiantwist2, jumpingjack2]
        
        
        
        self.canvas.delete("welcome", "exercise", "functional", "today", "new", "strength", "complete", "key")
        NUMBER_OF_EXERCISES = 10
        x = randint(0, NUMBER_OF_EXERCISES-1)
        global count
        
        count += 1 
        self.canvas.create_text(250, 75, text = "20 Reps of:",
                                font = "Times 10 bold", tags = "exercise")
        self.canvas.create_text(250, 150, text = self.deck[x],
                                font = "Times 10 bold underline", tags = "exercise")
        self.canvas.create_image(125,300, image = self.pic1[x], tags = "exercise")
        self.canvas.create_image(350,300, image = self.pic2[x], tags = "exercise")
        self.canvas.create_text(250, 400, text = "Click Exercise button for next exercise.", tags = "exercise")
        self.canvas.create_text(250, 450, text = "Click Complete Workout button when done with workout.", tags = "exercise")


    def total(self):
        self.canvas.delete("welcome", "functional", "new", "exercise", "complete", "first", "strength", "key", "quit")
        infile = open("myWorkout.txt", "r")       
        scrollbar = Scrollbar(self.canvas)
        scrollbar.pack(side = RIGHT, fill = Y)
        self.text = Text(self.canvas, width = 50, height = 22, bg = "green", wrap = WORD,
                    yscrollcommand = scrollbar.set)
        scrollbar.config(command = self.text.yview)
        self.text.insert(END, infile.read())
        self.text.pack()
        
        infile.close()
    
    def strength(self):
        import tkinter.simpledialog

        outfile = open("myWorkout.txt", "a")
        
        date = datetime.now()
        outfile.write("\n")
        outfile.write(str(date.month))
        outfile.write("/")
        outfile.write(str(date.day))
        outfile.write("/")
        outfile.write(str(date.year))
        outfile.write("\n")
        outfile.write("Strength Workout\n")
        outfile.write("\n")      
        
        self.canvas.delete("welcome", "functional", "new", "exercise", "complete", "first", "total", "key", "quit")
        
        exercise = " "
        while exercise != "done":
            
            exercise = tkinter.simpledialog.askstring(
                "Exercise", "Enter Exercise: (Enter done to complete workout)")
            if exercise != "done":
                outfile.write("Exercise: ")
                outfile.write(exercise)
                outfile.write(" / ")
                
            reps = tkinter.simpledialog.askstring(
                "Reps", "Enter Repetitions: (Enter 0 if complete)")
            if reps != "0":
                outfile.write(" Repetitions: ")
                outfile.write(reps)
                outfile.write(" / ")
            weight = tkinter.simpledialog.askstring(
                "Weight", "Enter Weight: (Enter 0 if complete)")
            if weight != "0":
                outfile.write(" Weight: ")
                outfile.write(weight)
                outfile.write(" pounds\n")

        outfile.close()
        self.canvas.create_text(250, 200, text = "Great job!", tags = "strength")
        self.canvas.create_text(250, 300, text = "Click on Strength Tracker in View Menu to see results.", tags = "strength")
        
        
        

ExerciseApplication()
