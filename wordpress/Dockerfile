FROM wordpress:5.1-php7.2-apache

ADD WordPress /var/www/html

#RUN certbot register -n --agree-tos -m "admin@example.com" \
#    && certbot certonly -n --webroot -w /var/www/html -d example.com -d www.example.com

HEALTHCHECK --interval=5m --timeout=3s \
    CMD curl -f http://localhost/ || exit 1