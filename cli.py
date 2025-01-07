# cli.py

from gpb_server.cli import app

def entry():
    print("Starting the program...")
    app.run()  # Calls the main function from gpb_server/cli.py

if __name__ == "__main__":
    entry()