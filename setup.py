# -*- coding: utf-8 -*_
# Author:Jerry gu
from distutils.core import setup
import setuptools

setup(
    name='trans_google_bing',  # 包的名字
    version='0.0.2',  # 版本号
    description='free translator by google or bing',  # 描述
    author='Jerry',  # 作者
    author_email='victor_jie@yeah.net',  # 你的邮箱**
    url='',  # 可以写github上的地址，或者其他地址
    # packages=setuptools.find_packages(exclude=['bingtrans', 'google_bing_trans']),  # 包内不需要引用的文件夹
    packages=setuptools.find_packages(),  # 包内不需要引用的文件夹
    # license='MIT',
    # 依赖包
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: Microsoft',  # 你的操作系统
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python',  # 支持的语言
        'Programming Language :: Python :: 3',  # python版本 。。。
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
    ],
    zip_safe=True,
)