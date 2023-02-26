
import os
from typing import List
import requests
from api import Program

from api import Todo
from api import update_status

# Här ska vi se om vi kan skapa ett script som gör det möjligt att: 
#-----STEG 1----------------

# 1. aktivera en timer. 

# 2. som loggas i en variabel. 

#---------------------------


#---STEG 2------------------

# 1. kunna välja agent 
# 1.2 som startar en timer assosierat med vald agent.

# 2. kunna stänga av timer.
# 3. Tiden stannar och... 
# 5. som loggas på den agenten.

#----------------------------


# att göra_ 

# en meny som man kan välja agent.
# se alla agenters alias (agents table)

# aktivera vald agent. 

# avkativera agent. 

# tiden loggas. 



# vi skapar en funktion som ska ta emot en route och en str. 
def url(route: str): 
    return f"http://127.0.0.1:8000{route}" # detta gör att du slipper skriva url hela tiden. 



print("Hello from program!")


def print_meny(): # visar en meny
    print( 
        """
        0: add todo
        1: get id, alias and active status
        2: Show agent detail
        3: activate agent/pick agent
        4: deactivate agent 
        5: delete agent
        6: exit program
        """
    )
    pass

# ------------------FOKA PÅ ATT FÅ DENNA ATT FUNKA --------
def get_alias(): # visar alla agenter och deras alias # get_todos
    agents_status = []  #todos 
    print("status")
    res = requests.get(url("/secret_agents")) # Här kallas information from routen 
    if not res.status_code == 200:
        return
    data = res.json() # resultatet av inehållet i tables secret agent lagras i data. 
    for status in data:
        status = update_status(**status) # här lägger vi en varabel med modellen i som ska visa datan. 
        print("___________")
        print(f"ID: {status.id}")
        print(f"Active: {status.active}")
        agents_status.append(status)
        return agents_status

# den funkade inte perfekt kan man säga. Jag har skrivit i Teams om vad som jag tror gick fel. 




# ------------------TESTFUNKTION SOM LÄNKAT TILL API FÖR ATT RADERA EN AGENT
def delete_agent():
    print("Delete agent")
    agent_to_delete = input("Id of agent you wish to delete: ")
    if not str.isdigit(agent_to_delete):
        print("Ids are integers")
        return
    res = requests.delete(url(f"/delete_agent_in_program/{agent_to_delete}"))
    print(res.json())
#------------------------------------------------------------------------------


# dena funktion skapades för att filtrera bort lite onödig info i terminalen. 
def get_agents(): # visar alla agenter och deras alias
    print("get agents")
    res = requests.get(url("/program_info")) #
    if not res.status_code == 200:
        return
    print(res.json())


# ----------HIT KOM JAG ----------------- ALLT OVAN FUNKAR --------------------------


# TANKEN MED PROGRAMMET: 
# i en drömvärld... 

# 1. kunna välja agent 
#    - Med knaptryck 1 kunna få fram alla agenters relevanta information från båda tables. 
#       - Detta blev ett större projekt då min datbas logic var dåligt från grunden. 
#         Jag hade inte behövt använda mig av alias i båda tables utan förhålla mig till id som relation endast. 
#         Detta gjorde att alias i det ena table inte stämde med id:et på det andra... 

# 2. med knapptryck två kunna få fram aktiveringsmenyn där programmet ber om alias, alltså tex: "007"
#       - Trycka enter och 007s table går från aktiv status 0 till 1 vilket blir aktiv. (" med tillhörande text ")

# 3. ett par funktioner som skulle vara intergerade med programmet och starta en timmer vid aktivering av agent 
#       - och logga tiden i en column vid av aktivering av agent. 



def activate_agent(agents_status: List[update_status]): 
    print("activate agent")
    agent_to_update = input("type the preferd agent id(singel nr): " )
    if not str.isdigit(agent_to_update):
        print("Id are integer")
        return
    agents_status.index()
    print(agent_to_update)
    # active = input("give activation code, 1: ")
    # activate = update_status(id=id, active=active)
    res = requests.put(url(f"/update_agent_status/{agent_to_update}"), json="")
                                                                        
    print(res.json())
    


def deactivate_agent(): # denna borde då också vara en update route för att ändra active till offline. 
    print("deactivate")
    res = requests.put(url("/update_agent_status/1"))
    print(res.json())
    pass




def main(): # vad vill vi att main ska göra. Våran huvud function 
    agents_status: List[update_status] = [] # todos(ny varable) och classen Todo fast min 
    print_meny()
    choice = input("Please choose your action: ")
    choice = choice.strip() 
    if not str.isdigit(choice): #---------------------------------Dessa hör ihop och gör att vi slipper skriva if elfi osv. 
        print("Please enter a VALID option...")
        return
    

# detta är vad man skulle kunna kalla en switch case eller if elif if elif i den ordningien. 
    match int(choice):
    #-----------------------------------------------------------------------------------------------------------------------  
        case 0:
            add_todo()  
        case 1:
            agents_status = get_alias() #todos och  # get_todo
        case 2:
            get_agents()
        case 3:
            agents_status = get_alias() 
            activate_agent(agents_status) # update_todo 
        case 4: 
            deactivate_agent()
        case 5:
            delete_agent()
        case 6:
            exit()
        case _:
            print("Please enter a VALID choice...")





# denna kod betyder att när denna fil körs blir mitt program filen program.py asignate namet __name__ och kör main om och om igen.
while __name__ =="__main__": # den gör också att vi kan fortsätta programmet efter att ha gjort en grej 
    main()




# DOCS 

# 01:50:00 i videolektion 11
# mitt skript får error att den saknas en string.
# Traceback (most recent call last):
#   File "c:\Users\Bananberg\Desktop\secret_agents_final_cut\API\program.py", line 117, in <module>
#     main()
#   File "c:\Users\Bananberg\Desktop\secret_agents_final_cut\API\program.py", line 101, in main
#     pick_agent()
#   File "c:\Users\Bananberg\Desktop\secret_agents_final_cut\API\program.py", line 69, in pick_agent
#     res = requests.get(url("/get_agent/1"))
#                        ^^^^^^^^^^^^^^^^^^^
# TypeError: url() missing 1 required positional argument: 'str'
# (secret_agents_final_cut) 

# detta kan ju vara för att jag redan har färdiga routes i andra filer som spökar med dessa... Vi får se... Tittar vidare på videon. 
# det kan också vara så att den kallar på apiet men behanldar bara input som är av str än så länge därav felet... 


# byggt en class i api.py som vi kan kalla på här. 
#  - eller. Det jag ska testa senare i morgon ör om get kan funka först, genom att lägga klassen Program i dens funktion 
# 02:10:00 i lektion 11 


# frågan är om jag bara kan byta klass på några routes?? till den klass som är skapat för programmet? 

# klassen Program kallas på här. 


# vi kan behöva addera en klas med fler None som gör det möjligt att bara updatera Actvie till true 