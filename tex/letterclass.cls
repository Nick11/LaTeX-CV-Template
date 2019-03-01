\ProvidesClass{letterclass}[2015/02/17 Letter class]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass{article}

%%%%%%%%%
% Fonts %
%%%%%%%%%

%%% modified by Karol Kozioł for ShareLaTex use
\RequirePackage[quiet]{fontspec}
\RequirePackage[math-style=TeX]{unicode-math}

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
\RequirePackage{hyperref}

\newcommand{\separ}{ \textbullet\, }

\newcommand{\header}[3]{%
	 \rule{\textwidth}{1pt}
	 \vspace{-3\baselineskip}\\
	 \begin{flushright}
	 	\textbf{#1} \\
	 	#2 \separ #3
	 	\vspace{\baselineskip}\\
	 	\today
	 \end{flushright}
}
\newcommand{\receiver}[1]{
	\vspace{\baselineskip}
	\begin{flushleft}
		#1
	\end{flushleft}
	\vfill
	}
	
\newcommand{\leading}[1]{\textbf{#1}\vspace{0.5\baselineskip}\\}

\newcommand{\opening}[1]{#1\vspace{\baselineskip}\\}

\newcommand{\closing}[1]{\vspace{2\baselineskip}\\#1}

%%%%%%%%%%%%%%
% Signature %
%%%%%%%%%%%%%%
\RequirePackage{graphicx}
\RequirePackage{xifthen}

\newenvironment{finalblock}{
	\vfill~
	\begin{flushleft}}{
	\end{flushleft}		
	}

\newcommand{\signature}[4]{
	\begin{finalblock}
		\ifthenelse{\equal{#2}{}}{} {
			\ifthenelse{\equal{#4}{}}{}{\vspace{#4}}
			\ifthenelse{\equal{#3}{}} {
				\includegraphics[width=4cm]{#2}
			}{
			\includegraphics[width=#3]{#2}
		}	
	}
	\\#1
	\end{finalblock}
	
	}

%%%%%%%%%%%%%%%%
% Other tweaks %
%%%%%%%%%%%%%%%%

\RequirePackage[left=3.5cm,top=1.5cm,right=2cm,bottom=1.5cm,nohead,nofoot]{geometry}
\RequirePackage{hyperref}
\setlength{\parindent}{0pt}
\setlength{\parskip}{\baselineskip}
\pagenumbering{gobble}