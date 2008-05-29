# TODO
# - pl
Summary:	Vim plugin: Secure, user-configurable modeline support for Vim
Name:		vim-plugin-securemodelines
Version:	20070518
Release:	3
# same as Vim
License:	Charityware
Group:		Applications/Editors/Vim
# Source0Download: http://www.vim.org/scripts/download_script.php?src_id=7142
Source0:	securemodelines.vim
# Source0-md5:	0efade2902d7b9142d4bf43f2569ec4d
URL:		http://www.vim.org/scripts/script.php?script_id=1876
Requires:	vim-rt >= 4:7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Vim's internal modeline support allows all sorts of annoying and potentially
insecure options to be set. This script implements a much more heavily
restricted modeline parser that permits only user-specified options to be set. 
 
%prep
%setup -q -c -T
install %{SOURCE0} securemodelines.vim

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_vimdatadir}/plugin}
install securemodelines.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/plugin/*
