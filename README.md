# Chatbot with SQLite Database

### Video Demo: https://youtu.be/UHkrq8-1W5s

## Description:
This project is a Python-based chatbot that interacts with users, responds to their queries, and learns from them. It uses a SQLite database to store and retrieve information, making it capable of learning new responses over time.

## Features

- **Interactive Prompt:** The chatbot uses a command-line interface to interact with the user. It provides prompts for user input and displays responses.
- **SQLite Database Integration:** Uses SQLite to store and manage a growing dataset of question-response pairs.
- **Learning Capability:** The bot can learn new responses based on user input. If it doesn't know the answer to a question, it prompts the user to provide one, which it then stores in the database.
- **Close Match Search:** Utilizes the `difflib` library to find the closest match to user queries, allowing for flexibility in answering questions that are not exactly as they were taught.
- **Colorful Interface:** Uses the `colorama` library to add color to the command-line interface, enhancing user experience.
- **Graceful Exit:** Allows for a clean exit from the program using either a specific command (`quit`) or a keyboard interrupt.

## How It Works

1. **Database Initialization:** Upon starting, the bot initializes a SQLite database to store question-response pairs.
2. **User Interaction:** The user inputs a question or statement, and the bot searches its database for a close match.
3. **Response and Learning:** If a match is found, the bot responds accordingly. If not, it asks the user to provide an answer and then stores this new information in the database.

## Requirements

- Python
- SQLite3
- `difflib` (for close matches)
- `colorama` (for colored text output)

## Setup and Usage

1. **Installation:** Ensure Python is installed along with necessary libraries.
2. **Running the Bot:** Execute the script to start the chatbot.
3. **Interacting:** Type questions or statements and receive responses. Teach the bot new responses when it encounters unknown queries.
4. **Exiting:** Type 'quit' or use Ctrl+C to exit the application.

## Future Enhancements

- Expanding the knowledge base with more sophisticated data structures.
- Implementing natural language processing (NLP) for more advanced understanding and responses.
- Adding more interactive features or integrating with a graphical user interface (GUI).
