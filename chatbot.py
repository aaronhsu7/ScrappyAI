from dotenv import load_dotenv
import spoonacular,os
from spoonacular.rest import ApiException
from pprint import pprint

load_dotenv()

# Defining the host is optional and defaults to https://api.spoonacular.com
# See configuration.py for a list of all supported configuration parameters.
configuration = spoonacular.Configuration(
    host = "https://api.spoonacular.com"
)

# Configure API key authorization: apiKeyScheme
configuration.api_key['apiKeyScheme'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyScheme'] = 'Bearer'


# Enter a context with an instance of the API client
with spoonacular.ApiClient(configuration) as api_client:
    api_instance = spoonacular.DefaultApi(api_client)
    analyze_recipe_request = spoonacular.AnalyzeRecipeRequest() 
    language = 'en' 
    include_nutrition = True 
    include_taste = True

    try:
        api_response = api_instance.analyze_recipe(analyze_recipe_request, language=language, include_nutrition=include_nutrition, include_taste=include_taste)
        print("The response of DefaultApi->analyze_recipe:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->analyze_recipe: %s\n" % e)
