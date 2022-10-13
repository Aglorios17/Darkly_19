## 6 - member search SQL injection
### Flag
9995cae900a927ab1500d317dfcc52c0ad8a521bea878a8e9fa381b41459b646

### Reproduce
On search member page do a union-based SQL query to find database structure with `105 UNION SELECT TABLE_NAME, COLUMN_NAME  FROM Information_schema.columns`. This allows to do union-based SQL queries on the database's content. When demanding this content `105 UNION SELECT Commentaire, countersign  FROM users`, we are asked to decrypt a password as shown below.
![](/images/6.png)<br>
After decrypting the password with the md5 hash function, we get 'FortyTwo'. Encrypting FortyTwo with the SHA256 function gives us '9995cae900a927ab1500d317dfcc52c0ad8a521bea878a8e9fa381b41459b646' which should be the flag.
  
### Understand
In apps containing a database, SQL injections consists of writing SQL code inside inputs, if this input is subsequently used inside an SQL database query, access is given to the database to unauthorized users.<br>
In this example we use a union-based SQL injection. A union-based injection leverages the power of the SQL keyword UNION. UNION allows us to take two separate SELECT queries and combine their results.

The danger of SQL injections is of course the ability of unauthorized users to interact with the database, most of the time it is used to retrieve sensitive datas such as passwords.

To prevent SQL-injections one can sanitize user inputs, meaning removing/replacing problematic characters that could lead to an SQL injection with safe versions. User inputs can also be validated, meaning if an email is not written in correct format it will be rejected for example, this can also prevent malicious inputs.<br>
However the best way to prevent SQL injections is to use 'prepared statements' inside SQL queries. Prepared statements are predefined SQL queries that take user input and place them into placeholders not considering those as SQL just as arguments for the predefined SQL query.

