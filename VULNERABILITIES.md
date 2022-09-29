## 1
### Flag
1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0

### Reproduce
Recover password, intercept request and change mail

## 2
### Flag
B9E775A0291FED784A2D9680FCFAD7EDD6B8CDF87648DA647AAF4BBA288BCAB3

### Reproduce
URL parameters are used to link to website's associated socials as I found here by reading HTML source code of index page.<br>
![](/images/3.png)<br>
I took the URL, changed the value in URL parameter 'site=' and browsed to this URL.<br>
![](/images/2.png)<br>

## 3
### Flag
46910D9CE35B385885A9F7E2B336249D622F29B267A1771FBACF52133BEDDBA8
### Reproduce
You can intercept the request and accept other than allowed files in the upload page (/index.php?page=upload#)
![](/images/4.png)<br>
