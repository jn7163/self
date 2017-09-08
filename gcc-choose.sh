## default gcc-4.4
yum install gcc -y

## delete default gcc
yum remove gcc cpp -y

## others
cat  << EOF >> /etc/profile
export mygccver="7.1.0"
export mygmpver="6.1.0"
export mympcver="1.0.3"
export mympfrver="3.1.4"
export myislver="0.16.1"
export LD_LIBRARY_PATH="/opt/gcc-${mygccver}/lib:/opt/gcc-${mygccver}/lib64:/opt/gmp-${mygmpver}/lib:/opt/mpc-${mympcver}/lib:/opt/mpfr-${mympfrver}/lib:/opt/isl-${myislver}/lib"
export PATH="$PATH:/opt/gcc-${mygccver}/bin"
export CC=/opt/gcc-${mygccver}/bin/gcc
export CXX=/opt/gcc-${mygccver}/bin/g++
export CPP=/opt/gcc-${mygccver}/bin/cpp
EOF
