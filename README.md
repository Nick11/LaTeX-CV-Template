# CV and Resumeé using PythonTex
Templates for a CV and Resume and a letter.
* CV and Resume are generated from the same data source (a python file)
* Letter is just a latex template


## Install:
1. Download and install:
	* pythontex: https://github.com/gpoore/pythontex
	* pygments: https://pypi.python.org/pypi/Pygments#downloads
	
	The installation directory will be denoted as <PYTHONTEX_DIR> and <PYGMENTS_DIR>.
2. Add both, \<PYTHONTEX_DIR> and \<PYGMENTS_DIR> to PYTHONPATH
3. Add \<PYTHONTEX_DIR>/pythontex/ to PATH


## How to use
You will have to deal with python and latex files.

\<BASEDIR> will denote the directory of this project

## Short
1. Python: Create your own <BASEDIR>/python/<name>_cv.py (see <BASEDIR>/python/sample_cv.py)
2. Latex: Modify the preamble of <BASEDIR>/tex/cv.tex and <BASEDIR>/tex/resume.tex:
a)

		#SET YOUR <name>_cv PYTHON FILE HERE
		from <name>_cv import cv
		
		#SET YOUR LANGUAGE HERE
		cv.language='en'
		
b) If you use another filename for your bibliography:

			%SET YOUR BIBLIOGRAPHY HERE
			\addbibresource{bibliography.bib} 

## Python
Copy or edit \<BASEDIR>/python/sample_cv.py and add your own info.

For any field you may either use strings or dictionaries. For the dictionaries you have to use a unique language identifier for each language ('en', 'de',... )and be consistent with it (also in the latex files).

You can use 'href' in the dictionaries to create links. Just add it as an additional entry to the dictionary. If you need different URLs for different languages use href_\<language> ('href_en', 'href_de',...) as keys.
If need a link, but only one language, add the display string with key 'int' (for international) e.g. 

		dict=(int='This is a link', href='this://isthe/url.html')

A few fields use the Entry and CVDate classes. Just checkout the examples.
Make sure your file compiles and all dependencies (pygment) work.

### Adding another language
1. Add translation to \<BASEDIR>/python/<name>_cv.py
 
If you add another language make sure all fields are either translated or a string.

Don't forget the SECTION TITLES

2. Set correct language in latex files (see latex section)


## LaTeX
You don't need to use both, \<BASEDIR>/tex/cv.tex AND \<BASEDIR>/tex/resume.tex. They both use the \<BASEDIR>/python/<name>_cv.py as source, but don't depend on each other

###  Setting the python file
 In both \<BASEDIR>/tex/cv.tex AND <BASEDIR>/tex/resume.tex set in the preamble:
 a)
	 	#SET YOUR <name>_cv PYTHON FILE HERE
		from <name>_cv import cv
	
		#SET YOUR LANGUAGE HERE
		cv.language='en'
		
The language string must be one of the keys used in the python dictionaries. If an invalid key is used, the english ('en') or international ('int') version will be used
	
b) If you use another filename for your bibliography:
		
		%SET YOUR BIBLIOGRAPHY HERE
		\addbibresource{bibliography.bib}
		
### Bibliography
Use the provided \<BASEDIR>/tex/bibliography.bib file or do as described above in b)

### Letter
The letter.tex works witout any python(tex) dependencies.

Don't forget to set the path to your signature at the end of the file.

### Compile

		xelatex cv.tex
		pythontex cv.tex
		xelatex cv.tex

Same for resume.tex

For the letter.tex you can simply use xelatex

NOTE: Delete the latex temp. files and the pythontex-files-* folders if you can't compile for some weird reasons.

NOTE: You also need to run biblatex to get the bibliography working

## Images
You can set two images. Put the images into the \<BASEDIR>/imgs folder.

### Portrait
You can add an image to the header of the CV.

Set the path in your \<BASEDIR>/python/<name>_cv.py, field image at the beginning of the file. If image is omitted, the design might behave weird.

The image is set to fill the whole page width, so choose an appropriate image ratio.

### Signature
\<BASEDIR>/tex/letter.tex uses an image as signature. Set the path at the end of the file.



## FAQ
Q: I can't compile for some weird reasons.

A: Delete the latex temp. files and the pythontex-files-* folders and try again.


Q: The PUBLICATIONS section is empty.

A: Compile the bibliography. Try using biblatex.
