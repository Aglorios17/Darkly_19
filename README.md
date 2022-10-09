# Darkly

In this project we need to hack a given website.<br>
Vulnerabilities are described in 'VULNERABILITIES.md'.<br>
Flags refer to vulnerability identifiers in the form of a random code and proves a vulnerability has been found.

https://cdn.intra.42.fr/pdf/pdf/60806/en.subject.pdf

## SETUP
To setup the webiste that has to be hacked follow the following steps:
1. Download 'Virtual Machine' and 'Darkly_i386.iso' (found here https://projects.intra.42.fr/projects/42cursus-darkly).<br>
2. Use VM to launch a virtual machine of type 'linux' and version 'Oracle 64bit'.<br>
3. In settings of this virtual machine go to 'Network' set 'Attached to' to 'Bridged Adapter', in 'Advanced' set 'Promiscuous Mode' to 'Allow All'.<br>
4. In settings of this virtual machine go to 'Storage' and as shown in image click on 'Empty' followed by the right disk and choose the downloaded disk file 'Darkly_i386.iso'.<br>
![](/images/1.png)
(Always click on ok to save virtual machine settings changes.)<br>
5. Launch virtual machine, wait, go to given link.

Possible issues:<br>
* VM does not work on apple M1 chips.
* Launching the VM with iso file does not return correct link when on macOS Montery but it does function on Catalina at least.

## Documentation
https://www.codecademy.com/learn/introduction-to-cybersecurity<br>
https://www.codecademy.com/learn/cybersecurity-for-business<br>
https://www.codecademy.com/learn/defending-express-applications-from-sql-injection-xss-csrf-attacks<br>
https://highon.coffee/blog/lfi-cheat-sheet
