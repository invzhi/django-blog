# invzhi.com source code

1. Create a Python3 virtualenv:

   ```bash
   $ virtualenv -p python3 venv
   ```

2. Install dependencies:

   ```bash
   $ pip install -r requirements.txt
   ```

3. Create databases:

   ```bash
   createuser -d username
   createdb -O username dbname
   ```

4. Create a superuser:

   ```bash
   $ ./manage.py createsuperuser
   ```

5. Run the `collectstatic` management command:

   ```bash
   $ ./manage.py collectstatic
   ```

   This will copy all files from your static folders into the `STATIC_ROOT` directory.

## Nginx

```nginx
server {
    listen 80;
    server_name example.org;
    access_log  /var/log/nginx/example.log;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  
    location /static/ {
        root /path_to_app/mysite;
    }
}
```