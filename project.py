import sys
import sqlite3
from difflib import get_close_matches
from colorama import Fore, init
init(autoreset=True)


def main():
    # call create_database function
    create_database()
    while True:
        try:
            # user prompt
            message = input(f"{Fore.CYAN}\n_User 🥸  : ").strip().lower()
            if message == 'quit':
                sys.exit('The bot shut down ...')
            elif message != "":
                # get response from the database
                bot_response = get_database(message)
                if bot_response:
                    print(f"{Fore.YELLOW}_Bot 🧠 : \n{bot_response}")
                else:
                    print(f"{Fore.YELLOW}_Bot 🧠 : I don't have knowledge about that. Teach me or type 'skip'.")
                    # allow the user to teach the bot new information
                    new_knowledge = input(f"{Fore.CYAN}_User 🥸  : ")

                    if new_knowledge != 'skip':
                        # learn & save new knowledge
                        learn_save_new_knowledge(message, new_knowledge)
                        print(f"{Fore.YELLOW}_Bot 🧠: I learned it 🧪, thank you. ")
                    else:
                        pass
            else:
                print(f"{Fore.YELLOW}_Bot 🧠 : Please say something ... ")


        except KeyboardInterrupt:
            sys.exit('\nExiting bot ...')


def create_database():
    # create database & connection
    connection = sqlite3.connect('data.db')

    # create a cursor
    cursor = connection.cursor()

    #create first table data
    cursor.execute("""CREATE TABLE IF NOT EXISTS data (
                        question text,
                        response text
                )""")

    # commit
    connection.commit()
    # close
    connection.close()

    return connection, cursor


def get_database(message):
    # create database & connection
    connection = sqlite3.connect('data.db')

    # create a cursor
    cursor = connection.cursor()

    # load question data
    cursor.execute("SELECT question from data")

    # fetch all question data
    question_db = cursor.fetchall()

    # convert list of tuple to list of string
    question_database = [''.join(i) for i in question_db]

    # try to find the closest matching question in the database
    best_match = get_close_matches(message, question_database, n=1, cutoff=.6)

    if best_match:
        closet_question = best_match[0]
        # retrieve the closest answer from the database
        cursor.execute("SELECT response FROM data WHERE question= ?", (closet_question,))
        # fetch only 1 answer
        answer = cursor.fetchone()

        if answer:
            return answer[0]

    return None

def learn_save_new_knowledge(question, response):
    # create database & connection
    connection = sqlite3.connect('data.db')

    # create a cursor
    cursor = connection.cursor()

    # insert new knowledge into the database
    cursor.execute("INSERT INTO data VALUES (?, ?)", (question, response))

    # commit
    connection.commit()

if __name__ == "__main__":
    main()
