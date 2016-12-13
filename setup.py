from distutils.core import setup
setup(
  name = 'pythloghlp',
  packages = ['pythloghlp'], # this must be the same as the name above
  version = '0.1.4',
  description = 'Python DynamoDB Log Helper',
  author = 'Gunder Biten',
  author_email = 'gunder.biten@gabcia.se',
  url = 'https://github.com/Immunovia-AB/PythLogHlp', # use the URL to the github repo
  download_url = 'https://github.com/Immunovia-AB/PythLogHlp/tarball/0.1', # I'll explain this in a second
  keywords = ['logging', 'DynamoDB'], # arbitrary keywords
  classifiers=[
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5'
  ],
  install_requires=[
    'boto3',
    'logging',
    'json',
    'os',
    'pwd',
    'datetime'
  ]
)