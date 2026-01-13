import csv
import os
import time

import gspread
from googleapiclient.errors import HttpError
from gspread.utils import ValueInputOption
from oauth2client.service_account import ServiceAccountCredentials

BASE = os.path.dirname(os.path.abspath(__file__))
RESOURCE = os.path.join(BASE, "RESOURCES")
SERVICE =
