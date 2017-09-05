yum install epel-release -y
yum update -y
yum upgrade -y
yum install -y pam-devel.i686 openssl openssl-devel lzo lzo-devel pam pam-devel automake pkgconfig python-setuptools vim git wget m2crypto
yum install -y apr* autoconf automake bison bzip2 bzip2* cloog-ppl compat* cpp curl curl-devel fontconfig fontconfig-devel freetype freetype* freetype-devel gcc gcc-c++ gtk+-devel gd gettext gettext-devel glibc kernel kernel-headers keyutils keyutils-libs-devel krb5-devel libcom_err-devel libpng libpng-devel libjpeg* libsepol-devel libselinux-devel libstdc++-devel libtool* libgomp libxml2 libxml2-devel libXpm* libtiff libtiff* make mpfr ncurses* ntp openssl openssl-devel patch pcre-devel perl php-common php-gd policycoreutils telnet t1lib t1lib* nasm nasm* wget zlib-devel swig python-devel libmcrypt-devel readline-devel
yum -y groupinstall "Development Tools"

curl https://bintray.com/sbt/rpm/rpm | tee /etc/yum.repos.d/bintray-sbt-rpm.repo
yum install sbt -y

wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
# wget https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz
wget https://dl.google.com/android/repository/android-ndk-r14b-linux-x86_64.zip
# wget https://dl.google.com/android/repository/android-ndk-r13-linux-x86_64.zip
unzip sdk-tools-linux-3859397.zip
# tar zxvf android-sdk_r24.4.1-linux.tgz
unzip android-ndk-r14b-linux-x86_64.zip
# unzip android-ndk-r13-linux-x86_64.zip

echo 'export ANDROID_HOME="/root/android-sdk-linux"' >> /etc/profile
echo 'export ANDROID_NDK_HOME="/root/android-ndk-r13"' >> /etc/profile
echo 'export PATH="$PATH:$ANDROID_HOME/tools:$ANDROID_NDK_HOME"' >> /etc/profile
source /etc/profile
echo "y" | android update sdk --filter tools,platform-tools,build-tools-23.0.2,android-23,extra-google-m2repository --no-ui -a

vim /etc/profile
export PATH="$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/23.0.2:$ANDROID_NDK_HOME"
source /etc/profile

echo "y" | android update sdk --filter extra-android-m2repository --no-ui --no-https -a
android update sdk --no-ui

git clone https://github.com/glzjin/shadowsocksr-android

//向vps上传一个jks密钥文件，同时编辑密钥设置

cd shadowsocksr-android
cp local.properties.example local.properties
vim local.properties

git submodule update --init
./build.sh
sbt clean android:package-release
