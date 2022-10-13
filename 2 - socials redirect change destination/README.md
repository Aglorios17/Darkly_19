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

