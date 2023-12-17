import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('services_stocks')

def retrieve_service_sales():
    """
    Get sales data from user input
    """
    print("Welcome to your stocks calculator.\n")
    print("This applications purpose is to work out how much stock should be ordered for the following weeks booked business.")
    print("This can also be used to pull previous weeks data and compare weekly business increases or decreases.\n")
    print("Please start by entering your booked services data for next week.")
    print("Your input should be 3 numbers, all separated by commas.")
    print("For example: 13, 14, 15\n")
    print("This can be reset using the 'Run Programme' button at the top\n")

    user_sales_data = input("Enter data here: ")
    print(f"Your data entry for next weeks service bookings are {user_sales_data}")

retrieve_service_sales()