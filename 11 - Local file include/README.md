## 11 - Local file include
### Flag
b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 

### Reproduce
URL query has the following query parameter "/?page=" when navigating to a page different than the index page. Changing the value of this query parameter we may be able to access unauthorized files.<br>
When changing the value of this query parameter we receive alert boxes with messages. When using values like those '../', '../..' to travel backwards in directories we receive messages inside those alert boxes indicating we are on the right path, until at this value '../../../../../../../' a message indicating we are in the right directory. That is when we try to add 'etc/passwd', an unauthorized file containing sensitive information, as this is a file found in most operating systems.

### Understand
This attack is an LFI (local file include), meaning the attacker is able to include (access or even execute) files that exist on the target web-server's local filesystem.<br>
Usually the danger lies in an attacker being able to retrieve sensitive datas from unauthorized files, as we did here with the commonly found, on most operating systems, '/etc/passwd' file.

To avoid this breach we could prevent the search of files outside of a predefined directory or we could validate the user input to only accept certain predefined files.
