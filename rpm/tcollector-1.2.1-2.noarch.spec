# File generated by Makefile, do not edit
# Put the RPM in the current directory.
%define _rpmdir .
# Don't check stuff, we know exactly what we want.
%undefine __check_files
BuildArch:      noarch
Name:           tcollector
Group:          System/Monitoring
Version:        1.2.1
Release:        2
Distribution:   buildhash=a399b1add09112b8806bfe534b2e51dc7c05f7ad
License:        LGPLv3+
Summary:        Data collection framework for OpenTSDB
URL:            http://opentsdb.net/tcollector.html
Provides:       tcollector = 1.2.1-2_a399b1a
Requires:       python(abi) = 2.7

# Disable the stupid stuff rpm distros include in the build process by
# default:
#   Disable any prep shell actions. replace them with simply 'true'
%define __spec_prep_post true
%define __spec_prep_pre true
#   Disable any build shell actions. replace them with simply 'true'
%define __spec_build_post true
%define __spec_build_pre true
#   Disable any install shell actions. replace them with simply 'true'
%define __spec_install_post true
%define __spec_install_pre true
#   Disable any clean shell actions. replace them with simply 'true'
%define __spec_clean_post true
%define __spec_clean_pre true
# Leave the --buildroot behind after building the RPM, so we can build more.
%clean true
# The rest of this file is generated by Makefile
%post
if [ "$1" = 1 ]; then
  chkconfig --add tcollector
  chkconfig tcollector on
  service tcollector start
fi
%preun
if [ "$1" = 0 ]; then
  service tcollector stop
  chkconfig tcollector off
  chkconfig --del tcollector
fi
%files
%dir "/opt/tcollector/collectors/0"
"/opt/tcollector/collectors/0/dfstat.py"
"/opt/tcollector/collectors/0/dfstat.pyc"
"/opt/tcollector/collectors/0/ifstat.py"
"/opt/tcollector/collectors/0/ifstat.pyc"
"/opt/tcollector/collectors/0/iostat.py"
"/opt/tcollector/collectors/0/iostat.pyc"
"/opt/tcollector/collectors/0/netstat.py"
"/opt/tcollector/collectors/0/netstat.pyc"
"/opt/tcollector/collectors/0/procnettcp.py"
"/opt/tcollector/collectors/0/procnettcp.pyc"
"/opt/tcollector/collectors/0/procstats.py"
"/opt/tcollector/collectors/0/procstats.pyc"
"/opt/tcollector/collectors/0/smart-stats.py"
"/opt/tcollector/collectors/0/smart-stats.pyc"
"/opt/tcollector/collectors/__init__.py"
"/opt/tcollector/collectors/__init__.pyc"
%dir "/opt/tcollector/collectors/lib"
"/opt/tcollector/collectors/lib/__init__.py"
"/opt/tcollector/collectors/lib/__init__.pyc"
"/opt/tcollector/collectors/lib/utils.py"
"/opt/tcollector/collectors/lib/utils.pyc"
"/opt/tcollector/tcollector.py"
"/opt/tcollector/tcollector.pyc"
%attr(755, -, -) "/etc/init.d/tcollector"
%changelog
* Tue Aug 26 2014 Kieren Hynd <kieren.hynd@ticketmaster.co.uk> 1.0.3-1
- Parameter for reconnect-interval, clean .pyc's on startup, stop stripping hostnames, add some start runlevels

* Mon Jun 30 2014 Stuart Warren <stuartwarren@ntlworld.com> 1.0.2-1
- Allow setting of extra tags, lists of tsd hosts, and other logfile options.

* Sat Jan 19 2013 Benoit 'tsuna' Sigoure <tsunanet@gmail.com> 1.0.1-1
- Fix the default value of $TCOLLECTOR in init.d script.

* Sun Oct 16 2011 Benoit 'tsuna' Sigoure <tsuna@stumbleupon.com> 1.0.0-1 
- Initialize release of tcollector as an EOS module.
%description
tcollector is a framework to collect data points and store them in OpenTSDB.
It allows you to write simple collectors that it'll run and monitor.  It also
handles the communication with the TSDs.

For more info, see

http://www.opentsdb.net/tcollector.html
