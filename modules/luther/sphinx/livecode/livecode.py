# Copyright (C) 2011  Bradley N. Miller
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = 'bmiller'

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive
import json
import os
from jinja2 import Environment, FileSystemLoader

# try:
#     import conf
#     version = conf.version
#     staticserver = conf.staticserver
# except:
#     version = '2.1.0'
#     staticserver = 'runestonestatic.appspot.com'

def setup(app):
    app.add_directive('livecode', LiveCode)
    app.add_stylesheet('codemirror.css')
    app.add_stylesheet('activecode.css')
    app.add_javascript('jobe.js')

class LiveCode(Directive):
    required_arguments = 1
    optional_arguments = 0
    has_content = True
    option_spec = {
        'language':directives.unchanged,
    }

    def run(self):
        self.options['divid'] = self.arguments[0]
        if 'language' not in self.options:
            raise KeyError("language must be specified")
        self.options['initialcode'] = self.content

        env = Environment(loader=FileSystemLoader(__path__))
        template = env.get_template('livecode.html')
        output = template.render(**self.options)

        return [nodes.raw('', output, format='html')]



