from bookgenres import Genres

class Fantasy(Genres):
    def __init__(self, title: str, author: str, publisher: str, section: str, cast_spell: bool):
        super().__init__(author, publisher, section, title)
        self.cast_spell = cast_spell

    def read(self) -> str:
        return self.title + ' was written by ' + self.author + ', and published by ' + self.publisher + '. You can find this book in the ' + self.section + 'section!'
      



