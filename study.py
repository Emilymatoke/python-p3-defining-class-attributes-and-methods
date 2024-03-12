class Album :
    album_count = 0 #class attribute
    GENRES = ["Hip-Hop", "Pop", "Jazz"] #class constant

    def __init__(self, date, genre) :
        if self.check-genre(genre) :
            self.increase_album_count()
            self.release_date = date
            self.genre = genre


    @classmethod
    def check_genre(cls, genre):
        return genre in cls.GENRES

    @classmethod
    def increase_album_count(cls, increment=1):
        cls.album_count += increment
```