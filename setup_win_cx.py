import sys
import pytz
from cx_Freeze import setup, Executable


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ["lxml._elementpath", "lxml.etree"],
        'excludes': ['unittest'],
        'include_files': (pytz.__path__[0], # http://stackoverflow.com/questions/10606932/cx-freeze-how-do-i-add-package-files-into-library-zip
                          'data/',
                          'translations/',
                          'readme.md',
                          'license',
                          'icon.ico')
    }
}

executables = [
    Executable('start.py',
               base=base,
               targetName="FMIDownloader.exe",
               icon="icon.ico")
]

setup(name='FMIDownloader',
      version='0.15.2',
      description='Download Finnish meteorological data',
      options=options,
      executables=executables
      )