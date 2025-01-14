from bookgenres import Genres
from cild1 import RomeoAndJuliet
from romance import Romance
from child2 import Overhyped
from fantasy import Fantasy


def test_romance():
    romeo_and_juliet = RomeoAndJuliet()
    assert romeo_and_juliet.has_kiss
    assert romeo_and_juliet.title == 'Romeo and Juliet'

    assert isinstance(romeo_and_juliet, Romance)
    assert isinstance(romeo_and_juliet, Genres)

def test_fantasy():
    harry_potter = Overhyped()
    assert harry_potter.cast_spell
    assert harry_potter.title == 'Harry Potter'

    assert isinstance(harry_potter, Fantasy)
    assert isinstance(harry_potter, Genres)


