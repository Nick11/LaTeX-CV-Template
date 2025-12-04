# -*- coding: utf-8 -*-
__author__ = 'scheuing'
import yaml

from CVDate import CVDate
from Entry import Entry

class CV:
    def __init__(self, language="en"):
        self.language = language

    @classmethod
    def from_yml(cls, filename, language):
        with open(filename, "r", encoding="utf-8") as file:
            yml = yaml.safe_load(file)
            cv = cls(language=language)
        
        cv._image = yml["image"]
        cv._personal = yml["personal"]
        cv._languages = [cls.parse_entry(entry) for entry in yml["languages"]]
        cv._programming_languages = yml["programming_languages"]
        cv._education = [cls.parse_entry(entry) for entry in yml["education"]]
        cv._interests = yml["interests"]
        cv._it_experience = [cls.parse_entry(entry) for entry in yml["it_experience"]]
        cv._skills = [cls.parse_entry(entry) for entry in yml["skills"]]

        #colors
        section_colors = yml["section_colors"]
        cv._section_colors = [('color'+str(i), section_colors[i][0], f"{section_colors[i][1]:06}") for i in range(len(section_colors))]

		#footer
        cv._footer_text = yml["footer_text"]
        return cv

    @classmethod
    def parse_date(cls, date):
        if isinstance(date, str):
            return date
        elif isinstance(date, dict) and "year" in date:
            return CVDate.from_dict(date)
    @classmethod
    def parse_entry(cls, data):
        return Entry.from_yml(data)
    @property
    def section_about(self):
        return self.translate(dict(en='about', de='über'))
    @property
    def section_programming_languages(self):
        return self.translate(dict(en='programming', de='programmieren'))
    @property
    def section_languages(self):
        return self.translate({"en":"languages", "de":"sprachen"})
    @property
    def section_interests(self):
        return self.translate(dict(en='interests', de='Interessen'))
    @property
    def section_education(self):
        return self.translate(dict(en='education', de='Ausbildung'))
    @property
    def section_experience(self):
        return self.translate(dict(en='experience', de='Erfahrung'))
    @property
    def section_skills(self):
        return self.translate(dict(en='skills', de='Fähigkeiten'))
    @property
    def section_projects(self):
        return self.translate(dict(en='projects', de='Projekte'))
    @property
    def section_publications(self):
        return self.translate(dict(en='publications', de='Publikationen'))
    @property
    def about_since(self):
        return dict(en='since', de='seit')
		
    def about_birthday(self, use_swiss_format=False, use_pre_word=True):
        if self.language == 'de' or use_swiss_format:
            form = '{d:}.{m:}.{y:}'
        else:
            form = '{m:}/{d:}/{y:}'
        ret = self.birthday.format(form=form, language=self.language)
        if use_pre_word:
            ret = self.translate(self.about_since) + ' ' + ret
        return ret
    @property
    def birthday(self):
        return CVDate.from_yml(self._personal["birthday"])
    @property
    def title(self):
        return self.translate(self._personal["title"]).lower()
    @property
    def address(self):
        return self.translate(self._personal["address"]).lower()
    @property
    def first_name(self):
        return self.translate(self._personal["first_name"]).lower()
    @property
    def sure_name(self):
        return self.translate(self._personal["sure_name"]).lower()
    @property
    def city(self):
        return f"{self.translate(self._personal['zip']).lower()} {self.translate(self._personal['city']).lower()}"
        
    @property
    def country(self):
        return self.translate(self._personal["country"]).lower()
    @property
    def address_no_newlines(self):
        ret = '{street:}, {zip:} {city:}'
        ret = ret.format(street=self.translate(self._address),
                         zip=self.translate(self.zip),
                         city=self.translate(self.city),
                         country = self.country)
        return ret
    @property
    def nation(self):
        return self.translate(self._personal["nation"]).lower()
    @property
    def email(self):
        return self._personal["email"].lower()
    @property
    def phone(self):
        return self._personal["phone"].lower()
    @property
    def languages(self):
        ret = []
        for entry in self._languages:
            ret.append([self.translate(entry.title).lower(), self.translate(entry.quality).lower()])
        return ret

    @property
    def programming_languages(self):
        return self._programming_languages
    @property
    def interests(self):
        return [self.translate(entry).lower() for entry in self._interests]
    @property
    def education(self):
        return self._education
    @property
    def experience(self):
        return self._it_experience
    @property
    def skills(self):
        return self._skills
    @property
    def section_colors(self):
        return self._section_colors
    @property
    def image(self):
        if self._image==None:
            return ''
        else:
            return '\\includegraphics[width=\\paperwidth]{{{img:}}}'.format(img=self._image)
	
    @property
    def footer_text(self):
        return self.translate(self._footer_text)
	
    #resume specific
    @property
    def education_res(self):
        form = '\\rightentry{{{place:}}}{{{city:}}}{{None}}{{{date:}}}{{{title:}}}{{{descr:}}}'
        return self.format_entries(entries=self._education[:-1], form=form, date_form=self.education_date_format_res)
    @property
    def experience_res(self):
        form = '\\rightentry{{{place:}}}{{{city:}}}{{None}}{{{date:}}}{{{title:}}}{{{descr:}}}'
        return self.format_entries(entries=self._it_experience+self._other_experience, form=form, date_form=self.experience_date_format)
    @property
    def interests_res(self):
        ret = ', '.join([entry for entry in self._interests])
        return ret
    @property
    def languages_res(self):
        form = '\\rightentry{{{title:}}}{{{descr:}}}{{None}}{{None}}{{None}}{{None}}'
        return self.format_entries(entries=self._languages, form=form, date_form=self.experience_date_format)
    @property
    def skills_res(self):
        ret = [self.translate(entry.title) for entry in self._skills]
        ret = [self.translate(skill) for skill in self._programming_languages] + ret[:-2]
        return ', '.join(ret)

    #general
    def translate(self, property):
        if property == None:
            return
        if type(property)==dict:
            text='{{{text:}}}'
            href = '\\href{{{href:}}}'
            if 'href' in property.keys():
                href = href.format(href=property['href'])
            elif 'href_'+self.language in property.keys():
                href = href.format(href=property['href_'+self.language])
            else:
                href=''
                text='{text:}'

            if self.language in property.keys():
                return href+text.format(text=property[self.language])
            elif 'int' in property.keys():
                return href+text.format(text=property['int'])

        elif type(property)==str:
            return property
        else:
            return str(property)

    def format_entries(self, entries, form, date_form=''):
        ret = []
        for entry in entries:
            if not entry.date_from == None:
                date_from = self.format_date(entry.date_from, date_form=date_form)
            else:
                date_from = ''
            if not entry.date_until == None:
                date_until = self.format_date(entry.date_until, date_form=date_form)
            else:
                date_until = ''
            if not date_from == '':
                date_from = date_from + '--'
            date = date_from+date_until
            entry_str = form.format(date=date,
                                    title=self.translate(entry.title),
                                    place=self.translate(entry.place),
                                    descr=self.translate(entry.description),
                                    city=self.translate(entry.city),
                                    quality=self.translate(entry.quality))
            ret.append(entry_str)
        return ret
    def format_date(self, date, date_form=''):
        if isinstance(date, CVDate):
            date_from = date.format(date_form, language=self.language)
        elif isinstance(date, dict):
            date_from = self.translate(date)
        else:
            date_from = date
        return date_from

    def __str__(self):
       return str([str(k)+':'+str(v) for k,v in vars(self).items() ])
