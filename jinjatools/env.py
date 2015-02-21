# python-jinjatools
#
# Various tools for Jinja2,
# including new filters and tests based on python-moretools,
# a JinjaLoader class for Django,
# and a simple JinjaBuilder class for SCons.
#
# Copyright (C) 2011-2015 Stefan Zimmermann <zimmermann.code@gmail.com>
#
# python-jinjatools is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-jinjatools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with python-jinjatools.  If not, see <http://www.gnu.org/licenses/>.

all = ['Environment']

from itertools import chain

import jinja2


class Environment(jinja2.Environment):
    def __init__(self, filters={}, tests={}, globals={}, **kwargs):
        jinja2.Environment.__init__(self, **kwargs)

        morefilters = __import__('jinjatools.filters').filters.filters
        for name, func in chain(morefilters.items(), filters.items()):
            self.filters[name] = func

        for name, func in tests.items():
            self.tests[name] = func

        for name, value in globals.items():
            self.globals[name] = value


# from .filters import filters as morefilters
