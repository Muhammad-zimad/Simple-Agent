# import the required openai module to create Agent
from agent1 import agent, Runner, AsyncOpenAi, set_default_openai_client, det_default_openai_api, set_tracking_disabled

# import the dotenv and od module to run .env file
from dotenv  import load_dotenv
import os

# import asynicio to run async function
import asyncio

# load the api key that is set in .env file 
load_dotenv()
gemini_api_key =os.getenv("GEMINI_API_KEY")

# setup the provider (3rd party)
external_provider = AsyncOpenAi(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

# changing the default provider (openai to gemini)
set_default_openai_client(external_provider)

#setup api communication method
set_default_openai_api("chat_completions")

# Turning of the tracking
set_tracking_disabled(True)

# setup Agent(with Instruction and model) and runnig with async function
def run_global():
    async def main():
        agent = Agent(
            name = "Assistant",
            instructions = "You are good agent.",
            model = "gemini-2.0-flash"
        )
        result = await Runner.run(
            agent,
            "Say hello" ,
        )
        # print the agent output
        print(result)    
    asyncio.run(main())