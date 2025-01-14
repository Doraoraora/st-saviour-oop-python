from romance import Romance

#the tradgedy class will be my specific class in order to identify Romeo and Juliet, a romance
class RomeoAndJuliet(Romance):
     def __init__(self):
        super().__init__('Romeo and Juliet', 'William Shakespeare', 'The Globe', True)
    
#Now I'm going to use the arg funtion to argue to the genre of RAJ
class arg:
    def __str__(*genre):
        for args in genre:
            print(args)
    genre = ('Tradedy', 'Romance', 'Fiction')
    



#Just like in my grandparent class, I want an output specifoc to my class
def intro(self)-> str:
    return self.romance_title + 'was written by ' + self.romance_author + 'and published by' + self.romance_publisher + 'You can find this book in the ' + arg + '.'
