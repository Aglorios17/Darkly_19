## 1 - recover password interception change email
### Flag
1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0

### Reproduce
On login page you can access the 'I forgot my password page' whereon you can submit a request, this request can be intercepted whereby we can change the value of the request header 'mail'.

We use the software named 'Burp Suite' to enable HTTP request interception.

### Understand
Someone could ask to recover the password from someone else and have the mail send to himself, allowing him to change someone else's password.

This can be avoided by keeping the receiving email address in the backend instead of sending it from the frontend.

