%global tl_name lua-check-hyphen
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7a
Release:	%{tl_revision}.1
Summary:	Mark hyphenations in a document, for checking
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/lua-check-hyphen
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-check-hyphen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-check-hyphen.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package looks at all hyphenation breaks in the document, comparing
them against a white-list prepared by the author. If a hyphenation break
is found, for which there is no entry in the white-list, the package
flags the line where the break starts. The author may then either add
the hyphenation to the white-list, or adjust the document to avoid the
break.

