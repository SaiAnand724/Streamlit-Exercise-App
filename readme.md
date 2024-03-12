Streamlit Excercise Tracker/Recommender

This application is a test build for working with RDMS (Relational Database Management Systems).

The UI and server middleware is built on the Python streamlit library, 
    the backend utilizes MySQL for user data (Name, dob, email, etc) 
    and MongoDB for project data (Chat message history, user prompts, etc).

Streamlit Docs: https://docs.streamlit.io/library/api-reference

PowerShell prompts
1. python -m venv .venv - sets the virtual environment (name of this venv is .venv)
2. .venv/Scripts/activate - activates virtual environment
    - deactivate - leaves the virtual environment and returns to working directory
3. python -m pip install {dependencies}
    - openai, 'tiktoken', python-dotenv, streamlit, streamlit-authenticator
    - For databases: [MySQL - mysqlclient, SQLAlchemy], [MongoDB - pymongo]
4. python -m streamlit run {streamlit app main python file}