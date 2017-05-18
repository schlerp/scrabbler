from distutils.core import setup
import py2exe

datafiles = (['./websters dict.json'])

setup(console=['scrabbler.py'],
      data_files = datafiles,
      options = {'py2exe': {'bundle_files': 1,
                            }
                 },
      zipfile = None,)