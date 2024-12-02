import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts 

from PIL import ImageTk,Image #import PIL==9.5.0 | pip install PIL==9.5.0
from image import ImageSong #Because Module ANTIALIAS was removed from version 10.0.0

def modify_text(text_area, content): #Define a methods to delete or insert a content in text area
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CreateTrack():
    def __init__(self, window): #Define a size and title of Create Track GUI
        window.geometry("1100x650") #With a size 1100x650 px 
        window.title("Create Track list")

        #Display "Enter Track Number" button
        enter_lbl = tk.Label(window, text="Enter Track Number")  
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)   #Receive an input number
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)
        
        #Button "Add Track"
        add_track_btn = tk.Button(window, text="Add Track", command=self.add_track_button)
        add_track_btn.grid(row=0, column=2, padx=5, pady=5)
        
        #Button "Play Playlist"
        play_playl = tk.Button(window, text="Play Playlist", command=self.play_the_playlist)
        play_playl.grid(row=0, column=3, padx=10, pady=10)
        
        #Button "Reset Playlist"
        reset_playl = tk.Button(window, text="Reset Playlist", command=self.reset_playlist)
        reset_playl.grid(row=2, column=1, padx=10, pady=10)
        
        #Text area to display a playlist
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        
        #Text area
        self.track_txt = tk.Text(window, width=50, height=10, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)
        
        #Image label to display image
        self.image_lb = tk.Label(window)
        self.image_lb.grid(row=2, column=3, padx=10, pady=10)
        
        #Display a status desription
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Label and input for search term
        search_lbl = tk.Label(window, text="Search Tracks/Singers")
        search_lbl.grid(row=3, column=0, padx=10, pady=10)
        self.search_txt = tk.Entry(window, width=20)
        self.search_txt.grid(row=3, column=1, padx=10, pady=10)
         # Button to perform search
        search_btn = tk.Button(window, text="Search", command=self.search_tracks)
        search_btn.grid(row=3, column=2, padx=10, pady=10)
        # Text area for search results
        self.search_results_txt = tk.Text(window, width=41, height=8, wrap="none")
        self.search_results_txt.grid(row=3, column=3, sticky="NW", padx=10, pady=10)
       
        
        #Initialize an empty list of playlist
        self.playlist = [] 
        self.track_list()
        
        
    def add_track_button(self):
        key = self.input_txt.get() #Get the input
        print(f"User entered an input: {key}")  #Print a user's input
        #Display an image
        image_num = img_song.get_image_path(key)
        if image_num is not None: 
            self.display_image(image_num)
        else:
            self.image_lb.configure(image='', text=f"Please enter a valid number (01-05): {key}")
        track_name = lib.get_name(key)
        if track_name is not None:
            self.playlist.append(key)
            self.status_lbl.config(text=f"Added '{track_name}' to the playlist.")
        else:
            self.status_lbl.config(text=f"Error: Track number '{key}' not found.")
        self.display_playlist()

    def display_playlist(self): # Display the list of tracks from the library
        if not self.playlist:
            modify_text(self.track_txt, "No tracks in the playlist.")
            return
        playlist_content = "\n".join(
            f"{lib.get_name(track)} - {lib.get_singer(track)}\n"
            f"Rating: {lib.get_rating(track)}\n"
            f"Play Count: {lib.get_play_count(track)}\n"
            f"Youtube Link: {lib.get_youtube_link(track)}\n"
            for track in self.playlist
        )
        print("Playlist Content to Display:", playlist_content)  
        modify_text(self.track_txt, playlist_content)
        
          
    def track_list(self): #List all tracks in playlist
        track_lists = lib.list_all()   
        modify_text(self.list_txt, track_lists)
        self.status_lbl.configure(text="Available tracks listed.") 

    def play_the_playlist(self):#Play the playlist button
        if not self.playlist:
            self.status_lbl.configure(text="Error: Cannot play an empty playlist.")
            return

        for track_number in self.playlist: #Create loop to check track_number in playlist
            play_count = lib.increment_play_count(track_number) #Increase play count number
            if play_count is None: #If play count is empty or invalid
                self.status_lbl.configure(text=f"Error track ID to play track '{track_number}'.") #Display error message in status description
                return

        self.display_playlist() #Display a results
        self.track_list() #Refresh a detail playlist in scrolled text area
        self.status_lbl.configure(text="Playlist played successfully! Play counts updated.")
 
    def search_tracks(self): #Search track method 
        matching_pattern = self.search_txt.get().strip() #Receice an input without whitespace
        if not matching_pattern: 
            self.status_lbl.configure(text="Error: Please enter a search term.")
            return

        results = lib.search_library(matching_pattern)  # Call the search methods
        self.display_search_results(results)
    
    def display_search_results(self, results): #Display a result in text area for result pattern
        self.search_results_txt.delete("1.0", tk.END)
        self.search_results_txt.insert("1.0", results)
 
 
    def display_image(self, image_path): #Display an image with given track number
        try:
            img = Image.open(image_path) #open image path
            resize_img = img.resize((200,150), Image.ANTIALIAS) #resize image
            converted_img = ImageTk.PhotoImage(resize_img)
            self.image_lb.config(image=converted_img)
            self.image_lb.image = converted_img
        except Exception as e: #If invalid image path, it will print the error message 
            self.image_lb.config(image='', text=f"Error loading image: {e}")

    def display_result(self,result_match): #Display a results for searching functions 
        self.matching_result_txt.delete("1.0", tk.END)
        self.matching_result_txt.insert("1.0", result_match)
        
        
    
    #Reset playlist function
    def reset_playlist(self):
        self.playlist.clear() #clear all playlist infomation in process
        self.track_txt.delete("1.0", tk.END) #Delete informations in text area 
        self.status_lbl.configure(text="Playlist was reset.") 
    
img_song = ImageSong() #Initialize the ImageSong class

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    #Intialize the CreateTrack
    CreateTrack(window)
    window.mainloop()