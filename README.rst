=============
WebHomeControl
=============

The WebHomeControl project provides users a way to interface with the PiHomeControl project via a web interface.

Download
-------

To install latest::

    pip install git+git://github.com/marbaugh/PiHomeControl.git


Config
-----

Once installed you can configure the routes.py file for Flask::

    MAIL_USERNAME and MAIL_PASSWORD for the email address used to send email notifications

    A SQLite database must be created in /tmp/webhomecontrol.db with a table names status with columns ID, Hardware, Time, and Status.

    THe "host" variable  can be set at the bottom of the file to tell the Flask server where to run



Usage
-----

Once installed you can simpy run the routes.py file for Flask::

    python routes.py
    
