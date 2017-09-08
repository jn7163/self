keytool -genkey -alias testname -keystore /root/ssr.keystore #ssr编译用时，最后一步密码留空即可
keytool -list -keystore /root/ssr.keystore
keytool -delete -keystore /root/ssr.keystore
