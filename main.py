import psycopg2
from config import host, user as db_user, password, db_name

def add_user(login, pas):
   
    connection = None 

    try:
        connection = psycopg2.connect(
            host=host,
            user=db_user,
            password=password,
            database=db_name
        )
        
        cursor = connection.cursor()
        
        insert_query = """
        INSERT INTO test (login, password)
        VALUES (%s, %s)
        RETURNING id;
        """
        
        cursor.execute(insert_query, (login, pas))
        
        user = cursor.fetchone()[0]
        
        connection.commit()
        
        print("User successfully add")
            
    except Exception as _ex:
        print("Error", _ex)
    finally:
        if connection:
            connection.close()
            print("Connection closed")
            

        
