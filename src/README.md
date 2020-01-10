GNOME Dictionary
===============================================================================

### Look up words in dictionary sources.

GNOME Dictionary is a simple, clean, elegant application to look up words in
online dictionaries using the [DICT][dict-rfc] protocol.

## Building Dictionary

In order to build GNOME Dictionary you will need:

  - a C99 compatible compiler
  - Python 3
  - [Ninja](https://ninja-build.org)
  - [Meson](http://mesonbuild.com)

You will also need the development files for:

  - GLib 2.x
  - GTK+ 3.x

After cloning the `gnome-dictionary` repository, enter the source directory
and configure the project using:

```sh
$ meson _build .
```

Where `_build` is the location where the build artefacts should be placed.
After the configuration succeeds, you can build, test, and install GNOME
Dictionary using:

```sh
$ cd _build
$ ninja
$ meson test
$ sudo ninja install		# Will install under /usr/local by default
```

If you wish to install in a different prefix, use the `--prefix` command
line option for `meson`.

[dict-rfc]: https://tools.ietf.org/html/rfc2229
