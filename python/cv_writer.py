import sys

from pylatex import Command, Document, UnsafeCommand, LineBreak
from pylatex.utils import NoEscape, italic
from pylatex.base_classes import Environment

from CV import CV

BIBLIOGRAPHY = "cv"
ACCENT_COLOR = "accentcolor"
BACKGROUND_COLOR = "pagebg"

class CVWriter:
    def __init__(self, cv):
        self.cv = cv
        self.doc = Document("cv", documentclass="cvclass", fontenc=None, lmodern=False)
        
    def write(self, outfile):
        self.define_colors()
        self.define_bibliography()
        self.define_bottom_part()
        self.contents()
        
        print(f"Creating: {outfile}")
        self.doc.generate_tex(filepath=outfile)

    def contents(self):
        # Header with image, name and title
        self.doc.append(
            UnsafeCommand( 
                "header",
                extra_arguments=[cv.first_name, cv.sure_name, cv.title, cv.image]
            )
        )
        
        # Left aside
        with self.doc.create(Aside(options=5.98)):
            self.about_section()
            self.language_section()
            self.programming_language_section()
            self.interests_section()
        
        self.eduction_section()
        self.experience_section()

        self.doc.append(Command("cvpagebreak"))
        self.side_image()

        self.publication_section()
        self.skill_section()
        self.bottom_section()

    # SIDE SECTIONS
    def about_section(self):
        self._cvsection(cv.section_about)
        self.doc.append(self.blank_line())
        self.doc.append(self.cv.about_birthday(use_swiss_format=True))
        self.doc.append(self.blank_line())
        self._write_lines(
            self.cv.address,
            self.cv.city,
            self.cv.country
        )
        self.doc.append(self.blank_line())
        self._write_lines(
            self._href(self.cv.email),
            self.cv.phone
        )

    def language_section(self):
        self._cvsection(cv.section_languages.lower())
        self.doc.append(self.blank_line())
        self._write_nested_lines(
            [(language, italic(skill)) for (language, skill) in cv.languages]
        )

    def programming_language_section(self):
        self._cvsection(cv.section_programming_languages.lower())
        self.doc.append(self.blank_line())
        self._write_lines(*[NoEscape(lang) for lang in cv.programming_languages])

    def interests_section(self):
        self._cvsection(cv.section_interests.lower())
        self.doc.append(self.blank_line())
        self._write_lines(*cv.interests)

    # MAIN SECTIONS
    def eduction_section(self):
        self._cvsection(self.section_title(self.cv.section_education.lower()))
        self.doc.append(self.blank_line())
        with self.doc.create(EntryList()):
            self._write_lines(*[self._entry(entry) for entry in cv.education])

    def experience_section(self):
        self._cvsection(self.section_title(self.cv.section_experience.lower()))
        self.doc.append(self.blank_line())
        with self.doc.create(EntryList()):
            self._write_lines(*[self._experience_entry(entry) for entry in cv.experience])

    def publication_section(self):
        self._cvsection(self.section_title(self.cv.section_publications.lower()), top=True)
        self.doc.append(self.blank_line())
        self.doc.append(Command("printbibsection", extra_arguments=["thesis", "Thesis"]))

    def skill_section(self):
        self._cvsection(self.section_title(self.cv.section_skills.lower()))
        self.doc.append(self.blank_line())
        with self.doc.create(EntryList()):
            self._write_lines(*[self._skill_entry(entry) for entry in cv.skills])

    def bottom_section(self):
        with self.doc.create(BottomPart()):
            self.doc.append(self.cv.footer_text)

    # DEFINITIONS
    def define_colors(self):
        # Defined in the preamble so they're available to anything in cvclass.cls
        # that runs at \AtBeginDocument (e.g. \pagecolor{pagebg}).
        self.doc.preamble.append(
            Command(
                "definecolor",
                extra_arguments=[ACCENT_COLOR, "HTML", self.cv.section_accent_color]
            )
        )
        self.doc.preamble.append(
            Command(
                "definecolor",
                extra_arguments=[BACKGROUND_COLOR, "HTML", self.cv.background_color]
            )
        )

    def define_bibliography(self):
        self.doc.preamble.append(
            Command(
                "addbibresource",
                extra_arguments=[f"{BIBLIOGRAPHY}.bib"]
            )
        )
    def define_bottom_part(self):
        new_env = UnsafeCommand(
            "newenvironment",
            "bottompar",
            options=0,
            extra_arguments=[
                "\\par\\vspace*{\\fill}\\centering",
                "\\clearpage"
            ]
        )
        self.doc.append(new_env)

    # HELPERS
    def _cvsection(self, title, top=False):
        name = "cvsection*" if top else "cvsection"
        self.doc.append(Command(name, extra_arguments=[title]))

    def _href(self, ref):
        return Command("href", extra_arguments=[ref, ref])
    def blank_line(self):
        return NoEscape("\n")
    def _write_lines(self, *lines):
        for index, line in enumerate(lines):
            if index > 0:
                self.doc.append(LineBreak())
            self.doc.append(line)

    def _write_nested_lines(self, lines):
        for index, line in enumerate(lines):
            if index > 0:
                self.doc.append(LineBreak())
            for index, inner_line in enumerate(line):
                if index > 0:
                    self.doc.append(NoEscape(r"\ "))
                self.doc.append(inner_line)
    def _entry(self, entry):
        return Command(
            "entry",
            extra_arguments=[
                NoEscape(entry.date_formatted(self.cv.language)),
                NoEscape(entry.title_formatted(self.cv.language)),
                NoEscape(entry.place_formatted(self.cv.language)),
                NoEscape(entry.description_formatted(self.cv.language))
            ]
        )
    def _experience_entry(self, entry):
        return Command(
            "rightentry",
            extra_arguments=[
                NoEscape(entry.place_formatted(self.cv.language)),
                NoEscape(None),
                NoEscape(entry.city_formatted(self.cv.language)),
                NoEscape(entry.date_formatted(self.cv.language)),
                NoEscape(entry.title_formatted(self.cv.language)),
                NoEscape(entry.description_formatted(self.cv.language))
            ]
        )
    def _skill_entry(self, entry):
        return Command(
            "rightentry",
            extra_arguments=[
                NoEscape(entry.title_formatted(self.cv.language)),
                NoEscape(entry.description_formatted(self.cv.language)),
                NoEscape(None),
                NoEscape(entry.quality_formatted(self.cv.language)),
                NoEscape(None),
                NoEscape(None)
            ]
        )
    def section_title(self, title):
        return Command(
            "textcolor",
            extra_arguments=[ACCENT_COLOR, title[:3], title[3:]]
        )
class Aside(Environment):
    _latex_name = "aside"
class EntryList(Environment):
    _latex_name = "entrylist"
class BottomPart(Environment):
    _latex_name = "bottompar"

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        yaml_file = sys.argv[1]
        language = sys.argv[2]
        out_file = sys.argv[3]
    else:
        yaml_file = "./example.yml"
        language = "en"
        out_file = "./cv"
    cv = CV.from_yml(filename=yaml_file, language=language)
    writer = CVWriter(cv=cv)
    writer.write(out_file)
