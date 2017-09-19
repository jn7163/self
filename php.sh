ver=7.1.9
yum install openssl-devel bzip2-devel curl-devel gd-devel readline-devel -y
#curl-devel会安装autoconf、automake
wget http://jp2.php.net/distributions/php-${ver}.tar.gz
tar -xzvf php-${ver}.tar.gz
cd php-${ver}
./configure \
--prefix=/opt/php-${ver} \
--enable-fpm \
--with-fpm-user=www \
--with-fpm-group=www \
--with-mysqli=mysqlnd \
--with-pdo-mysql=mysqlnd \
--with-libxml-dir \
--with-mcrypt \
--with-bz2 \
--with-readline \
--with-openssl \
--with-zlib \
--with-mhash \
--with-curl \
--with-libmbfl \
--with-gd \
--with-iconv \
--with-xmlrpc \
--with-jpeg-dir \
--with-freetype-dir \
--with-gettext \
--with-pear \
--enable-mbstring \
--enable-opcache \
--enable-zip \
--enable-inline-optimization \
--enable-shared \
--enable-xml \
--enable-bcmath \
--enable-shmop \
--enable-sysvsem \
--enable-mbregex \
--enable-ftp \
--enable-gd-native-ttf \
--enable-pcntl \
--enable-sockets \
--enable-session \
--enable-sysvmsg \
--enable-sysvsem \
--enable-sysvshm \
--enable-bcmath \
--enable-phar

make && make test && make install
cp /root/php-${ver}/sapi/fpm/php-fpm.conf /opt/php-${ver}/etc/php-fpm.conf
cp /opt/php-${ver}/etc/php-fpm.d/www.conf.default /opt/php-${ver}/etc/php-fpm.d/www.conf
cp /opt/php-${ver}/bin/php /usr/bin/php

cp /root/php-${ver}/php.ini-production /usr/local/lib/php.ini
cp /root/php-${ver}/sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm
chmod +x /etc/init.d/php-fpm
vi /usr/local/etc/php-fpm.conf
最下面 NONE 改为/usr/local
chkconfig php-fpm on
service php-fpm start
