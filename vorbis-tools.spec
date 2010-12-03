%define	name	vorbis-tools
%define version 1.4.0
%define release %mkrel 2
%define	theirversion %version

# Define Mandriva Linux version we are building for
%define mdkversion %(perl -pe '/(\\d+)\\.(\\d)\\.?(\\d)?/; $_="$1$2".($3||0)' /etc/mandriva-release)

Name:		%{name}
Summary:	Several Ogg Vorbis Tools
Version:	%{version}
Release:	%{release}
Group:		Sound
License:	GPL
URL:		http://www.xiph.org/
Source:		http://downloads.xiph.org/releases/vorbis/%{name}-%{theirversion}.tar.gz
Patch4:		vorbis-tools-1.4.0-next_on_SIGUSR1.patch
Patch5:		vorbis-tools-1.2.0-ogg123-play-stdin.patch
Patch9:		vorbis-tools-1.2.0-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	curl-devel
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	libao-devel >= 1.0
BuildRequires:	libflac-devel
BuildRequires:  libspeex-devel
BuildRequires:	libvorbis-devel >= 1.3.0
BuildRequires:	texinfo
# (gc) needed for AM_PATH_PROG_WITH_TEST
BuildRequires:	gettext-devel

%description
This package contains oggenc (encoder), oggdec, ogg123 (command line player)
vorbiscomment (metadata editor) and vcut (cut tool).

Find some free Ogg Vorbis music here: http://www.vorbis.com/music/

%prep
%setup -q -n %{name}-%{theirversion}
%patch4 -p1 -b .next-on-USR1
%patch5 -p1 -b .ogg123-play-stdin
%patch9 -p0

#ACLOCAL=aclocal-1.9 AUTOMAKE=automake-1.9 autoreconf --install --force
touch config.rpath
autoreconf --install --force

%build
%configure2_5x \
	--enable-vcut

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

# cleanup
rm -rf %{buildroot}/%{_docdir}/%{name}-%{version}

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc COPYING README ogg123/ogg123rc-example
%{_bindir}/ogg123
%{_bindir}/oggdec
%{_bindir}/oggenc
%{_bindir}/ogginfo
%{_bindir}/vcut
%{_bindir}/vorbiscomment
%{_mandir}/man1/ogg123*
%{_mandir}/man1/oggenc*
%{_mandir}/man1/oggdec*
%{_mandir}/man1/ogginfo*
%{_mandir}/man1/vcut*
%{_mandir}/man1/vorbiscomment*
