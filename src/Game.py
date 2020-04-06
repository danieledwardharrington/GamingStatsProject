class Game:

    name = ""
    sort_name = "" #This is specifically for sorting the list alphabetically, trimming "the" from the beginning of any titles
    genre = ""
    steam_app_id = ""
    minutes_played = 0.0
    hours_played = 0.0
    rating = 0.0

    def __init__(self, name = "", genre = "", steam_app_id = "", minutes_played = 0.0):
        self.name = name
        self.genre = genre
        self.steam_app_id = steam_app_id
        self.minutes_played = minutes_played
        self.hours_played = minutes_played / 60
        self.hours_played = round(self.hours_played, 1)
        
        #Checking to see if the game title starts with "the" so I can remove it for the purposes of sorting
        if self.name.find("The ") == 0 or self.name.find("the ") == 0:
            self.sort_name = self.name[4:]
        else:
            self.sort_name = self.name  

    def set_sort_name(self):
        if self.name.find("The ") == 0 or self.name.find("the ") == 0:
            self.sort_name = self.name[4:]
        else:
            self.sort_name = self.name
