'use strict';

/**
 * Parse CSV file
 * @param text - String containing data
 * @param sep - String separator. By default : ,
 * @returns {{}}
 */

function parseCsv(text, sep=',') {
    const rows = text.split('\n');
    let array = {};
    array.data = [];
    array.header = rows[0].split(sep);
    for (let i = 1; i<rows.length; i++) {
        let raw_values = rows[i].split(sep); let values = [];
        for (let v of raw_values) {
            if (!isNaN(v))  {values.push(parseFloat(v));}
            else            {values.push(v);}
        }
        array.data.push(values);
    }
    return array
}

async function readFile(ev) {
    // console.log(ev.target.files[0]);
    const file = ev.target.files[0];
    const txt = await file.text(); // continue l'exécution une fois le fichier téléchargé
    const array = parseCsv(txt, ';');
    console.info(array);
}