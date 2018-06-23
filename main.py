# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
from os import getenv
import logging


class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info("get request")
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('AppEngine sample app which logs'
                            'posted data to stdout/log.')

    def post(self):
        logging.info(self.request.body)
        self.response.write('Data posted , see logs for received data..!')





app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if getenv('DEV', None):
    print 'Running Dev mode...'
    main()
