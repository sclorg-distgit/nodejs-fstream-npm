%{?scl:%scl_package nodejs-fstream-npm}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-fstream-npm
Version:    1.1.0
Release:    1%{?dist}
Summary:    An fstream class for creating npm packages
License:    ISC
URL:        https://github.com/isaacs/fstream-npm
Source0:    http://registry.npmjs.org/fstream-npm/-/fstream-npm-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/fstream-npm
cp -pr fstream-npm.js package.json %{buildroot}%{nodejs_sitelib}/fstream-npm

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/fstream-npm
%doc README.md example LICENSE

%changelog
* Wed Sep 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-1
- Updated with script

* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.7-2
- Resolves: rhbz#1334856 , fixes wrong license

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.7-1
- Update

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-1
- New upstream release 1.0.1

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.6-1
- New upstream release 0.1.6

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.1.5-2
- replace provides and requires with macro

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.5-1
- new upstream release 0.1.5

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.4-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.4-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.4-2
- Add support for software collections

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.4-1
- new upstream release 0.1.4

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.3-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.3-1
- new upstream release 0.1.3
- clean up for submission

* Wed Apr 18 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-1
- New upstream release 0.0.6

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-1
- initial package
