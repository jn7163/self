## single ip
iptables -t nat -N SHADOWSOCKS
iptables -t nat -A SHADOWSOCKS -p tcp -j REDIRECT --to-port 1081
iptables -t nat -A PREROUTING -p tcp -d 123.123.123.123 -j SHADOWSOCKS
service iptables save
service iptables restart
