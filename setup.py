from sys import platform
from cx_Freeze import setup, Executable

base = None
if platform == 'win32':
    base = 'Win32Gui'

setup(
    name = 'translator_of_smiile', 
    version = '1.0', 
    description = "Translator made with Dunossauro's tutorial on live #177", 
    options = {
        'build_exe': { 
            'includes': ['tkinter', 'ttkthemes']
        }
    }, 
    executables = [
        Executable('translator.py', base=base)
    ],
)
