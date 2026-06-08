\ProvidesClass{cvclass}[2025/06/08 CV class]
\NeedsTeXFormat{LaTeX2e}

\ProcessOptions\relax
\LoadClass{article}

%%%%%%%%%%
% Colors %
%%%%%%%%%%

\RequirePackage{xcolor}

\definecolor{darkergray}{RGB}{80,80,80}
\definecolor{lightgray}{HTML}{999999}

\colorlet{textcolor}{darkergray}
\colorlet{headercolor}{darkergray}
\colorlet{bannertext}{white}
% pagebg is defined per-document by cv_writer.py from the yml `background_color`.
% \pagecolor here paints the page with it so the side image's fade target
% matches the actual page color.
\AtBeginDocument{\pagecolor{pagebg}}

%%%%%%%%%
% Fonts %
%%%%%%%%%

\RequirePackage[quiet]{fontspec}
\RequirePackage[]{unicode-math}

\newfontfamily\bodyfont
[Path=./Fonts/,
BoldFont=texgyreheros-bold.otf,
ItalicFont=texgyreheros-italic.otf,
BoldItalicFont=texgyreheros-bolditalic.otf]
{texgyreheros-regular.otf}
\newfontfamily\thinfont[Path=./Fonts/]{Lato-Light.ttf}
\newfontfamily\headingfont[Path=./Fonts/]{texgyreheros-bold.otf}

\defaultfontfeatures{Mapping=tex-text}
\setmainfont
[Path=./Fonts/,
Mapping=tex-text, Color=textcolor,
BoldFont=texgyreheros-bold.otf,
ItalicFont=texgyreheros-italic.otf,
BoldItalicFont=texgyreheros-bolditalic.otf
]
{texgyreheros-regular.otf}

\setmathfont[Path=./Fonts/]{texgyreheros-regular.otf}


%%%%%%%%%%%%%%%%%%%%
% Header & images  %
%%%%%%%%%%%%%%%%%%%%

\RequirePackage{tikz}
\usetikzlibrary{fadings}
\tikzfading[name=fade-east,left color=transparent!100,right color=transparent!0]

\newcommand{\header}[4]{%
\begin{tikzpicture}[overlay,remember picture]
	\node[shift={(0cm,-4cm)}] (img) at (current page.north){#4};
	\node [anchor=south east,shift={(0cm,0.8cm)}] (name) at (img.south east) {%
		\fontsize{40pt}{100}\color{bannertext}%
		{\thinfont #1}{\bodyfont  #2}
	};
	\node [anchor=north] at (name.south) {%
		\fontsize{14pt}{24pt}\color{bannertext}%
		\thinfont #3%
	};
\end{tikzpicture}
\vspace{4.2cm}
}

\newcommand{\sideimage}[1]{%
\begin{tikzpicture}[overlay,remember picture]
	\node[anchor=north west,inner sep=0pt] (sideimg) at (current page.north west) {\includegraphics[width=5.6cm,height=\paperheight]{#1}};
	\fill[pagebg,path fading=fade-east] ([xshift=-1mm]sideimg.north east) rectangle (sideimg.south east);
\end{tikzpicture}%
}


%%%%%%%%%%%%%%%%%%%%
% Section headings %
%%%%%%%%%%%%%%%%%%%%

\RequirePackage{parskip}

\RequirePackage{xparse}
\NewDocumentCommand{\cvsection}{s m}{%
  \IfBooleanF{#1}{\vspace{\parskip}}%
  {\LARGE\headingfont\textcolor{headercolor}{#2}}%
  \par\vspace{0.3\parskip}%
}
\pagestyle{empty}


%%%%%%%%%%%%%%%%%%%%
% Entry lists      %
%%%%%%%%%%%%%%%%%%%%

\RequirePackage{etoolbox}
\RequirePackage{longtable}
\newcommand{\ifnone}[3]{\ifstrequal{#1}{None}{#2}{#3}}
\setlength{\tabcolsep}{0pt}
\newenvironment{entrylist}{%
	\setlength\LTleft{0pt}
	\setlength\LTright{0pt}
	\begin{longtable}{@{\extracolsep{\fill}}ll}
}{%
  \end{longtable}
}
\renewcommand{\bfseries}{\headingfont\color{headercolor}}
\newcommand{\entry}[4]{%
  #1&\parbox[t]{11.8cm}{%
    \textbf{#2}%
    \hfill%
    {\footnotesize\addfontfeature{Color=lightgray} #3}\\%
    #4\vspace{1.5\parsep}%
  }\\}

\newcommand{\rightentry}[6]{%
	\parbox[t]{\textwidth}{%
		\textbf{#1}
		\ifnone{#2}{}{\textit{#2}}
		\hfill
		{\footnotesize\addfontfeature{Color=lightgray}
				\ifnone{#3}{}{\textit{#3}\quad}
				\ifnone{#4}{}{#4}
		}%
		\ifnone{#5}{}{\\#5}
		\ifnone{#6}{}{\vspace{3pt}\\#6}
		\vspace{1.5\parsep}%
	}\\}


%%%%%%%%%%%%%%
% Aside      %
%%%%%%%%%%%%%%

\RequirePackage[absolute,overlay]{textpos}
\setlength{\TPHorizModule}{1cm}
\setlength{\TPVertModule}{1cm}
\newenvironment{aside}[1][0pt]{%
  \renewcommand{\cvsection}[1]{%
    \par\vspace{2\baselineskip}{\Large\headingfont\color{headercolor} ##1}%
  }
  \begin{textblock}{4.3}(0.7,#1)
  \begin{flushright}
}{%
  \end{flushright}
  \end{textblock}
  \par
}


%%%%%%%%%%%%%%%%
% Bibliography %
%%%%%%%%%%%%%%%%

\RequirePackage[style=verbose,sorting=ydnt,backend=bibtex]{biblatex}

\DeclareSortingScheme{chronological}{
	\sort[direction=descending]{\field{year}}
	\sort[direction=descending]{\field{month}}
}

\DeclareFieldFormat[thesis]{title}{\bfseries{#1}\par}
\DeclareFieldFormat{abstract}{\par Abstract: #1}
\DeclareFieldFormat{school}{#1}
\DeclareFieldFormat{url}{#1}

\DeclareBibliographyDriver{thesis}{%
	\printfield{title}%
	\newblock%
	\printnames{author}%
	\par%
	\newblock%
	{%
		\footnotesize\addfontfeature{Color=lightgray}\itshape%
		\printfield{type}%
		\setunit{\addcomma\space}%
		\printfield{school}%
		\setunit{\addcomma\space}%
		\printfield{year}%
		\newunit%
	}
	\newblock
	\footnotesize\addfontfeature{Color=lightgray}
	\printfield{abstract}%
	\par%
	\newblock
	\printfield{url}%
	\par\vspace{0.3\baselineskip}
}

\DeclareNameFormat{author}{%
	\small\addfontfeature{Color=lightgray}%
	\ifgiveninits
	{\usebibmacro{name:given-family}
		{\namepartfamily}
		{\namepartgiveni}
		{\namepartprefix}
		{\namepartsuffix}}
	{\usebibmacro{name:given-family}
		{\namepartfamily}
		{\namepartgiven}
		{\namepartprefix}
		{\namepartsuffix}}%
	\usebibmacro{name:andothers}}

\newcommand{\printbibsection}[2]{
    \nocite{*}
    \printbibliography[type={#1},title={#2},heading=subbibliography]
}


%%%%%%%%%%%%%%
% Page setup %
%%%%%%%%%%%%%%

\RequirePackage[left=6.1cm,top=2cm,right=1.5cm,bottom=1cm,nohead,nofoot]{geometry}
\RequirePackage{hyperref}

% Page break that also reduces the top margin for the new page.
% Use between page 1 (with its banner) and continuation pages where the
% banner space isn't needed.
\newcommand{\cvpagebreak}{%
  \newpage
  \newgeometry{left=6.1cm,top=1.5cm,right=1.5cm,bottom=1cm,nohead,nofoot}%
}
