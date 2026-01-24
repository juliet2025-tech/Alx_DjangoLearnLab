# HTTPS Deployment Configuration

To enforce HTTPS in production, the application is configured using Django's
built-in security settings such as SECURE_SSL_REDIRECT and HSTS headers.

## SSL/TLS Configuration
In a production environment, HTTPS would be enabled by configuring the web
server (e.g., Nginx or Apache) with an SSL/TLS certificate.

Example using Nginx:
- Obtain an SSL certificate (e.g., via Let's Encrypt)
- Configure Nginx to listen on port 443
- Redirect all HTTP (port 80) traffic to HTTPS

## Django Configuration
Django is configured to:
- Redirect all HTTP requests to HTTPS
- Enforce secure cookies
- Apply HSTS policies to prevent downgrade attacks

These measures ensure secure communication between clients and the server.
