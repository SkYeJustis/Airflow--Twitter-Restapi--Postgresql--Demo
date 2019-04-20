from sqlalchemy import create_engine

def create_engine_pgsql():
    #postgresql+psycopg2://user:password@hostname:host/database_name
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/postgres',
                           echo=False)
    return engine

def insert_to_db(engine, df, table_name):
    df.to_sql(table_name, con=engine, if_exists="append")