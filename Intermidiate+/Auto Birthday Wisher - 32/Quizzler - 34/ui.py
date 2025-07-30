from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        
        # Create a Frame to hold the canvas and center it
        frame = Frame(self.window, bg= THEME_COLOR)
        frame.pack(expand=True)

        # Scoreboard
        self.score = 0
        self.scoreboard = Label(frame, text = f"Score: {self.score}", bg = THEME_COLOR, fg = "white", font = ("Ariel", 15, "italic"))
        self.scoreboard.grid(row = 0, column = 1, padx = (20,0), pady = 20)

        # Load the canvas
        self.canvas = Canvas(frame, width=300, height=250, highlightthickness=0, bg= "white")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.q_text = self.canvas.create_text(
            150,
            125,
            text = "What color is your Buggati?",
            fill = "black", font = ("Ariel", 20, "italic"),
            width = 280)

        # Create a Frame to hold the buttons and center it horizontally
        button_frame = Frame(self.window, bg=THEME_COLOR)
        button_frame.pack()

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(button_frame, image=true_image, highlightthickness=0, command= self.true_pressed)
        self.true_button.pack(side="left", padx=(50, 20), pady = 20)  # Add left padding to move it near the middle

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(button_frame, image=false_image, highlightthickness=0, command= self.false_pressed)
        self.false_button.pack(side="right", padx=(20, 50), pady = 20)  # Add right padding to move it near the middle
        
        self.get_next_question()
        
        self.window.mainloop() 
    
    def get_next_question(self):
        if (self.quiz.still_has_questions()):
            self.canvas.config(bg = "white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text = q_text)
        else :
            self.canvas.config(bg = "yellow")
            self.canvas.itemconfig(self.q_text, text = "You have reached the end of the questions.")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")
        
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if (is_right):
            self.canvas.config(bg = "green")
            self.score += 1
            self.scoreboard.config(text = f"Score: {self.score}")
        else :
            self.canvas.config(bg = "red")
            
        self.window.after(1000, self.get_next_question)