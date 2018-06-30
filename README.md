# soco-remote
SoCo-Remote
====
I have a TV line out connected to a Sonos Connect:Amp and I needed a way to control the Sonos volume with my TV remote, so I built SoCo-Remote. SoCo-Remote is a basic background app that will listen for keyboard hotkeys and then trigger SoCo functions to control volume up/down of a Sonos player. I use this with a Raspberry Pi and a `FLIRC USB`_ that I have programmed to trigger those (full) keyboard hotkeys based on volume up/down IR calls from my TV remote.

SoCo-Remote uses SoCo (Sonos Controller) for all it's magic, which is a Python project that allows you to programmatically control `Sonos speakers`_. Visit the `SoCo documentation`_, or check out the `GitHub repository`_ for a more detailed overview of all the functionailty.

Installation
------------

SoCo-remote requires Python 2.7, or 3.4 or newer and SoCo and Keyboard packages.

Use pip:

``pip install soco``


``pip install keyboard``

If you want to run this as a systemd service, you'll need to copy the service file to your systemd directory and enable it.

``sudo mv soco-remote.service /etc/systemd/system/soco-remote.service``

``sudo systemctl daemon-reload``

``sudo systemctl start soco-remote``

``sudo systemctl status soco-remote``

``sudo systemctl enable soco-remote``

Related Projects
----------------

Socos is a command line tool for controlling Sonos devices. It is developed
in conjunction with Soco, but in a `separate repository <https://github.com/SoCo/socos>`_.

License
-------

SoCo-Remote is released under the `MIT license`_.

.. _Sonos speakers: http://www.sonos.com/system/
.. _MIT license: http://www.opensource.org/licenses/mit-license.php
.. _GitHub repository: https://github.com/SoCo/SoCo
.. _SoCo documentation: https://soco.readthedocs.org/en/latest/
.. _FLIRC USB: https://flirc.tv/more/flirc-usb