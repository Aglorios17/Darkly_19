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


