from distutils.core import setup
import sys
import py2exe

setup(name="appName",
      version="1.0.0",
      author="Titouan Benoit",
      author_email="titouan.benoit@gmx.fr",
      windows=[{"script": "appName.py"}],
      options={"py2exe": {'bundle_files': 1, 'compressed': True,"includes": ["sip"], "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"]}})