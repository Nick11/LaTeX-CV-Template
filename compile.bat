python .\python\cv_writer.py %~f1 %2 cv
if not exist cv.aux (
    lualatex -interaction=nonstopmode cv.tex
)
bibtex cv
lualatex -interaction=nonstopmode cv.tex

DEL cv.tmp
DEL cv.aux
DEL cv.bbl
DEL cv.blg
DEL cv.log
DEL cv.out
DEL cv.run.xml
DEL cv-blx.bib
DEL texput.log