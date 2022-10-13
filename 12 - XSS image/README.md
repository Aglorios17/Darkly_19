## 12 - XSS image
### Flag
928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D

### Reproduce
When randomly clicking on index of website, the blue eagle image links towards a page consisting of itself with the following query string `?page=media&src=nsa` which is suspicious.<br>
HTML img tags have the attribute src which can accept an image name or directly a Data URL which is a file represented in string format.<br>
Because the query string equals an image name it could also equal a Data URL. We can transform a malicious script into a Data URL and give that Data URL as src's query parameter value.<br>
We use [this website](https://base64.guru/converter/encode/html) to transform '<script>alert(1);</script>' into a Data URL. Then we transform the query string into `?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=`, which gives us the flag.

### Understand
In this example we did a reflected XSS attack.<br>
Cross-Site Scripting (XSS) is a common web application vulnerability that occurs when a web application returns unsanitized input to the frontend of an application.<br>
Reflected XSS occurs when a user’s input is immediately returned back to the user, it exists as a value in the URL or request. Through phishing, an attacker could disguise using URL shorteners and spread this transformed URL of a legitimate site to unsuspecting victims leading to execution of malicious scripts which could download malware on victim's computer or get their data and send it to the attacker's server for example.

As explained in flag 5 usually sanitization is used to prevent XSS attacks.<br>
Here we had to encode the malicious script using base64 as base64 is used to create Data URLs. The danger here lies in that because the malicious script is encoded it can evade detection and bypass certain forms of sanitization.<br>
Thus to prevent base64 encoded XSS attacks, as in this example, the input must be validated, meaning it should be verified as being one of the possible files and nothing else.

