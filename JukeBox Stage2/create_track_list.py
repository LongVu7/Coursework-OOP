import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts 


def modify_text(text_area, content): #Define a methods to delete or insert a content in text area
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CreateTrack():
    def __init__(self, window): #Define a size and title of Create Track GUI
        window.geometry("900x400") #With a size 900x400 px 
        window.title("Create Track list")

        #Display "Enter Track Number" button
        enter_lbl = tk.Label(window, text="Enter Track Number")  
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)   #Receive an input number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)
        #Button "Add Track"
        check_track_btn = tk.Button(window, text="Add Track", command=self.add_track_button)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)
        #Button "Play Playlist"
        play_playl = tk.Button(window, text="Play Playlist", command=self.play_the_playlist)
        play_playl.grid(row=1, column=3, padx=10, pady=10)
        #Button "Reset Playlist"
        reset_playl = tk.Button(window, text="Reset Playlist", command=self.reset_playlist)
        reset_playl.grid(row=2, column=3, padx=10, pady=10)
        #A text area to display a playlist
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        #Text area
        self.track_txt = tk.Text(window, width=40, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        #Display a status desription
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_tracks_clicked()
        #Initialize an empty list of playlist
        self.playlist = []
        

    def add_track_button(self): #Initialize a add track button
        #Get an input of track number and name
        track_number = self.input_txt.get() 
        track_name = lib.get_name(track_number)
        #If track_name is valid, add track number to playlist and display a message
        if track_name is not None:
            self.playlist.append(track_number)
            self.status_lbl.config(text=f"Added a {track_name} to playlist")
        else: #If it invalid, display an error message
            self.status_lbl.config(text=f"Please enter a valid number (01-05): '{track_number}'")
        self.display_playlist()
        
    def list_tracks_clicked(self): #Display a status when button was clicked
        track_list = lib.list_all()
        modify_text(self.list_txt, track_list)
        self.status_lbl.configure(text="Create Tracks button was clicked!")


    def display_playlist(self): #Display the playlist with a corresponding track
        playls_area = "\n".join(f"{lib.get_name(track)} - Plays: {lib.get_play_count(track)}"
        for track in self.playlist)
        modify_text(self.track_txt, playls_area)
       

    def play_the_playlist(self): #Play the playlist methods
        for track_number in self.playlist: #Search track number in playlist
            lib.increment_play_count(track_number) #Increment a play count with corresponding track number
        if not self.playlist: 
            self.status_lbl.configure(text= "Can not running an empty playlist") #Invalid input
            return
        self.display_playlist()
        self.status_lbl.configure(text="Played a playlist. Track play incremently counted")
        
        
    def reset_playlist(self): #Create a reset method
        self.playlist.clear() #Clear a playlist
        self.track_txt.delete("1.0", tk.END) #Delete the all displayed result
        self.status_lbl.configure(text="Playlist was cleared")



if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    #Intialize the CreateTrack
    CreateTrack(window)
    window.mainloop()