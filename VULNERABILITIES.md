## 1 - recover password interception change email
### Flag
1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0

### Reproduce
Recover password, intercept request and change mail.<br>

### Understand
Someone could ask to recover the password from someone else and have the mail send to himself, allowing him to change someone else's password.

## 2 - socials redirect change destination
### Flag
B9E775A0291FED784A2D9680FCFAD7EDD6B8CDF87648DA647AAF4BBA288BCAB3

### Reproduce
URL parameters are used to link to website's associated socials as I found here by reading HTML source code of index page.<br>
![](/images/3.png)<br>
I took the URL, changed the value in query parameter 'site=' and browsed to this URL.<br>
![](/images/2.png)<br>

### Understand
The risk is that someone could set the query parameter 'site=' to a malicious site that downloads malware to the victim's computer, a URL shortener can be used to disguise the crafted URL and this URL can be transmitted through a phishing attack.

This can be avoided by validating the input. In this case only 'facebook', 'instagram' or 'twitter' should be acceptable values, all other values should be rejected.

## 3 - image upload interception accept all files
### Flag
46910D9CE35B385885A9F7E2B336249D622F29B267A1771FBACF52133BEDDBA8
### Reproduce
You can intercept the request and accept other than allowed files in the upload page (/index.php?page=upload#).
![](/images/4.png)<br>

### Understand
By having the server accept files who are not images it can also accept and execute malicious scripts.

Spoofing consists of disguising as a trusted entity for the hacker to get what he wants at the detriment of the victim. Here we spoof by making believe a file to be of an acceptable type while it is not.<br>
This breach could be avoided by not trusting request headers and instead manually verifying the file type.

## 4 - survey vote interception add votes
### Flag
03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA
### Reproduce
You can intercept the request and change the value for the vote in the survey page (/?page=survey#).
![](/images/5.png)<br>

### Understand
Someone could manipulate the votes by giving extra votes for someone.

## 5 - feedback comments XSS attack
### Flag
0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E

### Reproduce
I found this flag by trying on feedback page 'Name' input to do an XSS attack or more specifically a javascript injection.<br>
I wrote `<script>al` which comes from `<script>alert(1);</script>` but input size is limited.<br>
Because protection is given against javascript injections the `<script>` tags are removed and this is when I realized just writing `al` as the name was sufficient to get the flag. Later I also found the letter combination can also be written in the 'Message' input for a flag.<br>
Next to `al` I also found other letter combinations to return a flag:
* a, al, ale, aler, alert
* e, er, ert, 
* r, rt, ri, rip, ript
* t
* i, ip, ipt
* p, pt
* s, sc, scr, scri, scrip, script
* l, le, ler, lert
* c, cr, cri, crip, cript

### Understand
From the found letter combinations to give a flag, `script` and `alert` stand out as those are present in the base XSS attack proof-of-concept payload, namely what I initially tried `<script>alert(1);</script>`.<br>
Thus I conclude this flag comes from XSS attacks which consists of unsanitized input to the frontend.

This XSS attack would be a stored XSS attack, meaning the written feedback containing a malicious script will be send in the database. The danger of this is that all the users that open the feeback page will execute the malicious script which could download malware on victim's computer or get their data and send it to the attacker's server for example.

The main way to prevent an XSS attack is by sanitizing user inputs. Sanitization is the process of removing/replacing problematic characters with safe versions, usually libraries/modules exist that do it automatically. For example '<' '>' could indicate HTML code that tries to inject a javascipt script, thus those characters can be replaced with HTML-encoded versions, this retains the character but removes their capacity to affect the page’s HTML.<br>
User inputs can also be validated, meaning if an email is not written in correct format it will be rejected for example, this can also prevent malicious inputs.

## 6 - member search SQL injection
### Flag
9995cae900a927ab1500d317dfcc52c0ad8a521bea878a8e9fa381b41459b646

### Reproduce
On search member page do a union-based SQL query to find database structure with `105 UNION SELECT TABLE_NAME, COLUMN_NAME  FROM Information_schema.columns`. This allows to do union-based SQL queries on the database's content. When demanding this content `105 UNION SELECT Commentaire, countersign  FROM users`, we are asked to decrypt a password as shown below.
![](/images/6.png)<br>
After decrypting the password with the md5 hash function, we get 'FortyTwo'. Encrypting FortyTwo with the SHA256 function gives us '9995cae900a927ab1500d317dfcc52c0ad8a521bea878a8e9fa381b41459b646' which should be the flag.
  
### Understand
In apps containing a database, SQL injections consists of writing SQL code inside inputs, if this input is subsequently used inside an SQL database query, access is given to the database to unauthorized users.<br>
In this example we use a union-based SQL injection. A union-based injection leverages the power of the SQL keyword UNION. UNION allows us to take two separate SELECT queries and combine their results.

The danger of SQL injections is of course the ability of unauthorized users to interact with the database, most of the time it is used to retrieve sensitive datas such as passwords.

To prevent SQL-injections one can sanitize user inputs, meaning removing/replacing problematic characters that could lead to an SQL injection with safe versions. User inputs can also be validated, meaning if an email is not written in correct format it will be rejected for example, this can also prevent malicious inputs.<br>
However the best way to prevent SQL injections is to use 'prepared statements' inside SQL queries. Prepared statements are predefined SQL queries that take user input and place them into placeholders not considering those as SQL just as arguments for the predefined SQL query.

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

A robots.txt file tells search engine crawlers which URLs the crawler can access on a site it is used to keep certain files off Google/browser-searches. Hackers can use it to find hidden files.<br>
'htpasswd' is a flat-file used to store usernames and password for basic authentication. It should never be accessible to unauthorized users.<br>
On this website robots.txt enabled us to find the httpasswd file and subsequently the admin's password.

## 8 - search image SQL injection
### Fag
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

### Reproduce
On search image page display all the available images with the following boolean-based SQL injection `105 OR 1=1` (it always return true and thus returns all the images). This gives us the image with title 'Hack me ?'.<br>
Retrieve the database's structure to be able to query sensitive data afterwards with this union-based SQL injection `105 UNION SELECT TABLE_NAME, COLUMN_NAME FROM Information_schema.columns`. This gives us a table named list_images with the columns comment, title, url and id.<br>
When querying for the comment column with this union-based SQL injection `105 UNION SELECT comment, title FROM list_images` we get this as comment from the image titled 'Hack me ?' 'If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46'.<br>
When decrypting '1928e8083cf461a51303633093573c46' with the md5 hash function we get 'albatroz' which is the song on the Diomedeidae page. Lastly encrypting albatroz with the SHA256 function gives us 'f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188' which should be the flag.

### Understand
View Flag 6 to learn more about SQL injections.

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

## 10 - brute force login page
### Flag
B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2

### Reproduce
Using Burp Suite or Curl and a list of password (https://github.com/danielmiessler/SecLists) you can brute force the login page url (/?page=signin&username=admin&password=test&Login=Login HTTP/1.1)
Here the admin password is shadow

### Understand
Burp Suite or curl ?
