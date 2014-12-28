Summary:	General tool for mathematics
Summary(pl.UTF-8):	Rozbudowane narzędzie matematyczne
Name:		drgeo
Version:	1.1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/ofset/%{name}-%{version}.tar.gz
# Source0-md5:	4ee0a887e819266740867959cbb4095f
Patch0:		%{name}-locale_names.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.ofset.org/en/drgeo
BuildRequires:	ImageMagick-coder-png
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-tools
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gmp-devel >= 3.1.1
BuildRequires:	guile-devel
BuildRequires:	libglade2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	readline-devel >= 4.2
Obsoletes:	drgenius
Obsoletes:	genius
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dr. Geo is a general tool for mathematics, including a mathematical
programming language and evaluator, an euclidian geometry tool, a
2D/3D function grapher and a console calculator. The console
calculator handles multiple precision floating point numbers, infinite
precision integers, complex numbers and matrixes.

%description -l pl.UTF-8
Dr. Geo to narzędzie do rozwiązywania problemów matematycznych.
Zawiera ono matematyczny język programowania, narzędzie do geometrii
euklidesowej, narzędzie do generowania wykresów 2D/3D oraz konsolowy
kalkulator. Kalkulator obsługuje liczby zmiennoprzecinkowe wysokiej
precyzji, liczby całkowite, zespolone oraz macierze.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -f po/no.po

# missing file
[ ! -f glade/drgeo.xpm ]
convert glade/drgeo.{png,xpm}

%build
rm -f acinclude.m4
# doesn't work(?)
#%%{__libtoolize}
#%%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_desktopdir}

install glade/drgeo.png $RPM_BUILD_ROOT%{_pixmapsdir}
%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/texmacs/TeXmacs/plugins/%{name}/
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
