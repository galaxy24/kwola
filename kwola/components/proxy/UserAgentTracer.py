#
#     Kwola is an AI algorithm that learns how to use other programs
#     automatically so that it can find bugs in them.
#
#     Copyright (C) 2020 Kwola Software Testing Inc.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import datetime
from ...config.logger import getLogger
import os
import urllib.parse

class UserAgentTracer:
    def __init__(self):
        self.lastUserAgent = ""

    def requestheaders(self, flow):
        if 'User-Agent' in flow.request.headers:
            self.lastUserAgent = flow.request.headers['User-Agent'].replace(" Kwola", "")
        elif 'user-agent' in flow.request.headers:
            self.lastUserAgent = flow.request.headers['user-agent'].replace(" Kwola", "")


addons = [
    UserAgentTracer()
]
