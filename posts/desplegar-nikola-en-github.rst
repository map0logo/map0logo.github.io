.. title: Desplegar nikola en github
.. slug: desplegar-nikola-en-github
.. date: 2014-09-01 22:39:11 UTC-05:30
.. tags: nikola, github, virtualenv
.. link: 
.. description: 
.. type: text

Importante seguir las instrucciones con atención, no vale la pena intentar ser
originales :-D.

Para crear un despliegue de nikola en github como página principal seguir los
siguientes pasos:


1. Crear en tu cuenta de github un repositorio con nombre ``[usuario].github.io``

2. Clonar ese repositorio y crear un entorno virtual (python 3.4) para
   esa carpeta.

.. code-block:: console

   $ git clone https://github.com/[usuario]/[usuario].github.io.git
   $ mkvirtualenv -p /usr/bin/python3 [usuario].github.io # Necesitas tener virtualenvwrapper
   $ cd [usuario].github.io.git

3. Crear una rama "sources" para la nueva instancia de nikola

.. code-block:: console

   $ touch README.md # necesitas al menos un commit
   $ git add README.md
   $ git commit REAME.md -m "Initial commit"
   $ git branch sources # la rama con los fuentes de nikola
   $ git checkout sources # ahora trabajamos sobre los fuentes

4. En el nuevo entorno virtual y en la rama sources instalar nikola

.. code-block:: console

   $ pip install nikola
   $ nikola init ./

5. En conf.py que debe ahora estar en la raíz del repositorio, descomentar y
   editar las variables

.. code-block:: python

   GITHUB_SOURCE_BRANCH = 'sources'
   GITHUB_DEPLOY_BRANCH = 'master'

6. Finalmente añadir algo de contenido usando ``nikola new_post`` o
   ``nikola new_page``, ¡ojo!, siempre en la rama ``sources``

   Editar el post

.. code-block:: console

   $ git add posts/[nuevo_post].rst
   $ git commit -a "Add [nuevo_post]"
   $ nikola github_deploy

Puede ser conveniente crear el correspondiente .gitignore en la raíz del
repositorio, con más o menos el siguiente contenido

::

   .idea/
   __pycache__/
   output/
   cache/
   .doit.db

``.idea`` para proyectos de pycharm, el resto son carpetas y archivos generados
por nikola.