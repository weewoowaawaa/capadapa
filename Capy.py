import nextcord
import requests
import datetime
from nextcord.ext import application_checks, commands
from nextcord import ChannelType, Interaction
import cooldowns
from cooldowns import SlashBucket, CallableOnCooldown

# Make everything work lol
bot = commands.Bot(command_prefix="!!", intents = nextcord.Intents.all(), help_command=None)

# Gets raw content of key and code from pastebin

url2 = "https://pastebin.com/raw/xQWMxehh"
e = requests.get(url2)
pasteCode = e.text


url = "https://pastebin.com/raw/N8ENYjnX"
r = requests.get(url)
pasteKey = r.text

# Get Date
now = datetime.datetime.now().strftime('%H:%M')

# prints a message when bot is online and sets the status
@bot.event
async def on_ready():
    print("Logged in and ready.")
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="for /tut"))
    print("")

# tutorial on how to completely use free version
@bot.slash_command(name="tut", description="Full tutorial for using capysploit. Bot and all.")
async def tut(interaction: nextcord.Interaction):
    embed = nextcord.Embed(title="Capysploit Tutorial", url="https://streamable.com/fe08me", description="The link above is a full tutorial on how to fully use the menu. This is a rushed tut lol. if anyone else wants to make one, by all means be my guest.", color=nextcord.Color.blue())
    embed.set_footer(text=f"Bot coded by heqds • Today at {now}")
    await interaction.send(embed=embed)

# alternative to /tut
@bot.event
async def on_message(message):
    if message.content.startswith("wrong key"):
        embed = nextcord.Embed(title="Capysploit Tutorial", url="https://streamable.com/fe08me", description="The link above is a full tutorial on how to fully use the menu. This is a rushed tut lol. if anyone else wants to make one, by all means be my guest.", color=nextcord.Color.blue())
        embed.set_footer(text=f"Bot coded by heqds • Today at {now}")

        await message.channel.send("Use the below link to get the correct key and full tutorial.")
        await message.channel.send(embed=embed)

@bot.event
async def on_message(message):
    if message.content.startswith("You do not have any verification pending."):
        embed = nextcord.Embed(title="Capysploit Tutorial", url="https://streamable.com/fe08me", description="The link above is a full tutorial on how to fully use the menu. This is a rushed tut lol. if anyone else wants to make one, by all means be my guest.", color=nextcord.Color.blue())
        embed.set_footer(text=f"Bot coded by heqds • Today at {now}")

        await message.channel.send("Use the below link to get the correct key and full tutorial.")
        await message.channel.send(embed=embed)

# when someone does !verify {key} they get a tutorial on how to do stuff
@bot.event
async def on_message(message):
    if message.content.startswith("!verify"):
        user = nextcord.User
        embed = nextcord.Embed(title="Capysploit Tutorial", url="https://streamable.com/fe08me", description="The link above is a full tutorial on how to fully use the menu. This is a rushed tut lol. if anyone else wants to make one, by all means be my guest.", color=nextcord.Color.blue())
        embed.set_footer(text=f"Bot coded by heqds • Today at {now}")

        await message.delete()
        await message.channel.send("Use the below link to get the correct key and full tutorial.")
        await message.channel.send(embed=embed)

@bot.event
async def on_message(message):
    if message.content.startswith("/verify"):
        user = nextcord.User
        embed = nextcord.Embed(title="Capysploit Tutorial", url="https://streamable.com/fe08me", description="The link above is a full tutorial on how to fully use the menu. This is a rushed tut lol. if anyone else wants to make one, by all means be my guest.", color=nextcord.Color.blue())
        embed.set_footer(text=f"Bot coded by heqds • Today at {now}")

        await message.delete()
        await message.channel.send(f"Use the below link to get the correct key and full tutorial.")
        await message.channel.send(embed=embed)

@bot.slash_command(name="privserv", description="My private server")
async def priv(interaction: Interaction):
    await interaction.send("https://www.roblox.com/games/8737602449?privateServerLinkCode=31807813608613627662207045649029")

# If given the correct code (linkvertise code) this will give them the key to the script.
@bot.slash_command(name="verify", description="used to validate your key.")
async def verify(interaction: nextcord.Interaction, key):
    user = interaction.user

    correctEm = nextcord.Embed(title="Correct key!", description="Use the key below to enter into the script. Need help? do the command /tut", color=nextcord.Color.green())
    correctEm.add_field(name="Key:", value=f"`{pasteKey}`")
    correctEm.set_footer(text=f"Bot coded by heqds • Today at {now}")

    if key == pasteCode:
        await interaction.send(embed=correctEm, ephemeral=True)

        print(f"{user.name} entered the correct key. Key given: {pasteKey}")
        print("")

    else:

        embed = nextcord.Embed(title="Click Here To Get Key", url="https://link-center.net/466545/pls-donate-script-link", description="The key you entered is invalid. The key has most likely changed or you are using a bypasser. Head to <#1053055945107836949> and select key updates so you never miss a update on the key", color=nextcord.Color.red())
        correctEm.set_footer(text=f"Bot coded by heqds • Today at {now}")
        
        await interaction.send(embed=embed)
        print(f"{user.name} entered a incorrect key. The key they entered was: {key}")
        print("")

# if the user that ran the command has admin perms this gives them the current key for the script
@bot.slash_command(name="admin-key", description="Gives an admin the key.")
@application_checks.has_guild_permissions(administrator=True)
async def admin_key(interaction: nextcord.Interaction):
    embed = nextcord.Embed(title="Admin Key", description=f"Correct permissions! here is your key. `{pasteKey}`", color=nextcord.Color.blue())
    await interaction.send(embed=embed, ephemeral=True)

# if the user that ran the command has admin perms this gives them the current code for the bot from linkvertise
@bot.slash_command(name="admin-linkvertise", description="Gives an admin the code for linkvertise.")
@application_checks.has_guild_permissions(administrator=True)
async def admin_key(interaction: nextcord.Interaction):
    embed = nextcord.Embed(title="Admin Key", description=f"Correct permissions! here is your key: `{pasteCode}`", color=nextcord.Color.blue())
    await interaction.send(embed=embed, ephemeral=True)

# Gives the specified user the buyer role.
@bot.slash_command(name="customer-add", description="Adds the buyer role to the specified user.")
@application_checks.has_guild_permissions(administrator=True)
async def customer_add(interaction: nextcord.Interaction, user: nextcord.User):
    guild = interaction.guild

    embed = nextcord.Embed(title="Buyer role added!", description="You have been given the buyer role.", color=nextcord.Color.blue())
    embed.add_field(name="To run script:", value="Go to the channel <#1048599193532498040> and run the loadstring in there.")
    embed.set_footer(text=f"Bot coded by heqds • Today at {now}")

    role = guild.get_role(1048599068848439356)

    await interaction.send(f"Check your dms {user.mention}")
    await user.send(embed=embed)
    await user.add_roles(role)
    await interaction.send("Done", ephemeral=True)

# removes the specified users customer role.
@bot.slash_command(name="customer-remove", description="Removes the buyer role to the specified user.")
@application_checks.has_guild_permissions(administrator=True)
async def customer_remove(interaction: nextcord.Interaction, user: nextcord.User):
    guild = interaction.guild
    userr = nextcord.User
    
    embed = nextcord.Embed(title="Buyer role removed :(", description="You have been revoked of the buyer role.", color=nextcord.Color.blue())
    embed.add_field(name="**More info:**", value="*Please create a ticket in the server for more info*")
    embed.set_footer(text=f"Bot coded by heqds • Today at {now}")

    role = guild.get_role(1048599068848439356)
    
    await user.send(embed=embed)
    await user.remove_roles(role)
    await interaction.send("Done", ephemeral=True)

# Deletes the inputted amount of messages
@bot.slash_command(name="purge", description="deletes a specified amount of messages")
@application_checks.has_guild_permissions(administrator=True)
async def purge(interaction: nextcord.Interaction, amount: int):
    if amount < 1:
        return await interaction.send("Please enter a number greater than 0.")
    await interaction.channel.purge(limit=amount)
    await interaction.send(f"{amount} messages have been purged.", ephemeral=True)

# sends an announcment in announcments
@bot.slash_command(name="announce", description="Sends a message in announcments with a ping.")
@application_checks.has_guild_permissions(administrator=True)
async def announce(interaction: nextcord.Interaction):
    return

# Without the correct permissions, this stops the user from using the command and notifies them
@bot.event
async def on_application_command_error(interaction: Interaction, error):
    if isinstance(error, application_checks.ApplicationMissingPermissions):
        await interaction.send("You are missing the permisisons to use this command.", ephemeral=True)

# Disable dm commands
@bot.event
async def on_application_command_error(interaction: Interaction, error):
    if isinstance(error, application_checks.ApplicationNoPrivateMessage):
        await interaction.send("You may only use commands in the Capybara Moment server.", ephemeral=True)

@bot.event
async def on_application_command_error(inter: nextcord.Interaction, error):
    error = getattr(error, "original", error)

    if isinstance(error, CallableOnCooldown):
        await inter.send(f"This command is on cooldown. Retry in `{error.retry_after}` seconds.", ephemeral=True)

    else:
        raise error

@bot.slash_command(name="test", description="test")
@cooldowns.cooldown(1, 10, bucket=cooldowns.SlashBucket.author)
async def test(interaction: Interaction):
    await interaction.send("test")

# runs the bot
bot.run("MTA1MjczMjg5NTc1Nzg3MzE1Mg.G8zpPn.iBoWAgNHdef6N0iqz05BpYtg9Wc4VhsEYjeUzE")