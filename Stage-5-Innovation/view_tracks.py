import tkinter as tk
import tkinter.scrolledtext as tkst


import track_library as lib
import font_manager as fonts

from PIL import ImageTk,Image #import PIL==9.5.0 | pip install PIL==9.5.0
from image import ImageSong #Because Module ANTIALIAS was removed from version 10.0.0

def set_text(text_area, content): #to setting a text area
    text_area.delete("1.0", tk.END)  #delete the first text area
    text_area.insert(1.0, content) #insert the first text area


class TrackViewer(): 
    def __init__(self, window): #modify a GUI interface
        window.geometry("970x650") #setting a size
        window.title("View Tracks") #name a label title "View Tracks"

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked) #modify a label of "List All Tracks" button 
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Track Number")  #modify a label of "Enter Track Number" button
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)
        #"View track" button
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked) #display a label "View Track"
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(window, width=36, height=12, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        #Image area to display image
        self.image_lb = tk.Label(window)
        self.image_lb.grid(row=2, column=3, padx=10, pady=10)

        # Label and input for search term
        search_lbl = tk.Label(window, text="Search Tracks/Artists")
        search_lbl.grid(row=3, column=0, padx=10, pady=10)
        self.search_txt = tk.Entry(window, width=20)
        self.search_txt.grid(row=3, column=1, padx=10, pady=10)
         # Button to perform search
        search_btn = tk.Button(window, text="Search", command=self.search_tracks)
        search_btn.grid(row=3, column=2, padx=10, pady=10)
        # Text area for search results
        self.search_results_txt = tk.Text(window, width=41, height=8, wrap="none")
        self.search_results_txt.grid(row=3, column=3, sticky="NW", padx=10, pady=10)

        self.list_tracks_clicked()
       

    def view_tracks_clicked(self): #Display a message when clicked a view tracks button
        key = self.input_txt.get()
        name = lib.get_name(key) 
        if name is not None: #Make a conditional when "name" variable is not empty
            artist = lib.get_singer(key)#Define a artist variable by assign a artist by calling a get_artist methods
            rating = lib.get_rating(key)#Define a rating variable by assign a rating by calling a get_rating methods
            play_count = lib.get_play_count(key)#Define a play_count variable by assign a rating by calling a get_play_count methods
            youtube_link = lib.get_youtube_link(key)#Define a yb link 
            #Assign track_details to a defined format 
            track_details = (f"{name} - {artist}\n"
            f"Rating: {rating}\n"
            f"Play counts: {play_count}\n"
            f"Youtube link: {youtube_link}\n"
            )
            set_text(self.track_txt, track_details)
        else:#In other case(An invalid input format), display a message
            set_text(self.track_txt, f"Track {key} not found") #Display error message
        self.status_lbl.configure(text="View Track button was clicked!")#Display a button clicked

        #Display an image when track number was entered
        image_numb = img_song.get_image_path(key)
        if image_numb is not None: #If the image is not empty
                self.display_image(image_numb)
        else: #Display error message
                self.image_lb.configure(image='', text=f"Error track number:{key}, can not display image ")
   
   #Display an image with resized and converted the image 
    def display_image(self, image_path):
        try: #If image is valid, it will display the image 
            img = Image.open(image_path) 
            resize_img = img.resize((200,150), Image.ANTIALIAS)
            converted_img = ImageTk.PhotoImage(resize_img)
            self.image_lb.config(image=converted_img)
            self.image_lb.image = converted_img
        except Exception as e: #Display error message when entered an invalid input
            self.image_lb.config(image='', text=f"Error loading image: {e}")

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
        

    def list_tracks_clicked(self): #Display a message when clicked a list tracks button
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")


img_song = ImageSong() #Intitialize the ImageSong class


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
