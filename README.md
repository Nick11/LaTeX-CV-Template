# CV using pylatex

Python script generating a latex CV file.

## Install:

```sh
pip install -r requirements.txt
```

## How to use

### Add Your Info

The `example.yml` file contains sample CV information.  
Create your own yml.  
In `python/vs_writer.py` change the line, update it to use your own yml file.

```python
yaml_file = "./example.yml"
```

If you want a mulit-language cv, the entries must use the languages you want.  


### Set language

In `python/cv_writer.py` set the language in this line:

```python
language = "de"
```

## Details

Copy or edit `<BASEDIR>/python/sample_cv.py` and add your own info.
For any field you may either use strings or dictionaries. For the dictionaries you have to use a unique language identifier for each language ('en', 'de', ...) and be consistent with it (also in the LaTeX files).
You can use `href` in the dictionaries to create links. Just add it as an additional entry to the dictionary. If you need different URLs for different languages use `href_<language>` (`href_en`, `href_de`,...) as keys.
If need a link, but only one language, add the display string with key 'int' (for international) e.g. `dict=(int='This is a link', href='this://isthe/url.html')`
A few fields use the Entry and CVData classes. Just checkout the examples.
Make sure your file compiles and all dependencies (pygments) work.


### Bibliography

Use the provided `<BASEDIR>/tex/cv.bib` file or do as described in the note in the previous section.


### Compile:

Run the `compile.bat` script.

or

Execute:
```bash
python .\python\cv_writer.py %~f1 %2 cv
xelatex -interaction=nonstopmode cv.tex
bibtex cv
xelatex -interaction=nonstopmode cv.tex
```

## Images

You can set two images. Put the images into the `<BASEDIR>/imgs` folder.


### Portrait

You can add an image to the header of the CV.
Set the path in your `<BASEDIR>/python/<name>_cv.py`, field image at the beginning of the file. If image is omitted, the design might behave weird.
The image is set to fill the whole page width, so choose an appropriate image ratio.
