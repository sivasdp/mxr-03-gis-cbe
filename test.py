from src.login_credentials.login_credential import login
from utils import about

a=login(login_title="Please login to continue",login_name="Chain Snatching Detection System")
if a == True:
    about()
else:
    print("Something went wrong!")