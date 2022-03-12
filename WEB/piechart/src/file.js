/* ./src/file.js */

/*
 * Remote file fetcher and csv-file data parser
 * @author: Léo Gillet
 * @date:   March 2022
 *
 * Incompatible with :
 *      - Internet Explorer and Edge versions 13 and earlier
 *          (<Array>.includes 40:25)
 *
 * File chosen has some particularities:
 *      - Line separator is Windows CRLF (\r\n) and not Unix standard (\n)
 *      - Rows are created on a regular basis, even is the data is zeroed
 *          rendering their parsing useless
 *      - Each value is contained in double-quotes, even numerical values
 *          requiring their removal beforehand
 *
 * File attributes :
 *      1st column: "date_fin_semaine"  -- Date of entry
 *      2nd column: "type_de_vaccin"    -- Vaccine vendor
 *      3rd column: "nb_ucd"            -- Number of vaccine 'bottles'
 *                                      "Unité Commune de Dispensation"
 *      4th column: "nb_doses"          -- Number of doses (10 per bottle,
 *                                         which means values are 'nb_ucd'
 *                                         values multiplied 10 fold)
 */
'use strict';

/**
 * Transforms a user-uploaded text file from a large string
 *                                      to an array of arrays of values
 * @param text:     {String} - Content of the uploaded file
 * @param sep:      {String} - Separator, default is ',' (csv).
 *                           General alternatives are ';' ' ' '\t'
 * @param lineSep:  {String} - Line separator, default is '\n' (Unix LF),
 *                           alternatives are '\n' (Windows CRLF)
 *                           & '\r' (Classic MacOSX CR)
 * @returns {{}}:   array of rows,
 *                  with rows being arrays of values per column/attribute
 */
function parseCsv(text, sep=",", lineSep="\n") {
    const rows = text.split(lineSep);

    // The following expression can be translated by
    // 'replace all double-quotes globally'
    const regex_quotes = (/"/g);

    let array = {}; array.data = [];
    array.header = rows[0].replace(regex_quotes, "").split(sep);

    for (let i=1; i<rows.length-1; i++) /* Last line is empty */ {
        let raw_values = rows[i].replace(regex_quotes, "").split(sep);
        let values = [];
        if (!raw_values.includes("0")) { // Excludes zeroes
            for (let v of raw_values) {
                if (!isNaN(v))  {values.push(parseInt(v));}
                else {
                    if (v.includes("�")) {v = "PfizerPed";}
                    values.push(v);
                }
            }
            array.data.push(values);
        }
    }

    return array;
}

/*
 * Output of the CSV parser :
 * Object   - header:   {Array(4)}
 *          - data:     {Array(149)}
 *              - Array(4)
 *                  - [0]: date
 *                  - [1]: vaccine type
 *                  - [2]: nb ucd
 *                  - [3]: nb doses
 */

/**
 * Returns values their sums and percentages and total value of the parsed data
 * Used to draw charts
 * @param array {{}} Array of parsed data
 * @return {{   Percentages: {},
 *              Total: number,
 *              Values: {Pfizer: *[], Janssen: *[], PfizerPed: *[], Moderna: *[], AstraZeneca: *[]},
 *              Sums: {}
 *         }}
 */
function dataPerVaccine(array) {
    let values = {
        "AstraZeneca": [],
        "Janssen": [],
        "Moderna": [],
        "Pfizer": [],
        "PfizerPed": []
    };
    let sums = {}; let percentages = {};
    const known_vaccines = Object.keys(values);
    let total = 0;

    // Separates each value according to vaccine manufacturer
    for (let row of array.data) {
        total += row[3];
        values[row[1]].push(row[3]);
    }

    // Computes sum and percentage value to according arrays of the object
    for (let vaccine of known_vaccines) {
        let sum = 0;
        for (let value of values[vaccine]) {sum += value;}
        sums[vaccine] = sum;
        percentages[vaccine] = sum/total;
    }
    return {"Values": values, "Sums": sums, "Percentages": percentages, "Total": total}
}



/**
 * Fetches the text-file linked to the url in the URL constant
 * and converts it to a string
 * Called when clicking the associated element (button)
 * @param ev:   {Event} Information about the event associated
 *              with the element used to call this function, here, a click
 *              (Unused)
 * @returns {Promise<void>}
 */
async function uploadFile(ev) {
    const URL = "https://www.data.gouv.fr/fr/datasets/r/9c60af86-b974-4dba-bf34-f52686c7ada9";
    const response = await fetch(URL);
    console.info("File loaded");
    const txt = await response.text();
    console.info("File converted to text");
    // File is a CSV with Windows-type line-separator
    const array = parseCsv(txt, ",", "\r\n");
    console.info("Data parsed from text file");
    const vaccine = dataPerVaccine(array);
    console.info("Graph data ready");
    return vaccine;
}