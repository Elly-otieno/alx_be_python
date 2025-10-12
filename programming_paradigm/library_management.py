class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self._is_checked_out = False

    def is_available(self):
        '''Returns true if the book is not checked out'''
        return not self._is_checked_out

    def check_out(self):
        '''Mark the book as checked if available'''
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        '''Mark book as returned'''
        if self._is_checked_out:
            self._is_checked_out = False
            return False
        return True

class Library:
    def __init__(self):
        self._books = []

    def add_book(self):
        pass

    def check_out_book(self, title):
        pass

    def return_book(self, title):
        pass

    def list_available_books(self):
        pass