from gettext import install
from setuptools import find_packages, setup

setup(
    name='saas',
    version='1.0.0.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==2.1.2',
        'Flask-SQLAlchemy==2.5.1',
        'psycopg2-binary==2.9.3',
        'Flask-Migrate==3.1.0',
    ],
)
