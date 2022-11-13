Name:		texlive-lua-check-hyphen
Version:	47527
Release:	1
Summary:	Mark hyphenations in a document, for checking
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/lua-check-hyphen
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-check-hyphen.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-check-hyphen.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/lualatex/lua-check-hyphen
%doc %{_texmfdistdir}/doc/lualatex/lua-check-hyphen

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
