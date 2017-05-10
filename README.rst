========
Overview
========

This is a wiki application for `Mezzanine
<http://mezzanine.jupo.org/>`_, a content management platform using
the Django framework. Its features are:

- markdown syntax with [[Wiki links]] extension
- page history and diff viewing

Its current requirements are:

- mezzanine >= 4.0
- markdown
- diff-match-patch

Its former requirements are:

- south (now deprecated as of Django>=1.7)

===========
Quick start
===========

1. Download or clone and run:

    python setup.py install

2. Add "mezzanine_wiki" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'mezzanine_wiki',
    )

3. Run the following code to create the models:

   python manage.py makemigrations mezzanine_wiki
   python manage.py migrate

4. Include the wiki URLconf in your project urls.py like this::

   url(r'^wiki/', include('mezzanine_wiki.urls')),

5. Add "mezzanine_wiki.WikiPage" to SEARCH_MODEL_CHOICES setting like this:

    SEARCH_MODEL_CHOICES = ('pages.Page', 'blog.BlogPost', 'mezzanine_wiki.WikiPage')

6. Restart the server.

7. At this stage, you can visit the /wiki/ url, but it will give you a
"You don't have permission to add new wiki pages." It helps if you
create a mock web page first (using the admin panel), and then visit
/wiki/ to set up a default Main page.

8. Finally, add a new Rich Text Page with the name "Wiki". This will add
the wiki to the menu.
