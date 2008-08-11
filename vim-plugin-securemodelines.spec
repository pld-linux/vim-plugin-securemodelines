Summary:	Vim plugin: Secure, user-configurable modeline support for Vim
Summary(pl.UTF-8):	Wtyczka Vima: bezpieczna, konfigurowalna obsługa linii trybów dla Vima
Name:		vim-plugin-securemodelines
Version:	20080424
Release:	1
# same as Vim
License:	Charityware
Group:		Applications/Editors/Vim
# Source0Download: http://www.vim.org/scripts/download_script.php?src_id=8598
Source0:	securemodelines.vim
URL:		http://www.vim.org/scripts/script.php?script_id=1876
Requires:	vim-rt >= 4:7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
Vim's internal modeline support allows all sorts of annoying and
potentially insecure options to be set. This script implements a much
more heavily restricted modeline parser that permits only
user-specified options to be set. 

%description -l pl.UTF-8
Wewnętrzna obsługa linii trybów (modeline) Vima pozwala na włączanie
dowolonych uciążliwych i potencjalnie niebezpiecznych opcji. Ten
skrypt jest implementacją dużo bardziej restrykcyjnego analizatora
linii trybów, pozwalającego na ustawianie tylko opcji określonych
przez użytkownika.
 
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
