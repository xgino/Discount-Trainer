'''
Created on Nov 24, 2021
@summary: GameMenu screen
@author: git:buildergin
Update on Feb 04, 2022
'''


# #############################################
# imports for the GameMenu functionality
# #############################################

import tkinter as tk
from tkinter import Frame, ttk, font, PhotoImage
from tkinter.constants import FLAT
from typing import Text


# #############################################
# Own Files Import
# #############################################

## Decouple settings, config.py | Developer Changes, developer.py | switching frames, switchFrame.py
from assets import config, developer, switchFrame, sound, images
## About Window | about.py 
from windows import about

# Importing the module to know the lenght of the song
from mutagen.mp3 import MP3

from PIL import ImageTk, Image


## HERE UNDER START THE FUNCTIONS
class Main_Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(developer.APP_NAME)
        self.root.iconbitmap("static/icon/ice.ico")
        self.root.config(bg="#25292e")

        
        self.root.update_idletasks()

        self.LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
        self.DGRAY = '#25292e' # window background color               (Hex color)
        self.RGRAY = '#10121f' # title bar color                       (Hex color)


        # Styling
        self.s = ttk.Style()
        self.s.configure('Frame.TFrame', background=self.DGRAY)
        # Label Styling
        self.s.configure('small_txt.TLabel', foreground='white', background=self.DGRAY, font=('Salsa', 12))
        self.s.configure('middle_txt.TLabel', foreground='white', background=self.DGRAY, font=('Salsa', 22))
        self.s.configure('big_txt.TLabel', foreground='white', background=self.DGRAY, font=('Salsa', 42))
        self.s.configure('Train.TButton', background='#434343', foreground='#333', padding=6, relief="RAISED" )
        self.s.configure('log.TButton', )

        self.bg_music()
        self.app_frame()


    def bg_music(self):
        """
        Play Background Music
        :param: Rerun this code after the length of the song (After a song is ended)
        :return: Continue Playing songs from folder 'static/sound/background/..'
        """
        music_dir, random_music = sound.music_root()
        # Get Song Duration
        song = MP3(music_dir)
        songLength = song.info.length * 1000

        self.root.after(int(songLength), lambda: self.bg_music())


    def app_frame(self):
        """
        Head Frames for the app
        :param: Created Some Head Frames for windows
        :return: Head Frames
        """
        self.header_frame = ttk.Frame(self.root, style='Frame.TFrame')
        self.header_frame.pack(padx=15, pady=15, anchor="n", fill="x", expand="YES")

        self.container_frame = ttk.Frame(self.root, style='Frame.TFrame')
        self.container_frame.pack(padx=15, pady=10, anchor="n", fill="x", expand="YES")

        self.footer_frame = ttk.Frame(self.root, style='Frame.TFrame')
        self.footer_frame.pack(padx=15, pady=15, anchor="s", fill="x", expand="YES")

        self.homepage()


    def homepage(self):  
        """
        Home Window
        :param: Created frames and other needed for the home Window to work
        :return: Nice Home Window / Menu Window
        """

        # Header Section
        self.home_title_label = ttk.Label(self.header_frame, text=config.MENU_TITLE, style='big_txt.TLabel')
        self.home_title_label.pack(side="top")


        # Container Section
        self.home_button_frame = ttk.Frame(self.container_frame, style='Frame.TFrame')
        self.home_button_frame.pack(padx=15, pady=15, anchor="s", fill="x", expand="YES")


        # Container Buttons

        ## SQUAT BUTTON
        self.squat_image = ImageTk.PhotoImage(Image.open(images.squat_image_root()).resize((int(self.root.winfo_screenwidth() * 0.15), int(self.root.winfo_screenheight() * 0.55)))) 

        self.squat_image_label = ttk.Label(self.home_button_frame, image=self.squat_image, style='middle_txt.TLabel')
        self.squat_image_label.pack(padx=15, pady=15, anchor="n", fill="x", expand="YES")
        self.squat_image_label.configure(anchor="center")

        self.squat_button = ttk.Button(self.home_button_frame, text="Start Squat Game", cursor='hand2', style='Train.TButton', command=lambda:switchFrame.to_squat(self))
        self.squat_button.pack(padx=5, ipady=5, fill="both", side="left", expand=1)
        
        ## BICEPS BUTTON
        # STILL TO FIX




        # Footer Section
        self.home_Copyright = ttk.Label(self.footer_frame, text=developer.CREATED, style='small_txt.TLabel')
        self.home_Copyright.pack(side="left")

        self.home_update_log = PhotoImage(file='static/icon/log.png')
        self.home_update_log_btn = ttk.Button(self.footer_frame, image=self.home_update_log, cursor='hand2', command=lambda:switchFrame.to_about(self))
        self.home_update_log_btn.pack(side="right")

        self.home_game_version = ttk.Label(self.footer_frame, text=f'{developer.GAME_NAME} {developer.GAME_VERSION}', style='small_txt.TLabel')
        self.home_game_version.pack(side="right")    



def main_root(): 
    dtys = Main_Window()

    # Get Screen Height / Width, App hw = 30% orso
    screen_width = dtys.root.winfo_screenwidth()
    screen_height = dtys.root.winfo_screenheight()
    window_width = int(screen_width / 3.5)  
    window_height = int(screen_height / 3)

    # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    dtys.root.geometry(("%dx%d+%d+%d" % (screen_width,screen_height, 0, 0)))
    dtys.root.mainloop()

