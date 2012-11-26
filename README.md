pelican_admin
======================
pelican_admin was developed to assist you manage your [Pelican](https://github.com/getpelican/pelican) blog.

This is an alpha previous release and will have upcoming new features.

Usage
-----

Insert **pelican_admin** to the end of your INSTALLED_APPS in settings.py:

    INSTALLED_APPS = (
        ...
        'pelican_admin',
        ...
    )
    
Don't forget to sync your db with:

	python manage.py syncdb
	
Or, if you're using [south](http://pypi.python.org/pypi/South/):

	python manage.py migrate pelican_admin
	
Make sure your pelican service is running in `autoreload` mode:

	pelican /path/to/your/blog -s /path/to/pelican/settings -r &
	
This will have your pelican to reload itself whenever your folder blog changes. Without this configuration, **pelican_admin** is pretty much useless. So be sure to use it.

Features
--------

- **Settings management**: change your pelican settings through Django admin and have it automatically working.
- **Posting management**: CRUD for blog postings via interface.

Upcoming Features
-----------------
- **Pelican service management**: this will be a module available for [django-admin-tools](https://bitbucket.org/izi/django-admin-tools/wiki/Home) where you'll be able to see the current service status and perform actions like *stop*, *start*, and *restart*.

Requirements
------------
* [Django 1.4+](http://pypi.python.org/pypi/Django/1.4)

Installation
------------
I'll just assume you're already familiarized with pelican and move on.

Install using pip:

    pip install pelican_admin
    
Or you can clone the project and install it via:

    python setup.py install

Check This Out
--------------
1. [GitHub Repository](https://github.com/fjcaetano/pelican_admin)
2. [PyPi package](http://pypi.python.org/pypi/pelican_admin/0.1)
3. [Owner's website](http://flaviocaetano.com)
4. [Owner's Blog](http://blog.flaviocaetano.com)


Contact
==============
If you have any comments, ideas questions, feedback, etcetera, email me and we'll be in touch. I'm <flavio@vieiracaetano.com>
