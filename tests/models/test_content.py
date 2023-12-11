from api.models import Content

def test_init_content():
    content = Content([1000, 'tm84618','Taxi Driver','MOVIE',"A mentally unstable Vietnam War veteran works as a night-time taxi driver in New York City where the perceived decadence and sleaze feed his urge for violent action, attempting to save a preadolescent prostitute in the process.",1976,'R',113,'tt0075314',8.3,795222.0])
    assert content.title == 'Taxi Driver'