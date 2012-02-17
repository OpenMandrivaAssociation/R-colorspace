%define modulename colorspace
%define realver 1.0-1
%define r_library %{_libdir}/R/library
%define _requires_exceptions libR.so

Summary:	Color Space Manipulation for R
Name:		R-cran-%{modulename}
Version:	%(echo %{realver} | tr '-' '.')
Release:	%mkrel 1
License:	BSD
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package carries out mapping between assorted color spaces 
including RGB, HSV, HLS, CIEXYZ, CIELUV, HCL (polar CIELUV), CIELAB 
and polar CIELAB. Qualitative, sequential, and diverging color 
palettes based on HCL colors are provided.

%prep
%setup -q -c

%build

R CMD build --no-vignettes %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
