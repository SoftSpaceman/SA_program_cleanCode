from sqlite3 import Time
from fastapi import FastAPI
from pydantic import BaseModel




# denna används i api.py för att skapa en ny agent. 
# vi börjar med att lägga till ett gäng aliaser som sedan angeter blri tilldeade. Det kan alltså vara fler aliaser än agenter.


class new_alias(BaseModel):
    id: int = None
    alias_id: str
    active: bool



class new_agent(BaseModel):
    id: int = None
    first_name: str
    last_name: str
    age: int
    total_active_service_time: str #Time  # ska ju automatiskt loggas här när man stänger av funktionen 
    agent_alias: str