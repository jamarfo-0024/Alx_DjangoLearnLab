# Security Review

This application was configured to use HTTPS and strict transport security.

## Security Measures Implemented

1. **HTTPS Enforcement**
   - `SECURE_SSL_REDIRECT = True`
   - Forces all HTTP requests to use HTTPS.

2. **HSTS**
   - `SECURE_HSTS_SECONDS = 31536000`
   - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
   - `SECURE_HSTS_PRELOAD = True`

3. **Secure Cookies**
   - `SESSION_COOKIE_SECURE = True`
   - `CSRF_COOKIE_SECURE = True`

4. **Browser Security Headers**
   - X-Frame-Options: DENY
   - X-XSS-Protection enabled
   - nosniff enabled

5. **Forms Protected with CSRF**
   - All POST forms include `{% csrf_token %}`

6. **Deployment Notes**
   - SSL certificates required for production web server.
