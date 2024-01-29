# Hangman Game with Python and MySQL Database Connection

Developed by [@Punchulo](https://www.github.com/punchulo)

## Overview

This project combines the classic "Hangman" game implemented in Python with a MySQL database connection and password encryption for enhanced security. By integrating these elements, we create an interactive and secure gaming experience for users, ensuring the integrity of stored data in the database.

## Screenshots

![Hangman](https://github.com/punchulo/PY/assets/63676351/250bde05-3028-4a78-8d28-4778599b170f)

![Game](https://github.com/punchulo/PY/assets/63676351/791d5ec0-3484-4cbe-bc79-f565815005a3)

## Deployment

1. **Create the database [ahorcado](https://github.com/punchulo/PY/blob/main/ahorcado_usuarios.sql).**
2. **Set up a virtual environment and install the required packages.**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    pip install -r requirements.txt
    ```
3. **In the code, provide the necessary information for the MySQL connection and encryption key.**
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

In addition to the core functionality, the project includes the following aspects:

- **Password Encryption:** Utilizes the "hashlib" library to encrypt user passwords. Passwords are hashed using "sha256" from the hashlib module, ensuring secure storage in the database.

- **Database Structure:** The project employs a simple database structure with minimal tables, focusing on essential information for the game. This contributes to maintaining an efficient and purpose-specific database.

- **Game Features:** Implements various features such as user account creation, login, account deletion, random word selection, letter guessing, and the Hangman game itself, providing a comprehensive gaming experience.

- **Python Modules:** Utilizes various Python modules and libraries, including hashlib for encryption, random for word generation, and mysql.connector for MySQL database connection and manipulation.

## Future Enhancements

1. **Multiplayer Mode:** Introduce a multiplayer mode where users can challenge each other to a game of Hangman.

2. **Leaderboard:** Implement a leaderboard to track and display the highest-scoring players.

3. **GUI:** Develop a graphical user interface to enhance the gaming experience.

## 🔗 Links
- [LinkedIn](https://www.linkedin.com/in/pablo-garcia-bermejo-lopez-168020239/)
- [Twitter](https://twitter.com/punchis_0)

## License

This work is licensed under CC BY-NC-SA 4.0. For details, visit [Creative Commons](http://creativecommons.org/licenses/by-nc-sa/4.0/).
