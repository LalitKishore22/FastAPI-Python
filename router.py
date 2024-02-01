from fastapi import APIRouter, Request, Body
from fastapi.encoders import jsonable_encoder
from typing import List
from models import usermodel,updatemodel,deletemodel


router=APIRouter()

@router.get("/getdata", response_model=List[usermodel])
def get_Data(request: Request):
    try:
        return list(request.app.database["Users"].find())
    except Exception as e:
        print(e)

@router.post("/insertdata")
def insert_data(request: Request, data: usermodel=Body()):
    try:
        request.app.database["Users"].insert_one(jsonable_encoder(data))
        return {"Message":"Insertion successful."}
    except Exception as e:
        print("Error in data Entry.")
        return{"Error": e.args[0]}

@router.put("/updatedata")
def update_data(request: Request, data: updatemodel=Body()):
    try:
        data=jsonable_encoder(data)
        update_data = {k: v for k, v in data.items() if v is not None}
        request.app.database["Users"].find_one_and_update(
            {"ph_no":data.get("ph_no")},
            {'$set':update_data}
        )
        return{"Update":"Success"}
    except Exception as e:
        print("Error in data update")
        return{"Error":e.args[0]}

@router.delete("/deletedata")
def delete_data(request: Request, data: deletemodel=Body()):
    try:
        request.app.database["Users"].delete_one(jsonable_encoder(data))
        return {"Message":"Data deleted successfully !"}
    except Exception as e:
        print("Error in deletion")
        return{"Error":e.args[0]}