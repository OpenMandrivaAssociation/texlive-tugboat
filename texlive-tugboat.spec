# revision 22462
# category Package
# catalog-ctan /macros/latex/contrib/tugboat
# catalog-date 2011-05-13 02:06:40 +0200
# catalog-license lppl
# catalog-version 2.8
Name:		texlive-tugboat
Version:	2.8
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides both ltugboat.cls (for ordinary issues of the journal)
and ltugproc.cls (for issues that are proceedings of TUG
meetings). The distribution also includes a BibTeX style
appropriate for use with the classes' "harvard" option.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
