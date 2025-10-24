import os
from dotenv import load_dotenv

# Load environment variables from a .env file for local development
load_dotenv()

# Fetch the API key from the environment
LINKUP_API_KEY = os.getenv("LINKUP_API_KEY")

# Fail-fast validation: Ensure the API key is set
if not LINKUP_API_KEY:
    raise ValueError("A LINKUP_API_KEY environment variable is required.")