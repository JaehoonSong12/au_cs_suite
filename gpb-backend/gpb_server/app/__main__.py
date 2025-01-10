# gpb_server.app.__main__.py
from gpb_server.app.cli import app
# from gpb_server.app.gui import app

def entry():
    print("Starting the program from __main__.py...")
    print("CLI Module:", __name__)
    print("Attributes in CLI Module:", dir())
    app.run()

if __name__ == "__main__":
    entry()