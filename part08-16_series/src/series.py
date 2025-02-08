# Write your solution here:


class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        self.ratingcount = 0
        self.ratingsum = 0
        self.ratingavg = 0


    def rate(self, rating: int):
        self.ratings.append(rating)
        self.ratingcount +=1
        self.ratingsum+=rating
        self.ratingavg = self.ratingsum/self.ratingcount

    def __str__(self):
        a = (f"{self.title} ({self.seasons} seasons)\n")
        genre_string = ", ".join(self.genres)
        b = (f"genres: {genre_string}\n")
        if self.ratingcount == 0:
            c = "no ratings"
        else:
            c = (f"{self.ratingcount} ratings, average {self.ratingavg:.1f} points")
        return (a+b+c)
        
def minimum_grade(grade: float, series: list):
    nlist = []
    for s in series:
        if s.ratingavg >= grade:
            nlist.append(s)
    return nlist
        
def includes_genre(genre: str, series: list):
    nlist = []
    for s in series:
        for g in s.genres:
            if g == genre:
                nlist.append(s)
    return nlist


