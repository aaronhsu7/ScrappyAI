from flask import Flask, request, jsonify
import json
import spoonacular
import os
from spoonacular.rest import ApiException
from pprint import pprint
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 

# Set up the configuration with API key authorization
configuration = spoonacular.Configuration(
    host="https://api.spoonacular.com"
)
configuration.api_key['apiKeyScheme'] = os.environ.get("API_KEY")

def query_api(query):
    # Create an API client instance
    with spoonacular.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = spoonacular.ProductsApi(api_client)
        number = 10  # Number of results to return
        try:
            # Autocomplete Product Search
            api_response = api_instance.autocomplete_product_search(query, number=number)
            # Extract and print only the product titles
            results = [result.title for result in api_response.results]
            send_to_chat = ""
            for title in results:
                send_to_chat = send_to_chat + (f"- {title}") + '\n'
            print(f"send to chat: {send_to_chat[:-2]}")
            return jsonify({'result': send_to_chat})

        except ApiException as e:
            print(f"Exception when calling ProductsApi->autocomplete_product_search: {e}\n")
        except Exception as e:
            print(f"Unexpected error: {e}\n")

@app.route('/')
def hello_world():
    return jsonify({'result':  "Hello world"})


@app.route('/get_foods', methods=['POST'])
def query_endpoint():
    data = request.json
    print(f"data; {data}")
    foods_list = data.get('content')[9:]
    print(f"foods_list:{foods_list}")
    return query_api(foods_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
