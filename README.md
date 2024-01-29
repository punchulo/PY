
# Python (connection with MySQL)


"Hangman/Ahorcado" with Python and the connection to a MySQL database, in addition to the implementation of password encryption.

By combining these elements, the creation of a "Hangman/ahorcado" game with Python that connects to a MySQL database is achieved, ensuring the security of passwords through encryption before storage. This comprehensive approach offers an interactive and secure gaming experience for users, while ensuring the integrity of the data stored in the database.
## Screenshots

![ahorcado py](https://github.com/punchulo/PY/assets/63676351/250bde05-3028-4a78-8d28-4778599b170f)


![image](https://github.com/punchulo/PY/assets/63676351/791d5ec0-3484-4cbe-bc79-f565815005a3)


## Deployment

Create the database [ahorcado](https://github.com/punchulo/PY/blob/main/ahorcado_usuarios.sql).

-In the code, you place the necessary information for it to connect."
```bash
mydb = mysql.connector.connect(
    host=" ", --> Host de MySQL(Suele ser localhost)
    user=" ", --> Usuario de MySQL
    password=" ", --> Contraseña de MySQL
    database="ahorcado",
)
```
-Run the .py file.
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pablo-garcia-bermejo-lopez-168020239/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/punchis_0)


## Author

- [@Punchulo](https://www.github.com/punchulo)

## License

[Creative common](https://bind40.com/wp-content/uploads/2023/06/by-nc-sa.eu_.png)
This work is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/
