from fastapi import BackgroundTasks, FastAPI,Response,Request
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from connection.connection import Connection1


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

class CreateRequest(BaseModel):
    name: str
    description: str
    dimension: int 
    python: str
    java: str 
    c: str 

class SearchRequest(BaseModel):
    name: str
    dimension: int 

@app.post(
    "/add-dq-dimension"
)
def processDQDimensions(request: CreateRequest):
    connection.insertDataDefitions(request)
    print(request)

code = "if substring(orgkey,1,3) = '103' then Last_name exists and len(trim(Last_name)) > 1 and Last_name matches_regex "

@app.get(
    "/dq-dimensions",
)
# searchRequest: SearchRequest
def getDimensions():
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


# @app.get(
#     "/health",
# )
# def health(response: Response):
#     return "test"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)