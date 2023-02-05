import asyncio
import aiohttp
from config import openai_api_key

async def make_openai_request(prompt):
    async with aiohttp.ClientSession() as session:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}"
        }
        payload = {
        	"model": 'text-davinci-002',
            "prompt": prompt,
            "max_tokens": 1024,
            "temperature": 0.5,
            "n": 1,
            "stop": None,
        }
        async with session.post("https://api.openai.com/v1/completions", headers=headers, json=payload) as response:
            response_json = await response.json()
            return response_json
