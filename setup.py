import setuptools

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
	name='jeyyapi',
	version='1.0',
	description='Python wrapper for JeyyAPI',
	long_description=long_description,
	url='http://github.com/JeyyGit/jeyyapi',
	author='JeyyGit',
	license='MIT',
	packages=['jeyyapi'],
	install_requires=['aiohttp'],
	requirements=requirements
)