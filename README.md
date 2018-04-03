Field data tools for Agriculture and Agri-Food Canada
=====================================================

[![launch binder]][Binder this repo]

## Quick start

Click the "launch binder" button in this document to open Jupyter and
access the project files.

Look inside the `notebook` folder for Jupyter notebooks you can use.

If something in a notebook seems to have failed to load or display
properly, try re-running the cells.

You can refresh the notebook's calculations and widgets in the menus at
the top of the page: _Cell_ &rarr; _Run All_.


### Project pages

- [Home page and log][GitHub Pages] on GitHub Pages
- [Interact in Jupyter][Binder this repo] on _mybinder.org_
- [Planning and issue tracking][github-project] on GitHub Projects
- [Source code and datasets history][github-repo] on GitHub


Feature goals:
--------------

In this release, only basic features are available, such as starting a
[Jupyter Notebook][jupyter.org] server to interact with the datasets
that are included with this project.


**Long term goals:**

- import data files with import/export helpers
- pre-made "dashboard" notebooks, for data querying and analysis
- export query results as files
- support for data file formats in and out:
  - CSV (comma separated or tab separated)
  - Excel (Microsoft Office)
  - ODF (Open Document Format)
- database of well-structured data for research
- database management helper
- REST API for remote access without Jupyter Notebook (usable by Access,
  Excel, and other applications)


About Bundled Datasets
----------------------

Data files in this repository are from real research projects at
Agriculture and Agri-Food Canada, and will be used in published papers.
You can find them in [`notebook/src/`][datasets].


About Jupyter Notebook
----------------------

Description from [jupyter.org]:

> The Jupyter Notebook is an open-source web application that allows you
> to create and share documents that contain live code, equations,
> visualizations and narrative text. Uses include: data cleaning and
> transformation, numerical simulation, statistical modeling, data
> visualization, machine learning, and much more.

[![jupyterpreview]][Try Jupyter]

You can [try Jupyter now][Try Jupyter], to get a feel for it. Various
languages are available, including Python, R, and Julia.


### mybinder.org on the Web

**Recommended for:**

* **sharing notebooks**
* **working anywhere**


#### mybinder.org Advantages:

* **can open notebooks, code, and data files from any GitHub
  repository**
* no software installation required
* free to use
* available anywhere with a browser


#### mybinder.org Disadvantages:

* the workspace is destroyed after a certain period of inactivity
* changes you make during a session don't automatically transfer back to
  the repository they originally came from


### Docker Container on Any Operating System

**Recommended for:**

* **making technical changes to this project**
* **maintaining total privacy**


#### Docker advantages:

* **automatically shares files between your computer and the
  containerized Jupyter Notebook file system, so your work persists
  between sessions**
* all files are under your control, and stay on your computer unless you
  send them elsewhere
* can be accessed without an ongoing connection to the Internet


#### Docker disadvantages:

* requires Docker to be installed on your computer, which requires
  administrator access
* doesn't automatically publish or help you share your work


Using Jupyter Notebook with this project
----------------------------------------

To use Jupyter Notebook with the tools and example data in this project,
you can do one of the following:

* upload your notebooks and data to GitHub (like this project)
* use the "upload" button on any Jupyter server
* start your own Jupyter server on your computer


### mybinder.org

Access this repository on [mybinder.org] right now:

[![launch binder]][Binder this repo]


### Docker launched by _repo2docker_

#### Prerequisites for using repo2docker

- Docker
- Python 3


#### Installing Docker

To get **Docker** on your system, go to the [Docker Store] and follow
the appropriate steps depending on which edition of Docker is the best
fit. For most cases, when running Docker on your personal or work
computer, the **Community Edition** is sufficient.

You can also
[download the Community Edition of Docker][docker-ce download] for your
specific operating system instead of entering through the
[Docker Store], if that's all you need. Instructions will be provided
there.


#### Installing Python

Many operating systems come with Python, so you may not need to install.
Check your Python version before deciding to download.

If you type this command and see something similar, you're good to go!

```sh
$ python3 --version
Python 3.6.3
```

If you see an error about a missing file or unknown command, you don't
have Python 3 ready to use. Downloading the newest release may be a good
idea.

```
python3: command not found
```

To download and install Python for your operating system, see:

- https://www.python.org/downloads/


#### Installing _repo2docker_

Once Python 3 is ready to use, install **repo2docker**. Instructions are
at:

- http://repo2docker.readthedocs.io/en/latest/install.html

At the moment, these are the recommended instructions from that page:

>We recommend installing repo2docker with the pip tool:
>
>```
>python3 -m pip install jupyter-repo2docker
>```
>>
>For information on using repo2docker, see [Using repo2docker].


#### Starting the notebook server with repo2docker

On your computer, open a shell terminal. On the command line, from
within the project directory, execute the command that's appropriate for
your operating system.

Linux, BSD, macOS:

```sh
jupyter-repo2docker --image-name jupyter-server -v $PWD:/home/$USER .
```

Windows:

```sh
jupyter-repo2docker --image-name jupyter-server -v $CD:/home/$USERNAME .
```

The first time you run this command, the necessary image will be built,
which may take a few minutes. After a while, some text will appear,
containing the URL to visit in your web browser to start your session
with Jupyter Notebook.

```
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://0.0.0.0:60019/?token=4898a3ae6fc2f380588543cabb895c62df62280ab13ccdbf
```

Copy the entire URL from your console, beginning with `http:`, including
the `?token=…` part, and paste it into your browser's URL bar to go that
address. At this point, you're not on the Web, but your own computer,
which has a "web server" for you. You should see a file browser page
with the Jupyter logo on it, and your project files.

![jupyter-localhost]


[Binder this repo]: https://mybinder.org/v2/gh/devvyn/aafc-field-data/master
[mybinder.org]: https://mybinder.org/
[datasets]: https://github.com/devvyn/aafc-field-data/tree/master/notebook/src
[Docker Store]: https://store.docker.com/
[docker-ce download]: https://www.docker.com/community-edition#/download
[github-project]: https://github.com/devvyn/aafc-field-data/projects
[github-repo]: https://github.com/devvyn/aafc-field-data
[GitHub Pages]: http://aafc.devvyn.io/
[jupyter-localhost]: /docs/static/jupyter-localhost.png "Jupyter Notebook on localhost"
[jupyter.org]: https://jupyter.org/
[jupyterpreview]: /docs/static/jupyterpreview.png "Jupyter Notebook web page screen shots"
[launch binder]: https://mybinder.org/badge.svg "launch binder (button)"
[Try Jupyter]: https://jupyter.org/try
[Using repo2docker]: http://repo2docker.readthedocs.io/en/latest/usage.html#usage

