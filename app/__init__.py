"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chab1ae7avj5o49lukj0-a.oregon-postgres.render.com",
        database="todo_fth5",
        user="root",
        password="nzYqKw80NqY8B1Hs96zXDBiICKvLuzNX")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
