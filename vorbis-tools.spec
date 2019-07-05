Summary:	Several Ogg Vorbis Tools
Name:		vorbis-tools
Version:	1.4.0
Release:	15
Group:		Sound
License:	GPLv2
Url:		http://www.xiph.org/
Source0:	http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.gz
Patch0:		vorbis-tools-automake-1.13.patch
Patch4:		vorbis-tools-1.4.0-next_on_SIGUSR1.patch
Patch5:		vorbis-tools-1.2.0-ogg123-play-stdin.patch
Patch9:		vorbis-tools-1.2.0-fix-str-fmt.patch
# (gc) needed for AM_PATH_PROG_WITH_TEST
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(ogg)
BuildRequires:  pkgconfig(speex)
BuildRequires:	pkgconfig(vorbis)

%description
This package contains oggenc (encoder), oggdec, ogg123 (command line player)
vorbiscomment (metadata editor) and vcut (cut tool).

Find some free Ogg Vorbis music here: http://www.vorbis.com/music/

%prep
%autosetup -p1

touch config.rpath
autoreconf -fi

%build
%configure \
	--enable-vcut

%make_build

%install
%make_install

%find_lang %{name}

# cleanup
rm -rf %{buildroot}/%{_docdir}/%{name}-%{version}

%files -f %{name}.lang
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
