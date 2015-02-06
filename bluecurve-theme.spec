%define iversion 8.0.0
Summary: Bluecurve GNOME theme
Name: bluecurve-theme
Version: 1.0.0
Release: 5
BuildArch: noarch
License: GPL+
Group: Graphical desktop/GNOME
Source0: bluecurve-gnome-theme-%{version}.tar.bz2
Source1: bluecurve-icon-theme-%iversion.tar.bz2
Source2: bluecurve-metacity-theme-%version.tar.bz2
Source3: bluecurve-classic-metacity-theme-%version.tar.bz2
URL: http://www.redhat.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl-XML-Parser
Requires: gtk-engines2 >= 2.13.3-2mdv

%description
This package contains the Bluecurve GNOME meta theme, the icon and metacity
themes.

%prep
%setup -q -n bluecurve-gnome-theme-%version -a 1 -a 2 -a 3

%build
./configure --prefix=%_prefix
make
cd bluecurve-icon-theme-%iversion
./configure --prefix=%_prefix
make
cd ../bluecurve-metacity-theme-%version
./configure --prefix=%_prefix
make
cd ../bluecurve-classic-metacity-theme-%version
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
cd bluecurve-icon-theme-%iversion
%makeinstall_std
touch %buildroot%_datadir/icons/Bluecurve/icon-theme.cache
cd ../bluecurve-metacity-theme-%version
%makeinstall_std
cd ../bluecurve-classic-metacity-theme-%version
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache Bluecurve

%postun
%clean_icon_cache Bluecurve

%files
%defattr(-, root, root)
%doc AUTHORS
%{_datadir}/themes/Bluecurve
%{_datadir}/themes/Bluecurve-classic
%dir %{_datadir}/icons/*Bluecurve*
%{_datadir}/icons/Bluecurve/index.theme
%{_datadir}/icons/*/*.cursortheme
%{_datadir}/icons/*/cursors
%_datadir/icons/Bluecurve/??x??/
%ghost %_datadir/icons/Bluecurve/icon-theme.cache



%changelog
* Tue Jul 26 2011 Götz Waschk <waschk@mandriva.org> 1.0.0-4mdv2012.0
+ Revision: 691690
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-3mdv2011.0
+ Revision: 243355
- rebuild

* Tue Jan 08 2008 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2008.1
+ Revision: 146708
- import bluecurve-theme


* Tue Jan  8 2008 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2008.1
- initial Mandriva package

* Tue Sep 25 2007 Ray Strode <rstrode@redhat.com> - 1.0.0-1
- Initial import, version 1.0.0
