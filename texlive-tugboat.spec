%global tl_name tugboat
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.38
Release:	%{tl_revision}.1
Summary:	LaTeX macros for TUGboat articles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tugboat
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides ltugboat.cls for both regular and proceedings issues of the
TUGboat journal. Also provides a BibTeX style, tugboat.bst.

