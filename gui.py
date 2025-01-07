# gui.py

from gpb_server.gui import app

def entry():
    print("Starting the program...")
    app.run()  # Calls the main function from gpb_server/gui.py

if __name__ == "__main__":
    entry()