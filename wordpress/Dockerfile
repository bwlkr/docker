FROM alpine:3.8.4

RUN apk add lighttpd php5-common php5-iconv php5-json php5-gd php5-curl php5-xml php5-pgsql php5-mysql php5-imap php5-cgi fcgi php5-zlib wget openrc \
    php5-pdo php5-pdo_pgsql php5-pdo_mysql php5-soap php5-xmlrpc php5-posix php5-mcrypt php5-gettext php5-ldap php5-ctype php5-dom certbot openssl \
    && rm -rf /var/cache/apk/*

#ADD source /var/www/localhost/htdocs

#RUN certbot register -n --agree-tos -m "admin@example.com" \
#    && certbot certonly -n --webroot -w /var/www/localhost/htdocs -d example.com -d www.example.com

RUN mkdir /etc/lighttpd/ssl/ && \
	openssl req -x509 -newkey rsa:4096 -keyout /tmp/key.pem -out /tmp/cert.pem -days 365 -subj '/CN=localhost' -nodes -sha256 && \
	cat /tmp/key.pem /tmp/cert.pem > /etc/lighttpd/ssl/localhost.pem && \
	rm /tmp/key.pem /tmp/cert.pem && \
  chmod 400 /etc/lighttpd/ssl/localhost.pem

COPY config/lighttpd/*.conf /etc/lighttpd/

RUN rc-update add lighttpd default && mkdir -p /run/lighttpd && chown lighttpd /run/lighttpd

#HEALTHCHECK --interval=5m --timeout=3s \
  #  CMD curl -f http://localhost/ || exit 1

EXPOSE 80 443

ENTRYPOINT ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]