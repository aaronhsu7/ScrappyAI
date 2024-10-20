from dotenv import load_dotenv
import spoonacular
import os
from spoonacular.rest import ApiException
from pprint import pprint

# Load environment variables from .env file
load_dotenv()

# Set up the configuration with API key authorization
configuration = spoonacular.Configuration(
    host="https://api.spoonacular.com"
)
configuration.api_key['apiKeyScheme'] = os.environ.get("API_KEY")

# Create an API client instance
with spoonacular.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spoonacular.ProductsApi(api_client)
    query = 'pork, carrots'  # The search query
    number = 10  # Number of results to return

    try:
        # Autocomplete Product Search
        api_response = api_instance.autocomplete_product_search(query, number=number)
        
        # Extract and print only the product titles
        results = [result.title for result in api_response.results]
        print("Product Titles:")
        for title in results:
            print(f"- {title}")

    except ApiException as e:
        print(f"Exception when calling ProductsApi->autocomplete_product_search: {e}\n")
    except Exception as e:
        print(f"Unexpected error: {e}\n")
