'use strict';

// Créer un élément
/*for (let i=0; i<10; i++) {
    const el = document.createElement('p');
    el.setAttribute('id', `hello${i+1}`); el.setAttribute('class', 'text');
    el.textContent = `This is paragraph n°${i+1}!`;
    document.body.appendChild(el);
}*/

const body_firstChild = this.document.body.firstChild;
console.log(body_firstChild);

/*const hello4 = this.document.getElementById('hello4');
hello4.previousElementSibling.style.color = '#FF0000';
hello4.style.color = '#FFFF00';
hello4.nextElementSibling.style.color = '#00FF00';*/

/*const inserted_el = document.createElement('p'); inserted_el.textContent = 'This has been inserted';
document.body.insertBefore(inserted_el, hello4);*/


const button = document.createElement('button');
document.body.appendChild(button); button.textContent = 'Cliquez moi';
const clicked = function (ev) {
    const clicks = ["Left Click", "Middle Click", "Right Click"];
    const modifiers = ["", "Shift", "Alt", "Shift+Alt", "Ctrl", "Ctrl+Shift", "Ctrl+Alt", "Ctrl+Shift+Alt"]
    let sh = (ev.shiftKey) ? 1 : 0;
    let alt = (ev.altKey) ? 2 : 0;
    let ctrl = (ev.ctrlKey) ? 4 : 0;
    let sum = sh+alt+ctrl
    alert(clicks[ev.which-1]+' '+modifiers[sum]);
}

button.addEventListener("click", clicked); // Pareil
