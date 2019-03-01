__author__ = 'scheuing'
class CV:
    def __init__(self,
                 first_name,
                 sure_name,
                 title,
                 birthday,
                 nation,
                 address,
                 zip,
                 city,
                 country,
                 email,
                 phone,
                 section_about,
                 section_prog,
                 section_lang,
                 section_int,
                 section_goals,
                 section_edu,
                 section_exp,
                 section_skills,
                 section_proj,
                 section_pub,
                 about_since,
                 lang_skills,
                 prog_skills,
                 interests,
                 goals,
                 education,
                 it_experience,
                 other_experience,
                 skills,
                 section_colors,
                 education_date_format,
                 education_date_format_res,
                 experience_date_format,
                 middle_name=None,
                 language='en',
                 image=None):

        #image
        self._image = image

        #about
        self.first_name = first_name
        self.sure_name = sure_name
        self.title = title
        self._birthday = birthday
        self._nation = nation

        self._address=address
        self.zip=zip
        self.city=city
        self._country=country
        self._email=email

        self.phone = phone

        self._prog_skills = prog_skills
        #section titles
        self._section_about = section_about
        self._section_prog = section_prog
        self._section_lang = section_lang
        self._section_int = section_int
        self._section_goals = section_goals
        self._section_edu = section_edu
        self._section_exp = section_exp
        self._section_skills = section_skills
        self._section_proj = section_proj
        self._section_pub = section_pub

        #languages
        self._lang_skills = lang_skills

        #education
        self._education = education

        #interests
        self._interests=interests

        #goals
        self._goals = goals

        #work experience
        self._it_experience = it_experience
        self._other_experience = other_experience

        #tools
        self._skills = skills

        #colors
        self.section_colors = [('color'+str(i), section_colors[i][0], section_colors[i][1]) for i in range(len(section_colors))]

        #dates
        self.education_date_format = education_date_format
        self.education_date_format_res = education_date_format_res
        self.experience_date_format = experience_date_format

        self._about_since = about_since
        if middle_name == None:
            self.middle_name = ''
        else:
            self.middle_name = middle_name
        self.language = language

    @property
    def section_about(self):
        return self.translate(self._section_about)
    @property
    def section_prog(self):
        return self.translate(self._section_prog)
    @property
    def section_lang(self):
        return self.translate(self._section_lang)
    @property
    def section_int(self):
        return self.translate(self._section_int)
    @property
    def section_goals(self):
        return self.translate(self._section_goals)
    @property
    def section_edu(self):
        return self.translate(self._section_edu)
    @property
    def section_exp(self):
        return self.translate(self._section_exp)
    @property
    def section_skills(self):
        return self.translate(self._section_skills)
    @property
    def section_proj(self):
        return self.translate(self._section_proj)
    @property
    def section_pub(self):
        return self.translate(self._section_pub)
		
    def about_birthday(self, use_swiss_format=False, use_pre_word=True):
        if self.language == 'de' or use_swiss_format:
            form = '{d:}.{m:}.{y:}'
        else:
            form = '{m:}/{d:}/{y:}'
        ret = self._birthday.format(form=form, language=self.language)
        if use_pre_word:
            ret = self.translate(self._about_since) + ' ' + ret
        return ret
    @property
    def address(self):
        ret = '{street:}\\\\{zip:} {city:}\\\\{country:}'
        ret = ret.format(street=self.translate(self._address),
                         zip=self.translate(self.zip),
                         city=self.translate(self.city),
                         country = self.country)
        return ret
    @property
    def address_no_newlines(self):
        ret = '{street:}, {zip:} {city:}'
        ret = ret.format(street=self.translate(self._address),
                         zip=self.translate(self.zip),
                         city=self.translate(self.city),
                         country = self.country)
        return ret
    @property
    def country(self):
        return self.translate(self._country)
    @property
    def nation(self):
        return self.translate(self._nation)
    @property
    def email(self):
        return '\href{{mailto:{mail:}}}{{{mail:}}}'.format(mail=self._email)
    @property
    def languages(self):
        ret = ''
        for entry in self._lang_skills:
            ret = ret +'{lang:} \\textit{{{skill:}}}\\\\'.format(lang=self.translate(entry.title), skill=self.translate(entry.quality))
        return ret[:-2]

    @property
    def prog_skills(self):
        ret = '\\\\'.join(self._prog_skills)
        return ret
    @property
    def interests(self):
        ret = '\\\\'.join([entry.lower() for entry in self._interests])
        return ret
    @property
    def goals(self):
        ret = ',\\\\\\vspace{0.1\\baselineskip}'.join([self.translate(entry).lower()  for entry in self._goals])
        return ret
    @property
    def education(self):
        form = '\\entry{{{date:}}}{{{title:}}}{{{place:}}}{{{descr:}}}'
        return self.format_entries(entries=self._education, form=form, date_form=self.education_date_format)

    #CV specific
    @property
    def it_experience(self):
        form = '\\rightentry{{{place:}}}{{None}}{{{city:}}}{{{date:}}}{{{title:}}}{{{descr:}}}'
        return self.format_entries(entries=self._it_experience, form=form, date_form=self.experience_date_format)

    @property
    def other_experience(self):
        form = '\\rightentry{{{place:}}}{{None}}{{{city:}}}{{{date:}}}{{{title:}}}{{{descr:}}}'
        return self.format_entries(entries=self._other_experience, form=form, date_form=self.experience_date_format)

    @property
    def experience(self):
        form = '\\rightentry{{{place:}}}{{None}}{{{city:}}}{{{date:}}}{{{title:}}}{{{descr:}}}'
        return self.format_entries(entries=self._it_experience+self._other_experience, form=form, date_form=self.experience_date_format)
    @property
    def skills(self):
        form = '\\rightentry{{{title:}}}{{{descr:}}}{{None}}{{{quality:}}}{{None}}{{None}}'
        return self.format_entries(entries=self._skills, form=form)
    @property
    def color_def(self):
        ret = ''
        for (name,type,color) in self.section_colors:
            entry = '\\definecolor{{{name:}}}{{{type:}}}{{{color:}}}'.format(name=name, type=type,color=color)
            ret = ret + entry
        return ret

    @property
    def section_color_names(self):
        return [col[0] for col in self.section_colors]
    @property
    def image(self):
        if self._image==None:
            return ''
        else:
            return '\\includegraphics[width=\\paperwidth]{{{img:}}}'.format(img=self._image)

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
        return self.format_entries(entries=self._lang_skills, form=form, date_form=self.experience_date_format)
    @property
    def skills_res(self):
        ret = [self.translate(entry.title) for entry in self._skills]
        ret = [self.translate(skill) for skill in self._prog_skills] + ret[:-2]
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
        ret = ''
        for entry in entries:
            if not entry.date_from == None:
                date_from = entry.date_from.format(date_form, language=self.language)+' -- '
            else:
                date_from = ''
            if not entry.date_until == None:
                date_until = entry.date_until.format(date_form, language=self.language)
            else:
                date_until = ''
            date = date_from+date_until
            entry_str = form.format(date=date,
                                    title=self.translate(entry.title),
                                    place=self.translate(entry.place),
                                    descr=self.translate(entry.description),
                                    city=self.translate(entry.city),
                                    quality=self.translate(entry.quality))
            ret = ret+entry_str
        return ret

    @classmethod
    def color_first_letters(self, text, color, n_letters):
        return '\\textcolor{{{color:}}}{{{first:}}}{second:}'.format(color=str(color),
                                                                     first=text[:n_letters],
                                                                     second=text[n_letters:])

    def __str__(self):
       return str([str(k)+':'+str(v) for k,v in vars(self).items() ])
