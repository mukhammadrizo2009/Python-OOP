### ✅ **Task 7 – Movie klassi bilan ishlash**


class Movie:
    def __init__(self , title: str,
                 genre: str ,
                 duration: int ,
                 rating: float):
        
        self.title    = title
        self.genre    = genre
        self.duration = duration
        self.rating   = rating
        
        def show_sumary():
            return None
        
        
movie = Movie('Tilim qursin','komediya', 94 , 8.7)


print(f"{movie.title} - {movie.genre} janrdagi film | Reyting: {movie.rating}/10")