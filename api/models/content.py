
class Content:
    """Content class for netflix movie or tv show"""
    __tablename__ = 'content'

    columns = ['id', 'netflix_id', 'title', 'type', 'description', 'release_year', 'age_certification', 'runtime', 'imdb_id', 'imdb_score', 'imdb_votes']

    def __init__(self, values) -> None:
        self.__dict__ = dict(zip(self.columns, values))