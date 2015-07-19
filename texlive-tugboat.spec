# revision 32478
# category Package
# catalog-ctan /macros/latex/contrib/tugboat
# catalog-date 2013-12-23 22:50:28 +0100
# catalog-license lppl
# catalog-version 2.14
Name:		texlive-tugboat
Version:	2.14
Release:	5
Summary:	LaTeX macros for TUGboat articles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tugboat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tugboat.source.tar.xz
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
%{_texmfdistdir}/bibtex/bst/tugboat/ltugbib.bst
%{_texmfdistdir}/tex/latex/tugboat/ltugboat.cls
%{_texmfdistdir}/tex/latex/tugboat/ltugboat.sty
%{_texmfdistdir}/tex/latex/tugboat/ltugcomn.sty
%{_texmfdistdir}/tex/latex/tugboat/ltugproc.cls
%{_texmfdistdir}/tex/latex/tugboat/ltugproc.sty
%doc %{_texmfdistdir}/doc/latex/tugboat/README
%doc %{_texmfdistdir}/doc/latex/tugboat/ltubguid.ltx
%doc %{_texmfdistdir}/doc/latex/tugboat/ltubguid.pdf
%doc %{_texmfdistdir}/doc/latex/tugboat/manifest.txt
%doc %{_texmfdistdir}/doc/latex/tugboat/tugboat.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tugboat/tugboat.dtx
%doc %{_texmfdistdir}/source/latex/tugboat/tugboat.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
