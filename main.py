from fastapi import BackgroundTasks, FastAPI,Response,Request
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from connection.connection import Connection1, CreateRequest
from models.validateData import default_message, validate_email, validate_gender
app = FastAPI(title="DQ Dimensions API",docs_url="/doc", redoc_url=None)
connection = Connection1 ()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ValidateRequest(BaseModel):
    id: str
    data: str

class SearchRequest(BaseModel):
    name: str
    dimension: int 


@app.post(
    "/validate-dq-dimension"
)
def processDQDimensions(request: ValidateRequest):
    if(request.id == "3"):
        genderList = getReferenceData("4")
        print( validate_gender(genderList,request))
        return validate_gender(genderList,request)
    elif(request.id == "1"):
        return validate_email(request.data)
    
    return default_message()


@app.post(
    "/add-dq-dimension"
)
def processDQDimensions(request: CreateRequest):
    connection.insertDataDefitions(request)

@app.get(
    "/dq-dimensions",
)
def getDimensions(name: str | None = None,dimension: str | None = None):
    print(name)
    print(dimension)
    if(name or dimension):
     return connection.getFilteredDataDefitions(name,dimension)
    
    return connection.getAllDataDefitions()

@app.get(
    "/reference-tables",
)
def getReferenceTables():
    return connection.getReferenceTables()

@app.get(
    "/reference-data/{id}",
)
def getReferenceData(id):
    return connection.getReferenceData(id)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)