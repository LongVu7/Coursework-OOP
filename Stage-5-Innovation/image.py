from PIL import Image, ImageTk

image_path = "image"

class ImageSong:
    def __init__(self):
        # Map track IDs to corresponding image filenames
        self.image_map = {
            "01": "img_song/song1.jpg",
            "02": "img_song/song2.jpg",
            "03": "img_song/song3.jpg",
            "04": "img_song/song4.jpg",
            "05": "img_song/song5.jpg"
        }

    def get_image_path(self, track_id):
        """Retrieve the image path for a given track ID."""
        return self.image_map.get(track_id, None)
    
    
    