import json
from db import DB   

db = DB("secret_agents.db")

create_alias = """
INSERT INTO agents
( alias_id,  active ) 
VALUES 
( ?, ? )
"""

with open("SEED.json", "r") as seed:
    data = json.load(seed)

    for secret_agents in data:
        db.call_db(create_alias, secret_agents["alias_id"], secret_agents["active"])