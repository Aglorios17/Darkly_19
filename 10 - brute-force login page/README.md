## 10 - brute-force login page
### Flag
B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2

### Reproduce
On the login page we tried to enter an account of someone else using a brute-force attack. For the brute-force attack we used a software called 'Burp Suite'.<br>
Burp can take two lists one of potential logins and one of potential passwords. We used lists found on github's popular repository describing common logins and passwords (https://github.com/danielmiessler/SecLists). Burp will try all the possible combinations by putting them in the appropriate URL ({DARKLY_WEBSITE_URL}/?page=signin&username={LOGIN}&password={PASSWORD}&Login=Login), display them and the result is represented as returned content's length. The good combination of 'admin' and 'shadow' or 'root' and 'shadow' will return the flag and thus a content length that is longer. By ordering on returned content's length we can view the successful combinations with a longer content's length.

Here for the login 'admin' and 'root' the password is 'shadow'.

### Understand
A brute-force attack consists of trying to find all possible login and password combinations possible to be able to login in someone else's account. Sometimes the login is known and only the password is searched. Sometimes lists with common logins and passwords are used or sometimes literally all possible letter combinations are tried which is more time consuming.  

The danger of a brute-force attack is of course an attacker having access to someone else's account on which he can make changes or retrieve sensitive datas. Another danger is if the user uses the same password on different platforms, if this is the case after seizing the user's password the attacker could try to login with that same password on other platforms such as those surrounding finance.

One way of preventing brute-force attacks is to require users for passwords of a minimal strength.<br>
Another way is to use multiple-factor-authentication at least when connecting from a new machine, the most common one being two-factor-authentification often consisting of first a password and second a phone text with a code being send to user's phone number. This is particularly useful in the case whereby the password got discovered by an attacker on another platform and now tries to login on this platform.<br>
The simplest and most effective way of preventing this attack is account lockout, meaning users that try different passwords to login can get blocked after a certain amount of tries.
