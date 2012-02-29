# TODO
# - build from source: https://code.google.com/p/closure-stylesheets/wiki/BuildingFromSource
%include	/usr/lib/rpm/macros.java
Summary:	Closure Stylesheets
Name:		closure-stylesheets
Version:	20111230
Release:	1
License:	Apache v2.0
Group:		Applications/WWW
Source0:	https://closure-stylesheets.googlecode.com/files/%{name}-%{version}.jar
# Source0-md5:	eb82b5672843df21ad6fae6eb1547fa1
Source1:	%{name}.sh
Source2:	get-source.sh
URL:		https://code.google.com/p/closure-stylesheets/
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Closure Stylesheets is an extension to CSS that adds variables,
functions, conditionals, and mixins to standard CSS. The tool also
supports minification, linting, RTL flipping, and CSS class renaming.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

# jars
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/*.jar
