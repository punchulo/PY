# Hangman Game with Python and MySQL Database Connection

Developed by [@Punchulo](https://www.github.com/punchulo)

## Overview

Experience the classic "Hangman" game brought to life in Python, enriched with a MySQL database connection and robust password encryption for heightened security. The amalgamation of these elements ensures an engaging and secure gaming experience, guaranteeing the integrity of stored data in the database.

## Screenshots

![Ahorcado](https://github.com/punchulo/PY/assets/63676351/250bde05-3028-4a78-8d28-4778599b170f)

![Juego](https://github.com/punchulo/PY/assets/63676351/791d5ec0-3484-4cbe-bc79-f565815005a3)


## Deployment

1. **Create the Database: [ahorcado](https://github.com/punchulo/PY/blob/main/ahorcado.sql).**
2. **Set Up the Virtual Environment and Install Dependencies.**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    pip install -r requirements.txt
    ```
3. **Configure MySQL Connection and Encryption Key in the Code.**
    ```python
    import mysql.connector
    from hashlib import sha256

    # MySQL Connection
    mydb = mysql.connector.connect(
        host=" ",  # MySQL Host (usually localhost)
        user=" ",  # MySQL User
        password=" ",  # MySQL Password
        database="ahorcado",
    )

    # Encryption Key (Replace with a secure key)
    encryption_key = "your_secure_key"
    ```

4. **Run the .py file.**

## Additional Notes

Beyond the core functionality, the project encompasses the following features:

- **Password Encryption:** Leverages the "hashlib" library to encrypt user passwords. Passwords undergo hashing using "sha256" from the hashlib module, ensuring secure storage in the database.

- **Database Structure:** Adopts a simple yet effective database structure, with minimal tables focused on essential information for the game. This maintains an efficient and purpose-specific database.

- **Game Features:** Encompasses various aspects such as user account creation, login, account deletion, random word selection, letter guessing, and the Hangman game itself. This provides a holistic and immersive gaming experience.

- **Python Modules:** Harnesses diverse Python modules and libraries, including hashlib for encryption, random for word generation, and mysql.connector for MySQL database connection and manipulation.

## Future Enhancements

1. **Leaderboard:** Implement a dynamic leaderboard to track and showcase the highest-scoring players.

2. **GUI Enhancement:** Develop an intuitive graphical user interface to elevate the overall gaming experience.

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pablo-garcia-bermejo-lopez-168020239/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/punchis_0)

## License

This work is licensed under [![CC BY-NC-SA 4.0](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/).  
View the [license details](http://creativecommons.org/licenses/by-nc-sa/4.0/).

