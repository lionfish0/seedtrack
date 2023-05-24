from distutils.core import setup
setup(
  name = 'seedtrack',
  packages = ['seedtrack'],
  version = '1.01',
  description = 'Tracks seed location.',
  author = 'Mike Smith',
  author_email = 'm.t.smith@sheffield.ac.uk',
  url = 'https://github.com/lionfish0/seedtrack.git',
  download_url = 'https://github.com/lionfish0/seedtrack.git',
  keywords = ['image processing','seed','video'],
  classifiers = [],
  install_requires=['numpy','opencv-python'],
  scripts=['bin/seedtrack'],
)
