import sqlite3


def get_user_info(username):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    user_info = cursor.fetchone()
    return user_info


# Testing the function
print(get_user_info("john"))
