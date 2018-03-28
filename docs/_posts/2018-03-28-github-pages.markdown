---
layout: post
title:  "Using GitHub Pages"
date:   "2018-03-28 16:43:00 -0600"
categories: update
---
GitHub has a service that publishes web pages that you include with your repository. This is quite
handy if you don't have a dedicated project site already online. It's also quite logical to have
your documentation or development log inside your code repository, so everything important is in
the same place.

## Accidental breakage

### Links to posts

Unfortunately, it's also easy to confuse GitHub Pages by allowing the stock configuration supplied
by Jekyll, the build tool that GitHub Pages uses---which you can install on your local development
environment to create the boilerplate site to start you off. If you happen to supply the `baseurl: ""`
line in your `_config.yml` configuration file, GitHub will attempt to honour it, badly, regardless
of the fact that you may be using a project page that happens to publish to a subdirectory of your
personal page on a custom domain.

So, let this be a lesson: don't let Jekyll initialize your project page unless you understand how
GitHub Pages overrides your configuration. You could instead add to the tiny configuration file
that GitHub provides when you use their _Theme Chooser_ to select _minima_ or any other theme.
This method generates (and commits remotely) a `_config.yml` file with only one line:

```yaml
theme: minima
```

And if you do this, you minimize your complexity, avoid wasting time troubleshooting a mysterious
issue that breaks all the links to your posts, and you can get right down to more important things,
like coding your project.

### Home page and post page layouts

The default theme from GitHub Pages is `minima`, and the _minima_ theme comes with certain "layouts"
for any given page you author, such as "post", "home", and "default".

Unfortunately, any of the other themes---including those in the _Theme Chooser_---offer no layouts besides "default".
Attempting to use a non-existent layout results in utterly blank pages. If you want to use layouts such as
your home page (linking to posts and contact info), you need to provide the layout files yourself. You can
copy them from the _minima_ Ruby gem, but that's a bunch of hassle you should probably avoid.

In conclusion: stick with the default theme unless you have time to invest in the design of your
project page. If _minima_ isn't your thing, you may want to scrounge up another person's project
page on GitHub and copy their layouts rather than starting from scratch.
