from setuptools import setup

setup(
    name='flaskerino',
    packages=['flaskerino'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pylint'
    ],
)
