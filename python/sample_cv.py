__author__ = 'scheuing'
from CV import CV
from Entry import Entry
from CVDate import CVDate

#image
image='./../imgs/sample/portrait.png'

#personal information
first_name = 'Boris'
sure_name = 'Spider'
title = 'Bachelor of Science in Computer Science'
birthday = CVDate(day=10, month=1, year=1979)
nation = dict(en='Middleearth', de='Mittelerde')

address = 'Treeroad 2'
zip = '33666'
city = 'Mirkwood'
country = dict(en='Middleearth', de='Mittelerde')

email = 'boris@spider.com'
phone= '+123 456 789'

#languages
lang_german =  Entry(title=dict(en='German',de='Deutsch'),
                     quality=dict(en='academic', de='akademisch'),
                     description=dict(en='Fluent (speaking, reading, writing)',de='Fliessend (mündlch, schriftlich)'))
lang_english = Entry(title=dict(en='English',de='Englisch'),
                     quality=dict(en='native', de='Muttersprache'),
                     description=dict(en='Native language',de='Muttersprache'))
lang_french = Entry(title=dict(en='French',de='Französisch'),
                     quality=dict(en='school', de='schule'),
                     description=dict(en='Intermediate (speaking, reading, writing)',de='Gymnasiales Niveau (mündlich, schriftlich)'))


lang_skills = [lang_english, lang_german, lang_french]

#programming skills
prog_skills = ['Java',
                      'Python',
                      '\\LaTeX'
                      ]

#intersts
interests = [ 'Computers', 'Excel', 'Latex templates', 'Flowers'
]

#goals
goals = [   dict(en='PhD in Computer Science', de='PhD in Computer Wissenschaften'),
            dict(en='Build a airplane',de='Ein Flugzeug bauen'),
            'Bananen pflanzen'
]

###############################
# EDUCATION
# Add all entries to the list!
###############################
ba = Entry( date_from=CVDate(year=2000, month=9),
            date_until=CVDate(year=2001,month=2),
            title='B.Sc in Computer Science',
            place={'en':'University of Londinium','de':'Universität Londinium', 'href_en':'http://en.wikipedia.org/wiki/University', 'href_de':'http://de.wikipedia.org/wiki/Universit%C3%A4t'},
            city=dict(en='Londinum, Middleearth', de='Londinium, Mittelerde'),
            description={'en':'Minor in Music History', 'de':'Minor in Musikgeschichte'})

ma = Entry( date_from=CVDate(year=2000, month=9),
            date_until=CVDate(year=2001,month=2),
            title='M.Sc in Computer Science',
            place={'en':'University of Londinium','de':'Universität Londinium', 'href_en':'http://en.wikipedia.org/wiki/University', 'href_de':'http://de.wikipedia.org/wiki/Universit%C3%A4t'},
            city=dict(en='Londinum, Middleearth', de='Londinium, Mittelerde'))

#Add all entries to this list
education = [ba, ma]

###############################
# IT EXPERIENCE
# Add all entries to the list!
###############################
job1 = Entry(date_from=CVDate(year=2013, month=9),
            date_until=CVDate(year=2014, month=9),
            title=dict(en='Software engineering internship', de='Praktikum Softwareentwicklung'),
            place=dict(en='Some Company', de='Eine Firma'),
            city=dict(en='City, Country', de='Stadt, Land'),
            description=dict(en='A description of what you did',
                        de='Eine Beschreibung der Arbeit')
            )

job2 = Entry(date_from=CVDate(year=2013, month=9),
            date_until=CVDate(year=2014, month=9),
            title=dict(en='Another Job', de='Eine andere Arbeit'),
            place=dict(en='Some Company', de='Eine Firma'),
            city=dict(en='City, Country', de='Stadt, Land'),
            description=dict(en='A description of what you did',
                        de='Eine Beschreibung der Arbeit')
            )
#Add all entries to this list
it_experience = [job1, job2]

###############################
# Other EXPERIENCE
# Add all entries to the list!
###############################
job3 = Entry(date_from=CVDate(year=2013, month=9),
            date_until=CVDate(year=2014, month=9),
            title=dict(en='Yet Another Job', de='Noch eine  andere Arbeit'),
            place=dict(en='Some Company', de='Eine Firma'),
            city=dict(en='City, Country', de='Stadt, Land'),
            description=dict(en='A description of what you did',
                        de='Eine Beschreibung der Arbeit')
            )
#Add all entries to this list
other_experience = [job3]

###############################
# SKILLS
# Add all entries to the list!
###############################
good = dict(en='experienced', de='erfahren')
basic = dict(en='basic', de='basis')

eclipse = Entry(title='Eclipse',
                description='Java IDE',
                quality=good)
pycharm = Entry(title='Pycharm',
                description=dict(en='Python IDE by JetBrains',de='Python IDE von JetBrains'),
                quality=good)
texstudio = Entry(title='TeXstudio',
                description='\\LaTeX\,IDE',
                quality=good)
#Add all entries to this list
skills = [eclipse, pycharm, texstudio, eclipse, pycharm, texstudio,eclipse, pycharm, texstudio]


###############################
# SECTION TITLES
# Add all entries to the list!
###############################
section_about = dict(en='about', de='über')
section_prog = dict(en='programming', de='programmieren')
section_lang = dict(en='languages', de='Sprachen')
section_int = dict(en='interests', de='Interessen')
section_goals = dict(en='goals', de='Ziele')
section_edu = dict(en='education', de='Ausbildung')
section_exp = dict(en='experience', de='Erfahrung')
section_skills = dict(en='skills', de='Fähigkeiten')
section_proj = dict(en='projects', de='Projekte')
section_pub = dict(en='publications', de='Publikationen')

#words form about block
about_since = dict(en='since', de='seit')

#date
education_date_format = '{y:}'
education_date_format_res = '{M:} {y:}'
experience_date_format = '{M:} {y:}'

section_colors = [  ('HTML','22ad00'),
                    ('HTML','58d100'),
                    ('RGB','154,191,7'),
                    ('HTML','b0aa00'),
                    ('HTML','a87900')]

cv = CV(image=image,
        first_name=first_name,
        sure_name=sure_name,
        title=title,
        birthday=birthday,
        nation=nation,
        address=address,
        zip=zip,
        city=city,
        country=country,
        email=email,
        phone=phone,
        section_about=section_about,
        section_prog=section_prog,
        section_lang=section_lang,
        section_int=section_int,
        section_goals=section_goals,
        section_edu=section_edu,
        section_exp=section_exp,
        section_skills=section_skills,
        section_proj=section_proj,
        section_pub=section_pub,
        about_since= about_since,
        lang_skills=lang_skills,
        prog_skills=prog_skills,
        interests=interests,
        goals=goals,
        education=education,
        it_experience=it_experience,
        other_experience=other_experience,
        skills=skills,
        section_colors=section_colors,
        education_date_format=education_date_format,
        education_date_format_res=education_date_format_res,
        experience_date_format=experience_date_format,
        language='en')
if __name__=='__main__':
    print(cv)
    print(cv.prog_skills)
    print(cv.education)
    print(CV.color_first_letters('blabla',cv.section_colors[0][0],3))
    print(cv.section_color_names)

    print(cv.about_birthday)
    print(cv.section_goals)
    print(cv.interests)
    print(cv.image)
