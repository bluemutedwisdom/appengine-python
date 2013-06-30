Google AppEngine Python SDK - Cloud development
===============================================

The Python language version of the `Google App Engine SDK`_ enables
developers to build Python web applications that can be hosted on
Google's App Engine platform, on the same scalable infrastructure
that power Google's own applications. App Engine applications are
easy to build, easy to maintain, and easy to scale.

We also have versions of the Google App Engine SDK for the `Java`_
and `Go`_ programming languages.

This appliance includes all the standard features in
`TurnKey Core`_, and on top of that:

-  Google AppEngine SDK configurations:
   
   -  Installed from upstream source code to
      /var/www/google\_appengine
   -  Preconfigured cgi, webapp and django appengine application
      templates:
      /var/www/appengine/template-\*

   -  Template-Django is `preconfigured for NoSQL`_.
   -  Includes Python imaging library (PIL) for appengine Image API.
   -  Includes welcome page with useful information and link to
      offline documentation.

-  Includes TurnKey Web Control panel with useful information,
   references, and link to offline documentation (convenience).

-  Postfix MTA (bound to localhost) to allow sending of email
   (e.g., password recovery)

-  Includes Webmin Postfix module.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH: username **root**

.. _Google App Engine SDK: https://developers.google.com/appengine/
.. _Java: http://www.turnkeylinux.org/appengine-java
.. _Go: http://www.turnkeylinux.org/appengine-go
.. _TurnKey Core: http://www.turnkeylinux.org/core
.. _preconfigured for NoSQL: http://www.allbuttonspressed.com/projects/djangoappengine
