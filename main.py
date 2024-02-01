from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from router import router as r

app=FastAPI()
connection_data=dotenv_values(".env")

@app.on_event("startup")
def connection_establishment():
    try:
        app.mongodb_client=MongoClient(connection_data["mongo_host"],int(connection_data["mongo_port"]))
        app.database=app.mongodb_client[connection_data["mongo_db"]]
        print("Connection Established !")

    except Exception as e:
        print(f"Exception: {e}") 

@app.on_event("shutdown")
def connection_close():
    try:
        app.mongodb_client.close()

    except Exception as e:
        print(f"Exception: {e}")

app.include_router(r,prefix="/api")
