class Game(object):

    name = ""
    genre = ""
    time_played = 0.0
    rating = 0.0

    def __init__(self, name, genre, time_played):
        self.name = name
        self.genre = genre
        self.time_played = time_played