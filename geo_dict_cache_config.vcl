DAEMON _OPTS="-a :80\
  -T localhost:3000
  -f /etc/varnish/geo_dict_cache_config.vcl
  -s malloc,256m"
  -S /etc/varnish/secret
