__author__ = 'scheuing'

class Entry:
    def __init__(self, title, place=None, description=None, date_from=None, date_until=None, city=None, quality=None):
        self.date_from = date_from
        self.date_until = date_until
        self.title = title
        self.place = place
        self.description = description
        self.city = city
        self.quality = quality