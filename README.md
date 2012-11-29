pelican_admin
======================
*pelican_admin* was developed to assist you manage your [Pelican] blog.

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
	
Now, you must tell *pelican_admin* what's the path to you pelican blog. In your settings.py you must add:

	PELICAN_PATH = '/path/to/your/blog'
	PELICAN_SETTINGS = 'your_pelican_settings.py # The default value is 'pelicanconf.py'
	PELICAN_BIN = 'pelican' # Path to pelican executable. Default value is '/usr/local/bin/pelican'
	
Make sure your pelican service is running in `autoreload` mode:

	pelican /path/to/your/blog -s /path/to/pelican/settings -r &
	
	
This will have your pelican to reload itself whenever your folder blog changes. Without this configuration, **pelican_admin** is pretty much useless. So be sure to use it.
	
If you're using [django-admin-tools] there's a module available where you can manage your pelican service via admin interface. Add *pelican_admin* to your urls.py:

	import pelican_admin
	
	url_patterns = patterns('',	
    	url(r'^admin/', include(admin.site.urls)),
	    url(r'^admin_tools/', include('admin_tools.urls')),
	   	...
	)
	
	urlpatterns += pelican_admin.pelican_urls()
	
And finally, add *pelican_admin*'s module to your dashboard.py:

	from pelican_admin.modules import PelicanAdmin
	
	class CustomIndexDashboard(Dashboard):

    	def init_with_context(self, context):
			...
	        self.children.append(PelicanAdmin())
	        
This module is super useful not only to check [Pelican]'s service status, but also to reload it if any change you made doesn't load.
	        
The Looks
---------

This is how *pelican_admin*'s module for [django-admin-tools] looks like when enabled:

![Screenshot1](https://raw.github.com/fjcaetano/pelican_admin/master/ss1.png)

![Screenshot2](https://raw.github.com/fjcaetano/pelican_admin/master/ss2.png)

![Screenshot3](https://raw.github.com/fjcaetano/pelican_admin/master/ss3.png)


Features
--------

- **Settings management**: change your pelican settings through Django admin and have it automatically working.
- **Posting management**: CRUD for blog postings via interface.
- **Service management**: Manage your pelican service through the admin interface
- **Internationalization**: *pelican_admin* is localizable. Currently only pt_BR and en_US are officially supported.

Requirements
------------
* [Django 1.4+](http://pypi.python.org/pypi/Django/1.4)
* [psutil](http://code.google.com/p/psutil/)

Installation
------------
I'll just assume you're already familiarised with pelican and move on.

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

[django-admin-tools]: https://bitbucket.org/izi/django-admin-tools/wiki/Home
[pelican]: (https://github.com/getpelican/pelican)