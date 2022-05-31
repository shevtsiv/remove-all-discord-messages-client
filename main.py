import discord

# Go to Chrome Developer Tools, switch to mobile view, open Local Storage and copy "token"'s value
token = str("YOUR_DISCORD_TOKEN_FROM_BROWSER")
# Go to Discord Advanced Tab, enable Developer Mode, right click on Server name and hit "Copy ID"
server_id = int(1234567890)
heartbeat = int(86400)

class RemoveAllMyMessagesClient(discord.Client):
  async def on_ready(self):
    channels = self.get_guild(server_id).channels
    print("Successfully acquired channels list from the specified Discord server, start deleting")
    for channel in channels:
      print("Deleting all the messages from: " + channel.name + "\n")
      try:
        async for mss in channel.history(limit=None):
          if(mss.author == self.user):
            print(mss.content)
            try:
              await mss.delete()
            except Exception as couldNotDeleteException:
              print("Could not delete a message: " + couldNotDeleteException + "\n")
      except Exception as couldNotReadHistoryException:
        print("Could not read history: " + couldNotReadHistoryException + "\n")

client = RemoveAllMyMessagesClient(heartbeat_timeout = heartbeat, guild_subscriptions = False)
client.run(token, bot = False)
