import setuptools

setuptools.setup(
    name="nb_anacondacloud",
    version='0.1.0',
    url="http://github.com/anaconda-notebook/nb_anacondacloud",
    author="Continuum Analytics",
    description="Integration with Anaconda-Cloud",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=['anaconda-client']
)
