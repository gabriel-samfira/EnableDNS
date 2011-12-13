from distutils.core import setup
from py2exe.build_exe import py2exe

setup(
    name = 'EnableDNS updater',
    description = 'EnableDNS updater',
    version = '1.0',

    windows = [
                  {
                      'script': 'EDnsUpdater.py',
                      'icon_resources': [(1, 'icon.ico')],
                  }
              ],
    data_files = data_f,
    options = {
                  'py2exe': {
                      'packages'        :'encodings',
                      'includes'        : 'requests, PyQt4, sip',
                      'optimize'        : 2,
					  'dll_excludes': ['MSVCP90.dll', ],
                  }
              },

)
