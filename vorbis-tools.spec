%global optflags %{optflags} -O3

# (tpg) enable PGO build
%bcond_without pgo

Summary:	Several Ogg Vorbis Tools
Name:		vorbis-tools
Version:	1.4.2
Release:	4
Group:		Sound
License:	GPLv2
Url:		http://www.xiph.org/
Source0:	http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.gz
# (tpg) https://www.audiocheck.net/testtones_highdefinitionaudio.php
Source1:	https://www.audiocheck.net/download.php?filename=Audio/audiocheck.net_hdsweep_1Hz_44000Hz_-3dBFS_30s.wav
Patch0:		vorbis-tools-1.4.2-clang15.patch
Patch4:		vorbis-tools-1.4.0-next_on_SIGUSR1.patch
Patch5:		vorbis-tools-1.2.0-ogg123-play-stdin.patch
# (gc) needed for AM_PATH_PROG_WITH_TEST
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(speex)
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
%if %{with pgo}
export LD_LIBRARY_PATH="$(pwd)"

CFLAGS="%{optflags} -fprofile-generate" \
CXXFLAGS="%{optflags} -fprofile-generate" \
LDFLAGS="%{build_ldflags} -fprofile-generate" \
%configure \
	--enable-vcut

%make_build
cp %{SOURCE1} .
    ./oggenc/oggenc -q 10 *.wav
    ./oggdec/oggdec *.ogg

unset LD_LIBRARY_PATH
llvm-profdata merge --output=%{name}-llvm.profdata $(find . -name "*.profraw" -type f)
PROFDATA="$(realpath %{name}-llvm.profdata)"
rm -f *.profraw

make clean

CFLAGS="%{optflags} -fprofile-use=$PROFDATA" \
CXXFLAGS="%{optflags} -fprofile-use=$PROFDATA" \
LDFLAGS="%{build_ldflags} -fprofile-use=$PROFDATA" \
%endif
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
%doc %{_mandir}/man1/ogg123*
%doc %{_mandir}/man1/oggenc*
%doc %{_mandir}/man1/oggdec*
%doc %{_mandir}/man1/ogginfo*
%doc %{_mandir}/man1/vcut*
%doc %{_mandir}/man1/vorbiscomment*
