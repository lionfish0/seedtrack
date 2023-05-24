# seedtrack
Tracks seed falling in video

![Example of a frame showing the tracked seed, using the tool](example.png)

# Requirements

For the tracking component you will need:
- numpy
- opencv-python

To use the dataset, you will need:
- pandas

For rendering to a file you will also need
- moviepy

Install with, for example:
`pip install moviepy`

# Install

To install this module, run:

```
pip install git+https://github.com/lionfish0/seedtrack.git
```

# Commandline usage

```
usage: seedtrack [-h]
```
(will update later)

## Example commandline

Render to a file (default with suffix '_track')
```
seedtrack data/*.mp4 -r
```

Record to a CSV (default name, summary.csv)
```
seedtrack *.mp4 -s
```

## Python import

To use in your python code, see the [demo notebook](https://github.com/lionfish0/seedtrack/blob/main/jupyter/Demo.ipynb).

## Description of method from paper

Will include later.

## Citation

To cite this work please use [TBC].

