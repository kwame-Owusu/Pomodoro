import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import random
import math
import pygame
from settings import *





# window setup
pomodoro = ctk.CTk()
pygame.mixer.init()
pomodoro.iconbitmap("imgs/tomato_icon.ico")
pomodoro.resizable(False, False)
pomodoro.title("")
pomodoro.config(padx=200, pady=224, bg=COLORS["green"])

# timer variables
reps = 0
timer = None






pomodoro_img = PhotoImage(file="imgs/tomato.png")

# create pomodoro img in the middle of window
canvas = Canvas(width=200, height=224, bg=COLORS["green"], highlightthickness=0)
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 170, text="00:00", fill=WHITE, font=(FONT, SMALL_FONT_SIZE,))
canvas.grid(column=2, row=1)

# UI setup

# labels
timer_label = ctk.CTkLabel(pomodoro,text="Timer", font=(FONT, BIG_FONT_SIZE), text_color=COLORS["pink"]["fg"], bg_color=COLORS["green"])
timer_label.grid(column=2, row=0)

playlist_label = ctk.CTkLabel(pomodoro,text="Study  Playlists", font=(FONT, 40), text_color=COLORS["pink"]["fg"], bg_color=COLORS["green"])
playlist_label.configure(pady=STYLING["gap"])
playlist_label.grid(column=2, row=3)

checkmark_label = ctk.CTkLabel(pomodoro,text="", font=(FONT, 19,), text_color=COLORS["pink"]["fg"], bg_color=COLORS["green"])
checkmark_label.grid(column=2, row=2,)

# ------- commands--- #



PLAYLISTS= ["music/playlist_1.mp3", "music/playlist_2.mp3", "music/playlist_3.mp3", "music/playlist_4.mp3" , "music/playlist_5.mp3", "music/playlist_6.mp3"]
current_list = []


# commands for the buttons

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







def reset_timer():
    pomodoro.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.configure(text="Timer")
    checkmark_label.configure(text="")
    global reps
    reps = 0



break_music = "music/break_time.mp3"
def start_timer():
   global reps
   reps += 1
   work_sec = WORK_MIN * 60
   short_break_sec = SHORT_BREAK_MIN * 60
   long_break_sec = LONG_BREAK_MIN * 60

   if reps % 8 == 0:
       countdown(long_break_sec)
       timer_label.configure(text="Long Break", text_color=COLORS["red"])
       pygame.mixer.music.load(break_music)
       pygame.mixer.music.play()
       pygame.mixer.music.set_volume(0.09)
   
   elif reps % 2 == 0:
       countdown(short_break_sec)
       timer_label.configure(text="Short Break", text_color=COLORS["yellow"])
       pygame.mixer.music.load(break_music)
       pygame.mixer.music.play()
       pygame.mixer.music.set_volume(0.09)
   
   else:
       countdown(work_sec)
       timer_label.configure(text="Work", text_color=COLORS["pink"]["fg"])

   
    
   



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
        timer = pomodoro.after(1000, countdown, count - 1)
    
    else:
        start_timer()
#   everytime a work session is done, a checkmark will appear
        marks = ""
        
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.configure(text=marks)
    

    









# button images
play_img = ctk.CTkImage(light_image=Image.open("imgs/play_img.png"), dark_image=Image.open("imgs/play_img.png"), size=(30,30))
pause_img = ctk.CTkImage(light_image=Image.open("imgs/pause_img.png"), dark_image=Image.open("imgs/pause_img.png"), size=(30,30))
resume_img = ctk.CTkImage(light_image=Image.open("imgs/resume_img.png"), dark_image=Image.open("imgs/resume_img.png"), size=(27,27))

start_img = ctk.CTkImage(light_image=Image.open("imgs/start_img.png"), dark_image=Image.open("imgs/start_img.png"), size=(50,50))
reset_img = ctk.CTkImage(light_image=Image.open("imgs/reset_img.png"), dark_image=Image.open("imgs/reset_img.png"), size=(50,50))




# buttons

start_button = ctk.CTkButton(pomodoro, text="", command=None, font=(FONT, SMALL_FONT_SIZE), bg_color=COLORS["green"], fg_color=COLORS["green"], image=start_img)
start_button.configure(width=60, height=35, hover_color=COLORS["pink"]["hover"], command=start_timer)
start_button.grid(column=1, row=2)

reset_button = ctk.CTkButton(pomodoro, text="", command=None, font=(FONT, SMALL_FONT_SIZE), bg_color=COLORS["green"], fg_color=COLORS['green'], image=reset_img)
reset_button.configure(width=60, height=35, hover_color=COLORS["pink"]["hover"], command=reset_timer)
reset_button.grid(column=3, row=2)


# button images
play_img = ctk.CTkImage(light_image=Image.open("imgs/play_img.png"), dark_image=Image.open("imgs/play_img.png"), size=(30,30))
pause_img = ctk.CTkImage(light_image=Image.open("imgs/pause_img.png"), dark_image=Image.open("imgs/pause_img.png"), size=(30,30))
resume_img = ctk.CTkImage(light_image=Image.open("imgs/resume_img.png"), dark_image=Image.open("imgs/resume_img.png"), size=(27,27))






# playlists buttons
play_button = ctk.CTkButton(pomodoro, text="", command=None, font=(FONT, SMALL_FONT_SIZE), bg_color=COLORS["green"], fg_color=COLORS["green"], image=play_img)
play_button.configure(width=80, height=35, hover_color=COLORS["pink"]["hover"], command=Play)
play_button.grid(column=1, row=4)


pause_button = ctk.CTkButton(pomodoro, text="", command=None, font=(FONT, SMALL_FONT_SIZE), bg_color=COLORS["green"], fg_color=COLORS["green"], image=pause_img)
pause_button.configure(width=60, height=35, hover_color=COLORS["pink"]["hover"], command=Pause)
pause_button.grid(column=2, row=4)



resume_button = ctk.CTkButton(pomodoro,  text="",command=None, font=(FONT, SMALL_FONT_SIZE), bg_color=COLORS["green"], fg_color=COLORS["green"],image= resume_img )
resume_button.configure(width=60, height=35, hover_color=COLORS["pink"]["hover"], command=Resume)
resume_button.grid(column=3, row=4)










if __name__ == "__main__":
   pomodoro = pomodoro
   pomodoro.mainloop()
    