class LibraryItem: #create parent class with attributes
    def __init__(self, name, artist, rating=0):
        self.name = name
        self.artist = artist
        self.rating = rating
        self.play_count = 0

    def info(self): #define a information 
        return f"{self.name} - {self.artist} {self.stars()}"

    def stars(self): #define a rating star 
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
