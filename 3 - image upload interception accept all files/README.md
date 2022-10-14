## 3 - image upload interception accept all files
### Flag
46910D9CE35B385885A9F7E2B336249D622F29B267A1771FBACF52133BEDDBA8

### Reproduce
On the page to upload images, when manually adding files only files who are images get accepted.<br>
But when intercepting the image upload request we can change the request header 'Content-Type' to an image-file-type such as 'image/jpg' instead of a non-image-file-type such as 'application/octet-stream', allowing us to upload files who are not images.
![](/images/4.png)<br>

### Understand
By having the server accept files who are not images it can also accept and execute malicious scripts.

Spoofing consists of disguising as a trusted entity for the hacker to get what he wants at the detriment of the victim. Here we spoof by making believe a file to be of an acceptable type while it is not.<br>
This breach could be avoided by verifying manually the file type using a specialized software for it. Specialized software can also be used to scan the file content for malware. To remove risk further and make sure that files contain no hidden threats, it is best practice to remove any possible embedded objects (malicious scripts hidden inside normal file) by using a methodology called 'content disarm and reconstruction' (CDR). The file content could also be sanitized to replace potentially dangerous characters and prevent malicious scripts.  

