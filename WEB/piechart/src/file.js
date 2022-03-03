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
 *      4th column: "nb_doses"          -- Number of doses (10 per bottle,
 *                                         which means values are 'nb_ucd'
 *                                         values multiplied 10 fold)
 */


/**
 * Transforms a user-uploaded text file from a large string
 *                                      to an array of arrays of values
 * @param text:     string - Content of the uploaded file
 * @param sep:      string - Separator, default is ',' (csv).
 *                           General alternatives are ';' ' ' '\t'
 * @param lineSep:  string - Line separator, default is '\n' (Unix LF),
 *                           alternatives are '\n' (Windows CRLF)
 *                           & '\r' (Classic MacOSX RN)
 * @returns {{}}:   array of rows,
 *                  with rows being arrays of values per column/attribute
 */
function parseCsv(text, sep=",", lineSep="\n") {
    const rows = text.split(lineSep);

    // This expression can be translated by 'replace all double-quotes globally'
    const regex_quotes = (/"/g);

    let array = {}; array.data = [];
    array.header = rows[0].replace(regex_quotes, "").split(sep);

    for (let i=1; i<rows.length; i++) {
        let raw_values = rows[i].replace(regex_quotes, "").split(sep);
        let values = [];
        if (!raw_values.includes("0")) {
            for (let v of raw_values) {
                if (!isNaN(v))  {values.push(parseInt(v));}
                else            {values.push(v);}
            }
            array.data.push(values);
        }
    }

    return array;
}

/**
 * Fetches the text-file linked to the url in the URL constant
 * and converts it to a string
 * Called when clicking the associated element (button)
 * @param ev:   Information about the event associated
 *              with the element used to call this function, here, a click
 *              (Unused)
 * @returns {Promise<void>}
 */
async function uploadFile(ev) {
    const URL = "https://www.data.gouv.fr/fr/datasets/r/9c60af86-b974-4dba-bf34-f52686c7ada9";
    const response = await fetch(URL);
    const txt = await response.text();
    const array = parseCsv(txt, ",", "\r\n");
    console.log(array);
}