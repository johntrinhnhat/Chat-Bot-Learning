import sqlite3
from project import create_database, get_database, learn_save_new_knowledge

def test_create_database():
    # Test if create_database function creates a database and cursor
    connection, cursor = create_database()
    assert isinstance(connection, sqlite3.Connection)
    assert isinstance(cursor, sqlite3.Cursor)

    # Clean up by closing the connection
    connection.close()

def test_get_database():
    # Test the get_database function with a known question and response
    question = "What is the capital of France?"
    response = "The capital of France is Paris."

    # Learn and save this knowledge
    learn_save_new_knowledge(question, response)

    # Check if the function returns the correct response
    bot_response = get_database(question)
    assert bot_response == response

def test_learn_save_new_knowledge():
    # Test the learn_save_new_knowledge function by inserting new knowledge
    question = "What is the capital of Italy?"
    response = "The capital of Italy is Rome."

    # Insert new knowledge into the database
    learn_save_new_knowledge(question, response)

    # Check if the inserted knowledge exists in the database
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT response FROM data WHERE question=?", (question,))
    result = cursor.fetchone()
    connection.close()

    assert result is not None
    assert result[0] == response
