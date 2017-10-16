docker build ./ -t geo_dict_api 
docker stop geo_dict_api || true && docker rm geo_dict_api||true & docker run -p 80:3000  --name geo_dict_api geo_dict_api 
