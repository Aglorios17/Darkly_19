## 4 - survey vote interception add votes
### Flag
03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA

### Reproduce
On survey page when submitting a vote the HTTP request can be intercepted, at interception the value of the HTTP request header named 'valeur' can be changed so that it is outside the acceptable range, in this case namely above 10.

### Understand
Someone could manipulate the votes by giving extra votes for someone.

This breach could be avoided by having the backend verify if the received vote number is inside the acceptable range, basically validating the user input data.

