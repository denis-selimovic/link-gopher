from setuptools import setup

setup(
    name='link_gopher',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'link-gopher=link_gopher:link_gopher'
        ]
    }
)
