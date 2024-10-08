from fastapi import APIRouter,  HTTPException
from .config import JINA_KEY
import requests

router = APIRouter()

@router.post("/fetch-content/")
def fetch_content(webpage_url: str):
    try:
        # Define the Jina API URL
        api_url = f'https://r.jina.ai/{webpage_url}'

        # Set the headers for the request
        headers = {
            'Authorization': f'Bearer {JINA_KEY}',
            'X-Timeout': '10',
            'X-With-Links-Summary': 'true'
        }

        # Make the GET request to the API
        response = requests.get(api_url, headers=headers)

        # Debugging: Print out the raw response text
        print(response.text)

        # Attempt to parse the response as JSON
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                # If parsing fails, return the raw text content
                return {"content": response.text}
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch content from the API")

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))