---
layout: post
title:  "Cleaning Badly Formed CSV Data"
date:   "2018-04-05 15:18:56 -0600"
categories: data-cleaning
---
## The Problem

I'm tasked with merging two Excel spreadsheets which researchers and
their associates created by importing CSV files from an old version of
an Android app which the research centre is using to collect field data
about insect pests on food crops. The data is simple, but the CSV files
are obtusely formatted.


### How it should be

The creator of regular, well-formed data files organizes them into
columns with clear names and rows which list the relevant data according
to those columns. This way, you can pick any row in the file that
happens to have, let's say, a relevant date on which an observer counted
the insects, and all the related data for that date are in the same row,
under corresponding columns.

| date                    | observer | sample # | BCO aphids | EGA aphids | aphid_mummies_brown | aphid_mummies_blk | lady_beetle_larvae | lady_beetle_adult | lacewing_larvae | lacewing_adult |
|:------------------------|:---------|---------:|-----------:|-----------:|--------------------:|------------------:|-------------------:|------------------:|----------------:|---------------:|
| 2017-07-14T12:31:24.194 | Tyler    |        1 |          7 |          0 |                   1 |                 1 |                  0 |                 0 |               0 |              0 |
| 2017-07-14T12:31:24.194 | Tyler    |        2 |          0 |          0 |                   0 |                 0 |                  0 |                 0 |               0 |              0 |


### How it is (sadly)

This is how the same data appears in the files needing cleanup:

| fields\_\_oSets\_\_date | fields\_\_oSets\_\_obsName | fields\_\_oSets\_\_oPoints\_\_id | fields\_\_oSets\_\_oPoints\_\_name | fields\_\_oSets\_\_oPoints\_\_observations\_\_id | fields\_\_oSets\_\_oPoints\_\_observations\_\_name | fields\_\_oSets\_\_oPoints\_\_observations\_\_enum | fields\_\_oSets\_\_oPoints\_\_observations\_\_a1\_\_number | fields\_\_oSets\_\_oPoints\_\_observations\_\_a2\_\_number | fields\_\_oSets\_\_oPoints\_\_observations\_\_a3\_\_number | fields\_\_oSets\_\_oPoints\_\_observations\_\_&#124; | fields\_\_oSets\_\_oPoints\_\_observations\_\_&#124;\_\_number |
|:------------------------|:---------------------------|:---------------------------------|:-----------------------------------|:-------------------------------------------------|:---------------------------------------------------|:---------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------------------------|:---------------------------------------------------------------|
| 2017-07-14T12:31:24.194 | Tyler                      | 0                                | Observation Point 1                | 0                                                | Aphid Observation 1                                |                                                    | 7                                                          | null                                                       | null                                                       |                                                      |                                                                |
|                         |                            |                                  |                                    | 1                                                | Aphid Observation 2                                |                                                    | null                                                       | null                                                       | null                                                       |                                                      |                                                                |
|                         |                            |                                  |                                    | 2                                                | Aphid Observation 3                                |                                                    | null                                                       | null                                                       | null                                                       |                                                      |                                                                |
|                         |                            |                                  |                                    | 3                                                | Aphid Observation 4                                |                                                    | null                                                       | null                                                       | null                                                       |                                                      |                                                                |
|                         |                            |                                  |                                    | 4                                                | Aphid Observation 5                                |                                                    | null                                                       | null                                                       | null                                                       |                                                      |                                                                |
|                         |                            |                                  |                                    | 5                                                | Natural Enemy Observation                          | 2                                                  |                                                            |                                                            |                                                            | e1                                                   | 1                                                              |
|                         |                            |                                  |                                    |                                                  |                                                    |                                                    |                                                            |                                                            |                                                            | e2                                                   | 1                                                              |
|                         |                            |                                  |                                    |                                                  |                                                    |                                                    |                                                            |                                                            |                                                            | e3                                                   | null                                                           |
|                         |                            |                                  |                                    |                                                  |                                                    |                                                    |                                                            |                                                            |                                                            | e4                                                   | null                                                           |
|                         |                            |                                  |                                    |                                                  |                                                    |                                                    |                                                            |                                                            |                                                            | e5                                                   | null                                                           |
|                         |                            |                                  |                                    |                                                  |                                                    |                                                    |                                                            |                                                            |                                                            | e6                                                   | null                                                           |
|                         |                            |                                  |                                    |                                                  |                                                    |                                                    |                                                            |                                                            |                                                            | e7                                                   | null                                                           |
|                         |                            |                                  |                                    |                                                  |                                                    |                                                    |                                                            |                                                            |                                                            | e8                                                   | null                                                           |
|                         |                            |                                  |                                    |                                                  |                                                    |                                                    |                                                            |                                                            |                                                            | e9                                                   | null                                                           |

I truly wish I were joking. The names of the specimens aren't even present
in the data. The columns are mostly empty. Some data goes across and
some goes downward as you read it. It's a mess. This example table has
been significantly trimmed, so imagine the actual quagmire one would
wade through by hand and eyes alone.

Sure, it's logical in its own way, but this is no way handle data that
scientists need united with other data sets. Imagine having 200
observation points that you needed to get numbers from. Someone asks you
how many ladybird beetles there were on a given date in a given field:
how would you answer that question? What about the ratio of natural
enemies to English grain aphids amongst only wheat fields within a
certain month? This is a real problem.


### Processing by hand

Okay, sure, it's possible to spend a few hours a day copying and pasting
into a new sheet, until it's all fixed up---but what happens if you
suspect an error somewhere in the processes? Would you retrace your
steps? Re-do a suspect area of a sheet? How would you even confirm the
lack of an error?


## The Solution

So, tedious copying and pasting for hours or days in Excel is out.
What's the reliable, repeatable, fast, and accurate solution? Automation!


### Language choice: Python

I'm already comfortable in Python and for beginners, Python has a
shallower learning curve while still being powerful and ubiquitous.

I'm a fan of Python, because as far as programming languages go, it's
natural and expressive. If you have a list of items, for example, and
you want to filter and transform them, it's easy:

```python
crops = ['Wheat', 'Barley', 'Oats', 'Beans'] 
thoughts_on_crops = [f'I love {crop}!' for crop in crops if crop != 'Wheat']
```

The results, if displayed, would be:

```python
print(thoughts_on_crops)
['I love Barley!', 'I love Oats!', 'I love Beans!']
```

Once you get used to things like the square brackets for lists, and a
few other aspects of the syntax, it starts to feel like plain English a
lot of the time. Very useful when you want to reserve your brainpower
for problem solving with messy data.


### Data framework of choice: pandas

From https://pandas.pydata.org/:

>### Python Data Analysis Library
>
>*pandas* is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the  [Python](https://www.python.org/) programming language.

A nice thing about *pandas* is that it handles columnar data in a way
that users of *R* might expect. *NumPy* is another, similar data
framework you'll hear data scientists talk about---in fact, *pandas*
uses *NumPy* internally.

A big part of the reason for choosing *pandas* is that I don't want to
get my hands dirty with *R*.


### Document format for showing work in progress: Jupyter

In earlier log entries, I've extolled the virtues of using Jupyter to
share the results of data analysis. I'm not the only one---check the web
for "data science notebook" and see what comes up.

While I figure out a good series of commands to read the data, find the
start of each section, and assemble the related points into a nice set
of ordered outputs, I'll use a Jupyter notebook to run the Python
commands and display bits of data as I go. By the time I'm done the job,
the notebook will contain all the commands in sequence, with comments
explaining my decisions.

Anyone who wants to check my work or recreate the resulting output can
load the notebook (possibly on mybinder.org) and hit the play button to
re-run the calculations.


## Outline of Approach

My thoughts on solving this problem by reading data into *pandas*:

* certain columns have mostly blank/empty/null values under them, except
  for when a new section of the file begins
* I can detect the beginning of a section by looking in a relevant
  column for non-null values, then reading from that row until the next
  non-null value
* while "inside" a section, certain columns are irrelevant
* when data starts flowing downward instead of across, it's easy to
  select a vertical range of values and assign them to a range of
  columns in a new data frame, for later output
* once I populate all the columns in the new data frame, the results can
  be output to a new file
* file writing to Excel or CSV is straightforward with *pandas*---Excel
  format would specify the type of data in each column
