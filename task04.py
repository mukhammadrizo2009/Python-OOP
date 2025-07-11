### ✅ 4. **Movie klassini yozing**


class Movie:
    def __init__(self , title: str ,
                 genre: str ,
                 duration: int ,
                 rating: float):
        
        self.title    = title
        self.genre    = genre
        self.duration = duration
        self.rating   = rating
        
        
movie = Movie('Tilim qursin','comedy', 94 , 8.7)


print(f"Kino nomi- {movie.title} | Janri- {movie.genre} | Davomiylik- {movie.duration} daqiqa | Reyting- {movie.rating}")