ajgarlag.elasticsearch
======================

Ansible role to install Elasticsearch.

[![Build Status](https://travis-ci.org/ajgarlag/ansible-elasticsearch.svg?branch=master)](https://travis-ci.org/ajgarlag/ansible-elasticsearch)

Role Variables
--------------

* **ajgarlag_elasticsearch_minor_version**: Minor version to configure the elasticsearch repository (defaults to `1.5`).
* **ajgarlag_elasticsearch_java_package**: Name of the package to install a JAVA JRE environment (defaults to `openjdk-7-jre-headless`).
* **ajgarlag_elasticsearch_settings**: Dict of parameters to write into the elasticsearch config file (defaults to `{}`).
* **ajgarlag_elasticsearch_plugins**: Dict of plugins to install (defaults to `{}`).

Example Playbook
----------------

```yml
- hosts: all
  roles:
    - role: ajgarlag.elasticsearch
      ajgarlag_elasticsearch_plugins:
        "head": "mobz/elasticsearch-head"
      ajgarlag_elasticsearch_settings:
        "network.host": "127.0.0.1"
```


License
-------

MIT

Author Information
------------------

Developed with ♥ by [Antonio J. García Lagar](http://aj.garcialagar.es).
