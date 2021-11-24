import aiohttp
from typing import List
from io import BytesIO


class ApiError(Exception):
	pass


class JeyyAPIClient:
	def __init__(self, *, session: aiohttp.ClientSession = None):
		self.session = session or aiohttp.ClientSession
		self.base_url = 'https://api.jeyy.xyz'

	# image
	async def _image_fetch(self, endpoint, **params) -> BytesIO:

		async with self.session.get(f'{self.base_url}/image/{endpoint}', params=params) as resp:
			if resp.status != 200:
				raise ApiError(await resp.text())

			data = await resp.read()

		buffer = BytesIO(data)
		return buffer

	async def patpat(self, image_url: str) -> BytesIO:
		return self._image_fetch('patpat', image_url=image_url)

	async def burn(self, image_url: str) -> BytesIO:
		return self._image_fetch('burn', image_url=image_url)
	
	async def glitch(self, image_url: str, level: int = 3) -> BytesIO:
		return self._image_fetch('glitch', image_url=image_url, level=level)
	
	async def boil(self, image_url: str, level: int = 2) -> BytesIO:
		return self._image_fetch('boil', image_url=image_url, level=level)
	
	async def earthquake(self, image_url: str, level: int = 3) -> BytesIO:
		return self._image_fetch('earthquake', image_url=image_url, level=level)

	async def hearts(self, image_url: str, rainbow: bool = True) -> BytesIO:
		return self._image_fetch('hearts', image_url=image_url, rainbow=rainbow)
	
	async def shock(self, image_url: str) -> BytesIO:
		return self._image_fetch('shock', image_url=image_url)
	
	async def abstract(self, image_url: str) -> BytesIO:
		return self._image_fetch('abstract', image_url=image_url)
	
	async def infinity(self, image_url: str) -> BytesIO:
		return self._image_fetch('infinity', image_url=image_url)
	
	async def bomb(self, image_url: str) -> BytesIO:
		return self._image_fetch('bomb', image_url=image_url)
	
	async def bonks(self, image_url: str) -> BytesIO:
		return self._image_fetch('bonks', image_url=image_url)
	
	async def sob(self, image_url: str) -> BytesIO:
		return self._image_fetch('sob', image_url=image_url)
	
	async def explicit(self, image_url: str) -> BytesIO:
		return self._image_fetch('explicit', image_url=image_url)
	
	async def blur(self, image_url: str) -> BytesIO:
		return self._image_fetch('blur', image_url=image_url)
	
	async def lamp(self, image_url: str) -> BytesIO:
		return self._image_fetch('lamp', image_url=image_url)
	
	async def rain(self, image_url: str) -> BytesIO:
		return self._image_fetch('rain', image_url=image_url)
	
	async def canny(self, image_url: str) -> BytesIO:
		return self._image_fetch('canny', image_url=image_url)
	
	async def cartoon(self, image_url: str) -> BytesIO:
		return self._image_fetch('cartoon', image_url=image_url)
	
	async def layers(self, image_url: str) -> BytesIO:
		return self._image_fetch('layers', image_url=image_url)
	
	async def radiate(self, image_url: str) -> BytesIO:
		return self._image_fetch('radiate', image_url=image_url)
	
	async def shoot(self, image_url: str) -> BytesIO:
		return self._image_fetch('shoot', image_url=image_url)
	
	async def tv(self, image_url: str) -> BytesIO:
		return self._image_fetch('tv', image_url=image_url)
	
	async def shear(self, image_url: str, axis: str = 'X') -> BytesIO:
		return self._image_fetch('shear', image_url=image_url, axis=axis)
	
	async def magnify(self, image_url: str) -> BytesIO:
		return self._image_fetch('magnify', image_url=image_url)
	
	async def gallery(self, image_url: str) -> BytesIO:
		return self._image_fetch('gallery', image_url=image_url)
	
	async def balls(self, image_url: str) -> BytesIO:
		return self._image_fetch('balls', image_url=image_url)
	
	async def equation(self, image_url: str) -> BytesIO:
		return self._image_fetch('equation', image_url=image_url)
	
	async def half_invert(self, image_url: str) -> BytesIO:
		return self._image_fetch('half_invert', image_url=image_url)
	
	async def roll(self, image_url: str) -> BytesIO:
		return self._image_fetch('roll', image_url=image_url)
	
	async def optics(self, image_url: str) -> BytesIO:
		return self._image_fetch('optics', image_url=image_url)
	
	async def scrapbook(self, text: str) -> BytesIO:
		return self._image_fetch('scrapbook', text=text)

	# text
	async def emojify(self, image_url: str) -> dict:
		params = {'image_url': image_url}
		async with self.session.get(f'{self.base_url}/text/emojify', params=params) as resp:
			if resp.status != 200:
				raise ApiError(await resp.text())
			
			result = await resp.json()

		return result

	# discord
	async def spotify(self, title: str, cover_url: str, duration_seconds: int, start_timestamp: float, artists: List[str]) -> BytesIO:

		params = {
			'title': title,
			'cover_url': cover_url,
			'duration_seconds': duration_seconds,
			'start_timestamp': start_timestamp,
			'artists': artists
		}

		async with self.session.get(f'{self.base_url}/discord/spotify', params=params) as resp:
			if resp.status != 200:
				raise ApiError(await resp.text())
			
			data = await resp.read()

		buffer = BytesIO(data)
		return buffer
