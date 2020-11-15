from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='english_dict',
    url='https://github.com/alejandroxag/cmu_f20_df_python/english_dict',
    author='Alejandro Alvarez',
    author_email='alejandro.alvarez.1804@gmail.com',
    # Needed to actually package something
    packages=['english_dict'],
    # Needed for dependencies
    install_requires=['pkg_resources', 'sys'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package, out of my HW2 of the DF Python course at CMU.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)