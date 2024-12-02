import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts 

def modify_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateTrack():
    def __init__(self, window):
        window.geometry("900x400")
        window.title("Update Track")

        #Display "Enter Track Number" button
        enter_lbl = tk.Label(window, text= "Enter Track Number")  
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)
        #Receive an input number for Track Number
        self.input_txt = tk.Entry(window, width=2)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)
        ##Receive an input number for New Rating
        enter_rating = tk.Label(window, text= "Enter Rating")  
        enter_rating.grid(row=0, column=3, padx=10, pady=10)
        self.rating_num = tk.Entry(window, width=2)
        self.rating_num.grid(row=0, column=4, padx=10, pady=10)
    
        #Button "Update Track"
        check_track_btn = tk.Button(window, text= "Update Track", command=self.update_rating)
        check_track_btn.grid(row=1, column=3, padx=10, pady=10)
        #Button "Enter new rating"
        #A text area to display a playlist
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        #Display a status desription
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.clicked_action()
        #Initialize an empty list of playlist
        self.playlist = []
        
        
    def update_rating(self):
        #Get an input of track number and rating
        track_num = self.input_txt.get() 
        rating_num = self.rating_num.get()
        
        rating_num = int(rating_num)#Convert rating number to interger
        track_num = str(track_num)#Convert track number as an interger to a string
        
        #Prevent invalid input rating
        if rating_num < 0 or rating_num > 5:
            self.status_lbl.configure(text="Invalid input: Please enter rating from 0 to 5")
            return
        track_num = lib.get_name(track_num)
        if track_num is not None:
            lib.set_rating(track_num, rating_num)#Set and increase a play count
            incre_play_count = lib.increment_play_count(track_num)
            #Display a track number, rating number, and playcount into text area
            self.status_lbl.configure(text=f"Set a track {track_num}, new rating to {rating_num}. Play count incresed to {incre_play_count}")
            track_details = f"Track: {track_num}\nRating: {rating_num}\nPlay Count: {incre_play_count}"
            modify_text(self.track_txt, track_details)
        else:
            self.status_lbl.configure(text=f"Invalid result, cannot found {track_num}")#Print the error message

    def clicked_action(self): #Print a button's name was clicked
        track_list = lib.list_all()
        modify_text(self.list_txt, track_list)
        self.status_lbl.configure(text="Update Tracks button was clicked!")


   

if __name__ == "__main__": #Initialize an application
    window = tk.Tk()
    fonts.configure()
    UpdateTrack(window)
    window.mainloop()