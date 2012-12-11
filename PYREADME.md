pelican_admin
=============
*pelican_admin* was developed to assist you manage your `Pelican <https://github.com/getpelican/pelican>`_ blog.

This is a beta release and will have upcoming new features.

.. contents::

Usage
-----

Insert **pelican_admin** to the end of your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'pelican_admin',
        ...
    )
	
Now, you must tell *pelican_admin* what's the path to you pelican blog. In your settings.py you must add::

	PELICAN_PATH = '/path/to/your/blog'
	PELICAN_SETTINGS = 'your_pelican_settings.py # The default value is 'pelicanconf.py'
	PELICAN_BIN = 'pelican' # Path to pelican executable. Default value is '/usr/local/bin/pelican'
    
Don't forget to sync your db with::

	python manage.py syncdb
	
Or, if you're using `south <http://pypi.python.org/pypi/South/>`_::

	python manage.py migrate pelican_admin

*pelican_admin* is already set to run `Pelican <https://github.com/getpelican/pelican>`_'s service for you. It'll be running in the autoreload mode in the background.
	
If you're using `django-admin-tools <https://bitbucket.org/izi/django-admin-tools/wiki/Home>`_ there's a module available where you can manage your pelican service via admin interface. Add *pelican_admin* to your urls.py::

	import pelican_admin
	
	url_patterns = patterns('',	
    	url(r'^admin/', include(admin.site.urls)),
	    url(r'^admin_tools/', include('admin_tools.urls')),
	   	...
	)
	
	urlpatterns += pelican_admin.pelican_urls()
	
And finally, add *pelican_admin*'s module to your dashboard.py::

	from pelican_admin.modules import PelicanAdmin
	
	class CustomIndexDashboard(Dashboard):

    	def init_with_context(self, context):
			...
	        self.children.append(PelicanAdmin())
	        
This module is super useful not only to check `Pelican <https://github.com/getpelican/pelican>`_'s service status, but also to reload it if any change you made doesn't load.

If you experience any troubles in this step and your `django-admin-tools <https://bitbucket.org/izi/django-admin-tools/wiki/Home>`_ interface is scrambled, you may have too many modules in your dashboard. I never found out why, but my experience with  `django-admin-tools <https://bitbucket.org/izi/django-admin-tools/wiki/Home>`_ never allowed lots of modules, so just try removing some things you don't use.
	        
The Looks
---------
This is how *pelican_admin*'s module for `django-admin-tools <https://bitbucket.org/izi/django-admin-tools/wiki/Home>`_ looks like when enabled:

.. image:: https://raw.github.com/fjcaetano/pelican_admin/master/ss1.png

.. image:: https://raw.github.com/fjcaetano/pelican_admin/master/ss2.png

.. image:: https://raw.github.com/fjcaetano/pelican_admin/master/ss3.png


New Features
------------
- **Metadata management**: Now you can manage your posts' metadatas via interface since, now, they're attributes of your posts.
- **Category model**: Though `category` is just another post metadata, it was made to be an model to ease filtering, insertion, etc.
- **View Draft button**: In the blog post edit page there's a new button called `View Draft` to help you visualise the post you're writing in your blog. It simply set the `status` metadata as *draft* in that post.
- **Better post management**: Blog posts had a very bad management earlier. Now the model list page has filters, more fields being displayed, search, date hierarchy, etc.

Bugfixes
--------
- **Encoding issues**: Some people were experiencing encoding issues when *pelican_admin* attempted to write special characters. Some of it were solved, but if you find any mode problems, please, let me know.
- **Slow build**: Due to poor programming, *pelican_admin* was taking a very long time to run it's \__init__.py

Known Issues
------------
*pelican_admin* is running `Pelican <https://github.com/getpelican/pelican>`_'s service in background as a subprocess, but I wasn't able to kill it when python dies. Currently there's a method registered in `atexit` therefore, if python dies normally, the background service is killed with no trouble, but if python crashes, the method registered isn't called and `Pelican <https://github.com/getpelican/pelican>`_'s service may still be running in background.

Other than that, when you're running Django in "development mode" (`manage.py runserver`), every time you update a `Setting` in *pelican_admin*, Django is reloading. I'm still to find out why.

If `pelican <https://github.com/getpelican/pelican>`_ raises an Exception from within it's Generators, *pelican_admin* thinks it's still running since the subprocess doesn't die, even though it's running in the background. When an Exception like that occurs, `pelican <https://github.com/getpelican/pelican>`_'s process simply halts.

Old Features
------------
- **Settings management**: change your pelican settings through Django admin and have it automatically working.
- **Posting management**: CRUD for blog postings via interface.
- **Service management**: Manage your pelican service through the admin interface
- **Internationalization**: *pelican_admin* is localizable. Currently only pt_BR and en_US are officially supported.

Requirements
------------
* `Django 1.4+ <http://pypi.python.org/pypi/Django/1.4>`_
* `psutil 0.6.1+ <http://code.google.com/p/psutil/>`_
* `pelican 3.0+ <https://github.com/getpelican/pelican>`_

Installation
------------
I'll just assume you're already familiarised with pelican and move on.

Install using pip:

    pip install pelican_admin
    
Or you can clone the project and install it via:

    python setup.py install
    
Migration From Older Versions
-----------------------------
When you migrate, whether installing from pip or cloning the repository, do not forget to sync the app. You can either do it through Django or using south, though south is better because you won't lose any data.

Check This Out
--------------
1. `GitHub Repository <https://github.com/fjcaetano/pelican_admin>`_
2. `PyPi package <http://pypi.python.org/pypi/pelican_admin/0.3>`_
3. `Owner's website <http://flaviocaetano.com>`_
4. `Owner's Blog <http://blog.flaviocaetano.com>`_


Contact
=======
If you have any comments, ideas questions, feedback, etcetera, email me and we'll be in touch. I'm `flavio@vieiracaetano.com <flavio@vieiracaetano.com>`_