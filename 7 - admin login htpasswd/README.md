## 7 - admin login htpasswd
### Flag
d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

### Reproduce
On website we can access the robots.txt with '/robots.txt', this indicates us the path '/whatever' exists. On /whatever a download link exists named 'htpasswd'. The content of the downloaded file is this 'root:437394baff5aa33daa618be47b75cb49'.<br>
On website we can access the admin login page by adding '/admin' in URL.<br>
Using prior found information (root:437394baff5aa33daa618be47b75cb49), we can successfully enter the admin area.<br>
The password can be decrypted with the md5 hash function so we get 'qwerty123@'.<br>
Now we can login on '/admin' with root as username and qwerty123@ as password.

### Understand
The danger here of course comes from unauthorized users accessing the admin area. The admin password should never be freely available on website.

A robots.txt file tells search engine crawlers which URLs the crawler can access, on a site it is used to keep certain files off Google/browser-searches. Hackers can use it to find hidden files.<br>
'htpasswd' is a flat-file used to store usernames and password for basic authentication. It should never be accessible to unauthorized users.<br>
On this website robots.txt enabled us to find the httpasswd file and subsequently the admin's password.
