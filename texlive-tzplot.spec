Name:		texlive-tzplot
Version:	64537
Release:	2
Summary:	Plot graphs with TikZ abbreviations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tzplot
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tzplot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tzplot.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX package that provides TikZ-based macros to make
it easy to draw graphs. The macros provided in this package are
just abbreviations for TikZ codes, which can be complicated;
but using the package will hopefully make drawing easier,
especially when drawing repeatedly. The macros were chosen and
developed with an emphasis on drawing graphs in economics. The
package depends on TikZ, xparse, and expl3.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tzplot
%doc %{_texmfdistdir}/doc/latex/tzplot

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
