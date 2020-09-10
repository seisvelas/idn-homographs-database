from distutils.core import setup
setup(
  name = 'homograph',
  packages = ['homograph'],
  version = '0.99',
  license='MIT',
  description = 'IDN Homograph detection tools',
  author = 'Alex Alvarado',
  author_email = 'alex@flowcrypt.com',
  url = 'https://github.com/seisvelas/idn-homograph-database',
  # Note: The below release doesn't exist yet!
  download_url = 'https://github.com/seisvelas/idn-homographs-database/archive/0.99.tar.gz',
  keywords = ['IDN', 'homograph', 'attack', 'security'],
  install_requires = [],
  include_package_data = True,
  classifiers = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Topic :: Security',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
