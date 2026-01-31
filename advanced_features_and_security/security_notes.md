# Security Enhancements

## 1. Browser Security Settings
Enabled the following in settings.py:
- SECURE_BROWSER_XSS_FILTER = True
- SECURE_CONTENT_TYPE_NOSNIFF = True
- X_FRAME_OPTIONS = 'DENY'

## 2. Cookie Security
- CSRF_COOKIE_SECURE = True
- SESSION_COOKIE_SECURE = True

## 3. CSRF Protection
All HTML forms updated to include `{% csrf_token %}`.

## 4. SQL Injection Protection
All search/filter logic uses Django ORM with cleaned form data.

## 5. Content Security Policy (CSP)
Added CSP header: `default-src 'self'`
via custom middleware to reduce XSS risks.

## 6. Testing
Manually tested form submissions, invalid input, XSS injection, and CSRF attacks.
