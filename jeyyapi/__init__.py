import aiohttp
import typing
import yarl
import datetime
from io import BytesIO


class APIError(Exception):
	pass


class JeyyAPIClient:
	def __init__(self, api_key: str, *, session: typing.Optional[aiohttp.ClientSession] = None) -> None:
		self.base_url: yarl.URL = yarl.URL('https://api.jeyy.xyz/v2/')
		self.headers = {'Authorization': f'Bearer {api_key}'}
		self.new_session = False
		if session is None:
			self.session = aiohttp.ClientSession()
			self.new_session = True
		else:
			self.session = session

	async def close(self) -> None:
		if self.new_session:
			if self.session.closed:
				raise TypeError('session is already closed')
				
			await self.session.close()
		else:
			raise TypeError('session was created manually. call .close() on the session instead.')

	async def __aenter__(self):
		if self.session.closed:
			raise TypeError('session has closed')
			
		return self

	async def __aexit__(self, exc_type, exc, tb):
		try:
			await self.close()
		except:
			pass

	# image
	async def _image_fetch(self, endpoint, **params) -> BytesIO:
		url = self.base_url / f'image/{endpoint}'
		async with self.session.get(url, params=params, headers=self.headers) as resp:
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
	
	def dilute(self, image_url: str) -> BytesIO:
		return self._image_fetch('dilute', image_url=str(image_url))
	
	def dither(self, image_url: str) -> BytesIO:
		return self._image_fetch('dither', image_url=str(image_url))

	def pattern(self, image_url: str) -> BytesIO:
		return self._image_fetch('pattern', image_url=str(image_url))

	def logoff(self, image_url: str) -> BytesIO:
		return self._image_fetch('logoff', image_url=str(image_url))

	def dilate(self, image_url: str):
		return self._image_fetch('dilate', image_url=str(image_url))

	def fire(self, image_url: str):
		return self._image_fetch('fire', image_url=str(image_url))

	def fall(self, image_url: str) -> BytesIO:
		return self._image_fetch('fall', image_url=str(image_url))

	def fan(self, image_url: str):
		return self._image_fetch('fan', image_url=str(image_url))
	
	def flag(self, image_url: str) -> BytesIO:
		return self._image_fetch('flag', image_url=str(image_url))

	def melt(self, image_url: str):
		return self._image_fetch('melt', image_url=str(image_url))

	def contour(self, image_url: str, rainbow: bool = False) -> BytesIO:
		return self._image_fetch('contour', image_url=str(image_url), rainbow=rainbow)

	def cracks(self, image_url: str):
		return self._image_fetch('cracks', image_url=str(image_url))

	def im_emojify(self, image_url: str, size: int = 32):
		return self._image_fetch('emojify', image_url=str(image_url), size=size)

	def endless(self, image_url: str):
		return self._image_fetch('endless', image_url=str(image_url))

	def bayer(self, image_url: str):
		return self._image_fetch('bayer', image_url=str(image_url))

	def slice(self, image_url: str):
		return self._image_fetch('slice', image_url=str(image_url))

	def spikes(self, image_url: str):
		return self._image_fetch('spikes', image_url=str(image_url))

	def blocks(self, image_url: str):
		return self._image_fetch('blocks', image_url=str(image_url))

	def phone(self, image_url: str):
		return self._image_fetch('phone', image_url=str(image_url))

	def laundry(self, image_url: str):
		return self._image_fetch('laundry', image_url=str(image_url))

	def pizza(self, image_url: str):
		return self._image_fetch('pizza', image_url=str(image_url))

	def ripped(self, image_url: str):
		return self._image_fetch('ripped', image_url=str(image_url))

	def cinema(self, image_url: str):
		return self._image_fetch('cinema', image_url=str(image_url))

	def stretch(self, image_url: str):
		return self._image_fetch('stretch', image_url=str(image_url))

	def dots(self, image_url: str):
		return self._image_fetch('dots', image_url=str(image_url))

	def tunnel(self, image_url: str, direction: typing.Literal['h', 'horizontal', 'v', 'vertical', 'c', 'circle', 'r', 'rotate']):
		return self._image_fetch('tunnel', image_url=str(image_url), direction=direction)

	def zonk(self, image_url: str):
		return self._image_fetch('zonk', image_url=str(image_url))

	def knit(self, image_url: str):
		return self._image_fetch('knit', image_url=str(image_url))

	def plank(self, image_url: str):
		return self._image_fetch('plank', image_url=str(image_url))

	def shred(self, image_url: str):
		return self._image_fetch('shred', image_url=str(image_url))

	def liquefy(self, image_url: str):
		return self._image_fetch('liquefy', image_url=str(image_url))

	def poly(self, image_url: str):
		return self._image_fetch('poly', image_url=str(image_url))

	def spin(self, image_url: str):
		return self._image_fetch('spin', image_url=str(image_url))

	def plates(self, image_url: str):
		return self._image_fetch('plates', image_url=str(image_url))

	def lsd(self, image_url: str):
		return self._image_fetch('lsd', image_url=str(image_url))

	def lines(self, image_url: str):
		return self._image_fetch('lines', image_url=str(image_url))

	def ipcam(self, image_url: str):
		return self._image_fetch('ipcam', image_url=str(image_url))

	def reflection(self, image_url: str):
		return self._image_fetch('reflection', image_url=str(image_url))

	def stereo(self, image_url: str):
		return self._image_fetch('stereo', image_url=str(image_url))

	def kanye(self, image_url: str):
		return self._image_fetch('kanye', image_url=str(image_url))

	def letters(self, image_url: str):
		return self._image_fetch('letters', image_url=str(image_url))

	def wiggle(self, image_url: str):
		return self._image_fetch('wiggle', image_url=str(image_url))

	def tiles(self, image_url: str, n_edges: typing.Literal[3, 4, 5, 6, 7, 8] = 4):
		return self._image_fetch('tiles', image_url=str(image_url), n_edges=n_edges)

	def gameboy_camera(self, image_url: str):
		return self._image_fetch('gameboy_camera', image_url=str(image_url))

	def ripple(self, image_url: str):
		return self._image_fetch('ripple', image_url=str(image_url))

	def globe(self, image_url: str):
		return self._image_fetch('globe', image_url=str(image_url))

	def cow(self, image_url: str):
		return self._image_fetch('cow', image_url=str(image_url))

	def pyramid(self, image_url: str):
		return self._image_fetch('pyramid', image_url=str(image_url))

	def wall(self, image_url: str):
		return self._image_fetch('wall', image_url=str(image_url))

	def cube(self, image_url: str):
		return self._image_fetch('cube', image_url=str(image_url))

	def paint(self, image_url: str):
		return self._image_fetch('paint', image_url=str(image_url))
	
	def painting(self, image_url: str):
		return self._image_fetch('painting', image_url=str(image_url))

	def shine(self, image_url: str):
		return self._image_fetch('shine', image_url=str(image_url))

	def neon(self, image_url: str):
		return self._image_fetch('neon', image_url=str(image_url))

	def flush(self, image_url: str):
		return self._image_fetch('flush', image_url=str(image_url))

	def ace(self, name: str, side: typing.Literal['attorney', 'prosecutor'], text: str) -> BytesIO:
		return self._image_fetch('ace', name=str(name), side=str(side), text=str(text))

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
	
	def heart_locket(self, image_url: str, image_url_2: str = None):
		return self._image_fetch('heart_locket', image_url=str(image_url), image_url_2=str(image_url_2) if image_url_2 else image_url_2)
	
	def roll(self, image_url: str) -> BytesIO:
		return self._image_fetch('roll', image_url=str(image_url))

	def wave(self, image_url: str, frequency: float = 0.05, amplitude: typing.Literal[1, 2, 3, 4, 5] = 1) -> BytesIO:
		return self._image_fetch('wave', image_url=str(image_url), frequency=frequency, amplitude=amplitude)

	def clock(self, image_url: str) -> BytesIO:
		return self._image_fetch('clock', image_url=str(image_url))
	
	def optics(self, image_url: str) -> BytesIO:
		return self._image_fetch('optics', image_url=str(image_url))
	
	def warp(self, image_url: str) -> BytesIO:
		return self._image_fetch('warp', image_url=str(image_url))

	def ads(self, image_url: str) -> BytesIO:
		return self._image_fetch('ads', image_url=str(image_url))

	def billboard(self, image_url) -> BytesIO:
		return self._image_fetch('billboard', image_url=str(image_url))

	def bubble(self, image_url: str) -> BytesIO:
		return self._image_fetch('bubble', image_url=str(image_url))

	def cloth(self, image_url: str) -> BytesIO:
		return self._image_fetch('cloth', image_url=str(image_url))

	def youtube(self, avatar_url: str, author: str, title: str) -> BytesIO:
		return self._image_fetch('youtube', avatar_url=str(avatar_url), author=str(author), title=str(title))

	def scrapbook(self, text: str) -> BytesIO:
		return self._image_fetch('scrapbook', text=str(text))

	# text
	async def emojify(self, image_url: str) -> dict:
		params = {'image_url': str(image_url)}
		async with self.session.get(self.base_url / 'text/emojify', params=params, headers=self.headers) as resp:
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

		async with self.session.get(self.base_url / 'discord/spotify', params=params, headers=self.headers) as resp:
			if resp.status != 200:
				raise APIError(await resp.text())
			
			data = await resp.read()

		buffer = BytesIO(data)
		return buffer

	async def spotify_from_object(self, spotify: 'discord.Spotify') -> BytesIO:
		if spotify.__class__.__name__ != 'Spotify':
			raise TypeError(f'discord.Spotify is expected, {spotify.__class__.__name__} is passed instead.')

		kwargs = {
			'title': spotify.title,
			'cover_url': spotify.album_cover_url,
			'duration': spotify.duration.seconds,
			'start': spotify.start.timestamp(),
			'artists': spotify.artists
		}

		return await self.spotify(**kwargs)

	async def player(self, title: str, thumbnail_url: str, seconds_played: float, total_seconds: float, line_1: typing.Optional[str], line_2: typing.Optional[str]):
		params = {
			'title': title,
			'thumbnail_url': thumbnail_url,
			'seconds_played': seconds_played,
			'total_seconds': total_seconds,
			'line_1': line_1,
			'line_2': line_2,
		}

		async with self.session.get(self.base_url / 'discord/player', params=params, headers=self.headers) as resp:
			if resp.status != 200:
				raise APIError(await resp.text())
			
			data = await resp.read()

		buffer = BytesIO(data)
		return buffer

	async def wheel(self, args: typing.Union[typing.List[str], typing.Tuple[str]]) -> dict:
		async with self.session.get(self.base_url / 'discord/wheel', params={'args': args}, headers=self.headers) as resp:
			if resp.status != 200:
				raise APIError(await resp.text())
			
			result = await resp.json()

		return result

	async def ansi(
		self, 
		text: str, 
		bold: bool = False, 
		underline: bool = False, 
		text_color: typing.Literal['gray', 'red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'white'] = None,
		bg_color: typing.Literal['dark blue', 'orange', 'gray 1', 'gray 2', 'gray 3', 'gray 4', 'indigo', 'white'] = None,
		codeblock: bool = True
		) -> str:

		params = {
			'text': text,
			'bold': str(bold),
			'underline': str(underline),
			'text_color': text_color,
			'bg_color': bg_color,
			'codeblock': str(codeblock),
		}

		async with self.session.get(self.base_url / 'discord/ansi', params=params, headers=self.headers) as resp:
			if resp.status != 200:
				raise APIError(await resp.text())
			
			result = await resp.json()

		return result

		