from PIL import Image, ImageTk




# size
# APP_SIZE = (700, 800)

# rows and columns
MAIN_ROWS = 5
MAIN_COLUMNS = 4

# colors
WHITE = "#EEEEEE"
COLORS = {
    "yellow":"#F3E99F",
    "red": "#FF6969",
    "green": "#C7E8CA",
    "pink": {"fg":"#F4BFBF", "hover":"#ABC4AA", "text": WHITE}

    
}


FONT = "small fonts"
BIG_FONT_SIZE = 50
SMALL_FONT_SIZE = 20

TIMER_COLOR = {
    "long_break":"#FF6D60",
    "short_break":"#F3E99F",
}


STYLING = {
    "gap": 15,
    "corner-radius" : 5
} 

PLAYLISTS = ["music/playlist_1.mp3", "music/playlist_2.mp3","music/playlist_3.mp3", "music/playlist_4.mp3", "music/playlist_5.mp3"]



# timer settings
WORK_MIN = 50
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15