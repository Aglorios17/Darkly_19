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
FortyTwo

### Reproduce
On search member page do a union-based SQL query to find database structure with `105 UNION SELECT TABLE_NAME, COLUMN_NAME  FROM Information_schema.columns`. This allows to do union-based SQL queries on the database's content. When demanding this content `105 UNION SELECT Commentaire, countersign  FROM users`, we are asked to decrypt a password as shown below.
![](/images/6.png)<br>
After decrypting the password with the md5 hash function, we get 'FortyTwo'.<br>
Because the first name of the user from whom we decrypted the password is 'Flag' and last name 'GetThe' we consider the decrypted password 'FortyTwo' to be a flag.
  
### Understand
In apps containing a database, SQL injections consists of writing SQL code inside inputs, if this input is subsequently used inside an SQL database query, access is given to the database to unauthorized users.<br>
In this example we use a union-based SQL injection. A union-based injection leverages the power of the SQL keyword UNION. UNION allows us to take two separate SELECT queries and combine their results.

The danger of SQL injections is of course the ability of unauthorized users to interact with the database, most of the time it is used to retrieve sensitive datas such as passwords.

To prevent SQL-injections one can sanitize user inputs, meaning removing/replacing problematic characters that could lead to an SQL injection with safe versions. User inputs can also be validated, meaning if an email is not written in correct format it will be rejected for example, this can also prevent malicious inputs.<br>
However the best way to prevent SQL injections is to use 'prepared statements' inside SQL queries. Prepared statements are predefined SQL queries that take user input and place them into placeholders not considering those as SQL just as arguments for the predefined SQL query.
