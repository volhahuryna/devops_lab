from setuptools import setup, find_packages

setup(
    name="snapshot",
    entry_points={
        'console_scripts': [
            "snapshot=modules.snapshot:main"
        ]
    },
    install_requires=[
        'psutil'
    ],
    packages=['modules'],
    version="0.1",
    author="Volha Huryna",
    author_email="Volha_Huryna@epam.com",
    description="Application for saving snapshot of the system in file",
    license="MIT",
)
