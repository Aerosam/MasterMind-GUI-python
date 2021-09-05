
import tkinter as tk
from tkinter.messagebox import *
import random
import collections


class Mastermind:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(parent)
        self.entry = tk.Entry(parent)
        self.draw_board() 
        
    def draw_board(self, event=None): 
        self.parent.title("Mastermind")
        self.parent.geometry("275x765")
        self.parent.configure(bg="light blue")
        self.parent.resizable(height=False, width=False)
        self.canvas = tk.Canvas(self.parent, width=275, height=715, bg="light blue", highlightthickness=0)
                                
        
        self.canvas.pack()
        for a in range(15): 
            self.canvas.create_line(10, 40+a*50, 250, 40+a*50, fill="gray")
                                    
        for a in range(4): 
            self.canvas.create_oval(15+a*50, 8, 40+a*50, 33, fill="black")
                                    
        for a in range(13): 
            for b in range(4):
                self.canvas.create_oval(15+b*50, 58+a*50,40+b*50, 83+a*50, outline="gray", fill="gray")
                                        
                                        
            for c in range(2): 
                for d in range(2): 
                    self.canvas.create_oval(215+c*20, 58+a*50+d*14, 226+c*20, 69+a*50+d*14, outline="gray",fill="gray")


        self.entry = tk.Entry(self.parent,font=("Arial 20 bold"), justify="center", width=7, bg="#1E6FBA", fg="black")
        self.entry.focus()
        self.entry.pack()
        self.entry.bind("<Return>", self.check) 
        self.colors = ["r", "g", "b", "y", "c", "m"] 
        self.color_dic = {'r':'red', 'g':'green', 'b':'blue', 'y':'yellow', 'c':'cyan', 'm':'magenta'}
        self.guesses = [''] 

        while True:  
            self.passcode = [random.choice(self.colors) for _ in range(4)]
            freq = []
            check = list(set(self.passcode))
            for x in check:
                freq.append(self.passcode.count(x))
            if (freq[0]>2 or freq[1]>2):
                continue
            else:
                print(self.passcode) 
                break                
        self.counted = collections.Counter(self.passcode)
        
    def check(self, event=None): 
        exact_match = 0 
        partial_match = 0 
        guess = str(self.entry.get())
        self.guesses[-1] += guess
        if len(guess) != 4:  
            showwarning("Mastermind", "Only 4 characters allowed!")
            self.entry.delete(0, 'end') 
            return
        guess_count = collections.Counter(guess)
        for x in guess: 
            if x not in self.colors:
                showwarning("Mastermind", "Only letters (r)ed, (g)reen, (b)lue, (m)agenta, (c)yan, (y)ellow allowed.")
                self.entry.delete(0, 'end') 
                return
        

                
        partial_match = sum(min(self.counted[k], guess_count[k]) for k in self.counted)
        exact_match = sum(a == b for a, b in zip(self.passcode, guess))
        partial_match -= exact_match



        
        print("> b : ",exact_match,"w : ",partial_match) 
        offset = len(self.guesses)* 50 
        for a in range(4): 
            self.canvas.create_oval(15+a*50, 8+offset, 40+a*50, 33+offset, outline=self.color_dic[guess[a]], fill=self.color_dic[guess[a]])


        feedback = exact_match*["black"] + partial_match*["white"]
        fb_coordinates = [(215,7.5+offset,226,18.5+offset), (215,21.5+offset,226,32.5+offset), (235,7.5+offset,246,18.5+offset), (235,21.5+offset,246,32.5+offset)]

        for color, coord in zip(feedback, fb_coordinates): 
            self.canvas.create_oval(coord, outline=color, fill=color)
        if len(self.guesses) > 12: 
            for r in range(4):
                self.canvas.create_oval(15+r*50, 8, 40+r*50, 33, outline=self.color_dic[self.passcode[r]], fill=self.color_dic[self.passcode[r]])

            showinfo("Mastermind", "Game Over.\nPasscode is : {}" .format(self.passcode))
            self.entry.unbind("<Return>")
        elif exact_match == 4: 
            for a in range(4):
                self.canvas.create_oval(15+a*50, 8, 40+a*50, 33, outline=self.color_dic[self.passcode[a]], fill=self.color_dic[self.passcode[a]])
            showinfo("Mastermind", "You Win")
            self.entry.unbind("<Return>")
        else:
            self.guesses.append('') 
            self.entry.delete(0, 'end') 

            
root = tk.Tk()
game = Mastermind(root)
root.mainloop()
