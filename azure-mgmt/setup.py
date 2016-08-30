#!/usr/bin/env python

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

from setuptools import setup

# azure v0.x is not compatible with this package
# azure v0.x used to have a __version__ attribute (newer versions don't)
try:
    import azure
    try:
        ver = azure.__version__
        raise Exception(
            'This package is incompatible with azure=={}. '.format(ver) +
            'Uninstall it with "pip uninstall azure".'
        )
    except AttributeError:
        pass
except ImportError:
    pass

setup(
    name='azure-mgmt',
    version='0.30.0rc6',
    description='Microsoft Azure Resource Management Client Libraries for Python',
    long_description=open('README.rst', 'r').read(),
    license='MIT License',
    author='Microsoft Corporation',
    author_email='ptvshelp@microsoft.com',
    url='https://github.com/Azure/azure-sdk-for-python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
    zip_safe=False,
    install_requires=[
        'azure-mgmt-batch==1.0.0',
        'azure-mgmt-redis==1.0.0',
        'azure-mgmt-logic==1.0.0',
        'azure-mgmt-scheduler==1.0.0',
        'azure-mgmt-compute==0.30.0rc6',
        'azure-mgmt-keyvault==0.30.0rc6',
        'azure-mgmt-network==0.30.0rc6',
        'azure-mgmt-resource==0.30.0rc6',
        'azure-mgmt-storage==0.30.0rc6',
    ],
)
