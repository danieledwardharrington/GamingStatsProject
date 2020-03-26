class Game:

    name = ""
    genre = ""
    minutes_played = 0.0
    hours_played = 0.0
    rating = 0.0

    def __init__(self, name, genre, minutes_played):
        self.name = name
        self.genre = genre
        self.minutes_played = minutes_played
        self.hours_played = minutes_played / 60

    def update_rating(self, new_rating):
        pass