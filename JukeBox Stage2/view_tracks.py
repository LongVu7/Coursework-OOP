#import tkinter module to develop Graphical User Interface 
import tkinter as tk 
import tkinter.scrolledtext as tkst

#import track_library and font_manager to retrieve a defined methods for better scalability
import track_library as lib
import font_manager as fonts


def set_text(text_area, content): #to setting a text area
    text_area.delete("1.0", tk.END)  #delete the first text area
    text_area.insert(1.0, content) #insert the first text area


class TrackViewer(): 
    def __init__(self, window): #modify a GUI interface
        window.geometry("750x350") #setting a size
        window.title("View Tracks") #name a label GUI title "View Tracks"
        
        #List All Tracks button
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked) #modify a label of "List All Tracks" button 
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10) #Determine a button With a grid layout and where button appear

        #Label "Enter track number"
        enter_lbl = tk.Label(window, text="Enter Track Number") 
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)
        #An input area where user can enter a track number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)
       
        #View track button which perform a view track functionality
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked) #display a label "View Track"
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)
       
        #Scrolled text area where print a available tracks with details (name, rating..) 
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        
        #Text area: print a results after entered track number and clicked the "view Track" button 
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)
        
        #Status label below scrolled text area 
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_tracks_clicked() #By creating an empty methods without parameter to display which button was clicked

    def view_tracks_clicked(self): #View track methods
        key = self.input_txt.get() #Assign the track number to key variable 
        name = lib.get_name(key)  #Used a defined get_name methods from track_library.py module
        if name is not None: #Make a conditional when "name" variable is not empty
            artist = lib.get_artist(key) #Define a artist variable by assign a artist by calling a get_artist methods
            rating = lib.get_rating(key) #Define a rating variable by assign a rating by calling a get_rating methods
            play_count = lib.get_play_count(key)#Define a play_count variable by assign a rating by calling a get_play_count methods
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}" #Defined track_details to a defined format 
            set_text(self.track_txt, track_details) #Setting and printing to a text area with track_details variable format
        else: #Other case (An invalid input format)
            set_text(self.track_txt, f"Track {key} not found") #Print in track_txt(text area) an error message
        self.status_lbl.configure(text="View Track button was clicked!") #Print in status_lbl(scrolled text area) a message

    def list_tracks_clicked(self): #Display a message when clicked a list tracks button
        track_list = lib.list_all() #Assign retrieved method list_all from track_library to track_list method
        set_text(self.list_txt, track_list) #Modify and printing an all tracks in list_txt(scrolled text area)
        self.status_lbl.configure(text="List Tracks button was clicked!") #Display in GUI with formatted message

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
