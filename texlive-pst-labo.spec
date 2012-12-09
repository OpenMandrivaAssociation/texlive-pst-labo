# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-labo
# catalog-date 2007-03-11 16:56:01 +0100
# catalog-license lppl
# catalog-version 2.03
Name:		texlive-pst-labo
Version:	2.03
Release:	2
Summary:	Draw objects for Chemistry laboratories
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-labo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-labo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-labo.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pst-labo is a PSTricks related package for drawing basic and
complex chemical objects. The documentation of the package is
illuminated with plenty of illustrations together with their
source code, making it an easy read.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-labo/pst-labo.tex
%{_texmfdistdir}/tex/generic/pst-labo/pst-laboObj.tex
%{_texmfdistdir}/tex/latex/pst-labo/pst-labo.sty
%doc %{_texmfdistdir}/doc/generic/pst-labo/Changes
%doc %{_texmfdistdir}/doc/generic/pst-labo/README
%doc %{_texmfdistdir}/doc/generic/pst-labo/pst-labo-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docDE.ltx
%doc %{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docDE.pdf
%doc %{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docDE.tex
%doc %{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docEN.ltx
%doc %{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docEN.pdf
%doc %{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docEN.tex
%doc %{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docFR.ltx
%doc %{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docFR.pdf
%doc %{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docFR.tex
%doc %{_texmfdistdir}/doc/generic/pst-labo/pstlabo8-tab1-DE.tex
%doc %{_texmfdistdir}/doc/generic/pst-labo/pstlabo8-tab1-EN.tex
%doc %{_texmfdistdir}/doc/generic/pst-labo/pstlabo8-tab1-FR.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.03-2
+ Revision: 755319
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.03-1
+ Revision: 719363
- texlive-pst-labo
- texlive-pst-labo
- texlive-pst-labo
- texlive-pst-labo

