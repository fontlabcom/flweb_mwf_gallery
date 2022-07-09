from setuptools import setup, find_packages

setup(
    name='flweb_mwf_gallery',
    version='1.0.1',
    description='Internal tool to create "Made with FontLab" gallery pages',
    long_description='Internal tool to create "Made with FontLab" gallery pages',
    keywords='',
    url='https://github.com/fontlabcom/flweb_mwf_gallery',
    author='Adam Twardoch',
    author_email='adam+github@twardoch.com',
    license='MIT',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['flweb_mwf_gallery=flweb_mwf_gallery.flweb_mwf_gallery:cli'],
    }
)
