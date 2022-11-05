from setuptools import setup

setup(
    name='pyED-Api-Connector',
    version='0.0.1',
    packages=['connector', 'connector.base', 'connector.edsm'],
    package_dir={'': 'src'},
    url='https://github.com/preinboth/pyED-Api-Connector',
    license='MIT',
    author='preinboth',
    author_email='github@preinboth.de',
    description='Elite Dangerous Api Connector'
)
