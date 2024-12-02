import csv
import os

class Song:
    def __init__(self, title, youtube_link,singer, rating):
        self.title = title
        self.youtube_link = youtube_link
        self.singer = singer
        self.rating = rating

    def __str__(self):
        return f"{self.title} -{self.youtube_link} - {self.singer} - {self.rating}/5"


