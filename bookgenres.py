from abc import ABC, abstractmethod

class Genres(ABC):
    def __init__(self, author: str, publisher: str, section: str, title: str):
        self.author = author
        self.publisher = publisher
        self.section = section
        self.title = title
    
    @abstractmethod
    def read(self)-> str:
        pass