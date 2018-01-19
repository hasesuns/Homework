from setuptools import setup, find_packages

__author__ = 'Akiyuki Hasegawa'

setup(
    name='olkalmanflt',
    version='1.0',
    description='Tools for the most simplest Kalman filter',
    author='Akiyuki Hasegawa',
    author_email='hase.eeicm@gmail.com',
    url='https://github.com/hasesuns/PythonRobotics',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=find_packages(), # The directory with __init__.py is packaged
    include_package_data=True,
    keywords=['Kalman filter', 'linear system'],
    license='MIT License',
    install_requires=[
    ],
    entry_points={
        'console_scripts':[
        'olkalmanflt = Localization.kalman_filter.one_dim_linear_kalman_filter:.main',
        ],
    },
)
