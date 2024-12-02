class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        song_list = "\n".join(str(s) for s in self.songs)
        return f"{self.name}\n{song_list}"