const redButton = document.querySelector('.red');
redButton;
 const greenButton = document.querySelector('.green');
greenButton;
 const blueButton = document.querySelector('.blue');
 blueButton;

 const buttons = document.querySelectorAll('button');
buttons;
buttons.length;

 const box = document.querySelector('#box');
 buttons.forEach(button => {
  button.addEventListener('click', () => {
    const color = button.innerHTML;
    box.style.background = color;
  });
});
