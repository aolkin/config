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
