Summary: Program for converting bitmaps to vector graphics
Name: autotrace
Version: 0.31.1
Release: 1
Url: http://autotrace.sourceforge.net
Source: %{name}-%{version}.tar.gz
Copyright: GPL and LGPL
Group: Applications/Graphics
BuildRoot: %{_tmppath}/%{name}-root

%description
AutoTrace is a program for converting bitmaps to vector graphics. The
aim of the AutoTrace project is the development of a freely-available
application similar to CorelTrace or Adobe Streamline. In some
aspects it is already better. Originally being created as a plugin
for the GIMP, AutoTrace is now a standalone program and can be
compiled on any UNIX platform using GCC.


%prep
%setup -q

%build
%configure --without-magick --without-pstoedit
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr/ install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README 
%doc /usr/man/man1/autotrace.1.*

/usr/include/autotrace/autotrace.h
/usr/lib/pkgconfig/autotrace.pc
/usr/include/autotrace/types.h
/usr/lib/libautotrace.*
/usr/include/autotrace/exception.h
/usr/include/autotrace/input.h
/usr/include/autotrace/output.h
/usr/share/aclocal/autotrace.m4
/usr/bin/autotrace-config
/usr/bin/autotrace

%changelog
* Wed Oct 23 2002  Masatake YAMATO<jet@gyve.org>
- make disabled magick and pstoedit.

* Tue Jul  9 2002  Masatake YAMATO<jet@gyve.org>
- Supported shared library and bzip'ed manual.

* Sun May 12 2002  Masatake YAMATO<jet@gyve.org>
- Install output.h.

* Tue Apr 16 2002 Masatake YAMATO<jet@gyve.org>
- Added LGPL to Copyright

* Wed Apr  3 2002 Masatake YAMATO<jet@gyve.org>
- autotrace.1 -> autotrace.1.gz

* Thu Mar  7 2002 Masatake YAMATO<jet@gyve.org>
- Change %description.
- Update files.

* Thu Feb 21 2002 Han-Wen Nienhuys <hanwen@cs.uu.nl>
- Initial build.

