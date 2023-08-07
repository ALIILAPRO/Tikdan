from setuptools import setup, find_packages

setup(
	name='tikdan',
	version='1.0.0',
	description='Unofficial api tiktok',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	author='ALIILAPRO',
	author_email='aliilapro@pm.me',
	url='https://github.com/ALIILAPRO/Tikdan',
	packages=find_packages(),
	install_requires=['requests'],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
	],
)