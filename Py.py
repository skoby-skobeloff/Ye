# pip install huggingface_hub transformers
from transformers import pipeline
import discord
from discord.ext import commands
from discord import app_commands, message
import os
from sympy import sympify

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="echo", description="Echoes back the message")
@app_commands.describe(say="What should I say?")
async def echo(interaction: discord.Interaction, say: str):
    if isinstance(interaction.guild, discord.Guild): 
        if "bot cmds" in interaction.user.roles or interaction.user.id == 788377795620896768:
            await interaction.response.send_message(say)
        else:
            await interaction.response.send_message('missing role "bot cmds"')
    else:
        await interaction.response.send_message(say)

# text generation example
generator = pipeline(
    "text-generation",
    model="meta-llama/Llama-4-Scout-17B-16E-Instruct"
)

result = generator("Hello, explain the solar system", max_new_tokens=50)
print(result[0]['generated_text'])
