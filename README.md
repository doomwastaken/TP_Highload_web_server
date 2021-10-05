
```
git clone https://github.com/init/http-test-suite.git
cd http-test-suite

docker build -t server https://github.com/doomwastaken/TP_Highload_web_server.git
docker run -p 80:80 -v /etc/httpd.conf:/etc/httpd.conf:ro -v /var/www/html:/var/www/html:ro --name server -t server

./httptest.py
```

