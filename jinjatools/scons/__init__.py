# jinja-tools
#
# various tools for Jinja2
# including new filters and tests based on python-moretools,
# a JinjaLoader class for Django
# and a simple JinjaBuilder class for SCons
#
# Copyright (C) 2011 Stefan Zimmermann <zimmermann.code@googlemail.com>
#
# jinja-tools is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# jinja-tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with jinja-tools.  If not, see <http://www.gnu.org/licenses/>.

from SCons.Builder import BuilderBase
from SCons.Action import Action

from ..env import Environment

__all__ = 'JinjaBuilder',

class JinjaBuilder(BuilderBase):
  def __init__(self, jinja_loader, jinja_context = {}):
    BuilderBase.__init__(
      self,
      action = Action(self.__action),
      src_suffix = '.jinja',
      suffix = '',
      )

    self.__jinja_env = Environment(loader = jinja_loader)
    self.__context = jinja_context

  def __action(self, target, source, env):
    context = dict(self.__context)
    try:
      context.update(env['JINJACONTEXT'])
    except KeyError:
      pass

    open(str(target[0]), 'w').write(
      self.__jinja_env.from_string(open(str(source[0])).read())
      .render(context).encode())
