%define	name	vorbis-tools
%define version 1.4.0
%define release 4
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
BuildRequires:	curl-devel
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	libao-devel >= 1.0
BuildRequires:	libflac-devel
BuildRequires:  pkgconfig(speex)
BuildRequires:	pkgconfig(vorbis)
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-3mdv2011.0
+ Revision: 670774
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-2mdv2011.0
+ Revision: 608141
- rebuild

* Sun Mar 28 2010 Funda Wang <fwang@mandriva.org> 1.4.0-1mdv2010.1
+ Revision: 528351
- New version 1.4.0
- rediff next_on_SIGUSR1 patch
- drop upstream merged patches

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-7mdv2010.1
+ Revision: 524311
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.0-6mdv2010.0
+ Revision: 427531
- rebuild

* Sat Mar 07 2009 Funda Wang <fwang@mandriva.org> 1.2.0-5mdv2009.1
+ Revision: 351692
- fix str fmt
- rediff patch5
- rediff patch4

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Aug 06 2008 Olivier Blin <oblin@mandriva.com> 1.2.0-4mdv2009.0
+ Revision: 264257
- fix high cpu usage when using piped content (#42337)

* Thu Jul 03 2008 Michael Scherer <misc@mandriva.org> 1.2.0-3mdv2009.0
+ Revision: 231234
- add patch6, fix CVE-2008-1686, and close bug #40465

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2009.0
+ Revision: 225921
- rebuild

* Thu Apr 03 2008 Olivier Blin <oblin@mandriva.com> 1.2.0-1mdv2008.1
+ Revision: 192001
- fix crash when resampling FLAC (upstream changeset 14631)
- 1.2.0 (to fix crash in ogginfo with invalid comments, #30618)
- drop merged patches (flach/curl/conversion)

* Tue Jan 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.1-6mdv2008.1
+ Revision: 152147
- fix character set conversion (bug #36688)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-5mdv2008.0
+ Revision: 74262
- fix build


* Thu Nov 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.1-5mdv2007.0
+ Revision: 89374
- update patch 0
- patch for new curl
- Import vorbis-tools

* Wed Oct 18 2006 Götz Waschk <waschk@mandriva.org> 1.1.1-5mdv2007.1
- patch to support flac 1.1.3

* Mon Nov 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-4mdk
- rebuilt against openssl-0.9.8a

* Thu Oct 13 2005 Götz Waschk <waschk@mandriva.org> 1.1.1-3mdk
- fix description

* Wed Oct 12 2005 Götz Waschk <waschk@mandriva.org> 1.1.1-2mdk
- reenable vcut (thanks to Christopher Kelly)

* Mon Jul 11 2005 Götz Waschk <waschk@mandriva.org> 1.1.1-1mdk
- spec cleanup
- drop patch 6
- rediff patch 4
- source URL
- New release 1.1.1

* Tue Apr 19 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.0.1-7mdk
- rebuild with new libflac

* Fri Jan 21 2005 Abel Cheung <deaddog@mandrake.org> 1.0.1-6mdk
- P5: Allows ogg123 to play stdin -- https://nospam.dyndns.dk/hacks/ogg123/
- P6: Fix speex detection
- Try using configure flags to work around lib64 detection, but keep P0 for now

* Tue Aug 03 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.1-5mdk
- rebuild for new flac

* Thu Jul 01 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.1-4mdk
- rebuild for new curl

* Mon Dec 15 2003 Götz Waschk <waschk@linux-mandrake.com> 1.0.1-3mdk
- fix buildrequires again

* Sun Dec 14 2003 Götz Waschk <waschk@linux-mandrake.com> 1.0.1-2mdk
- add missing buildrequires

* Thu Dec 11 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-1mdk
- new version

