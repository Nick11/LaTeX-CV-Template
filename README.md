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
If you want a multi-language cv, the entries must use the languages you want.  



## Details

Create your own yml file or modifie the `example.yml`
For any field you may either use a single string value or dictionaries.
```yaml
title: Master Thief
city:
  en: Middle-Earth
  de: Mittelerde
```

Use he second option if you want to define multiple languages. Each key is a unique language identifier for each language ('en', 'de', ...) and must be consistent across all values, though you can mix single-value entries and multi-language entries.

You can use `href` in the dictionaries to create links. Just add it as an additional entry to the yml section. If you need different URLs for different languages use `href_<language>` (`href_en`, `href_de`,...) as keys.
If need a link, but only one language, add the display string with key 'int' (for international) e.g. `dict=(int='This is a link', href='this://isthe/url.html')`


### Bibliography

Use the provided `<BASEDIR>/cv.bib` file


### Compile:

Run the `compile.bat` script.

or

Execute:
```bash
python .\python\cv_writer.py <your-yml-file> <language-code> <out-filename>
lualatex -interaction=nonstopmode cv.tex
bibtex cv
lualatex -interaction=nonstopmode cv.tex
```

with`:
- `your-yml-file`: The yml file with your cv data, e.g. `example.yml`
- `language-code`: The language you want the cv to be compiled for. Your yml file must contain translation for the specified language code
- `out-filename`: Where to store the generated tex file to

Example:
```bash
python .\python\cv_writer.py .\example.yml en sample_cv
```

## Font

Requires a Variable Font (single TTF with a continuous weight axis).

To change: 
1. Pick a font at [fonts.google.com](https://fonts.google.com/), filter sidebar **Number of styles → Variable**.
    Italic variant is optional but recommended (CV uses italic in subtitles/meta).
2. Download **upright VF .ttf** (and italic VF if available — not static)
3. Place in `Fonts/<FontName>/`, rename to `VF.ttf` and `Italic-VF.ttf`.
    Example for `Inter` font:
    ```
    Fonts/
    └── Inter/
        ├── Italic-VF.ttf
        └── VF.ttf
    ```

4. Edit the `% --- Font family ---` block in `cvclass.cls`.
    ```latex
    \setmainfont{<new font>}[
      Path = ./Fonts/<new font>/,
      Extension = .ttf,
      UprightFont = VF,
      ItalicFont  = Italic-VF,
    ]
    ```
   Example for `Inter` font:
    ```latex
    \setmainfont{Inter}[
      Path = ./Fonts/Inter/,
      Extension = .ttf,
      UprightFont = VF,
      ItalicFont  = Italic-VF,
    ]
    ```
    *Single-file font (no italic VF):* omit the `ItalicFont` line and add `AutoFakeSlant = 0.2,` — synthetic italic via slanting.

5. `./compile.sh` and check `cv.pdf`.
  *If fonts or font styles are missing latex renders the text in a different font. Check carefully if the fonts are correct.*


## Images

You can set two images. Put the images into the `<BASEDIR>/imgs` folder.

### Portrait

You can add an image to the header of the CV.
Set the path in your yml file as `image`, If image is omitted, the design might look off.
The image is set to fill the whole page width, so choose an appropriate image ratio.

### Side Image

This is added on the second page on the left side.  
The image is supposed to be the height of the entire page and about the width of the left section of the CV.
Use the `side_image` configuration in your yml file to set the path to your image.