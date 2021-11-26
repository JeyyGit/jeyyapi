# jeyyapi (async)
Async python wrapper for JeyyAPI

# Example usage
```py
# import JeyyAPIClient
from jeyyapi import JeyyAPIClient

# Create JeyyAPICLient instance
client = JeyyAPIClient()

# fetch from `hearts` endpoint with its appropriate kwargs parameter
# returns io.BytesIO for image and discord endpoints
image = await client.hearts(image_url='IMAGE_URL', rainbow=True)
```

### spotify command example on discord.py (2.0)
```py
from jeyyapi import JeyyAPIClient

client = JeyyAPIClient()

# requires presence intent
@bot.command()
async def spotify(ctx, member: discord.Member=None):
    member = member or ctx.author
    spotify = discord.utils.find(lambda a: isinstance(a, discord.Spotify), member.activities)
    
    if spotify is None:
      return await ctx.send(f"**{member}** is not listening or connected to Spotify.")
    
    image = await client.spotify(
      title = spotify.title,
      cover_url = spotify.album_cover_url,
      duration_seconds = spotify.duration.seconds,
      start_timestamp = spotify.start.timestamp(),
      artists = spotify.artists
    )
    
    await ctx.send(f"> **{member}** is listening to **{spotify.title}**", file=discord.File(image, 'spotify.png'))
```

#### Close the client session with `await client.close()` if you didn't pass your own session
