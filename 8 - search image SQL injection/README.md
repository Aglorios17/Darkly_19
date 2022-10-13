## 8 - search image SQL injection
### Fag
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

### Reproduce
On search image page display all the available images with the following boolean-based SQL injection `105 OR 1=1` (it always returns true and thus returns all the images). This gives us the image with title 'Hack me ?'.<br>
Retrieve the database's structure to be able to query sensitive data afterwards with this union-based SQL injection `105 UNION SELECT TABLE_NAME, COLUMN_NAME FROM Information_schema.columns`. This gives us a table named list_images with the columns comment, title, url and id.<br>
When querying for the comment column with this union-based SQL injection `105 UNION SELECT comment, title FROM list_images` we get this as comment from the image titled 'Hack me ?' 'If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46'.<br>
When decrypting '1928e8083cf461a51303633093573c46' with the md5 hash function we get 'albatroz' which is the song on the Diomedeidae page. Lastly encrypting albatroz with the SHA256 function gives us 'f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188' which should be the flag.

### Understand
View Flag 6 to learn more about SQL injections.
