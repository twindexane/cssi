// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

console.log("Running Window Events Script");
let kp = document.querySelector('#box6');
let s = 100;
let radius = '30px';
window.addEventListener("keypress", e=> {
console.log(e.keyCode);
if(e.keyCode == 99){
s /= 2;
radius = '30px';
}
if (e.keyCode == 115){
s = 100;
radius = '0px';
}
kp.style.width = s +'px';
kp.style.height = s +'px';
kp.style.borderRadius = radius;
})

window.addEventListener('scroll',() => {
  if(window.scrollY <= 50){
    rect.style.backgroundColor = "black"
  }
  else{
    rect.style.backgroundColor = "tomato"
  }
  console.log('im Scrolling');
})


// insert a function that prints out the key code of a key pressed
