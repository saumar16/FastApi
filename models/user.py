from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class Movie(BaseModel):
    id: str
    title: str
    description: str
    type:str
    release_year: str
    age_certification: str
    genres: str
    type:str
    production_countries: str
    imdb_score : str

class Upadte_Movie(BaseModel):
    title: str
    description: str
    imdb_score : str
