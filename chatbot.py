import openai
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Global variable to hold the conversation
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

# Async function to get a response from the bot
async def get_response_bot(user_input):
    # Add the user's input to the conversation
    conversation.append({"role": "user", "content": user_input})
    
    # Call OpenAI's Chat API 
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation
    )
    
    # Extract the assistant's message content
    assistant_message = response.choices[0].message.content
    
    # Add the assistant's response to the conversation
    conversation.append({"role": "assistant", "content": assistant_message})
    
    return assistant_message

# Main function to handle the chat loop
def chat():
    print("You can start chatting with the bot. Type 'exit' to end.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Run the async function to get the response
        response = asyncio.run(get_response_bot(user_input))
        
        # Print the assistant's response
        print(f"Assistant: {response}")

# Entry point for the script
if __name__ == "__main__":
    chat()