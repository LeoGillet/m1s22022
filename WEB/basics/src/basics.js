/*	console.log("Hello");
	console.info("Hello");
	console.error("Hello");
	console.warn("Hello"); 	*/

'use strict';
let i = 98;
let j = -8;
let message = `i est égal à ${i}`;
console.info(message);

let bar = function (x,y) {
    return x+y;
}
bar = (x,y) => x+y; // même fonction

function action(x, y, fun) {
    return fun(x,y);
}

let stuff = action(i, j, bar);
let more_stuff = action(3, 7, function(x,y) {return x+y;});

console.log(bar(i, j));