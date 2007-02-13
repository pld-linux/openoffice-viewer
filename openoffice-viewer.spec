Summary:	OOoView - OpenOffice.org file viewer
Summary(pl.UTF-8):	OOoView - przeglądarka plików OpenOffice.org
Name:		openoffice-viewer
Version:	0
Release:	0.1
License:	limited/closed source (it will be made available soon under GPL)
Group:		X11/Applications
Vendor:		The University of the Philippines
Source0:	OpenOffice_orgViewer.zip
# Source0-md5:	2b0071f01220a3cae7428789ccb83162
URL:		http://www.engg.upd.edu.ph/~ooview/
BuildRequires:	unzip
Requires:	jre >= 1.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In 2003, the group of Christine Bejerasco, Cipriano Consolacion Jr.,
and Raquel Tarroza, under the supervision of Prof. R.Feria, have
created a prototype of an OpenOffice.org file viewer. The viewer,
called OOoView, was written in Java to ensure that it runs on any
platform with a proper Java Virtual Machine. This application allows
users to view OpenOffice.org files without installing OpenOffice.org
or StarOffice.

The University of the Philippines is releasing the limited version
here. It is limited because the source is not yet made available.
However, it will be made available soon under GPL.

%description -l pl.UTF-8
W 2003 roku grupa składająca się z Christine Bejerasco, Cipriano
Consolacion Jr. i Raquela Terrozy pod kierunkiem prof. R. Ferii
stworzyła prototyp przeglądarki plików OpenOffice.org. Przeglądarka o
nazwie OOoView została napisana w Javie, aby zapewnić działanie na
każdej platformie z właściwą maszyną wirtualną Javy. Ta aplikacja
pozwala użytkownikom oglądać pliki OpenOffice.org bez instalowania
OpenOffice.org ani StarOffice'a.

Ten pakiet zawiera wersję ograniczoną wydaną przez Uniwersytet
Filipiński. Jest ograniczona, ponieważ źródła jeszcze nie zostały
udostępnione; jednak ma być wkrótce udostępniona na licencji GPL.

%prep
%setup -q -c

%build
cat > oocalc-viewer <<EOF
#!/bin/sh
java -jar %{_javadir}/Calc.jar
EOF

cat > ooimpress-viewer <<EOF
#!/bin/sh
java -jar %{_javadir}/Impress.jar
EOF

cat > oowriter-viewer <<EOF
#!/bin/sh
java -jar %{_javadir}/Writer.jar
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}

install {Calc,Impress,Writer}.jar $RPM_BUILD_ROOT%{_javadir}
install oo{calc,impress,writer}-viewer $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oo*viewer
%{_javadir}/*.jar
