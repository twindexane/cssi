#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import os
import random
import jinja2


def get_fortune():
    #add a list of fortunes to the empty fortune_list array
    fortune_list=['fortune1', 'fortune2']
    #use the random library to return a random element from the array
    random_fortune =fortune_list[random.randint(0,1)]
    return(random_fortune)


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory =  jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        results_template= jinja_current_directory.get_template("templates/fortune-start.html")
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        self.response.write(results_template.render())

    def post(self):
        results_template= jinja_current_directory.get_template("templates/fortune-start.html")
        user_astro_sign= self.request.get("user_astrological_sign")
        my_dict={"sign": user_astro_sign}
        self.response.write(results_template.render(my_dict))#add a post method
    #def post(self):

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of my app')

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('My response is Goodbye World')


#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/farewell', GoodbyeHandler),
    ('/predict', FortuneHandler) #maps '/predict' to the FortuneHandler
], debug=True)
