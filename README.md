# Imhotep PEP8

Imhotep PEP8 is a plugin for [Glow's Imhotep fork](https://github.com/glowdigitalmedia/imhotep), which provides bindings to the pep8 linter.


## Installation
Install the plugin with:

```
pip install -e git+git://github.com/glowdigitalmedia/imhotep_pep8.git@0.1.1#egg=imhotep_pep8
```

It also requires the PEP8 linter:

```
pip install pep8
```

Optionally put ```tox.ini``` PEP8 linter config in the linted repo root if you want to change the defaults.