Django Config App
====================

Installation
--------------------

Add `config` to `INSTALLED_APPS` in your settings file.

To enable the template context processor, add `"config.context_processors.configuration"` to `TEMPLATE_CONTEXT_PROCESSORS` in your settings file.

Use
--------------------

This package provides many ways to access and set configuration values.

To use the `get_opt` and `option` template tags, place `{% load config %}` at the top of your template.
