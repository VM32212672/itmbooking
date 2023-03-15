from setuptools import setup

setup(
    name='myapp',
    version='0.1.0',
    packages=['myapp'],
    include_package_data=True,
    install_requires=[
        'django',
        'gunicorn',
        'django-heroku',
        'psycopg2-binary',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" with the actual Django version you are using
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
         'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
