---
layout: post
title:  "Work Anywhere With Jupyter"
date:   "2018-04-03 09:53:17 -0600"
categories: update
---

Update: Work Anywhere With Jupyter
----------------------------------

With the most recent update to this project, it's now possible to use
Jupyter on your local computer or on the Web, with 100% reproducible
results.

Furthermore, the data and notebooks bundled in this project are equally
available in both environments, in an interactive format.

The reason for this extreme portability is the relatively new technology
of "containerization". That's when software is wrapped in an abstract
version of what would typically be an entire computer system.

For usage instructions, see the [README] for this project on GitHub.

### Container?

As is the case with many modern server technologies, a Jupyter server
can be run within a [Docker container], so the exact setup and behaviour
of the server is completely reproducible and predictable no matter
whether you start it up on Windows, macOS, Linux, or any other operating
system that [supports Docker][docker-ce download].

A great number of cloud services operate in Docker or similar container
systems.

### On the Web at _mybinder.org_

Access this repository on [mybinder.org] right now:

[![launch binder]][Binder this repo]

If you visit that page, you'll see the files of the project laid out in
a file browser within the web page. You can click a notebook to open it,
and if you run any calculations, the results will appear in the
notebook.


#### How It Works

Under the hood, the website at [mybinder.org] is using a few open source
software utilities to make this possible. One of them is called
_repo2docker_, and its purpose is to create a Jupyter server on demand.
It does this with the help of containerization by [Docker].


#### The Upsides of Usinng _mybinder.org_

##### URLs are shareable

Because the whole process is based on web technologies, you can give out
a URL to any notebook so collaborators or other interested parties can
experience the genuine, predictable interaction opportunities you
created.


##### Protective isolation for multiple viewers

Because the project as seen on [mybinder.org] is downloaded from your
online repository at [GitHub.com], anyone can interact with it, and
they'll each get the same environment.

Because the server is in a container, the project workspace cannot be
damaged or corrupted by anyone, even when multiple people open the
project simultaneously. Each user can edit, save, delete, etc in their
own workspace.


#### The Downside of Using _mybinder.org_

Although you can edit your files through the web interface on
[mybinder.org], the changes won't automatically become permanent. You'll
have to export changed files if you want to keep them.


### On Your Computer

Just as the magic on [mybinder.org] is orchestrated by _repo2docker_, so
to can you have your own Jupyter server on your computer.

#### The Downside of the Local Server Approach

##### Some Installation Required

**Prerequisites:**

- Docker
- Python 3

If you don't have the ability to install software on your computer, this
option is not for you.

#### The Upsides of Using a Local Server Container

##### Create and Destroy at Will

If you can satisfy the prerequisites, you can easily create and destroy
your own Jupyter server at will, with no side effects.

When you need to run multiple servers for separate projects, there are
no conflicts, and each server gets a unique URL.

##### Your Project Files, Editable, Saved Automatically

When editing project files, whether they're spreadsheets, documentation,
or Jupyter notebooks, the files are maintained on your computer in
realtime. The Jupyter server is merely accessing them on your behalf, to
view, edit, or manage them through the web interface. You have the
option of working either way.

When you're satisfied with your edits, you don't have to export the
project from the web server, because it's already on your computer. This
is something the [mybinder.org] view of your project won't do.


[Binder this repo]: https://mybinder.org/v2/gh/devvyn/aafc-field-data/master
[Docker container]: https://www.docker.com/what-container
[docker-ce download]: https://www.docker.com/community-edition#/download
[Docker]: https://www.docker.com/what-docker
[launch binder]: https://mybinder.org/badge.svg "launch binder (button)"
[mybinder.org]: https://mybinder.org/
[README]: https://github.com/devvyn/aafc-field-data/blob/master/README.md
