from mypy_extensions import TypedDict

class ContentInterface(TypedDict, total=False):
    id: int
    netflix_id: str
    title: str 
    type: str
    description: str 
    release_year: int 
    age_certification: str 
    runtime: int 
    imdb_id: str 
    imdb_score: float
    imdb_votes: float