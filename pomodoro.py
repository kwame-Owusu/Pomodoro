import customtkinter as ctk
from tkinter import *
from PIL import Image
import random
import math
import pygame
from settings import *

# to make it pypass on systems that do not support thes libraries
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass



# window setup
pomodoro = ctk.CTk()
pygame.mixer.init()
pomodoro.iconbitmap("imgs/window-icon.ico")
pomodoro.resizable(False, False)
pomodoro.title("")
pomodoro.config(padx=180,pady=150, bg=colors["dark"])
pomodoro.attributes("-alpha", 0.90)



# this access the titlebar and changes it into the background color.
try:

    HWND = windll.user32.GetParent(pomodoro.winfo_id())
    title_bar_color = 0x2D2D2D
    windll.dwmapi.DwmSetWindowAttribute(HWND,35, byref(c_int(title_bar_color)), sizeof(c_int))

except:
    pass

# timer variables
reps = 0
timer = None





circle_img = PhotoImage(file="imgs/circle.png")

# create circle image in the middle of window
canvas = Canvas(width=300, height=300, bg=colors["dark"], highlightthickness=0)
canvas.create_image(150, 150, image=circle_img)
timer_text = canvas.create_text(150, 150, text="00:00", fill=WHITE, font=(FONT, SMALL_FONT_SIZE,))
canvas.grid(column=2, row=1)

#labels
timer_label = ctk.CTkLabel(pomodoro,text="Timer", font=(FONT, BIG_FONT_SIZE), text_color=WHITE, bg_color=colors["dark"])
timer_label.grid(column=2, row=0)

playlist_label = ctk.CTkLabel(pomodoro,text="Playlists", font=(FONT, 30), text_color=WHITE, bg_color=colors["dark"])
playlist_label.configure(pady=STYLING["gap"])
playlist_label.grid(column=2, row=3,)


checkmark_label = ctk.CTkLabel(pomodoro,text="", font=(FONT, 19,), text_color=WHITE, bg_color=colors["dark"])
checkmark_label.grid(column=2, row=2,)



break_music = ("music/break_time.mp3")
playlists = ["music/jazz.mp3", "music/lofi-3.mp3", "music/lofi.mp3",
             "music/light rain.mp3", "music/river.mp3", "music/lofi-2.mp3"]
current_list = []
# commands for the buttons
def Play():

    global current_list
    if not current_list:
        current_list = playlists[:]
        random.choice(current_list)

    def update_playlist_label():
        nonlocal song  # Use nonlocal keyword to access song from the outer function
        modified_playlists = [playlist.replace("music/", "").replace(".mp3", "") for playlist in playlists]
        current_song_index = playlists.index(song)
        modified_current_song = modified_playlists[current_song_index]
        playlist_label.configure(pomodoro, text=f"{modified_current_song} is playing")
    
   
    song = current_list[0]
    current_list.pop(0)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    pomodoro.after(1000, update_playlist_label)

def Pause():
    pygame.mixer.music.pause()

def Resume():
    pygame.mixer.music.unpause()



def reset_timer():
    start_button.configure(state="normal")
    pomodoro.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.configure(text="Timer")
    checkmark_label.configure(text="")
    playlist_label.configure(pomodoro, text="Playlists")
    global reps
    reps = 0


def start_timer():
   "start the timer countdown based on timer settings"
   global reps
   reps += 1
   work_sec = work_min * 60
   short_break_sec = short_break_min * 60
   long_break_sec = long_break_min * 60
   start_button.configure(state="disabled")

   if reps % 8 == 0:
       countdown(long_break_sec)
       timer_label.configure(text="Long Break", text_color=WHITE)
       pygame.mixer.music.load(break_music)
       pygame.mixer.music.play()
       pygame.mixer.music.set_volume(0.35)
       
   
   elif reps % 2 == 0:
       countdown(short_break_sec)
       timer_label.configure(text="Short Break", text_color=WHITE)
       pygame.mixer.music.load(break_music)
       pygame.mixer.music.play()
       pygame.mixer.music.set_volume(0.35)
   
   else:
       countdown(work_sec)
       timer_label.configure(text="Work", text_color=WHITE)



def countdown(count):
    # for couting the min, use math.floor to round down instead of up
    count_min = math.floor(count / 60)
    #give the remainder, which becomes the seconds.
    count_sec = count % 60
    #for the 0 to appear in front of number when it hits single digits and in the beginning
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global timer
        timer = pomodoro.after(100, countdown, count - 1)
       
    
    else:
        start_timer()
        #everytime a work session is done, a circle will appear to mark completion of 1 session.
        marks = ""
        
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks +=  "⚪"
        checkmark_label.configure(text=marks,)

       
    

def slider_volume(value):
    pygame.mixer.music.set_volume(playlist_slider.get())


 
# button images
start_img = ctk.CTkImage(light_image=Image.open("imgs/start.png"), dark_image=Image.open("imgs/start.png"), size=(30,30))
reset_img = ctk.CTkImage(light_image=Image.open("imgs/reset.png"), dark_image=Image.open("imgs/reset.png"), size=(30,30))

play_img = ctk.CTkImage(light_image=Image.open("imgs/next.png"), dark_image=Image.open("imgs/next.png"), size=(30,30))
pause_img = ctk.CTkImage(light_image=Image.open("imgs/pause.png"), dark_image=Image.open("imgs/pause.png"), size=(30,30))
resume_img = ctk.CTkImage(light_image=Image.open("imgs/play.png"), dark_image=Image.open("imgs/play.png"), size=(30,30))
theme_img = ctk.CTkImage(light_image=Image.open("imgs/change-theme.png"), dark_image=Image.open("imgs/change-theme.png"), size=(30,30))





# buttons
start_button = ctk.CTkButton(pomodoro, text="", command=None, font=(
    FONT, SMALL_FONT_SIZE), bg_color=colors["dark"], fg_color=colors["dark"], image=start_img)
start_button.configure(
    width=60, height=35, hover_color=colors["hover"], command=start_timer)
start_button.grid(column=1, row=2, pady=20)

reset_button = ctk.CTkButton(pomodoro, text="", command=None, font=(
    FONT, SMALL_FONT_SIZE), bg_color=colors["dark"], fg_color=colors["dark"], image=reset_img)
reset_button.configure(
    width=60, height=35, hover_color=colors["hover"], command=reset_timer)
reset_button.grid(column=3, row=2,pady=20)


themes = [
    {"dark": "#2D3250", "hover": "#7077A1"},
    {"dark": "#164863", "hover": "#427D9D"},
    {"dark": "#5C5470", "hover": "#B9B4C7"},
    {"dark": "#2C3639", "hover": "#3F4E4F"},
    {"dark": "#944E63", "hover": "#B47B84"},
    {"dark": "#643843", "hover": "#99627A"},
]


def change_theme():
    """Function to update UI elements with random theme colors"""
    
    # Select a random theme
    random_theme = random.choice(themes)
    
    # Update the colors dictionary
    colors = {
        "dark": random_theme["dark"],
        "hover": random_theme["hover"]
    }
    
    # Update UI elements with theme colors
    pomodoro.config(bg=colors["dark"])
    playlist_slider.configure(bg_color=colors["dark"], button_hover_color=colors["hover"])
    start_button.configure(bg_color=colors["dark"], fg_color=colors["dark"], hover_color=colors["hover"])
    reset_button.configure(bg_color=colors["dark"], fg_color=colors["dark"], hover_color=colors["hover"])
    play_button.configure(bg_color=colors["dark"], fg_color=colors["dark"], hover_color=colors["hover"])
    pause_button.configure(bg_color=colors["dark"], fg_color=colors["dark"], hover_color=colors["hover"])
    resume_button.configure(bg_color=colors["dark"], fg_color=colors["dark"], hover_color=colors["hover"])
    theme_button.configure(bg_color=colors["dark"], fg_color=colors["dark"], hover_color=colors["hover"])
    playlist_label.configure(bg_color=colors["dark"], fg_color=colors["dark"])
    timer_label.configure(bg_color=colors["dark"], fg_color=colors["dark"])
    checkmark_label.configure(bg_color=colors["dark"])
    canvas.configure(bg=colors["dark"], highlightthickness=0)



#playlists buttons
play_button = ctk.CTkButton(pomodoro, text="", command=None, font=(
    FONT, SMALL_FONT_SIZE), bg_color=colors["dark"], fg_color=colors["dark"], image=play_img)
play_button.configure(width=80, height=35,
                      hover_color=colors["hover"], command=Play)
play_button.grid(column=1, row=4)


pause_button = ctk.CTkButton(pomodoro, text="", command=None, font=(
    FONT, SMALL_FONT_SIZE), bg_color=colors["dark"], fg_color=colors["dark"], image=pause_img)
pause_button.configure(width=60, height=35,
                       hover_color=colors["hover"], command=Pause)
pause_button.grid(column=2, row=4,pady=20)


resume_button = ctk.CTkButton(pomodoro,  text="", command=None, font=(
    FONT, SMALL_FONT_SIZE), bg_color=colors["dark"], fg_color=colors["dark"], image=resume_img)
resume_button.configure(width=60, height=35,
                        hover_color=colors["hover"], command=Resume)
resume_button.grid(column=3, row=4)


# music slider to control the volume of the music
playlist_slider = ctk.CTkSlider(pomodoro, from_=0, to=2, number_of_steps=50, width=350, command=slider_volume,
bg_color=colors["dark"], fg_color=WHITE, button_color=WHITE, button_hover_color=colors["hover"])
playlist_slider.grid(column=2, row=5,)

theme_button = ctk.CTkButton(pomodoro, text="", command=None, font=(
    FONT, SMALL_FONT_SIZE), bg_color=colors["dark"], fg_color=colors["dark"], hover_color=colors["hover"] , image=theme_img)
theme_button.configure(command=change_theme)
theme_button.grid(column=3, row=0)




if __name__ == "__main__":
   pomodoro.mainloop()
   
    
