Scripts for Emby -> Jellyfin Migration
====================

Scripts to ease the migration between servers

* release 0.1
* open source: https://github.com/tiedtoastar/emby2jellyfin-Migration-Scripts
* Jellyfin is the FREE & OPEN SOURCE media player
* works with Jellyfin 10 and Emby 4.*
* Python 3.x compatible

Copyrights
----------

Released under the BSD 3-Clause License. See `LICENSE.txt`_.

Copyright (c) 2019 TiedToAStar <TiedToAStar@protonmail.com>

.. _`LICENSE.txt`: LICENSE.txt

Want to help?
-------------

If you find this project useful, please consider a donation to the following Monero address:
``47q3TVnd79QcMLqFE2HJC5HTWDadUXtMDVavERPfeT3xFiBeqQQX6knBNALTz4aciC6pSbnLoMCHXXsQDCPV1BT7TqoqZxW``

Haven't heard of Monero? Then do me the favor by checking out: https://www.getmonero.org/

Available Scripts
-----------
* usermigration.py : User Migrations
* * Description: This script will recreate all your Emby users, with their specified policies and configurations on another server.
* * Usage notes: The script will prompt you via the command line for your current media server information (IP/PORT/ADMIN user) and then again for you the destination media server.



Usage
-----------

1. Clone the repo

2. Create virtualenv & activate it

.. code-block:: bash

    python3 -m venv .venv
    source .venv/bin/activate

3. Install dependencies

.. code-block:: bash

    pip install -r requirements.txt -r test_requirements.txt

4. python <scriptname>.py

4a. The script may ask you for command line input

