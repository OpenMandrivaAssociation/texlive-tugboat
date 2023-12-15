Name:		texlive-tugboat
Version:	68694
Release:	1
Summary:	LaTeX macros for TUGboat articles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tugboat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides ltugboat.cls for both regular and proceedings issues
of the TUGboat journal. The distribution also includes a BibTeX
style appropriate for use with the classes' "harvard" option.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/tugboat
%{_texmfdistdir}/tex/latex/tugboat
%doc %{_texmfdistdir}/doc/latex/tugboat
#- source
%doc %{_texmfdistdir}/source/latex/tugboat

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
