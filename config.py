import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the value of a variable
variable_value = os.environ['MY_TOKEN']
