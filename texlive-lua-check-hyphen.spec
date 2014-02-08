# revision 27227
# category Package
# catalog-ctan /macros/luatex/latex/lua-check-hyphen
# catalog-date 2012-07-03 11:28:15 +0200
# catalog-license other-free
# catalog-version 0.1
Name:		texlive-lua-check-hyphen
Version:	0.1
Release:	2
Summary:	Mark hyphenations in a document, for checking
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/lua-check-hyphen
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-check-hyphen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-check-hyphen.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package looks at all hyphenation breaks in the document,
comparing them against a white-list prepared by the author. If
a hyphenation break is found, for which there is no entry in
the white-list, the package flags the line where the break
starts. The author may then either add the hyphenation to the
white-list, or adjust the document to avoid the break.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/lua-check-hyphen/lua-check-hyphen.lua
%{_texmfdistdir}/tex/lualatex/lua-check-hyphen/lua-check-hyphen.sty
%doc %{_texmfdistdir}/doc/lualatex/lua-check-hyphen/doc/README.md
%doc %{_texmfdistdir}/doc/lualatex/lua-check-hyphen/doc/luacheckhyphenmanual.pdf
%doc %{_texmfdistdir}/doc/lualatex/lua-check-hyphen/doc/luacheckhyphenmanual.tex
%doc %{_texmfdistdir}/doc/lualatex/lua-check-hyphen/doc/sample.pdf
%doc %{_texmfdistdir}/doc/lualatex/lua-check-hyphen/doc/sample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 813619
- Import texlive-lua-check-hyphen
- Import texlive-lua-check-hyphen

