from python_utils.import_ import import_global
from python_utils import converters
from social.models import USER
from Book.models import BOOK
import uuid

def generate_id(self):
    print(uuid.uuid1())

def calculate_fine(self,fine_per_day,day_exceeded):
      return day_exceeded*fine_per_day
