import pyodbc
from runable import main 

def create_connection():
    server = '<your_server_name>'
    database = '<your_database_name>'
    username = '<your_username>'
    password = '<your_password>'

    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    connection = pyodbc.connect(connection_string)

    return connection

def insert_conversation(user_input, bot_response):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('EXEC InsertConversation @UserInput=?, @BotResponse=?', user_input, bot_response)

    connection.commit()
    cursor.close()
    connection.close()

def conversational_ai_loop():
    while True:
        user_input = input('User: ')
        bot_response = ge(user_input)  # Replace with your actual AI logic
        print(f'Bot: {bot_response}')

        insert_conversation(user_input, bot_response)

if __name__ == '__main__':
    conversational_ai_loop()
