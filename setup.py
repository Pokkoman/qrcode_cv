from setuptools import setup
from setuptools import find_packages

setup(
    name = "qrscanner",
    version = "1.0.0",
    description = "qr scanner",
    author = "surit",
    author_email = "surit404@gmail.com",
    packages = find_packages(),
    entry_points = {
        'console_scripts':[
            'qrscanner-cli = qrcode_cv.qrscanner.py',
        ],
    },

)