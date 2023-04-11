import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    Token = "MTA4NTQzMjUzNDc3MjQ4NjE5NA.GN4oWZ.p0U8g6M0aDliYKkGCkYFw-o3GzwX1SCAzSVlLQ"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if channel != 'bot-cmd':
            return

        print(f'{username} said "{user_message}" ({channel})')

        await  send_message(message, user_message, is_private=False)

    client.run(Token)