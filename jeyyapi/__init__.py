import aiohttp
import typing
import yarl
import datetime
from io import BytesIO


class APIError(Exception):
	pass


class JeyyAPIClient:
	def __init__(self, *, session: typing.Optional[aiohttp.ClientSession] = None) -> None:
		self.session: aiohttp.ClientSession = session or aiohttp.ClientSession()
		self.base_url: yarl.URL = yarl.URL('https://api.jeyy.xyz/')

	async def close(self) -> None:
		await self.session.close()

	# image
	async def _image_fetch(self, endpoint, **params) -> BytesIO:
		url = self.base_url / f'image/{endpoint}'
		async with self.session.get(url, params=params) as resp:
			if resp.status != 200:
				raise APIError(await resp.text())

			data = await resp.read()

		buffer = BytesIO(data)
		return buffer

	def patpat(self, image_url: str) -> BytesIO:
		return self._image_fetch('patpat', image_url=str(image_url))

	def burn(self, image_url: str) -> BytesIO:
		return self._image_fetch('burn', image_url=str(image_url))
	
	def glitch(self, image_url: str, level: typing.Optional[int] = 3) -> BytesIO:
		return self._image_fetch('glitch', image_url=str(image_url), level=int(level))
	
	def boil(self, image_url: str, level: typing.Optional[str] = 2) -> BytesIO:
		return self._image_fetch('boil', image_url=str(image_url), level=int(level))
	
	def earthquake(self, image_url: str, level: typing.Optional[int] = 3) -> BytesIO:
		return self._image_fetch('earthquake', image_url=str(image_url), level=int(level))

	def hearts(self, image_url: str, rainbow: typing.Optional[bool] = True) -> BytesIO:
		return self._image_fetch('hearts', image_url=str(image_url), rainbow=str(bool(rainbow)))
	
	def shock(self, image_url: str) -> BytesIO:
		return self._image_fetch('shock', image_url=str(image_url))
	
	def abstract(self, image_url: str) -> BytesIO:
		return self._image_fetch('abstract', image_url=str(image_url))
	
	def infinity(self, image_url: str) -> BytesIO:
		return self._image_fetch('infinity', image_url=str(image_url))
	
	def bomb(self, image_url: str) -> BytesIO:
		return self._image_fetch('bomb', image_url=str(image_url))
	
	def bonks(self, image_url: str) -> BytesIO:
		return self._image_fetch('bonks', image_url=str(image_url))
	
	def sob(self, image_url: str) -> BytesIO:
		return self._image_fetch('sob', image_url=str(image_url))
	
	def explicit(self, image_url: str) -> BytesIO:
		return self._image_fetch('explicit', image_url=str(image_url))
	
	def blur(self, image_url: str) -> BytesIO:
		return self._image_fetch('blur', image_url=str(image_url))
	
	def lamp(self, image_url: str) -> BytesIO:
		return self._image_fetch('lamp', image_url=str(image_url))
	
	def rain(self, image_url: str) -> BytesIO:
		return self._image_fetch('rain', image_url=str(image_url))
	
	def canny(self, image_url: str) -> BytesIO:
		return self._image_fetch('canny', image_url=str(image_url))
	
	def cartoon(self, image_url: str) -> BytesIO:
		return self._image_fetch('cartoon', image_url=str(image_url))
	
	def layers(self, image_url: str) -> BytesIO:
		return self._image_fetch('layers', image_url=str(image_url))
	
	def radiate(self, image_url: str) -> BytesIO:
		return self._image_fetch('radiate', image_url=str(image_url))
	
	def shoot(self, image_url: str) -> BytesIO:
		return self._image_fetch('shoot', image_url=str(image_url))
	
	def tv(self, image_url: str) -> BytesIO:
		return self._image_fetch('tv', image_url=str(image_url))
	
	def shear(self, image_url: str, axis: typing.Optional[str] = 'X') -> BytesIO:
		return self._image_fetch('shear', image_url=str(image_url), axis=str(axis))
	
	def magnify(self, image_url: str) -> BytesIO:
		return self._image_fetch('magnify', image_url=str(image_url))

	def print(self, image_url: str) -> BytesIO:
		return self._image_fetch('print', image_url=str(image_url))

	def matrix(self, image_url: str) -> BytesIO:
		return self._image_fetch('matrix', image_url=str(image_url))

	def sensitive(self, image_url: str) -> BytesIO:
		return self._image_fetch('sensitive', image_url=str(image_url))
	
	def gallery(self, image_url: str) -> BytesIO:
		return self._image_fetch('gallery', image_url=str(image_url))

	def paparazzi(self, image_url: str) -> BytesIO:
		return self._image_fetch('paparazzi', image_url=str(image_url))
	
	def balls(self, image_url: str) -> BytesIO:
		return self._image_fetch('balls', image_url=str(image_url))
	
	def equation(self, image_url: str) -> BytesIO:
		return self._image_fetch('equation', image_url=str(image_url))
	
	def half_invert(self, image_url: str) -> BytesIO:
		return self._image_fetch('half_invert', image_url=str(image_url))
	
	def roll(self, image_url: str) -> BytesIO:
		return self._image_fetch('roll', image_url=str(image_url))
	
	def optics(self, image_url: str) -> BytesIO:
		return self._image_fetch('optics', image_url=str(image_url))
	
	def youtube(self, avatar_url: str, author: str, title: str) -> BytesIO:
		return self._image_fetch('youtube', avatar_url=str(avatar_url), author=str(author), title=str(title))

	def scrapbook(self, text: str) -> BytesIO:
		return self._image_fetch('scrapbook', text=str(text))

	# text
	async def emojify(self, image_url: str) -> dict:
		params = {'image_url': str(image_url)}
		async with self.session.get(self.base_url / 'text/emojify', params=params) as resp:
			if resp.status != 200:
				raise APIError(await resp.text())
			
			result = await resp.json()

		return result

	# discord
	async def spotify(self, title: str, cover_url: str, duration: typing.Union[datetime.timedelta, int, float], start: typing.Union[datetime.datetime, float], artists: typing.List[str]) -> BytesIO:
		if isinstance(duration, datetime.timedelta):
			duration = int(duration.seconds)
		else:
			duration = int(duration)
			
		if isinstance(start, datetime.datetime):
			start = float(start.timestamp())
		else:
			start = float(start)
		
		params = {
			'title': str(title),
			'cover_url': str(cover_url),
			'duration_seconds': duration,
			'start_timestamp': start,
			'artists': artists
		}

		async with self.session.get(self.base_url / 'discord/spotify', params=params) as resp:
			if resp.status != 200:
				raise APIError(await resp.text())
			
			data = await resp.read()

		buffer = BytesIO(data)
		return buffer

	async def spotify_from_object(self, spotify: 'discord.Spotify'):
		if spotify.__class__.__name__ != 'Spotify':
			raise APIError(f'discord.Spotify object is required, not {spotify.__class__.__name__} object.')

		params = {
			'title': spotify.title,
			'cover_url': spotify.album_cover_url,
			'duration_seconds': spotify.duration.seconds,
			'start_timestamp': spotify.start.timestamp(),
			'artists': spotify.artists
		}

		async with self.session.get(self.base_url / 'discord/spotify', params=params) as resp:
			if resp.status != 200:
				raise APIError(await resp.text())
			
			data = await resp.read()

		buffer = BytesIO(data)
		return buffer