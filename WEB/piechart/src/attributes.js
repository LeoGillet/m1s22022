/* ./src/attributes.js */
/*
 * Some functions dealing with Element Attributes and SVG Elements manipulation
 * @author: Léo Gillet
 * @date:   March 2022
 */
'use strict';

/**
 * Creates an SVG Element
 * @param type {String}: Type of element to be created
 * @return {SVG*Element}
 */
function create(type) {
    const el = document.createElementNS('http://www.w3.org/2000/svg', type);
    return el;
}

/**
 * Appends element to section
 * @param el {HTMLElement} : HTML Element to be appended
 * @param section_id {String} : Identifier of the section
 */
function addToSection(el, section_id) {
    document.getElementById(section_id).appendChild(el);
}

function append(parent, el) {
    parent.appendChild(el);
    return parent;
}

/**
 * Gets or sets attribute of an HTML element
 * @param el: HTML element to be edited
 * @param key: attribute's key to be edited
 * @param value: value to be set, if argument is not given, returns the value
 * @returns {string|*}: if argument 'value' is given element is returned ;
 *                      if not, returns the value of the attribute 'key'
 */
function attribute(el, key, value=null) {
    if (value === null)     {return el.getAttribute(key);}
    else                    {el.setAttribute(key, value);}
    return el;
}

/**
 * Sets an array of attributes to an HTML element
 * @param el: HTML element to be edited
 * @param array: Array of keys and values <{key1, value1, ..., keyN, valueN}>
 */
function attributes(el, array) {
    for (let i=0; i<array.length-1; i+=2) {
        const key = array[i]; const value = array[i+1];
        attribute(el, key, value);
    }
}


/**
 * Extracts pie piece when moused over
 * Prints label corresponding to certain vaccine
 * @author: Adapted from Grieve <https://codepen.io/grieve>
 * @param evt
 */
function onMouseOver(evt) {
    console.log(evt.path);
    let normal = evt.target.getAttribute('data-normal');
    let dX = Math.cos(normal) * 5;
    let dY = Math.sin(normal) * 5;
    evt.target.style.transform = `translate(${dX}px, ${dY}px)`;
    let t = text(dX, dY, evt.target.getAttribute('data-label'));
    document.querySelector('#label').textContent = evt.target.getAttribute('data-label');
}

/**
 * Nulls text of the label text
 * @author: Adapted from Grieve <https://codepen.io/grieve>
 * @param evt
 */
function onMouseOut(evt) {
    evt.target.style.transform = 'none';
    document.querySelector('#label').textContent = "";
}