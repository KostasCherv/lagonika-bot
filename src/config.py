import os
from dotenv import load_dotenv
load_dotenv()

RECIPIENTS = os.environ.get('RECIPIENTS', '')
GOOGLE_EMAIL = os.environ.get('GOOGLE_EMAIL', '')
GOOGLE_PASSWORD = os.environ.get('GOOGLE_PASSWORD', '')
INTERVAL_SECONDS = int(os.environ.get('INTERVAL_SECONDS'))
