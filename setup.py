import setuptools

setuptools.setup(
    name='ovirt_python_sdk',
    version='0.0.1',
    author='Toliak, Underlor',
    author_email='ibolosik@gmail.com',
    url='https://gitlab.keln.space/CrazyDev/ovirtsdk',
    description='Обертка для oVirt SDK',
    install_requires=[
        'ovirt-engine-sdk-python',
    ],
    packages=setuptools.find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description='GIT: https://github.com/gamehost/ovirt_python_sdk',
)