Django Config App
====================

Installation
--------------------

Add `config` to `INSTALLED_APPS` in your settings file.

To enable the template context processor, add `"config.context_processors.configuration"` to `TEMPLATE_CONTEXT_PROCESSORS` in your settings file. This will add `options` and `uncached_options` as template variables.

To change the app's name in Django's admin interface, use the setting `CONFIGURATION_APP_TITLE`.

Use
--------------------

This package provides many ways to access and set configuration values.

In python code, the preferred method is through the `config` and `uncached_config` objects provided by the root package.

To use the `get_opt` and `option` template tags, place `{% load config %}` at the top of your template.

Additionally, `get_nocache` and `option_uncached` are provided for systems where multiple systems share the same database.

The `context_processors.configuration` context processor will add `options`, `uncached_options`, and `numeric_options` (which will always try to return a number if possible) to the template context.

Autocomplete Suggestions
------------------------

This package also provides a model for storing autocomplete suggestions, and a
view at `config.views.autocomplete_json` that returns a JSON list of
suggestions given a key and search term, provided by the `key` and `q` HTTP
GET parameters to the request.
