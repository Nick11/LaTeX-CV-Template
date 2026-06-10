#!/usr/bin/env bash
set -euo pipefail

yml="${1:-example.yml}"
lang="${2:-en}"
out="cv"

# cv_writer.py uses a flat `from CV import CV`, so it must run from python/.
(cd python && python3 cv_writer.py "../$yml" "$lang" "../$out")

# biblatex needs lualatex → bibtex → lualatex → lualatex to resolve all refs.
lualatex -interaction=nonstopmode "$out.tex"
bibtex "$out"
lualatex -interaction=nonstopmode "$out.tex"
lualatex -interaction=nonstopmode "$out.tex"

rm -f "$out.aux" "$out.bbl" "$out.blg" "$out.log" "$out.out" \
      "$out.run.xml" "$out-blx.bib" texput.log
