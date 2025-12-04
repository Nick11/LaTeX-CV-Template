__author__ = 'scheuing'

from CVDate import CVDate

class Entry:
    def __init__(self, title, place=None, description=None, date_from=None, date_until=None, city=None, quality=None):
        self.date_from = date_from
        self.date_until = date_until
        self.title = title
        self.place = place
        self.description = description
        self.city = city
        self.quality = quality
    @classmethod
    def from_yml(cls, data):
        if isinstance(data, str):
            return data
        date_from = data.get("date_from", None)
        if date_from is not None:
            date_from = CVDate.from_yml(date_from)
        date_until = data.get("date_until", None)
        if date_until is not None:
            date_until = CVDate.from_yml(date_until)
        return cls(
            date_from = date_from,
            date_until = date_until,
            title = data.get("title", None),
            place = data.get("place", None),
            description = data.get("description", None),
            city = data.get("city", None),
            quality = data.get("quality", None)
        )

    def title_formatted(self, language):
        return self._translate(self.title, language)
    def place_formatted(self, language):
        return self._translate(self.place, language)
    def description_formatted(self, language):
        return self._translate(self.description, language)    
    def city_formatted(self, language):
        return self._translate(self.city, language)
    def quality_formatted(self, language):
        return self._translate(self.quality, language)
    def date_formatted(self, language):
        if not self.date_from == None:
            date_from = self._format_date(self.date_from, language)
        else:
            date_from = ''
        if not self.date_until == None:
            date_until = self._format_date(self.date_until, language)
        else:
            date_until = ''
        if not date_from == '':
            date_from = date_from + '--'
        return date_from + date_until
     
    def _format_date(self, date, language):
        if isinstance(date, CVDate):
            date_from = date.format("{y:}", language=language)
        elif isinstance(date, dict):
            date_from = self._translate(date, language)
        else:
            date_from = date
        return date_from
    
    def _translate(self, property, language):
        if property == None:
            return
        if type(property)==dict:
            text='{{{text:}}}'
            href = '\\href{{{href:}}}'
            if 'href' in property.keys():
                href = href.format(href=property['href'])
            elif 'href_' + language in property.keys():
                href = href.format(href=property['href_' + language])
            else:
                href=''
                text='{text:}'

            if language in property.keys():
                return href+text.format(text=property[language])
            elif 'int' in property.keys():
                return href+text.format(text=property['int'])

        elif type(property)==str:
            return property
        else:
            return str(property)
