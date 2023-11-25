# xmas-tree-lights

This repository is shameless ripped from Matt Parker's xmastree2020 project, with changes to project organization, some lighting examples, and installation made by me.

From the original: "This repository contains the code used for Matt's Christmas tree, as featured in ["I wired my tree with 500 LED lights and calculated their 3D coordinates"](https://www.youtube.com/watch?v=TvlpIojusBE)."

## Usage

This is a Python project which depends on [board](https://pypi.org/project/board/) for representing an n-dimensional board, and [neopixel](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage) for communicating with the LEDs.

With these packages installed, run `xmaslights-spin.py`.

## Contributing

You're welcome to contribute! There are a few different places that your PR could target:

- Small bug fixes, as well as small changes that significantly increase usability, will be accepted directly in to the original code.

- The `examples` folder has been created as a place for any effects contained within a single Python file. Files should be named based on the effect - `fire.py` for example.

- If you've done a bigger bit of work, consider keeping this in your own repository, and opening a PR to update the Further Work section below.


