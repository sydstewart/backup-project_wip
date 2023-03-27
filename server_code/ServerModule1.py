import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
import anvil.media
from anvil.tables import app_tables
import anvil.server
import anvil.tz
import io
import pandas as pd
from datetime import datetime, time , date , timedelta, timezone

@anvil.server.callable
def export_to_csv():
  """Launch a single crawler background task."""
  task = anvil.server.launch_background_task('make_backup')
  
  
@anvil.server.background_task
@anvil.server.callable
def make_backup():
    list_of_tables = ['application_area', 'geography','interface_types','last_date_refreshed','location','suppported_products','test','users']
    folder = app_files.systems_and_customers_tables_backup
    today = datetime.now()
    new_folder = folder.create_folder('systems_backup'+'_'+str(today))
    for item in list_of_tables:
       print(item)
             # rows = getattr(app_tables, 'tablename').search()
       db_name = item
        
       # waitinglist= getattr(app_tables, db_name).search()
       table_csv = getattr(app_tables, db_name).search().to_csv()
       filename0 = item + '_' +str(today)+' .csv'
       new_file0 = new_folder.create_file(filename0, table_csv)


