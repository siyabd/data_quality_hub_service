import psycopg2
from pydantic import BaseModel


class CreateRequest(BaseModel):
    name: str
    description: str
    dimension: int 
    python: str
    java: str 
    c: str 
    
class Connection1:
    def __init__(self):

        self.connection = psycopg2.connect(database="postgres", user="postgres", password="ylDoAvsR0woWU9I3XfGd", host="dataquality-hub.cd4sy48uq9cv.af-south-1.rds.amazonaws.com", port=5432)
        self.cursor = self.connection.cursor()

    def insertDataDefitions(self,r: CreateRequest):
        add_dq = ("INSERT INTO data_quality_definition "
               "(name, description, dimension, java, c, python,status) "
               "VALUES (%s, %s, %s, %s, %s,%s, %s)")
        data_dq = (r.name, r.description, r.dimension, r.java, r.c, r.python,'A')
        self.cursor.execute(add_dq, data_dq)
        self.connection.commit()

    def getAllDataDefitions(self):
        self.cursor.execute("SELECT a.name,a.description,rd.code,a.java,a.c,a.python,a.ref_data_table_id from data_quality_definition a, reference_data rd where a.dimension = rd.ref_id;")
        columns = ('name', 'description','dimension', 'java', 'c', 'python','refDataTable')
        results = []
        for row in self.cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return results
    
    def getReferenceTables(self):
        self.cursor.execute("SELECT * from reference_data_tables;")
        columns = ('name', 'description','id')
        results = []
        for row in self.cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return results
    
    def getReferenceData(self,table_id):
        query = "SELECT code,value from reference_data where reference_data_table = %s;"

        self.cursor.execute(query, table_id)
        columns = ('code', 'value')
        results = []
        for row in self.cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return results