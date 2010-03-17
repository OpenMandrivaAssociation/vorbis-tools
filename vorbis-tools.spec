%define	name	vorbis-tools
%define version 1.2.0
%define release %mkrel 7
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
# https://trac.xiph.org/changeset/14631
Patch0:		vorbis-tools-1.2.0-flac-resampling-crash.patch
Patch4:		vorbis-tools-1.2.0-next_on_SIGUSR1.patch
Patch5:		vorbis-tools-1.2.0-ogg123-play-stdin.patch
# https://trac.xiph.org/attachment/ticket/1347/vorbis-tools-1.2.0-sec.patch
Patch6:     vorbis-tools-1.2.0-sec.patch
# https://trac.xiph.org/ticket/1357
Patch7:		dont-decode-after-pipe-closes.patch
Patch8:		stop-eating-my-cpu.patch
Patch9:		vorbis-tools-1.2.0-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
%if %{mdkversion} >= 920
Requires:	libogg >= 1.0-1mdk libvorbis >= 1.0-1mdk
%else
Requires:	libogg0 >= 1.0-1mdk libvorbis0 >= 1.0-1mdk
%endif
BuildRequires:	libao-devel >= 0.8.3 libcurl-devel libogg-devel >= 1.0-1mdk zlib-devel liboggflac-devel
BuildRequires:  libspeex-devel
#BuildRequires:  automake1.8
BuildRequires:	openssl-devel libvorbis-devel >= 1.0-1mdk texinfo
# (gc) needed for AM_PATH_PROG_WITH_TEST
BuildRequires:	gettext-devel

%description
This package contains oggenc (encoder), oggdec, ogg123 (command line player)
vorbiscomment (metadata editor) and vcut (cut tool).

Find some free Ogg Vorbis music here: http://www.vorbis.com/music/

%prep
%setup -q -n %{name}-%{theirversion}
%patch0 -p3 -b .flac-resampling-crash
%patch4 -p1 -b .next-on-USR1
%patch5 -p1 -b .ogg123-play-stdin
%patch6 -p1 
%patch7 -p0 -b .pipe-close
%patch8 -p0 -b .stop-eating-cpu
%patch9 -p0

#ACLOCAL=aclocal-1.9 AUTOMAKE=automake-1.9 autoreconf --install --force
touch config.rpath
autoreconf --install --force

%build
%configure2_5x \
	--with-ogg-libraries=%{_libdir} \
	--with-vorbis-libraries=%{_libdir} \
	--with-ao-libraries=%{_libdir} \
	--with-curl-libraries=%{_libdir} \
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
