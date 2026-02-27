import mysql.connector
import os
from dotenv import load_dotenv
from functions import generate_apikey_token

class Clients:

    def list_clients(args):
        load_dotenv()

        con = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT'),
                database=os.getenv('DB_DATABASE'),
                user=os.getenv('DB_USERNAME'),
                password=os.getenv('DB_PASSWORD'))

        cur = con.cursor()
        cur.execute("SELECT * FROM clients")

        result = cur.fetchall()

        for client in result:
            print(client)

    def insert_client(args):
        load_dotenv()

        con = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT'),
                database=os.getenv('DB_DATABASE'),
                user=os.getenv('DB_USERNAME'),
                password=os.getenv('DB_PASSWORD'))

        cur = con.cursor()

        query = "INSERT INTO clients (`name`, `domain`, `mailto`, `active`) VALUES (%s, %s, %s, 1)";
        params = (args.name, args.domain, args.mailto)
        cur.execute(query, params)
        con.commit()

        lastID = cur.lastrowid
        token = generate_apikey_token(40)

        query = "INSERT INTO apikeys (`clientid`, `key`) VALUES (%s, %s)";
        params = (lastID, token)
        cur.execute(query, params)
        con.commit()

        cur.close()
        con.close()

        print("Client "+ args.name +" aangemaakt!")
