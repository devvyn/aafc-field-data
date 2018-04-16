---
layout: post
title: "Writing Purposefully: Choose a Target Audience"
author: Devvyn P M (Devin Murphy)
date:   "2018-04-15 17:15:23 -0600"
categories: personal writing
---
# I Started with Simple Intentions

I recently started a project that involves exploring an Excel
spreadsheet file. I began analysis in a [Jupyter] notebook, which is a
document format as well as a place to analyze data.

The initial purpose of the notebook was to rapidly construct a
workspace within which to probe the data using _pandas_, and the
highest priority was producing usable output in the form of more
spreadsheet files.

After many hours, I developed a document that shows my work so far,
with examples based on real spreadsheet files. With about 80% of the
work complete, and the notebook document 25 pages long, I faced an important
question: _who will read all of this?_


# Beneficial Side Effects of Doing Work in Jupyter Notebooks

The [Jupyter] notebook allows data, code, and prose to coexist in the same
document, which is great for documenting the techniques and processes
of one's data analysis work.

As a side effect of documenting my process along the way, with
true examples and sources, I developed a valuable instructive document.
Another person could, given a certain degree of preparedness,
comprehend the document and repeat my analytical steps with great
accuracy.

If I've made a mistake, it should be obvious from the document itself,
because the reproducible steps appear in writing. Re-running the code
may not be required to verify an error.


# Downsides of Writing for Multiple Audiences

Unfortunately, because educating others wasn't on my mind during the
early stages of the analysis, there are numerous issues with this
document as a piece of instructional writing. While writing it with
only the end results in mind, I'd left out explanations that I take
for granted.

To serve as more than my personal notebook of work done, the notebook
must be revised with an editor's perspective. Specifically, an
audience must be identified and targeted.

## If the audience is ...

### Myself:

I should explain only the newly learned
knowledge, such as the analytical results of the project data.


### Likely to want to interact with the notebook in Jupyter:

I should introduce the audience to the ways they can do that, and sources of
additional learning about Jupyter.


### Someone who has never programmed before:

I should explain rudimentary Python concepts wherever they aren't
obvious from the code shown in the document.


### Someone who has never worked with data science tools such as _panda:

I should explain the basic concepts surrounding collections of indexed data.


### Familiar with a different set of data science tools, such as _R_:

I should learn the differences and offer comparisons and notes about the differences.


### If I don't know enough about my audience:

I should write for the most likely cases.

## Initial Reaction

Once I realized that I may be leaving people out, I started including more
explanations and links to other documents. Subsequently, the document has
grown considerably, and lost some of its original focus.


## Responding to Loss of Focus in Writing

After discovering that writing for multiple audiences is something that
detracts from my focus on usable data output, I tried to stop writing
entirely, and decide whether it would be better to split the document
apart, into a generally instructional document and a project report,
or to maintain it all as a single document.


## Pondering a Quick Way Out

Maybe it would be better to omit the how-to portion entirely, if it's nothing
more than noise. I'm mostly done with the analysis of the source file,
and need only write a few more paragraphs to conclude the written
portion of this project, if usable data file output is the only required
outcome.

However, it would be a shame to lose an opportunity to share knowledge
if the document isn't useful for learning due to unfocused writing and rushed
editing.


# _Editing_ for Multiple Audiences

## Base Revision

Unlike writing from scratch, editing can be done from a
foundation of text and allow the editor to explore multiple revisions based
upon that common starting point.

With a base revision, it's possible to attempt multiple paths to a finished
edition and prioritize the most valuable or most timely ones depending on the
situation. In a best case scenario, multiple editions can fullfil
multiple needs.

If editing in a certain direction reveals gaps in the text, it becomes
obvious that more writing will be required.

If an attempt to edit the text for a certain purpose is unsuccessful,
the original basis of the revision can live on without the unnecessary,
unfinished portions.


# Moving forward


## My main audiences:

* Scientific researchers
* People with knowledge of statistics
* Non-programmers
* Myself, for reference


## Trial Edit

I decided to print out the notebook and proofread it on paper, with ink
in hand to mark it for corrections. If it becomes obvious that the
document would require too much work to be useful as an educational
piece, I would split it apart. If it would need only minor refinement, I
would finish writing in the educational style.


## Editing Towards the Next Revision

Now that I've done the edit on paper, I can see that most of the
document that was written while I was learning about _pandas_ and
checking my understanding at each step along the way demonstrates the
learning process as part of the lesson. This "learn with me" format is
probably good for instruction because leads to answering more questions that
other newcomers will be likely to ask.

The biggest shortcomings are structural, with only a small amount of missing
content. My brief explanation of Python data structures was relevant, but needed
to be repositioned in the flow of the overall document.

Overall, I think this is a good learning resource for people who have
not programmed, not used Jupyter, and who may or may not want to reproduce my
results. It just needs a final revision to fill the gaps and structure it as
a learning document which happens to produce usable output.

Now I can approach the final portion of analysis work as a focused writer,
because I know my audience. I expect to get good results in the writing
as well as the analysis. I won't be hesitating each time I begin a
paragraph or code block, wondering if I'm working against myself.

[Jupyter]: https://jupyter.org/
