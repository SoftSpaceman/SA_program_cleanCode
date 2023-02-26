
CREATE TABLE
    agents (
        id INTEGER PRIMARY KEY,
        alias_id VARCHAR(50) NOT NULL UNIQUE, -- kaskad funktion som tar bort allt även i nedersta tablen 
        active BOOLEAN NOT NULL
    );

-- Create a table for the agnets

-- Path: secret_agents.sql

CREATE TABLE
    agents_secret_info (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        age INTEGER NOT NULL,
        total_active_service_time TIME NOT NULL,
        agent_alias VARCHAR(50) NOT NULL UNIQUE,
        FOREIGN KEY (agent_alias) REFERENCES agents (id) 
    );

INSERT INTO
    agents ( alias_id, active )
        VALUES ("000", FALSE );


INSERT INTO
    agents_secret_info ( id, first_name, last_name, age, total_active_service_time, agent_alias )
    VALUES (1, "john", "Doe", 40, "48:00:00", "000");

