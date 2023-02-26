# nr 2 

# här skapar vi funktioner som gör det möjligt att importa denna class till api.py och köra den därifrån. 
# vi skapar funktioner som gör det möjlgit att exekvera SQL ramverket, aktualisera det och skapa kopplingen till en databas. 


import sqlite3
import os
from typing import Dict, Tuple, Union


class DB:
    db_url: str
#---------------------------------------------SKAPAR DATABSEN NÄR DEN KÖRS I APIfilen
# denna class innehåller 5 funcitoner och dessa två första är skapta så att om databsen
#  INTE finns, skapas den. 



# update och insert är kompliment till call_db och tillåter lite mer avancerad hantering av datbasen via API.

    def __init__(self, db_url: str): # funktionen som säger att om databsen inte finns. skapa den. 
        self.db_url = db_url
        if not os.path.exists(self.db_url): 
            self.__set_up_db() # här ber functionen om funcitonen nedan __set_up_db. som kopplar SQl scriptet med databasen. 


    # denna funktion visar vägen till SQL ramverket(min tilltänkta databasstruktur) och kopplar det med databsen. 
    def __set_up_db(self):
        connection = sqlite3.connect(self.db_url)
        with open(
            "C:/Users/Bananberg/Desktop/FINAL_assignment/API/db.sql", "r"
        ) as file:
            script = file.read() # variabeln script tilldelas filens inehåll och ber den läsa filen.
            connection.executescript(script) # Connection som inehåller sqlite2 ombeds exekvera script variabeln som inehåller vårt sql ramverk och datbaskontakten. 
            connection.commit()
        connection.close()


    def call_db(self, query, *args): # kan det vara så att denna line går att ändra så den innehåller insert här åvan?
        connection = sqlite3.connect(self.db_url)
        cur = connection.cursor()
        result = cur.execute(query, args)  
        data = result.fetchall()
        cur.close()
        connection.commit()
        connection.close()
        return data


    def insert(self, *, table: str, fields: Dict[str, Union[str, bool]]): # var tvungen att fixa så bool accepteras
        keys = ",".join(fields.keys())
        values = "','".join(str(v) for v in fields.values())

        query = f"""
        INSERT INTO {table} (
            {keys}
        ) VALUES (
            '{values}'
        )
        """
        return self.call_db(query)
    
    
    def update(self, *, table: str, where: Tuple[str, str], fields: Dict[str, str]):
        where_key, where_val = where
        field_query = ""
        for key, val in fields.items():
            field_query += f"{key} = '{val}',"
        field_query = field_query[:-1]
        update_query = f"""
        UPDATE {table} SET {field_query} WHERE {where_key} = '{where_val}' 
        """
        
        self.call_db(update_query)
        return self.call_db(update_query)
        









# This code calls the database and executes the given query. 
# THE ORIGINAL  it gave me a error when tryign to add a new alias.... 
    # def call_db(self, query): # kan det vara så att denna line går att ändra så den innehåller insert här åvan?
    #     connection = sqlite3.connect(self.db_url)
    #     cur = connection.cursor()
    #     result = cur.execute(query)  #2 (str(args))    #1  *args)  nr 1 är oginalet. 
    #     data = result.fetchall()
    #     cur.close()
    #     connection.commit()
    #     connection.close()
    #     return data    
  

  ## ORIGNALET jag testar bara att ta bort args för att se om put functionen blir bätter. 
    # def call_db(self, query, *args): # kan det vara så att denna line går att ändra så den innehåller insert här åvan?
    #     connection = sqlite3.connect(self.db_url)
    #     cur = connection.cursor()
    #     result = cur.execute(query, *args)  #2 (str(args))    #1  *args)  nr 1 är oginalet. 
    #     data = result.fetchall()
    #     cur.close()
    #     connection.commit()
    #     connection.close()
    #     return data


