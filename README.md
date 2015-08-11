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

Here is an example from my library where the FLAC decoder was signaling a
corrupt file:

    beet bad title::^$
    /tank/Music/__/00.flac: command exited with status 1
      00.flac: *** Got error code 2:FLAC__STREAM_DECODER_ERROR_STATUS_FRAME_CRC_MISMATCH
      00.flac: ERROR while decoding data
                 state = FLAC__STREAM_DECODER_READ_FRAME
