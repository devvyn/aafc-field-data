Field data tools for Agriculture and Agri-Food Canada
=====================================================

[![Binder badge](https://mybinder.org/badge.svg)][Binder this repo]

- [Home page] and log on GitHub Pages
- [Interactive notebook][Binder this repo] on _mybinder.org_
- [Planning and issue tracking][github-project] on GitHub Projects
- [Source code history][github-repo] on GitHub


Planned features:
-----------------

- import data files
- database of well-structured data for research
- export query results
- support for data file formats in and out:

  - CSV (comma separated or tab separated)
  - Excel (Microsoft Office)
  - ODF (Open Document Format)


Datasets
--------

Data files in this repository are provided as examples of data that
needs cleaning. They are from real research projects at Agriculture and
Agri-Food Canada, and will be used in published papers.


Tools
-----

### Jupyter Notebook

Description from [jupyter.org]:

> The Jupyter Notebook is an open-source web application that allows you
> to create and share documents that contain live code, equations,
> visualizations and narrative text. Uses include: data cleaning and
> transformation, numerical simulation, statistical modeling, data
> visualization, machine learning, and much more.

[![jupyterpreview]][Try Jupyter]

To use Jupyter Notebook with the tools and example data in this project,
you probably have multiple options:

* commit your data to a repository and push it to GitHub, then open it
  in [Binder]
* upload the tools and data to an online server, such as the ones you
  can reach from the [Try Jupyter] page
* start your own server with Docker, on your computer


#### Binder

This is the recommended way to share your work with others, because
anyone can access it on the web, and it only requires you to publish
your files to GitHub beforehand.

Access this repository in Binder right now:

[![Binder badge](https://mybinder.org/badge.svg)][Binder this repo]


##### Pros:

* **can open notebooks, code, and data files from any GitHub repository**
* no software installation required (and no administrator access)
* files can be downloaded from the server to your computer
* notebooks can be exported for safe keeping or use elsewhere
* free to use, powered by BinderHub and JupyterHub, hosted in the cloud


##### Cons:

* the workspace is destroyed after a certain period of inactivity


#### Decker container

This is the recommended way to make changes to the technical aspects of
the project that are not involved in analyzing research data, or when
privacy or expediency are priorities.

Sometimes online servers are less available depending on conditions
which will be beyond your control, but your own machine can operate
efficiently regardless of network conditions on the outside.


##### Pros:

* **automatically shares files between your computer and the
  containerized Jupyter Notebook file system, so your work persists
  between sessions**
* all files are under your control, and stay on your computer
* can be accessed without an ongoing connection to the Internet, once
  the initial container image is downloaded
* notebooks can be exported for safe keeping or use elsewhere


##### Cons:


* **requires Docker to be installed on your computer, which requires
  administrator access**
* can open any GitHub repository, but you'll have to checkout the
  repository manually, to the shared files directory (`notebook`-->`work`).


##### Installing Docker

To get Docker on your system, go to the [Docker Store] and follow the
appropriate steps depending on which edition of Docker is the best fit.
For most cases, when running Docker on your personal or work computer,
the Community Edition is sufficient.

You can also
[download the Community Edition of Docker][docker-ce download] for your
specific operating system instead of entering through the
[Docker Store], if that's all you need. Instructions will be provided
there.


##### Starting the notebook server

For the purposes of discussion, the "project directory" refers to
whichever directory on your computer that contains all the files from
this repository (which is the one that contains this `README.md`).

On the command line, from within the project directory, execute:

```bash
docker-compose up
```

The first time you run this command, the necessary image will be
downloaded, which may take a few minutes. After a while, some text will
appear, containing the URL to visit in your web browser to start your
session with Jupyter Notebook.

```
jupyter-notebook_1  |     Copy/paste this URL into your browser when you connect for the first time,
jupyter-notebook_1  |     to login with a token:
jupyter-notebook_1  |         http://localhost:8888/?token=16765258e74775731c75d4492d872e62cec56738aebee652
```

Copy the entire URL from your console, beginning with `http:`, including
the `?token=…` part, and paste it into your browser's URL bar to go that
address. At this point, you're not on the Web, but your own computer,
which has a "web server" for you. You should see a file browser page
with the Jupyter logo on it, and a folder called `work`.

![jupyter-localhost]


##### Sharing files with the notebook server

Files in the `work` that appears in your Jupyter file browser will be on
your computer in the `notebook` sub-directory of the project directory.

Depending on whether you're looking at your computer or the environment
inside the Jupyter Notebook container, the same directory is available
on different paths, but contains the same files, allowing you to share
in both directions between your host computer and the inside of the
container where Jupyter Notebook has your workspace.

| environment   | path                           |
|:--------------|:-------------------------------|
| host OS       | `<project directory>/notebook` |
| Jupyter files | `/work`                        |


##### Shutting down the notebook server

This command is the opposite of the one used to start the container:

```bash
docker-compose down
```

Running `docker-compose down` deletes the container, but keeps the image
and all the files in `/work`, which will still be in the `notebook`
subdirectory of your project location.


#### Try Jupyter


##### Pros:

* no software installation required (and no administrator access)
* files can be downloaded from the server to your computer
* notebooks can be exported for safe keeping or use elsewhere
* free to use, powered by BinderHub and JupyterHub, hosted in the cloud


##### Cons:

* **you must upload any files you need, each time you open a new session**
* the workspace is destroyed after a certain period of inactivity
* can open any GitHub repository, but you'll have to upload the
  repository manually, with Jupyter file browser


#### NBViewer

This is recommended for non-interactive sharing via URL when speed is
important. A shareable link will be generated for viewing the notebook.

Copy the URL of any GitHub repository that contains a Jupyter Notebook
document, and paste it into the form at [NBViewer]. A well formatted
version of your notebook will be viewable with its own URL, and can be
exported to other formats, such as Markdown or HTML.


##### Pros:

* **can open notebooks, code, and data files from any GitHub repository**
* no software installation required (and no administrator access)
* files can be downloaded from the server to your computer
* notebooks can be exported for safe keeping or use elsewhere
* free to use, hosted in the cloud


##### Cons:

* non-interactive


### Future tools

- import/export helpers
- database management helper
- pre-made "dashboard" notebooks, for data querying and analysis
- REST API for remote access without Jupyter Notebook (usable by Access,
  Excel, and other applications)


[Home page]: http://aafc.devvyn.io/
[github-project]: https://github.com/devvyn/aafc-field-data/projects
[github-repo]: https://github.com/devvyn/aafc-field-data
[jupyter.org]: https://jupyter.org/
[jupyterpreview]: /docs/static/jupyterpreview.png "Jupyter Notebook web page screen shots"
[Try Jupyter]: https://jupyter.org/try
[Binder this repo]: https://mybinder.org/v2/gh/devvyn/aafc-field-data/master?filepath=docs%2Fnotebook%2FExample%20of%20reading%20Excel%20sheet.ipynb
[Binder]: https://mybinder.org/
[Docker Store]: https://store.docker.com/
[docker-ce download]: https://www.docker.com/community-edition#/download
[jupyter-localhost]: /docs/static/jupyter-localhost.png "Jupyter Notebook on localhost"
[NBViewer]: https://nbviewer.jupyter.org/
