from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Account(BaseModel):
    accountid: int
    name:str
    balance:float=10.50

@app.get("/v1/accounts/{account-id}")
async def getAccoount(accountid: int)-> Account:

    account = Account(accountid=553355, name="Thiago EStevão")
    return account
