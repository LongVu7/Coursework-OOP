import csv
import os

class Song:
    def __init__(self, title, singer, youtube_link, rating):
        self.title = title
        self.youtube_link = youtube_link
        self.singer = singer
        self.rating = rating

    def __str__(self):
        return f"{self.title} - {self.singer.name} - {self.rating}/5"


