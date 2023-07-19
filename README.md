# seedtrack
Tracks seed falling in video

![Example of a frame showing the tracked seed, using the tool](example.png)

# Requirements

For the tracking component you will need:
- numpy
- opencv-python

(e.g. pip install opencv-python)

# Install

To install this module, run:

```
pip install git+https://github.com/lionfish0/seedtrack.git
```

# Commandline usage

```
usage: seedtrack *.MP4
```

by default it:
- creates a diagnositic png file of slices of frames of the original video that should have seeds in. Note that when a seed falls really fast an image might not be created [minor bug needs fixing]. This
- it adds a row to a CSV file. By default this is summary.csv, but can be altered with --recordfile option.

## Example commandline

```
seedtrack data/*.mp4 --recordfile records.csv
```

## Python import

To use in your python code, see the [demo notebook](https://github.com/lionfish0/seedtrack/blob/main/jupyter/Demo.ipynb).

## Known issues

- diagnostic images only created if seed is on the video for long enough.
- code assumes image is 1920 pixels wide.
- start/end times and diagnostic image is all decided using the results
  of the line fit. we assume that the seed falls at a constant speed
- not yet provided continuous velocity data (over time). (this is available
  also see the 'positions' variable returned by the getrawdata function,
  which this can be inferred from.

## Description of method from paper

Will include later.

## Citation

To cite this work please use [TBC].

