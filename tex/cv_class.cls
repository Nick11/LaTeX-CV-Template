\ProvidesClass{cv_class}[2015/02/17 CV class]
\NeedsTeXFormat{LaTeX2e}

\ProcessOptions\relax
\LoadClass{article}

%%%%%%%%%%
% Colors %
%%%%%%%%%%

\RequirePackage{xcolor}

\definecolor{white}{RGB}{255,255,255}
\definecolor{darkergray}{RGB}{80,80,80}
\definecolor{lightgray}{HTML}{999999}

\colorlet{fillheader}{darkergray}
\colorlet{header}{white}
\colorlet{textcolor}{darkergray}
\colorlet{headercolor}{darkergray}

%%%%%%%%%
% Fonts %
%%%%%%%%%

%%% modified by Karol Kozioł for ShareLaTex use
\RequirePackage[quiet]{fontspec}
\RequirePackage[math-style=TeX,vargreek-shape=unicode]{unicode-math}

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
[Mapping=tex-text, Color=textcolor,
BoldFont=texgyreheros-bold.otf,
ItalicFont=texgyreheros-italic.otf,
BoldItalicFont=texgyreheros-bolditalic.otf
]
{texgyreheros-regular.otf}

\setmathfont{texgyreheros-regular.otf}


%%%%%%%%%%
% Header %
%%%%%%%%%%

\RequirePackage{tikz}

\newcommand{\rolefont}{%
  \fontsize{14pt}{24pt}\selectfont%
  \thinfont%
  \color{white}%
}

\newcommand{\header}[4]{%
\begin{tikzpicture}[overlay,remember picture]
	\node[opacity=0.9,shift={(0cm,-4cm)}] (img) at (current page.north){
		#4
	};
    \node [anchor=west,shift={(1.2cm,1cm)}] (name) at (img.west) {%
      \fontsize{40pt}{100}\color{header}%
      {\thinfont #1}{\bodyfont  #2}
    };
    \node [anchor=north] at (name.south) {%
      \fontsize{14pt}{24pt}\color{header}%
      \thinfont #3%
    };
  \end{tikzpicture}
  \vspace{4.2cm}
 
}


%%%%%%%%%%%%%
% Structure %
%%%%%%%%%%%%%
\RequirePackage{parskip}

\renewcommand{\section}[1]{
  \par\vspace{\parskip}
  {%
    \LARGE\headingfont\textcolor{headercolor}{#1}
  }
  \par\vspace{\parskip}
}
%\renewcommand{\subsection}[1]{
%  \par\vspace{.25\parskip}%
%  {%
%  \large\headingfont\color{headercolor} \ifthenelse{\equal{#1}{*}} {} {#1}%
%  }
%  \par\vspace{.5\parskip}%
%}
\renewcommand{\subsection}[2]{}
\pagestyle{empty}


%%%%%%%%%%%%%%%%%%%%
% List environment %
%%%%%%%%%%%%%%%%%%%%
\RequirePackage{xifthen}
\RequirePackage{longtable}
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
		\ifthenelse{\equal{#2}{None}} {} {\textit{#2}}
		\hfill
		{\footnotesize\addfontfeature{Color=lightgray}
				\ifthenelse{\equal{#3}{None}} {} {\textit{#3}\quad}
			 	\ifthenelse{\equal{#4}{None}} {} {#4}
		}%
		\ifthenelse{\equal{#5}{None}} {} {\\#5}
		\ifthenelse{\equal{#6}{None}} {} {
			\vspace{3pt}\\
			#6	
		}
		\vspace{1.5\parsep}%
	}\\}

%%%%%%%%%%%%%%
% Side block %
%%%%%%%%%%%%%%

\RequirePackage[absolute,overlay]{textpos}
\setlength{\TPHorizModule}{1cm}
\setlength{\TPVertModule}{1cm}
\newenvironment{aside}[1][0pt]{%
  \let\oldsection\section
  \renewcommand{\section}[1]{
    \par\vspace{2\baselineskip}{\Large\headingfont\color{headercolor} ##1}
  }
  \begin{textblock}{4.3}(0.7,#1)
  \begin{flushright}
  \obeycr
}{%
  \restorecr
  \end{flushright}
  \end{textblock}
  \let\section\oldsection
}

%%%%%%%%%%%%%%%%
% Bibliography %
%%%%%%%%%%%%%%%%

\RequirePackage[style=verbose,sorting=ydnt,backend=bibtex]{biblatex}
%\RequirePackage[backend=bibtex,style=alphabetic,sorting=ydnt]{biblatex}
%\addbibresource{bibliography.bib} 

\DeclareSortingScheme{chronological}{
	\sort[direction=descending]{\field{year}}
	\sort[direction=descending]{\field{month}}
}

\DeclareFieldFormat[article]{title}{#1\par}
\DeclareFieldFormat[inproceedings]{title}{#1\par}
\DeclareFieldFormat[misc]{title}{#1\par}
\DeclareFieldFormat[report]{title}{#1\par}
\DeclareFieldFormat[thesis]{title}{\bfseries{#1}\par}
\DeclareFieldFormat[report]{title}{#1\par}
\DeclareFieldFormat{abstract}{\par Abstract: #1}
\DeclareFieldFormat{school}{#1}


\DeclareBibliographyDriver{article}{%
  \printfield{title}%
  \newblock%
  \printnames{author}%
  \par%
  \newblock%
  {%
    \footnotesize\addfontfeature{Color=lightgray}\itshape%
    \usebibmacro{journal+issuetitle}%
    \setunit{\space}%
    \printfield{pages}%
    \newunit%
    \printlist{publisher}%
    \setunit*{\addcomma\space}%
    \printfield{year}%
    \newunit%
  }
  \par\vspace{0.3\baselineskip}
}

\DeclareBibliographyDriver{inproceedings}{%
  \printfield{title}%
  \newblock%
  \printnames{author}%
  \par%
  \newblock%
  {%
    \footnotesize\addfontfeature{Color=lightgray}%
    \printfield{booktitle}%
    \setunit{\addcomma\space}%
    \printfield{year}%
    \setunit{\addcomma\space}%
    \printlist{location}%
    \newunit%
  }
  \par\vspace{0.3\baselineskip}
}

\DeclareBibliographyDriver{misc}{%
  \printfield{title}%
  \newblock%
  \printnames{author}%
  \par%
  \newblock%
  {%
    \footnotesize\addfontfeature{Color=lightgray}\itshape%
    \printfield{booktitle}%
    \setunit*{\addcomma\space}%
    \printfield{note}%
    \setunit*{\addcomma\space}%
    \printfield{year}%
    \setunit{\addcomma\space}%
    \printlist{location}%
    \newunit%
  }
  \par\vspace{0.3\baselineskip}
}

\DeclareBibliographyDriver{report}{%
  \printfield{title}%
  \newblock%
  \printnames{author}%
  \par%
  \newblock%
  {%
    \footnotesize\addfontfeature{Color=lightgray}\itshape%
    \printfield{type}%
    \setunit{\space}%
    \printfield{number}%
    \setunit{\addcomma\space}%
    \printfield{year}%
    \newunit%
  }
  \par\vspace{0.3\baselineskip}
}

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
	\par\vspace{0.3\baselineskip}
}

\DeclareBibliographyDriver{report}{%
	\printfield{title}%
	\newblock%
	\printnames{author}%
	\par%
	\newblock%
	{%
		\footnotesize\addfontfeature{Color=lightgray}\itshape%
		\printfield{type}%
		\setunit{\addcomma\space}%
		\printfield{institution}%
		\setunit{\addcomma\space}%
		\printfield{year}%
		\newunit%
	}
	\newblock
	\footnotesize\addfontfeature{Color=lightgray}
	\printfield{abstract}%
	\par\vspace{0.3\baselineskip}
}

\DeclareNameFormat{author}{%
  \small\addfontfeature{Color=lightgray}%
  \ifblank{#3}{}{#3\space}#1%
  \ifthenelse{\value{listcount}<\value{liststop}}
    {\addcomma\space}
    {}%
}

\newcommand{\printbibsection}[2]{
    \nocite{*}
    \printbibliography[type={#1},title={#2},heading=subbibliography]
}





%%%%%%%%%%%%%%%%
% Other tweaks %
%%%%%%%%%%%%%%%%

\RequirePackage[left=6.1cm,top=2cm,right=1.5cm,bottom=2.5cm,nohead,nofoot]{geometry}
\RequirePackage{hyperref}