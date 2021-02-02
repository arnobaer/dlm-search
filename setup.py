from setuptools import setup, find_packages

setup(
    name='dlm-search',
    version='1.1.0',
    author="Bernhard Arnold",
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'bottle>=0.12',
        'jinja2',
        'pony',
        'gunicorn'
    ],
    package_data={
        'dlmsearch': [
            'data/*.csv',
            'views/*.html'
        ],
    },
    test_suite='tests',
    license="GPLv3",
)
