'use strict';

function create(type) {
    const el = document.createElementNS('http://www.w3.org/2000/svg', type);
    return el;
}

/*
    Get or set attribute
    attribute(el, key) return 'el''s 'key' value
    attribute(el, key, value) sets the 'key' attribute with 'value'
 */
function attribute(el, key, value=null) {
    if (value === null)     {return el.getAttribute(key);}
    else                    {el.setAttribute(key, value);}
    return el;
}


// Set a collection of attributes to el
function attributes(el, array) {
    for (let i=0; i<array.length-1; i+=2) {
        const key = array[i]; const value = array[i+1];
        attribute(el, key, value);
    }
}