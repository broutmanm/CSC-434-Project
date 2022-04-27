from website import create_app
# okay
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)