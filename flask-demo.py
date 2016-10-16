from flask import Flask
from app import create_app

app = create_app({'MONGODB_URL': 'mongodb://localhost:27017/'})


if __name__ == '__main__':
    app.run(debug=True)