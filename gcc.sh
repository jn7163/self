export LD_LIBRARY_PATH=/opt/mpc-1.0.3/lib:/opt/gmp-6.1.0/lib:/opt/mpfr-3.1.4/lib:/opt/isl-0.16.1/lib
rm -rf gcc-7.2.0/test
mkdir gcc-7.2.0/test && cd gcc-7.2.0/test
../configure --prefix=/opt/gcc-7.2.0 -enable-threads=posix -enable-languages=c,c++ --with-gmp=/opt/gmp-6.1.0 --with-mpfr=/opt/mpfr-3.1.4 --with-mpc=/opt/mpc-1.0.3 --with-isl=/opt/isl-0.16.1 -disable-multilib
make -j4 > make.log 2>makeerror.log
make install
cd
