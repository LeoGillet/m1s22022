/* ./src/charts.js */

/*
 * Pie chart and Donut chart function set
 * @author: Léo Gillet
 * @date:   March 2022
 *
 * Dataset used :   COVID vaccines delivery data in France since 02/07/2021
 *                  Données relatives aux livraisons de vaccins contre la COVID-19
 * Source : Ministère des Solidarités et de la Santé
 *          <https://solidarites-sante.gouv.fr/>
 */

'use strict';

/**
 * Creates an SVG Element
 * @param w:    {Number} - width of the element
 * @param h:    {Number} - height of the element
 * @param box:  {{}} of form [min_X<int>, min_Y<int>, width<int>, height<int>]"
 * @returns     {SVGSVGElement}
 */
function svg(w=200, h=200, box=[0, 0, 100, 200]) {
    let el = create('svg');
    attributes(el, ['width', w, 'height', h, 'viewBox', box.join(" ")]);
    return el;
}

/**
 * Creates an SVG Rectangle Element
 * @param x {Number} : X position of the top-left corner of the rectangle
 * @param y {Number} : Y position of the top-left corner of the rectangle
 * @param w {Number} : Width of the rectangle
 * @param h {Number} : Height of the rectangle
 * @return {SVGRectElement}
 */
function rect(x, y, w, h) {
    if (w <= 0 && h <= 0) {
        throw(new Error("Size less or equal to 0"));
    }
    else if (w <= 0) {
        throw(new Error("Width less or equal to 0"));
    }
    else if (h <= 0) {
        throw(new Error("Height less or equal to 0"));
    }
    let el = create('rect');
    attributes(el, ['x', x, 'y', y, 'width', w, 'height', h])
    return el;
}

/**
 * (Unused) Creates an SVG Circle Element
 * @param cx {Number}: X position of the center of the circle
 * @param cy {Number}: Y position of the center of the circle
 * @param r {Number}: Radius of the circle
 * @return {SVGCircleElement}
 */
function circle(cx, cy, r) {
    if (r <= 0) {
        throw(new Error("Radius less or equal to 0"));
    }
    let el = create('circle');
    attributes(el, ['cx', cx, 'cy', cy, 'r', r])
    return el;
}

/**
 * Creates an SVG Text Element
 * @param x {Number}: X position of the text
 * @param y {Number}: Y position of the text
 * @param family {String}: Font family of the text
 * @param message {String}: text to be shown
 * @param color {String}: color of the text
 * @param size {Number}: font size
 * @return {SVGTextElement}
 */
function text(x, y, message, family="sans-serif", size=12, color="black") {
    let el = create('text');
    const textnode = document.createTextNode(message);
    attributes(el, ['x', x, 'y', y, 'fill', color, "font-family", family, "font-size", size]);
    el.appendChild(textnode);
    return el;
}

/**
 * Groups elements contained in array
 * @param els: {{Element}} Array of elements to be grouped
 * @return g: {GroupElement} Created group
 */
function group(els=null) {
    let g = create('g');
    if (els != null) {
        for (let el of els) {
            g.appendChild(el);
        }
    }
    return g;
}

/**
 * Converts percentage to the representative angle used in the charts
 * @param cx: {Number}
 * @param cy: {Number}
 * @param radius: {Number}
 * @param percentage: {Number} - Percentage (n/t) of the selected data
 * @returns {{Number, Number}}: Angle in radians
 */
function percentageToPoint(cx, cy, radius, percentage) {
    const degrees = percentage*360;
    const radians = (degrees-90) * Math.PI / 180;
    const x = cx + (radius * Math.cos(radians));
    const y = cy + (radius * Math.sin(radians));
    return {"x": x, "y": y}
}

/**
 * Creates an SVG Path element
 * @param arg: {String} "d" attribute value
 * @param color: {String} "fill" attribute value
 * @returns {SVGPathElement} Created SVG Path element
 */
function path(arg, color) {
    let el = create('path');
    attributes(el, ["d", arg, "fill", color]);
    return el;
}



// %% Charts %%
/**
 * Creates a complete legend by using a rectangle and a text grouped
 * @param data: {String} Name of the vaccine manufacturer
 * @param x: {Number} X position of the legend
 * @param y: {Number} Y position of the legend
 * @param w: {Number} Width of the rectangle
 * @param h: {Number} Height of the rectangle
 * @param color: {Number} Color of both rectangle and text
 * @returns {HTMLOptGroupElement}: Group
 */
function legend(data, x, y, w, h, color=null) {
    let box = rect(x, y, w, h);
    attributes(box, ["fill", color, "stroke", "black"]);
    let leg = text(x+25, y+8, data, color);
    let g = group([box, leg]);
    return g;
}


/**
 * Create an SVG box containing the pie chart using path elements,
 * aswell as the legend
 * Mouse over animation adapted from: Grieve <https://codepen.io/grieve>
 * @param data: {Object} Data to be used to draw the chart (percentages and labels)
 * @param cx: {Number} X Polar coordinates of the center of the pie
 * @param cy: {Number} Y Polar coordinates of the center of the pie
 * @param radius: {Number} Radius of the pie
 */
function pieChart(data, cx, cy, radius) {
    const viewbox = [0, 0, 500, 300];
    const svgbox = svg(1100, 700, viewbox);
    addToSection(svgbox, "drawbox");
    const colors = ["#E18335", "#E4CC37", "#8FC93A", "#0072BB", "#1E91D6"];
    const vaccines = Object.keys(data.Percentages);
    let angle = 0; let i = 0; let theta = -Math.PI * 0.5;
    for (let vaccine of vaccines) {
        let start = percentageToPoint(cx, cy, radius, angle)
        let startAng = angle;
        angle += data.Percentages[vaccine];
        let end = percentageToPoint(cx, cy, radius, angle);
        let endAng = angle;

        console.log(startAng, endAng)
        console.log({"Vaccine:": vaccine, "Perc": data.Percentages[vaccine] * 100});
        let direction = endAng - startAng >= 0.5 ? "1" : "0";

        /*
         * M: Starting point : center of the pie
         * L: Line towards starting point
         * A: Curved line towards end point
         * Z: Line going back to starting point
         */
        let d = `M ${cx} ${cy} ` +
            `L ${start.x} ${start.y} ` +
            `A ${radius} ${radius} 0 ${direction} 1 ${end.x} ${end.y} Z`;

        let delta = (endAng - startAng)*2*Math.PI;
        let normal = theta + delta * 0.5;
        theta += delta;
        let p = path(d, colors[i]);
        attributes(p, ['data-label', `${vaccine}: ${data.Sums[vaccine]} doses delivered (${Math.round(data.Sums[vaccine]/data.Total*100)}%)`,
            'data-normal', normal,
            'stroke', 'white', 'stroke-width', 1]);
        p.addEventListener('mouseover', onMouseOver);
        p.addEventListener('mouseout', onMouseOut);
        svgbox.appendChild(p);
        /* legend */
        let leg = legend(vaccine, 180, 65+i*15, 20, 10, colors[i]);
        svgbox.appendChild(leg); i++;
    }
    return svgbox;
}

/**
 * Create an SVG box containing the donut chart using path elements,
 * aswell as the legend
 * Mouse over animation adapted from: Grieve <https://codepen.io/grieve>
 * @param data: {Object} Data to be used to draw the chart (percentages and labels)
 * @param cx: {Number} X Polar coordinates of the center of the donut
 * @param cy: {Number} Y Polar coordinates of the center of the donut
 * @param innerRadius: {Number} Radius of the inner circle of the donut
 * @param outerRadius: {Number} Radius of the outer circle of the donut
 * @returns svgbox: {SVGElement} SVG Box containing all elements
 */
function donutChart(data, cx, cy, innerRadius, outerRadius) {
    const viewbox = [0, 0, 500, 300];
    const svgbox = svg(1100, 700, viewbox);
    addToSection(svgbox, "drawbox");
    const colors = ["#E4DFDA", "#D4B483", "#C1666B", "#4357AD", "#48A9A6"];
    const vaccines = Object.keys(data.Percentages);

    let angle = 0; let i = 0; let theta = -Math.PI * 0.5;
    for (let vaccine of vaccines) {
        let outerStart = percentageToPoint(cx, cy, outerRadius, angle);
        let innerStart = percentageToPoint(cx,cy, innerRadius, angle);
        let startAng = angle;
        angle += data.Percentages[vaccine];
        let outerEnd = percentageToPoint(cx, cy, outerRadius, angle);
        let innerEnd = percentageToPoint(cx, cy, innerRadius, angle);
        let endAng = angle;

        console.log(startAng, endAng)
        console.log({"Vaccine:": vaccine, "Perc": data.Percentages[vaccine] * 100});
        let direction = endAng - startAng >= 0.5 ? "1" : "0";

        /*
         * M: Starting point : center of the pie
         * L: Line towards starting point
         * A: Curved line towards end point
         * Z: Line going back to starting point
         */
        let d = `M ${outerStart.x} ${outerStart.y} ` +
            `A ${outerRadius} ${outerRadius} 0 ${direction} 1 ${outerEnd.x} ${outerEnd.y} ` +
            `L ${innerEnd.x} ${innerEnd.y} ` +
            `A ${innerRadius} ${innerRadius} 0 ${direction} 0 ${innerStart.x} ${innerStart.y} Z`;

        let delta = (endAng - startAng)*2*Math.PI;
        let normal = theta + delta * 0.5;
        theta += delta;
        let p = path(d, colors[i]);
        attributes(p, ['data-label', `${vaccine}: ${data.Sums[vaccine]} doses delivered (${Math.round(data.Sums[vaccine]/data.Total*100)}%)`,
            'data-normal', normal,
            'stroke', 'white', 'stroke-width', 1]);
        p.addEventListener('mouseover', onMouseOver);
        p.addEventListener('mouseout', onMouseOut);
        svgbox.appendChild(p);
        /* legend */
        let leg = legend(vaccine, 180, 65+i*15, 20, 10, colors[i]);
        svgbox.appendChild(leg); i++;
    }
    return svgbox;
}

/**
 * Creates a caption/title on top of the selected chart
 * @param message {String}: Text to be printed
 * @returns {SVGTextElement}: Representative SVG text element
 */
function caption(message) {
    let cap = text(10,10, message, "black", 9);
    attribute(cap, "font-weight", "bold");
    return cap;
}

/**
 * Deletes HTML code contained in an HTML section
 * @param section {String}: Section identifier
 * (Works for any HTML container [div, span, class])
 */
function voidSection(section) {
    document.getElementById(section).innerHTML = "";
}

/**
 * Calls voidSection, linked to #clearButton
 * @param ev
 */
function clear(ev) {
    voidSection("drawbox");
}

/**
 * Initiates data upload & parsing, creates according pie chart, caption & labels
 * @return {Promise<void>}
 */
async function drawPie(ev) {
    voidSection("drawbox");
    let data = await uploadFile(ev);
    console.log(data);
    let svgbox = pieChart(data, 100, 100, 50, "drawbox");
    let title = caption("Delivery of COVID-19 vaccines in France by vaccine manufacturer (2021-present)")
    svgbox.appendChild(title);
    let label = text(20, 40, "Hover over chart to print data"); attribute(label, "id", "label");
    svgbox.appendChild(label);
}

/**
 * Initiates data upload & parsing, creates according donut chart, caption & labels
 * @return {Promise<void>}
 */
async function drawDonut(ev) {
    voidSection("drawbox");
    let data = await uploadFile(ev);
    console.log(data);
    let svgbox = donutChart(data, 100, 100, 30, 50, "drawbox");
    let title = caption("Delivery of COVID-19 vaccines in France by vaccine manufacturer (2021-present)")
    svgbox.appendChild(title);
    let label = text(20, 40, "Hover over chart to print data"); attribute(label, "id", "label");
    svgbox.appendChild(label);
}



