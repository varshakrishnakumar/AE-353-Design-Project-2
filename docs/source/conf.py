extensions = ['sphinx.ext.intersphinx']

templates_path = ['_templates']

source_suffix = '.rst'


master_doc = 'index'

# General information about the project.
project = u'Differential Drive Robot'
copyright = u'2022, Varsha Krishnakumar'


exclude_trees = []


pygments_style = 'sphinx'


# HTML output 

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {
   'collapse_navigation': False,

}


static_path = ['_static']



# Output file - HTML
basename = 'SegBotDoc'


# LaTeX output 

latex_documents = [
  ('index', 'DjangoKong.tex', u'Django Kong Documentation',
   u'Eric Holscher', 'manual'),
]


intersphinx_mapping = {'http://docs.python.org/': None}
language = 'en'