%bcond_with bootstrap
%global packname  colorspace
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1_1
Release:          2
Summary:          Color Space Manipulation
Group:            Sciences/Mathematics
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-1.tar.gz
Requires:         R-methods 
%if %{with bootstrap}
Requires:         R-KernSmooth R-MASS R-kernlab R-mvtnorm
%else
Requires:         R-KernSmooth R-MASS R-kernlab R-mvtnorm R-vcd 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
%if %{with bootstrap}
BuildRequires:    R-KernSmooth R-MASS R-kernlab R-mvtnorm
%else
BuildRequires:    R-KernSmooth R-MASS R-kernlab R-mvtnorm R-vcd 
%endif
BuildRequires:    blas-devel
BuildRequires:    lapack-devel
%rename R-cran-colorspace

%description
Carries out mapping between assorted color spaces including RGB, HSV, HLS,
CIEXYZ, CIELUV, HCL (polar CIELUV), CIELAB and polar CIELAB. Qualitative,
sequential, and diverging color palettes based on HCL colors are provided.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
if [ x$DISPLAY != x ];	then %{_bindir}/R CMD check %{packname}
else			true
fi
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
