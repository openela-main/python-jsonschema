# Created by pyp2rpm-0.4.2
%global pypi_name jsonschema

Name:           python-%{pypi_name}
Version:        2.6.0
Release:        4%{?dist}
Summary:        An implementation of JSON Schema validation for Python

License:        MIT
URL:            http://pypi.python.org/pypi/jsonschema
Source0:        https://files.pythonhosted.org/packages/source/j/jsonschema/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-mock

# avoid functools32, vcversioner
Patch0: avoid-unpackaged-for-jsonschema-2.6.0.patch

Patch1: test-sys-executable.patch

%description
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        An implementation of JSON Schema validation for Python %{python3_version}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%prep
%setup -q -n %{pypi_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%py3_build


%install
%py3_install
mv %{buildroot}%{_bindir}/jsonschema %{buildroot}%{_bindir}/jsonschema-3

%check
%{__python3} -m nose -v

%files -n python%{python3_pkgversion}-%{pypi_name}
%license COPYING
%doc README.rst
%{_bindir}/jsonschema-3
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Wed May 30 2018 Petr Viktorin <pviktori@redhat.com> - 2.6.0-4
- Drop the Python2 subpackage
  https://bugzilla.redhat.com/show_bug.cgi?id=1584189
- Use sys.executable rather than unversioned "python" in tests

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Jan Beran <jberan@redhat.com> 2.6.0-1
- Update to 2.6.0
- Fix of missing Python 3 version executables

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.5.1-4
- Rebuild for Python 3.6

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.5.1-3
- Enable python3 builds for EPEL (bug #1395653)
- Ship python2-jsonschema
- Modernize spec
- Use %%license

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 26 2016 Lon Hohberger <lhh@redhat.com> 2.5.1-1
- Update to 2.5.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild


* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 2.4.0-3
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Sep 06 2014 Alan Pevec <apevec@redhat.com> - 2.4.0-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 10 2014 Pádraig Brady <pbrady@redhat.com> - 2.3.0-1
- Latest upstream

* Tue Feb 04 2014 Matthias Runge <mrunge@redhat.com> - 2.0.0-3
- fix %%{? issues in spec

* Thu Oct 17 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.0.0-2
- add python3 subpackage (#1016207)
- add %%check

* Fri Aug 16 2013 Alan Pevec <apevec@redhat.com> 2.0.0-1
- Update to 2.0.0 release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Pádraig Brady <P@draigBrady.com> - 1.3.0-1
- Update to 1.3.0 release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Pádraig Brady <P@draigBrady.com> - 0.2-1
- Initial package.
