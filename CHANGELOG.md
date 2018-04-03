Pre-release
===========

[Unreleased]
------------

No unreleased changes.

[0.3.0]

### Added

- documentation:
    - project page:
        - links to GitHub, mybinder.org, as with README
    - README:
        - quick start section, pointing user to "launch binder" (mybinder.org)

[0.2.0]
-------

### Added

- documentation:
    - README:
        - link to project URLs:
            - GitHub Pages: http://aafc.devvyn.io/
            - GitHub repository: https://github.com/devvyn/aafc-field-data
            - GitHub Projects: https://github.com/devvyn/aafc-field-data/projects
            - this repository on mybinder.org: https://mybinder.org/v2/gh/devvyn/aafc-field-data/master
        - instructions:
            - how to:
                - run a Jupyter Notebook server locally
                - use a cloud-based notebook server
    - log entry about:
        - the usefulness of Jupyter Notebook
        - using Jupyter locally versus mybinder.org
- configuration:
    - `docs/` (Jekyll/GitHub Pages):
        - timezone: America/Regina
    - developer:
        - `docker-compose.yml` for operating Jupyter Notebook service
        - `rbenv` Ruby version: 2.4.1
        - Git ignored files (added JetbrainsIDE directory)
        - `environment.yml` listing dependencies for notebooks
- example data in `notebook/src`
- example notebook in `notebook`

### Changed

- metadata in post:
    - category and title of _Using GitHub Pages_


[0.1.1]
-------

### Added

- documentation
  - README.md
  - [project site] in docs/
  - project log posts (2)


[Unreleased]: https://github.com/devvyn/aafc-field-data/compare/v0.3.0...master
[0.3.0]: https://github.com/devvyn/aafc-field-data/compare/v0.3.0...v0.2.0
[0.2.0]: https://github.com/devvyn/aafc-field-data/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/devvyn/aafc-field-data/tree/v0.1.1
[project site]: http://aafc.devvyn.io/
