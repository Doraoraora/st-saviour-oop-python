from bookgenres import Genres

class Romance(Genres):
    def __init__(self, title: str, author: str, publisher: str, has_kiss: bool):
        super().__init__(author, publisher, 'Romance', title)
        self.has_kiss = has_kiss

    def read(self) -> str:
        return self.title + ' was written by ' + self.author + ', and published by ' + self.publisher + '. You can find this book in the ' + self.section + 'section!'

    