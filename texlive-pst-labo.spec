%global tl_name pst-labo
%global tl_revision 74874

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.07
Release:	%{tl_revision}.1
Summary:	Draw objects for Chemistry laboratories
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-labo
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-labo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-labo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Pst-labo is a PSTricks related package for drawing basic and complex
chemical objects. The documentation of the package is illuminated with
plenty of illustrations together with their source code, making it an
easy read.

