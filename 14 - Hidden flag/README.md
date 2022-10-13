## 14 - Hidden flag
### Flag
d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466

### Reproduce
On website we can access the robots.txt with '/robots.txt', this indicates us the path '/.hidden' exists. From the path .hidden tons of different paths with files containing content exist. I tried to manually verify all the files in search for a flag without success because it is too much.<br>
Thus we deployed a crawler found in 'resources/crawler.py' to read all the files starting from '/.hidden' and find the flag which it successfully did.

### Understand
A robots.txt file tells search engine crawlers which URLs the crawler can access on a site it is used to keep certain files off Google/browser-searches. Hackers can use it to find hidden files which we did.<br>

We used a crawler to read all the files in '.hidden' and find the flag, a crawler works by reading one page, collecting all the URLs, going to all those URLs and so forth, read all available files until it reads all the available content or reaches a certain goal.

The danger of this breach comes from sensitive content being accessible to unauthorized users. To avoid this breach sensitive data should never be displayed on pages that are accessible to all users.


#### More about Robots.txt
Good :
- useful to limit crawler on the website
- block acces to specific page for the user
- limit the auto-index from some search engine

Bad :
- We can give some idea of secret page or documents to the attacker (disallow: /admin/)
- If you stock sensitive data on the webserver, the attacker can maybe find a link towards a password, ... (never store sensitve data)

Alternative :
- only use Https
- user & pass required (HTTP Basic, CookieAuth, NTLM, etc.)
- limit IPs that can access (Allow/Deny, Host Firewall)
- log access, review logs
- access control
- redirection to a about page (humans.txt)

