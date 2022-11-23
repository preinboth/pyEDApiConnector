from setuptools import setup

setup(
    name='pyED-Api-Connector',
    version='v0.0.1',
    packages=['utils', 'connector', 'connector.base', 'connector.base.edLogger', 'connector.eddb', 'connector.edsm',
              'connector.spansh', 'eddb', 'edsm', 'spansh'],
    package_dir={'': 'src'},
    url='https://github.com/preinboth/pyEDApiConnector',
    license='MIT',
    author='preinboth',
    author_email='github@preinboth.de',
    description='Elite Dangerous Api Connector'
)
