%define		_state		stable
%define		orgname		kalzium

Summary:	K Desktop Environment - A Periodic System of Elements database
Summary(pl.UTF-8):	K Desktop Environment - Baza danych Układu Okresowego Pierwiastków
Name:		kde4-kalzium
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	ac65c18b0d72f5dcea928b288bf0c111
URL:		http://www.kde.org/
BuildRequires:	avogadro-devel
BuildRequires:	boost-python-devel
BuildRequires:	eigen
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	ocaml
BuildRequires:	ocaml-facile
BuildRequires:	ocaml-runtime
BuildRequires:	openbabel-devel
Obsoletes:	kalzium < 4.8.0
Obsoletes:	kde4-kdeedu-kalzium < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Periodic System of Elements database. Kalzium provides you with all
kind of information about the PSE (Periodic System of Elements.) You
can lookup lots of information about the elements and also use
visualizations to show them.

%description -l pl.UTF-8
Baza danych Układu Okresowego Pierwiastków. Kalzium dostarcza wszelkie
informacje dotyczące UOP, informacje o pierwiastkach oraz ich
wizualizacje.

%package devel
Summary:	kalzium development files
Summary(pl.UTF-8):	Pliki dla programistów kalzium
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kalzium-devel < 4.8.0

%description devel
kalzium development files.

%description devel -l pl.UTF-8
Pliki dla programistów kalzium.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalzium
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_kalzium.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_didyouknow.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_molmassCalculator.so
%attr(755,root,root) %{_libdir}/kde4/concentrationCalculator.so
%attr(755,root,root) %{_libdir}/kde4/gasCalculator.so
%attr(755,root,root) %{_libdir}/kde4/nuclearCalculator.so

%attr(755,root,root) %ghost %{_libdir}/libcompoundviewer.so.?
%attr(755,root,root) %{_libdir}/libcompoundviewer.so.*.*.*

%attr(755,root,root) %ghost %{_libdir}/libscience.so.?
%attr(755,root,root) %{_libdir}/libscience.so.*.*.*

%{_datadir}/apps/desktoptheme/default/widgets/chalkboard.svg
%{_datadir}/apps/kalzium
%{_datadir}/config/kalzium.knsrc
%{_datadir}/config.kcfg/kalzium.kcfg
%{_datadir}/kde4/services/plasma-dataengine-kalzium.desktop
%{_datadir}/kde4/services/plasma_didyouknow.desktop
%{_datadir}/kde4/services/concentrationCalculator.desktop
%{_datadir}/kde4/services/gasCalculator.desktop
%{_datadir}/kde4/services/nuclearCalculator.desktop
%{_datadir}/kde4/services/plasma-applet-Molmasscalculator.desktop
%{_datadir}/apps/libkdeedu
%{_desktopdir}/kde4/kalzium.desktop
%{_desktopdir}/kde4/kalzium_cml.desktop
%{_iconsdir}/hicolor/scalable/apps/kalzium.svgz
%{_iconsdir}/hicolor/*x*/apps/kalzium.png
%{_mandir}/man1/kalzium.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libkdeedu
%attr(755,root,root) %{_libdir}/libcompoundviewer.so
%attr(755,root,root) %{_libdir}/libscience.so
