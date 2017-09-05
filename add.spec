%define debug_install_post %{rpmconfigdir}/find-debuginfo.sh %{?find_debuginfo_opts} “%{_builddir}/%{?buildsubdir}” %{nil}
