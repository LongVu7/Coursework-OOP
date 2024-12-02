import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts 

from view_tracks import TrackViewer
from create_track_list import CreateTrack
from update_tracks import UpdateTrack



def modify_text(text_area, content): #Define a methods to delete or insert a content in text area
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class GuiCombine(TrackViewer, CreateTrack, UpdateTrack):
    def __init__(self, window):
           #Define a size and title of GUI combine
        window.geometry("1150x680") #With a size 1100x650 px 
        window.title("GUI combine")
        #Display "Enter Track Number" button
        CreateTrack.enter_lbl = tk.Label(window, text="Enter Track Number")  
        CreateTrack.enter_lbl.grid(row=0, column=0, padx=10, pady=10)
        self.input_txt = tk.Entry(window, width=3)   #Receive an input number
        self.input_txt.grid(row=0, column=0,columnspan=2 , padx=10, pady=10)
        #Button "Add Track"
        CreateTrack.add_track_btn = tk.Button(window, text="Add Track", command=self.add_track_button)
        CreateTrack.add_track_btn.grid(row=1, column=2, padx=5, pady=5)
        #Button "Play Playlist"
        CreateTrack.play_playl = tk.Button(window, text="Play Playlist", command=self.play_the_playlist)
        CreateTrack.play_playl.grid(row=2, column=2, padx=5, pady=5)
        #Button "Reset Playlist"
        CreateTrack.reset_playl = tk.Button(window, text="Reset Playlist", command=self.reset_playlist)
        CreateTrack.reset_playl.grid(row=4, column=3, padx=5, pady=5)
        #Button "Update Track"
        UpdateTrack.update_btn = tk.Button(window, text="Update Track", command=self.update_rating)
        UpdateTrack.update_btn.grid(row=3, column=2, padx=5, pady=5)
        #Button "View Track"
        TrackViewer.check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked) #display a label "View Track"
        TrackViewer.check_track_btn.grid(row=0, column=3, padx=10, pady=10)
        # Label and input for new rating
        UpdateTrack.enter_rating = tk.Label(window, text="Enter Rating (0-5):")#Enter number from 01 to 05
        UpdateTrack.enter_rating.grid(row=0, column=2, padx=5, pady=5)
        #Rating number entry
        UpdateTrack.rating_num = tk.Entry(window, width=3)
        UpdateTrack.rating_num.grid(row=0, column=1,columnspan=3, padx=10, pady=10)
        #Text area to display a playlist
        self.list_txt = tkst.ScrolledText(window, width=47, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        #Text area
        self.track_txt = tk.Text(window, width=49, height=12, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)
        #Image label to display image
        self.image_lb = tk.Label(window)
        self.image_lb.grid(row=2, column=3, padx=10, pady=10)       
        #Display a status desription
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        # Label and input for search term
        search_lbl = tk.Label(window, text="Search Tracks/Artists")
        search_lbl.grid(row=4, column=0, padx=10, pady=10)
        self.search_txt = tk.Entry(window, width=20)
        self.search_txt.grid(row=4, column=1, padx=10, pady=10)
         # Button to perform search
        search_btn = tk.Button(window, text="Search", command=self.search_tracks)
        search_btn.grid(row=5, column=1, padx=10, pady=10)
        # Text area for search results
        self.search_results_txt = tk.Text(window, width=35, height=4, wrap="none")
        self.search_results_txt.grid(row=4, column=2,columnspan=3, sticky="NW", padx=10, pady=10)    
        #Initialize an empty list of playlist
        self.playlist = [] 
        self.track_list()
        self.list_tracks_clicked()
            
if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    #Intialize the GuiCombine class
    GuiCombine(window)
    window.mainloop()