from tkinter import Toplevel,Label
# colors
WHITE = "#EEEEEE"
colors = {
    "dark":"#2C3639",
    "hover": "#3F4E4F",
}


FONT = "JetBrains Mono"
BIG_FONT_SIZE = 50
SMALL_FONT_SIZE = 20


STYLING = {
    "gap": 15,
    "corner-radius" : 5
} 

PLAYLISTS = ["music/playlist_1.mp3", "music/playlist_2.mp3","music/playlist_3.mp3", "music/playlist_4.mp3", "music/playlist_5.mp3"]



# timer settings
work_min = 1
short_break_min = 5
long_break_min = 15


class NewWindow(Toplevel):
  def __init__(self, master = None):
    super().__init__(master = master)
    self.title("New Window")
    self.geometry("400x400")
    label = Label(self, text ="This is a new Window")
    label.pack()



