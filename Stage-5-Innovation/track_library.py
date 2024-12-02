import csv

#Create empty the library to store in global dictionary
library = {}

# Path to the CSV file
csv_file = 'songs.csv'

def load_library_from_csv(file_path):
    global library #Load csv data to global library
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            print("CSV Columns:", reader.fieldnames) #Check column name from csv file
            for row in reader: #read each row in csv dictionary 
                track_id = str(row['id']) 
                #Index the corresponding title with row's title in csv
                library[track_id] = {
                    'title': row['title'], 
                    'singer': row['singer'],  
                    'rating': int(row.get('rating', 0)),#Set default rating to 0, if it empty
                    'youtube_link': row['youtube link'],
                    'play_count': int(row.get('play_count', 0))  #Set default play count to 0
                }
        print("Library loaded successfully:", library)  
    except FileNotFoundError:
        print(f"File {file_path} not found. Starting with an empty library.")
        
        
def save_library_to_csv(file_path): #Save data from global dictionary to csv file
    global library
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'singer', 'rating', 'youtube link', 'play_count']) #Open dictionary writer to define a title row
        writer.writeheader()
        for track_id, track in library.items():
            writer.writerow({
                'id': track_id,
                'title': track['title'],
                'singer': track['singer'],
                'rating': track['rating'],
                'youtube link': track['youtube_link'],
                'play_count': track['play_count']
            })

def list_all(): #List all available track in csv file 
    global library
    return "\n".join(
        f"{track_id}:{details['title']} - {details['singer']} (Rating: {details['rating']}, Play: {details['play_count']})"
        for track_id, details in library.items()
    )

def get_name(track_id): #Get a track name from its track id
    return library.get(track_id, {}).get('title', None)

def get_singer(track_id):#Get a singer of track from its track id
    return library.get(track_id, {}).get('singer', None)

def get_rating(track_id):#Get a rating of track from its track id
    return library.get(track_id, {}).get('rating', None)

def increment_play_count(track_id): #Increase a play count number by 1 
    if track_id in library:
        library[track_id]['play_count'] += 1 
        save_library_to_csv(csv_file)  #Save permanently a new play count number to csv 
        return library[track_id]['play_count'] 
    return None

def get_play_count(track_id): #Get a play count number
    return library.get(track_id, {}).get('play_count', 0) #Set default play count number = 0
    
def get_youtube_link(track_id):#get a youtube link with corresponding index
    return library.get(track_id, {}).get('youtube_link', None)
    
def set_rating(track_id, rating):#Set rating number methods 
    if track_id in library:
        library[track_id]['rating'] = rating
        save_library_to_csv(csv_file)  # Save changes to the CSV file

def search_library(matching_pattern): #Search facilitate to search a matching pattern in csv library 
    global library
    matching_pattern = matching_pattern.lower()  # Make the search case-insensitive
    results = []

    for track_id, details in library.items():
        if (matching_pattern in details['title'].lower()) or (matching_pattern in details['singer'].lower()):
            results.append(
                f"{track_id}: {details['title']} by {details['singer']} "
                f"(Rating: {details['rating']}, Plays: {details['play_count']})"
            )

    return "\n".join(results) if results else "No matching tracks or artists found."




# Load the library at initialization
load_library_from_csv(csv_file)
