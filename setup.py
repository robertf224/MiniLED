from setuptools import setup, find_packages

setup(
	name = 'MiniLED',
	version = '0,1',
	description = 'A python API to display text/images to small LED badges and signs',
	author = 'Robert Fidler',
	author_email = 'robertf224@gmail.com',
	packages = find_packages(),
	install_requires = ['pyserial'],
	url = 'https://github.com/robertf224/MiniLED/',
	keywords = ['led', 'sign', 'badge']
	)