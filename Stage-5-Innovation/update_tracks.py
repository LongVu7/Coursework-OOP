import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts
from PIL import Image,ImageTk #Import PIL version 9.5.0 | pip install PIL==9.5.0  
from image import ImageSong #Because Module ANTIALIAS was removed from version 10.0.0

def modify_text(text_area, content): #Methods to modify content
    text_area.delete("1.0", tk.END) #Delete function
    text_area.insert(1.0, content)  #Insert function


class UpdateTrack: #Update track class
    def __init__(self, window):
        window.geometry("1050x520")#Size of GUI app
        window.title("Update Track") #Label title "Update track"

        # Label and input for track number
        enter_lbl = tk.Label(window, text="Enter Track Number(01-05):") #Enter number from 01 to 05
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Label and input for new rating
        enter_rating = tk.Label(window, text="Enter Rating (0-5):")#Enter number from 01 to 05
        enter_rating.grid(row=0, column=3, padx=10, pady=10)
        self.rating_num = tk.Entry(window, width=3)
        self.rating_num.grid(row=0, column=4, padx=10, pady=10)

        # Button to update track
        update_btn = tk.Button(window, text="Update Track", command=self.update_rating)
        update_btn.grid(row=1, column=3, padx=10, pady=10)

        # Scrolled text area where will display all tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text area to display all track details
        self.track_txt = tk.Text(window, width=40, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        #Image area to display image
        self.image_lb = tk.Label(window)
        self.image_lb.grid(row=2, column=3, padx=10, pady=10)

        # Status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

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

        # Display the list of all tracks
        self.track_list()
        
        
    def update_rating(self): #Update rating methods
        track_num = self.input_txt.get().strip() #Get an input and remove all trailing whitespace
        try: 
            rating_num = int(self.rating_num.get().strip())
        except ValueError: #Print an error message when rating is not in range of 0-5 
            self.status_lbl.configure(text="Error: Rating must be a number between 0 and 5.")#Define a range from 01 to 05
            return

        #Restrict an invailid number range
        if rating_num < 0 or rating_num > 5:
            self.status_lbl.configure(text="Error: Rating must be between 0 and 5.")
            return

        # Get the track name and update the rating
        track_name = lib.get_name(track_num)
        if track_name is not None:
            lib.set_rating(track_num, rating_num)  # Update the rating in the library
            play_count = lib.get_play_count(track_num)  # Get the current play count
            track_details = (
                f"Track: {track_name} - {lib.get_singer(track_num)}\n"
                f"New Rating: {rating_num}\n"
                f"Play Count: {play_count}\n"
                f"Youtube link: {lib.get_youtube_link(track_num)}"
            )
            self.status_lbl.configure(
                text=f"Updated '{track_name}' with new rating {rating_num}."
            )
            
            #Display image
            image_numb = img_song.get_image_path(track_num)
            if image_numb is not None: #If the image is not empty
                self.display_image(image_numb)
            else:
                self.image_lb.configure(image='', text=f"Error track number:{track_num}, can not display image ")
                
            modify_text(self.track_txt, track_details)  # Display track details
            self.track_list()  # Refresh the track list display
        else:
            self.status_lbl.configure(text=f"Error: Track ID '{track_num}' not found.")

    def track_list(self): #List all track in scrolled text 
        track_lists = lib.list_all()  # Fetch the updated list of tracks
        modify_text(self.list_txt, track_lists)  # Update the ScrolledText widget
        self.status_lbl.configure(text="Track and Rating was updated successfully.")
    

    def display_image(self, image_path): #Display an image with resized and converted the image 
        try:
            img = Image.open(image_path)
            resize_img = img.resize((200,150), Image.ANTIALIAS)
            converted_img = ImageTk.PhotoImage(resize_img)
            self.image_lb.config(image=converted_img)
            self.image_lb.image = converted_img
        except Exception as e:
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

img_song = ImageSong()

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateTrack(window)
    window.mainloop()
