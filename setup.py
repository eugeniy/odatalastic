from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
        name='odatalastic',
        version='0.1.0',

        packages=find_packages(),

        install_requires=['nose==1.3.0', 'pyparsing==2.0.1'],
        test_suite='nose.collector'
    )
