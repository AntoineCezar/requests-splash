===============
Requests Splash
===============

v0.1.0

`Splash`_ headless browser adapter for `Requests`_.

.. _`Splash`: https://splash.readthedocs.io/
.. _`Requests`: http://docs.python-requests.org/


Quick Start
-----------

First run a splash instance:

.. code:: shell

    sudo docker run --rm --name=splash -p 8050:8050 scrapinghub/splash

Then you can start your requests:

.. code:: python

    from requests_splash import Session

    with Session() as session:
        response = session.get('https://example.com')

Install
-------

Requirements for Installing Package:

* `pip` for installing packages
* `python3 -m venv venv` for creating a virtual environment.
* `setuptools >= 30.3.0` (to configure setup() using setup.cfg)

See the Python Packaging Authority's (PyPA) documention `Requirements for Installing Packages`_ for full details.

.. _`Requirements for Installing Packages`: https://packaging.python.org/tutorials/installing-packages/#requirements-for-installing-packages

On a Unix/Linux System
~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    $ export VENV=~/path/to/venv
    $ python3 -m venv $VENV
    $ $VENV/bin/pip install requests-splash

For development use:

.. code:: sh

    $ export VENV=~/path/to/venv
    $ python3 -m venv $VENV
    $ cd /path/to/requests-splash
    $ $VENV/bin/pip install -e . ".[develop]" ".[testing]"

A convenient Makefile is provided to ease development:

.. code:: sh

    $ make develop

For more useful commands run:

.. code:: sh

    $ make help

On a Windows System
~~~~~~~~~~~~~~~~~~~

.. code:: sh

    c:\> set VENV=c:\path\to\venv
    c:\> python -m venv %VENV%
    c:\> %VENV%\Scripts\pip install requests-splash

For development use:

.. code:: sh

    c:\> set VENV=c:\path\to\venv
    c:\> python -m venv %VENV%
    c:\> cd \path\to\requests-splash
    c:\> %VENV%\Scripts\pip install -e . ".[develop]" ".[testing]"


License
-------

BSD license
