import customtkinter
from tkinter import *
import pygame
import random
import math


app = customtkinter.CTk()
pygame.mixer.init() 


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F4BFBF"
RED = "#E97777"
GREEN = "#C7E9B0"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# 45 mins because i like to work a little longer with pomodoro
WORK_MIN = 45
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    app.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label["text"] = "Timer"
    checkmark_label["text"] = ""
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

break_music = ("break_time.mp3")
def start_timer():
    global reps
    reps += 1  
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60




# red for long break and yellow for a short break
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        pygame.mixer.music.load(break_music)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.09)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=YELLOW)
        pygame.mixer.music.load(break_music)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.09)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=PINK)

# ---------------------------- STUDY MUSIC------------------------------- #



PLAYLISTS= ["playlist_1.mp3", "playlist_2.mp3", "playlist_3.mp3", "playlist_4.mp3" , "playlist_5.mp3"]
current_list = []

# using pygame mixer because all other libraries were not working, although i do no know the reason

def Play():
    global current_list
    if not current_list:
        current_list = PLAYLISTS[:]
        random.shuffle(current_list)

    
    song = current_list[0]
    current_list.pop(0)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.04)

    

    
def Pause():
    pygame.mixer.music.pause()

def Resume():
    pygame.mixer.music.unpause()



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
#    for couting the min, use math.floor to round down instead of up
    count_min = math.floor(count / 60)
#    give the remainder, which becomes the seconds.
    count_sec = count % 60
#    for the 0 to appear in front of number when it hits single digits and in the beginning
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global timer
        timer = app.after(1000, countdown, count - 1)
    
    else:
        start_timer()
#   everytime a work session is done, a checkmark will appear
        marks = ""
        
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)

          




# ---------------------------- UI SETUP ------------------------------- #
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


        #  configure window
app.title("Pomodoro")
app.config(padx=200, pady=224, bg=GREEN,)
        
        # pomodoro image
pomodoro_img = PhotoImage(file="tomato_2.png")
        # canvas
canvas = Canvas(width=200, height=223, bg=GREEN, highlightthickness=0,)
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 160, text="00:00", fill="white", font=(FONT_NAME, 20, "bold") )
canvas.grid(column=2, row=1)

#checkmark for completion of 1 work session
checkmark_label = Label(fg=PINK,bg=GREEN)
checkmark_label.configure(font=(FONT_NAME, 10, "bold"), )
checkmark_label.grid(column=2, row=3)

timer_label = Label()
timer_label.config(text="Timer", font=("small fonts", 45, "bold"), fg=PINK, bg=GREEN, highlightthickness=0)
timer_label.grid(column=2, row=0)


start_button = customtkinter.CTkButton(app,text="start",hover=True,command=start_timer,font=("small fonts", 16, "bold",), bg_color=GREEN, fg_color=PINK,)
start_button.configure(width=50, height=30,hover_color=(YELLOW), command=start_timer)
start_button.grid(column=1, row=3)


reset_button = customtkinter.CTkButton(app,text="reset",hover=True,command=start_timer,font=("small fonts", 16, "bold",), bg_color=GREEN, fg_color=PINK,)
reset_button.configure(width=50, height=30,hover_color=(YELLOW),command=reset_timer )
reset_button.grid(column=3, row=3)

# music label
playlist_label = Label()
playlist_label.config(text="Study Music", font=("small fonts", 20, "bold"), fg=PINK, bg=GREEN, highlightthickness=0, pady=20)
playlist_label.grid(column=2, row=4)

# music buttons
music_button = customtkinter.CTkButton(app,text="Play playlist",hover=True,font=("small fonts", 16, "bold",), bg_color=GREEN, fg_color=PINK,)
music_button.configure(width=30, height=30,hover_color=(YELLOW),command=Play)
music_button.grid(column=1, row=5)

music_button = customtkinter.CTkButton(app,text="Pause",hover=True,font=("small fonts", 16, "bold",), bg_color=GREEN, fg_color=PINK,)
music_button.configure(width=30, height=30,hover_color=(YELLOW),command=Pause)
music_button.grid(column=2, row=5)

pause_button = customtkinter.CTkButton(app,text="Resume",hover=True,font=("small fonts", 16, "bold",), bg_color=GREEN, fg_color=PINK,)
pause_button.configure(width=30, height=30,hover_color=(YELLOW),command=Resume)
pause_button.grid(column=3, row=5)





app.mainloop()