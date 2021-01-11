import pandas as pd
import cx_Oracle    
connection = cx_Oracle.connect("djk7OraAdmin", "***", "<hostname>/<sid/service>")
cursor = connection.cursor()    
file = r'E:\\djcodeTestCode\\check.xlsx'        
tab_name = "TEST"
tab_exists = """
DECLARE
  v_exst INT;
BEGIN
  SELECT COUNT(*) 
    INTO v_exst 
    FROM cat 
   WHERE table_name = '"""+tab_name+"""' 
     AND table_type = 'TABLE';
  IF v_exst = 1 THEN
     EXECUTE IMMEDIATE('DROP TABLE """+tab_name+"""');
  END IF;   
END;
"""
cursor.execute(tab_exists)    
create_table = """
CREATE TABLE """+tab_name+""" (
       col1 VARCHAR2(50) NOT NULL,
       col2 VARCHAR2(50) NOT NULL,
       col3 VARCHAR2(50) NOT NULL
)    """    
cursor.execute(create_table)     
insert_table = "INSERT INTO "+tab_name+" VALUES (col1,:2,:3)"    
df = pd.read_excel(file)    
df_list = df.fillna('').values.tolist()    
cursor.executemany(insert_table,df_list)    
cursor.close()
connection.commit()
connection.close()