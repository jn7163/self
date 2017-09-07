iptables -t nat -N SHADOWSOCKS
iptables -t nat -A SHADOWSOCKS -d 123.123.123.123 -j RETURN
iptables -t nat -A SHADOWSOCKS -p tcp -j REDIRECT --to-ports 1081
iptables -t nat -A PREROUTING -p tcp -j SHADOWSOCKS
