import psycopg2
import pandas as pd
from settings import DATABASE, USER

conn = psycopg2.connect(database=DATABASE, user=USER)

df = pd.read_csv('./netflix_content.csv')

# add into the sql DB
def execute_many(conn, df, table):
    """
    Use cursor.executemany() to insert the dataframe
    """
    # update the columns
    clean_df = df.drop('index', axis=1)
    clean_df.rename(columns={'id' : 'netflix_id'}, inplace=True)

    # comma separate the DF column names
    cols = ','.join(list(clean_df.columns))
    # create a list of tuples from the dataframe values
    tuples = [tuple(x) for x in clean_df.to_numpy()]

    query = 'INSERT INTO %s(%s) VALUES (%%s, %%s, %%s, %%s,%%s, %%s,%%s, %%s,%%s, %%s)' % (table, cols)
    cursor = conn.cursor()

    try:
        cursor.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        conn.rollback()
        cursor.close(1)
        return 1
    
    print('Execute many done')
    cursor.close()

execute_many(conn, df, 'content')
