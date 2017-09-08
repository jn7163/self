curl https://bintray.com/sbt/rpm/rpm | tee /etc/yum.repos.d/bintray-sbt-rpm.repo
yum install sbt -y
yum install java-1.8.0-openjdk java-1.8.0-openjdk-devel -y

wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
wget https://dl.google.com/android/repository/android-ndk-r14b-linux-x86_64.zip
unzip sdk-tools-linux-3859397.zip
mkdir /root/android-sdk && mv /root/tools /root/android-sdk
unzip android-ndk-r14b-linux-x86_64.zip

echo 'export ANDROID_HOME="/root/android-sdk"' >> /etc/profile
echo 'export ANDROID_NDK_HOME="/root/android-ndk-r14b"' >> /etc/profile
echo 'export PATH="$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/26.0.1:$ANDROID_NDK_HOME"' >> /etc/profile
source /etc/profile

echo "y" | android update sdk --filter tools,platform-tools,build-tools-23.0.2,android-23,extra-google-m2repository --no-ui -a
mkdir /root/.android && touch /root/.android/repositories.cfg
/root/android-sdk/tools/bin/sdkmanager "platform;"
/root/android-sdk/tools/bin/sdkmanager "buildtools;26.0.1"
/root/android-sdk/tools/bin/sdkmanager "extra;google;m2repository"
/root/android-sdk/tools/bin/sdkmanager "extra;android;m2repository"

git clone https://github.com/shadowsocksr-backup/shadowsocksr-android

keytool -genkeypair -alias testname -keystore /root/ssr.keystore -sigalg MD5withRSA -keyalg RSA

cd shadowsocksr-android
cp local.properties.example local.properties
vim local.properties

echo "rm -rf /lib64/libc.so.6
LD_PRELOAD=/lib64/libc-2.12.so ln -s /lib64/libc-2.12.so /lib64/libc.so.6" >> /root/default-glibc.sh
chmod +x /root/default-glibc.sh
echo "ver=2.14
rm -rf /lib64/libc.so.6
LD_PRELOAD=/opt/glibc-${ver}/lib/libc-${ver}.so ln -s /opt/glibc-${ver}/lib/libc-${ver}.so /lib64/libc.so.6" >> /root/glibc-2.14.sh
chmod +x /root/glibc-2.14.sh
echo "ver=2.15
rm -rf /lib64/libc.so.6
LD_PRELOAD=/opt/glibc-${ver}/lib/libc-${ver}.so ln -s /opt/glibc-${ver}/lib/libc-${ver}.so /lib64/libc.so.6" >> /root/glibc-2.15.sh
chmod +x /root/glibc-2.15.sh

git submodule update --init
/root/glibc-2.15.sh
./build.sh
/root/glibc-2.14.sh
sbt clean android:package-release
