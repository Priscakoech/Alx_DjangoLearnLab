# Security Configuration

## HTTPS Configuration
- SECURE_SSL_REDIRECT: Redirects all HTTP traffic to HTTPS.
- SECURE_HSTS_SECONDS: Instructs browsers to use HTTPS exclusively for one year.
- SECURE_HSTS_INCLUDE_SUBDOMAINS: Applies the HSTS policy to subdomains.
- SECURE_HSTS_PRELOAD: Preloads the site in browsers' HSTS lists.

## Secure Cookies
- SESSION_COOKIE_SECURE: Ensures session cookies are transmitted over HTTPS.
- CSRF_COOKIE_SECURE: Ensures CSRF cookies are transmitted over HTTPS.

## Secure Headers
- X_FRAME_OPTIONS: Prevents clickjacking by disallowing iframes.
- SECURE_CONTENT_TYPE_NOSNIFF: Prevents MIME-sniffing attacks.
- SECURE_BROWSER_XSS_FILTER: Enables browser XSS protection.

## Deployment Configuration
- SSL/TLS certificates installed using Let's Encrypt.
- Nginx configured to enforce HTTPS with a 301 redirect from HTTP.
