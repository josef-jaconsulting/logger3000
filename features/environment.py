import os
import psycopg2

def before_all(context):
    context.base_url = os.getenv("API_URL", "http://localhost:3000/api")
    
    db_url = os.getenv("DATABASE_URL", "postgresql://postgres:postgrespassword@localhost:5432/carlist_db")
    try:
        context.db_conn = psycopg2.connect(db_url)
    except psycopg2.Error as e:
        print(f"Warning: Could not connect to database for resetting state: {e}")
        context.db_conn = None
        
def after_all(context):
    if hasattr(context, 'db_conn') and context.db_conn:
        context.db_conn.close()

def before_scenario(context, scenario):
    # Clear cars before each scenario
    if hasattr(context, 'db_conn') and context.db_conn:
        with context.db_conn.cursor() as cur:
            cur.execute("DELETE FROM cars")
        context.db_conn.commit()
    
    # Also prepare fresh headers for every scenario
    context.headers = {"Authorization": "Bearer test-token"}
    context.response = None
