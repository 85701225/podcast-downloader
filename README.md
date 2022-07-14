# Quick and dirty podcast downloader

Just a quick script I threw together to pull all episodes in a podcast feed.

Speed and ease took precedence over good form.

There are minimal deps, and I have only tested under Python 3.9.

To use, create a venv, install the deps, and copy sample-config.ini to 
config.ini.  In the newly created config.ini, settings are commented.

Episodes land in episodes/ and are named as the episode title, with spaces
replaced by underscores.

See LICENSE for MIT license.
