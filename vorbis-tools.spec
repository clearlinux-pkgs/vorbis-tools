#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vorbis-tools
Version  : 1.4.0
Release  : 1
URL      : http://downloads.xiph.org/releases/vorbis/vorbis-tools-1.4.0.tar.gz
Source0  : http://downloads.xiph.org/releases/vorbis/vorbis-tools-1.4.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: vorbis-tools-bin
Requires: vorbis-tools-locales
Requires: vorbis-tools-doc
BuildRequires : bison
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(ogg)
BuildRequires : pkgconfig(vorbis)

%description
vorbis-tools contains oggenc (an encoder) and ogg123 (a playback tool).
It also has vorbiscomment (to add comments to Vorbis files), ogginfo (to
give all useful information about an Ogg file, including streams in it),
oggdec (a simple command line decoder), and vcut (which allows you to 
cut up Vorbis files).

%package bin
Summary: bin components for the vorbis-tools package.
Group: Binaries

%description bin
bin components for the vorbis-tools package.


%package doc
Summary: doc components for the vorbis-tools package.
Group: Documentation

%description doc
doc components for the vorbis-tools package.


%package locales
Summary: locales components for the vorbis-tools package.
Group: Default

%description locales
locales components for the vorbis-tools package.


%prep
%setup -q -n vorbis-tools-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523044950
%configure --disable-static --without-kate
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1523044950
rm -rf %{buildroot}
%make_install
%find_lang vorbis-tools

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oggdec
/usr/bin/oggenc
/usr/bin/ogginfo
/usr/bin/vcut
/usr/bin/vorbiscomment

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files locales -f vorbis-tools.lang
%defattr(-,root,root,-)

