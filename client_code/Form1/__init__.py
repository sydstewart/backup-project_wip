from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.media
# import anvil.tables as tables
import anvil.tables.query as q
from anvil.google.drive import app_files
from anvil.tables import app_tables
import anvil.google.drive
from datetime import datetime, time , date , timedelta

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def list_tables_button_click(self, **event_args):

    anvil.server.call("export_to_csv")  
    pass


  