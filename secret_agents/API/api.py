# nr 1 
from typing import List # för program filen 
from fastapi import FastAPI
from pydantic import BaseModel # för program filen  
from fastapi.responses import HTMLResponse

from db import DB  
from models import *


# Denna class ska filen program använda sig av för att "aktivera" och "deaktivear" agenter... 
class Program(BaseModel): # en dataklas klassififserar bara avilka attribut en class ska ha och i vilken ordning. 
    first_name: str
    last_name: str
    age: int
    # total_active_service_time: str #Time  # ska ju automatiskt loggas här när man stänger av funktionen 
    agent_alias: str

class update_status(BaseModel):
    id: int 
    active: bool    



#-------TESTKLASS ----------------------
class Todo(BaseModel):
    id: int = None
    titel: str 
    description: str 

#------------------------------------




app = FastAPI()
db = DB("secret_agents.db")

app.agents_status: List[update_status] = []




# ------------ TESTZONE FÖR PROGRAM FILER --------------ROUTES  

# denna lilla kod hjälper att ge en id till varje post utan att va kopplad till databas... se lektion 
# app.curr_id = 1
# app.todos: List[Todo] = []

@app.post("/add_todo")
def add_todo(todo: Todo):
    print(todo)
    return "adds a task"

# lite filtrerad info som kommer visas i programmet när "Show agent detail" väljs. 
@app.get("/program_info")
def get_agents_info():
    query = """
    SELECT first_name, last_name, age, agent_alias FROM agents_secret_info
    """
    agents_info = db.call_db(query)
    return agents_info








# här får vi se om jag lyckas använda för att updatera active via programmet. 
@app.put("/update_agent_status/{agent_to_update}")
def update_agent_status(id: int, agents_to_active: update_status):
    pass                            #todo            #Todo

#------------------------------------------------------------------------------------------------




# DET HÄR ÄR VÅRT HTML LINKTREEE 
@app.get("/", response_class=HTMLResponse)
def root():
    with open("index.html") as f:
        return f.read()




#-----------------CONSTRUCTIONSZONE--- OMBYGGNAD PGA PROGRAM FILENS STURKTUR---- ----------------

@app.get("/secret_agents") # denna funkar men kanske skulle kunna snygga upp resultatet i thunder? 
def get_secret_agents():
    query = """
    SELECT * FROM agents
    """
    data = db.call_db(query) # här storeas queryn som utförs i denna function. 
    agents_status = []
    for element in data: 
        id, active = element
        agents_status.append(update_status(id=id, active=active))
        print(data)
    return agents_status


# ska hämta från TABLE agents 
# @app.get("/secret_agents") # denna funkar men kanske skulle kunna snygga upp resultatet i thunder? 
# def get_secret_agents():
#     query = """
#     SELECT * FROM agents
#     """
#     agents = db.call_db(query)
#     return agents

# return "alla agenters alias och om de är aktiva, alltså allt i table agents" # tex 007 
# funkar i browser och Thunder 


#-------------------------------------------------------------------------------------------


# ska hämta från TABLE agents 
@app.get("/secret_agent/{id}") 
def get_secret_agent(id: int):
    get_agent= """
    SELECT * FROM agents WHERE id = ?
    """
    result = db.call_db(get_agent, id)
    return result 

# return "allt om en hemlig agent från table agents. " 
# funkar i browser och Thunder pga: resutlatet sparas i en varable som kallas på vid return



# ska hämta från TABLE agents_secret_info och agents
@app.get("/agents_secret_info")
def get_agents_info():
    query = """
    SELECT * FROM agents_secret_info
    """
    agents_info = db.call_db(query)
    return agents_info
# return "allt om alla agenter från table agents_secret_info och om de är aktiva från table agents" 
# funkar i browser och Thunder 




@app.get("/agents_secret_info/{id}")
def get_agent_by_id(id: int):
    get_agent = """
    SELECT * FROM agents_secret_info WHERE id = ?
    """
    result = db.call_db(get_agent, id)
    return result
# funkar i browser och Thunder pga: resutlatet sparas i en varable som kallas på vid return



@app.post("/create_alias")
def create_alias(alias: new_alias): # denna ber om en class model. den skapar vi i models och importerar hit.
    print(alias)
    db.insert(table="agents", fields={"alias_id": alias.alias_id, "active": bool(alias.active) })  # insert är en egen funktion som importerast för att kunna lägga till info. Det kanske går att ta bort den helt.
    return "new alias avalible"



@app.post("/create_agent")
def create_agent(new_agent: new_agent):
    print(new_agent)
    db.insert(table="agents_secret_info", fields={"first_name": new_agent.first_name, "last_name": new_agent.last_name, 
                                                    "age": new_agent.age, "total_active_service_time": new_agent.total_active_service_time, "agent_alias": new_agent.agent_alias })
    print("New agent assigned to alias")
    return "new agent assigned to alias"
# # funkar i browser och Thunder 




@app.delete("/delete_agent/{id}") # ORGINALET 
def delete_agent(id: int):
    delete_query = """
    DELETE FROM agents_secret_info WHERE id = ? 
    """
    db.call_db(delete_query, id)
    return "Good bye and thank you for your service"
# # funkar i browser och Thunder 






#--------------------TESTFUNKTION FÖR ATT FÅ EN AGNET RADEARAD VIA PROGRAM FILEN. 
@app.delete("/delete_agent_in_program/{id}") # ORGINALET 
def delete_agent(id: int):
    delete_query = """
    DELETE FROM agents_secret_info WHERE id = ? 
    """
    db.call_db(delete_query, id)
    return "Good bye and thank you for your service"



#------------------------------------------------------------------------------






@app.delete("/delete_alias/{id}") # ORGINALET 
def delete_alias(id: int):
    delete_query = """
    DELETE FROM agents WHERE id = ? 
    """
    db.call_db(delete_query, id)
    return "alias deleted"



# FUNKAR OCH GER RESULTAT! 
@app.put("/update_agent")
def update_agent(update: new_agent): 
    print(update)
    db.update(
        table="agents_secret_info", fields={"first_name": update.first_name, "last_name": update.last_name, "age": str(update.age) ,
                "total_active_service_time": update.total_active_service_time , "agent_alias": update.agent_alias},
                
        where=("id", str(update.id))
    )
    print(new_agent)
    return "updated"
# # funkar i browser och Thunder 


#-------------------------------------------------------------------------------------------
#---------CONSTRUCTION ZONE---------------------FINNISHED-----------CLEAN UP NEEDED---------

# Ska radera från agnets och allt i alla andra tables. 
# @app.delete("/delete_agent/{id}") # ORGINALET 
# def delete_agent(id: int):
#     return "tar bort en agent baserat på id, all info relaterat till detta ska raderas." 
# # funkar i browser och Thunder 
#------------------------------------------------------------------------------------------


#-----------------CONSTRUCTION ZONE ----------------FINISHED--------------CLEAING NEEDED--------
# # Ska lägga till i Agents_secret_info
# @app.post("/create_agent")
# def create_agent(new_agent):
#     return "skapa en agent och lägg i agents_secret_info"
# # ger ERROR  422 Unprocessable Entity
#-----------------------------------------------------------------------------------------------