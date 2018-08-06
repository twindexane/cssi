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

console.log("Running Click Events Script");

document.getElementById('box1').addEventListener('click',()=>{boxcolor(0);});
document.getElementById('box2').addEventListener('click',()=>{boxcolor(1);});
document.getElementById('box3').addEventListener('click',()=>{boxcolor(2);});

const colors = ['red', 'pink', 'orange'];

function boxcolor(value) {
  let ng = document.getElementsByClassName('box')
  ng[0].style.backgroundColor = colors[value];
  ng[1].style.backgroundColor = colors[value];
  ng[2].style.backgroundColor = colors[value];
}

document.getElementById('box4').addEventListener('click',()=>{boxcol('box4');});
document.getElementById('box5').addEventListener('click',()=>{boxcol('box5');});

function boxcol(value){
  let cg = document.getElementById(value).classList.toggle('active');
}
