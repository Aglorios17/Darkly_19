## 9 - admin cookie
### Flag
df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

### Reproduce
Using google chrome developer tools we can see the HTTP requests we make to the website. In GET requests for a page we can find our cookie in the HTTP request header looking like this `Cookie: I_am_admin=68934a3e9455fa72420237eb05902327`.<br>
When decrypting '68934a3e9455fa72420237eb05902327' with the md5 hash function we get 'false'. When encrypting with md5 'true' we get 'b326b5062b2f0e69046810717534cb09'.<br>
We use 'curl' to make a HTTP GET request towards the website with a change in the 'Cookie' header like this `curl -s -H "Cookie: I_am_admin=b326b5062b2f0e69046810717534cb09" http://172.20.10.4/index.php | grep -i "flag"`. By indicating the cookie to 'I_am_admin=true' with true being encrypted we get the flag.

### Understand
Cookies can automatically log us in as a particular user, by having the admin's cookie the website will consider an unauthorized user as being the admin, enabling the unauthorized user access to the behind the scenes of the website, which he could use to access sensitive data or installing malware on the website.<br>
By having the cookie of another user, someone could connect to this user's session and make changes to it.

To avoid this breach websites should always consider cookies as sensitive data and prevent others from being able to access it.<br>
In this exercise we were able to guess the cookie of the admin by how our own cookie is presented 'I_am_admin=false' with false being encrypted and because the encryption method used, namely md5, is an outdated unsecure encryption method.<br>
Thus instead cookies should always be securely encrypted with the SHA256 hash function for example.<br>
When setting up cookies for security the attributes 'secure' and 'httpOnly' can be set to true. A cookie with the secure attribute is only sent to the server with an encrypted request over the HTTPS protocol. A cookie with the HttpOnly attribute is inaccessible to the JavaScript Document.cookie preventing malicious scripts from collecting it.

Spoofing consists of disguising as a trusted entity for the hacker to get what he wants at the detriment of the victim. Here we spoof by making believe we are admin through cookie manipulation.
