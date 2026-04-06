import random
from .data_loader import load_data

# load all emails
emails = load_data()

def get_random_email():
    return random.choice(emails)