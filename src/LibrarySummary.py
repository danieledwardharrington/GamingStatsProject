import tkinter
from tkinter import *
from Global import *
from operator import attrgetter
import statistics
from collections import Counter
from itertools import groupby

class LibrarySummary:
    
    def __init__(self, game_list):
        root = tkinter.Tk()
        root.title("Library Summary")
        root.iconbitmap("images/gspIconTransparent.ico")
        root.geometry("900x500")

        most_played_games_label = Label(root, text = "Most played games:", font = LARGE_FONT, anchor = W, width = 25, pady = 10)
        top_played_list = self._calculate_most_played_games(game_list)
        most_played_games_label.grid(row = 0, column = 0)

        #using for loops here in case of small library and "top" would be less than 5 (otherwise it's a top 5 list)
        for i in range(len(top_played_list)):
            game_label = Label(root, text = top_played_list[i], font = NORM_FONT, anchor = W, width = 25, pady = 5)
            game_label.grid(row = i + 1, column = 0)

        most_played_genres_label = Label(root, text = "Most played genres:", font = LARGE_FONT, anchor = W, width = 25, pady = 10)
        top_genres_played_list = self._calculate_most_played_genres(game_list)
        most_played_genres_label.grid(row = 0, column = 1)

        for i in range(len(top_genres_played_list)):
            genre_label = Label(root, text = top_genres_played_list[i], font = NORM_FONT, anchor = W, width = 25, pady = 5)
            genre_label.grid(row = i + 1, column = 1)

        highest_rated_games_label = Label(root, text = "Highest rated games:", font = LARGE_FONT, anchor = W, width = 25, pady = 10)
        highest_rated_games_list = self._calculate_highest_rated_games(game_list)
        highest_rated_games_label.grid(row = 6, column = 0)

        for i in range(len(top_genres_played_list)):
            rated_game_label = Label(root, text = highest_rated_games_list[i], font = NORM_FONT, anchor = W, width = 25, pady = 5)
            rated_game_label.grid(row = i + 7, column = 0)

        most_prevalent_genres_label = Label(root, text = "Most prevalent genres:", font = LARGE_FONT, anchor = W, width = 25, pady = 10)
        most_prevalent_genres_list = self._calculate_most_prevalent_genres(game_list)
        most_prevalent_genres_label.grid(row = 6, column = 1)

        for i in range(len(top_genres_played_list)):
            prev_genre_label = Label(root, text = most_prevalent_genres_list[i], font = NORM_FONT, anchor = W, width = 25, pady = 5)
            prev_genre_label.grid(row = i + 7, column = 1)

        root.mainloop()

    def _calculate_most_played_games(self, game_list):
        print("Sorting game_list by minutes played (descending)")
        game_list.sort(key = attrgetter("minutes_played"), reverse = True)

        print("Sorting complete")
        print("Creating new list and adding first five elements of game_list to it")
        top_five = []
        for i in range(5):
            top_five.append(game_list[i].name)

        print("Top list completed - most played games")
        return top_five

    def _calculate_most_prevalent_genres(self, game_list):
        print("Creating list of all genres in library (with dupes)")
        genre_list = []
        top_five = []
        for game in game_list:
            game_genres = [game.genre.split(", ")]
            genre_list.extend(game_genres)
        genre_list = list(filter(None, genre_list))
        flat_genres = []
        for sublist in genre_list:
            for item in sublist:
                if item == ": The RevolutionAction":
                    item = "Action"
                flat_genres.append(item)
        flat_genres = list(filter(None, flat_genres))

        print("Flat genre list completed")
        for genre in flat_genres:
            print(genre)
        
        print("Getting most prevalent genres and removing mode each iteration")
        most = ""
        for i in range(5):
            most = statistics.mode(flat_genres)
            top_five.append(most)
            flat_genres = list(filter(lambda x: x != most, flat_genres))

        print("Top list completed - most prevalent genres")
        
        return top_five

    def _calculate_highest_rated_games(self, game_list):
        print("Sorting game_list by rating (descending)")
        game_list.sort(key = attrgetter("rating"), reverse = True)

        print("Sorting complete")
        print("Creating new list to hold five highest rated games")
        top_five = []
        for i in range(5):
            top_five.append(game_list[i].name)
        print("Top list completed - highest rated games")
        return top_five

    def _calculate_highest_rated_genres(self, game_list):
        print("Sorting game_list by rating (descending)")
        game_list.sort(key = attrgetter("rating"), reverse = True)

        #creating smaller list of games to work with their genres
        small_game_list = []
        for i in range(5):
            small_game_list.append(game_list[i])

        genre_list = []
        top_five = []
        for game in small_game_list:
            game_genres = [game.genre.split(", ")]
            genre_list.extend(game_genres)
        genre_list = list(filter(None, genre_list))
        flat_genres = []
        for sublist in genre_list:
            for item in sublist:
                flat_genres.append(item)
        flat_genres = list(filter(None, flat_genres))

        print("Flat genre list completed")
        for genre in flat_genres:
            print(genre)
        
        print("Getting most prevalent genres and removing mode each iteration")
        most = ""
        for i in range(5):
            most = statistics.mode(flat_genres)
            top_five.append(most)
            flat_genres = list(filter(lambda x: x != most, flat_genres))

        print("Top list completed - highest rated genres")
        
        return top_five

    def _calculate_most_played_genres(self, game_list):
        print("Sorting game_list by minutes played (descending)")
        game_list.sort(key = attrgetter("minutes_played"), reverse = True)

        #creating smaller list of games to work with their genres
        small_game_list = []
        for i in range(5):
            small_game_list.append(game_list[i])

        genre_list = []
        top_five = []
        for game in small_game_list:
            game_genres = [game.genre.split(", ")]
            genre_list.extend(game_genres)
        genre_list = list(filter(None, genre_list))
        flat_genres = []
        for sublist in genre_list:
            for item in sublist:
                flat_genres.append(item)
        flat_genres = list(filter(None, flat_genres))

        print("Flat genre list completed")
        for genre in flat_genres:
            print(genre)
        
        # print("Getting most prevalent genres and removing mode each iteration")
        # most = ""
        # for i in range(5):
        #     most = statistics.mode(flat_genres)
        #     top_five.append(most)
        #     flat_genres = list(filter(lambda x: x != most, flat_genres))

        print("------------------------------------------")
        print("------------------------------------------")
        freqs = Counter(flat_genres)
        print(freqs)
        print("------------------------------------------")
        print("------------------------------------------")

        count = freqs.most_common(5)
        for i in range(5):
            top_five.append(count[i][0])
        print(top_five)

        print("Top list completed - most played genres")
        
        return top_five
