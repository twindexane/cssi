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

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")

    choice = raw_input("Enter your choice [a|b|c|d|e]:")

    if choice=="a":
        x=raw_input("Enter to add items:").lower()
        shopping_list.append(x)
    elif choice =="b":
        o=raw_input("Enter to remove items:")
        shopping_list.remove(o)
        print shopping_list
    elif choice =="c":
        v=raw_input("Enter to check items:")
        if v in shopping_list:
            print("items are there: \n")
        else:
            print("not there:")
    elif choice =="d":
            print("items are there: \n")
            for i in shopping_list:
                print i
    else:
        print "please try again"
