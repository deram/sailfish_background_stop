Name:          background_stop
Version:       0.1
Release:       1
Summary:       Stop terminal application while not visible
Group:         System/Tools
Vendor:        deram
Distribution:  SailfisfOS
Packager:      deram <deram@iki.fi>
URL:           https://github.com/deram/sailfish_background_stop
License:       MIT

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-build
Source:        %{name}.tar.gz

Requires:	bash
Requires:	sed
Requires:	dbus


%prep
%setup -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp bgr_stop.sh $RPM_BUILD_ROOT/%{_bindir}


%description
Program for stopping terminal applications while compositor reports it is not on top. 
Designed for freezing mosh to reserve battery power while in low connectivity locations.


%files
%defattr(-,root,root,-)
%attr(755,root,-) %{_bindir}/bgr_stop.sh
%doc README.md

%changelog
* Wed Mar 23 2017 deram <deram@iki.fi> 0.1
- First build.
