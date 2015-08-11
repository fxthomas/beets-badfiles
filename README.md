Adds a `beet bad` command to check for missing, and optionally corrupt files.

# Installation

I haven't uploaded this plugin to PyPI, but you can install this by running
`pip` on the repository itself:

    sudo pip install .

# Configuration

Here is a very basic configuration, requiring the
[mp3check](http://sourceforge.net/projects/mp3check/) and
[flac](https://xiph.org/flac/) packages to be installed.

    badfiles:
      commands:
        mp3: mp3check -e
        flac: flac --test --warnings-as-errors --silent
    plugins: ... badfiles

With this configuration, MP3 files will be checked with mp3check, FLAC with the
flac decoder's `--test` mode and all other files for existence only.

# Running

To run Badfiles, just use the `beet bad` command with Beets' usual query syntax.

For instance, this will run a check on all songs containing the word "wolf":

    beet bad wolf

This one will run checks on a specific album:

    beet bad album_id:1234
