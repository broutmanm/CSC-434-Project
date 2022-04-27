"""
This is a website, that is for injury prevention, it allows user to log in
Author: Kelsie S, Jen B, Jahnavi S, Michael B, Mohamad A
Git Hub: https://github.com/broutmanm/CSC-434-Project
Programming Assignment: Software Engineering Project
Last Changed: April 27, 2022
"""

from website import create_app

# run this file


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)