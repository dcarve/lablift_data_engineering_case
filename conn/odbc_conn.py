
import sqlite3
import pandas as pd



class odbcConn:
    
    def __init__(self, type_odbc):
        
        if type_odbc == 'sqlite':
            self.conn = sqlite3.connect('data/blood_donation_hist.db')


    def execute(self, query):
        
        cur = self.conn.cursor()
        
        cur.execute(query)
        
        cur.close()
        

    def select(self, query):
        
        return pd.read_sql(query, con=self.conn)
    
    def close(self):
        self.conn.close()
        


