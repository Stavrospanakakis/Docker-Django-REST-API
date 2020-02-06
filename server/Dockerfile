FROM ubuntu:18.04

# Install apache.
RUN apt-get update && apt-get install -y --no-install-recommends apache2 libapache2-mod-qos ca-certificates && \
  apt-get remove make && apt-get install make && \
  apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && \
  a2enmod rewrite proxy proxy_http headers proxy_wstunnel

# Set server name.
RUN echo 'ServerName localhost' >> /etc/apache2/apache2.conf

EXPOSE 80 443

CMD ["/usr/sbin/apachectl", "-DFOREGROUND"]