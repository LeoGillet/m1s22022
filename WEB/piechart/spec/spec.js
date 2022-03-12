

describe("Pie and Donut Charts", function() {
  // Create(..)
  describe("create(..)", function() {
    it("create('rect')", function() {
      const el = create('rect');
      expect(el instanceof SVGRectElement).toBe(true);
    });
    it("create('circle')", function() {
      const el = create('circle');
      expect(el instanceof SVGCircleElement).toBe(true);
    });
    it("create('g')", function() {
      const el = create('g');
      expect(el instanceof SVGGElement).toBe(true);
    });
    it("create('path')", function() {
      const el = create('path');
      expect(el instanceof SVGPathElement).toBe(true);
    });
    it("create('svg')", function() {
      const el = create('svg');
      expect(el instanceof SVGElement).toBe(true);
    });
  });
  // Append
    describe("Append a chid to the parent - function append(parent,child)", function() {
    let g;
    let c;
    beforeEach(function() {
      g = create('g');
      c = create('circle');
    });
    it("should get as last child a `circle` primitive", function() {
      let tmp = append(g,c);
      expect(g.lastChild instanceof SVGCircleElement).toBe(true);
    });
    it("should return the parent", function() {
      let tmp = append(g,c);
      expect(tmp instanceof SVGGElement).toBe(true);
    });
  });
  // Set Attribute
  describe("Set Attribute - function attribute(elt,key,value)", function() {
    let el;
    beforeEach(function() {
      el = create('rect');
      attribute(el,'id','rectangle');
      attribute(el,"color",150);
    });
    it("should set a color attribute equal to 150", function() {
      expect(el.getAttribute("color")).toBe("150");
    });
    it("should set an ID of `rectangle`", function() {
      expect(el.getAttribute("color")).toBe("150");
    });
  });
  // Get Attribute
  describe("Get Attribute - function attribute(elt,key)", function() {
    let el;
    beforeEach(function() {
      el = create('rect');
      attribute(el,'id','rectangle');
      attribute(el,"color",150);
    });
    it("should get a ID attribute equal to `rectangle`", function() {
      expect(attribute(el,"id")).toBe("rectangle");
    });
    it("should get a color attribute equal to 150", function() {
      expect(attribute(el,"color")).toBe("150");
    });
    it("should return `null` if  attribute is not defined", function() {
      expect(attribute(el,"data")).toBeNull();
    });
  });
  // Set a collection of attributes
    describe("Set a collection of Attributes - function attributes(elt,array)", function() {
      let el;
      beforeEach(function() {
        el = create('rect');
        attributes(el,['fill','blue','stroke','pink','stroke-width',5,'fill-opacity',0.1,'stroke-opacity',0.9]);
      });
      it("should get a `fill-opacity` attribute equal to 0.1", function() {
        console.log(attribute(el,'fill-opacity'));
        expect(attribute(el,"fill-opacity")).toBe("0.1");
      });
  });
  // svg(..)
  describe("Create an SVG element svg(w,h,box)", function() {
    it("should have a SVG with w=100, h=200 and viewBox='0 0 100 100'", function() {
      const sketch = svg(100,200,[0,0,100,100]);
      expect(sketch.getAttribute("width")).toBe("100");
      expect(sketch.getAttribute("height")).toBe("200");
      expect(sketch.getAttribute("viewBox")).toBe("0 0 100 100");
    });
  });
  describe("Create an SVG element svg(w,h) with **NO VIEWBOX**", function() {
    it("should have a SVG with a viewBox equal to `w` and `h`", function() {
      const sketch = svg(100,200);
      expect(sketch.getAttribute("viewBox")).toBe("0 0 100 200");
    });
  });
  // Primitives: rect(..), circle(..), etc.
  describe("Create Graphics Primitives rect(..), circle(..), etc.", function() {
    it("should create a <circle cx=10 cy=5 r=80>", function() {
      const el = circle(10,5,80);
      expect(el.getAttribute("cx")).toBe("10");
      expect(el.getAttribute("cy")).toBe("5");
      expect(el.getAttribute("r")).toBe("80");
    });
    it("should create a <rect x=10 y=5 width=80 height=30>", function() {
      const el = rect(10,5,80,30);
      expect(el.getAttribute("x")).toBe("10");
      expect(el.getAttribute("y")).toBe("5");
      expect(el.getAttribute("width")).toBe("80");
      expect(el.getAttribute("height")).toBe("30");
    });
    it("should create a <g>", function() {
      const el = group();
      expect(el instanceof SVGGElement).toBe(true);
    });
    it("should create a <path d='M 10 20 L 15 30' >", function() {
      const el = path('M 10 20 L 15 30');
      expect(el.getAttribute("d")).toBe("M 10 20 L 15 30");
    });
    it("should create a <text>Hello World</text> with default font `serif` and size of 12px", function() {
      const el = text(20,30,'Hello World');
      expect(el.textContent).toBe("Hello World");
      expect(el.getAttribute('font-family')).toBe('sans-serif');
      expect(el.getAttribute('font-size')).toBe('12');
    });
    it("should create a <text>Hello World</text> with font `serif` and size of 22px", function() {
      const el = text(20,30,'Hello World','serif',22);
      expect(el.textContent).toBe("Hello World");
      expect(el.getAttribute('font-family')).toBe('serif');
      expect(el.getAttribute('font-size')).toBe('22');
    });
  });
  describe("Test wrong creation of Graphics Primitives rect(..), circle(..), etc.", function() {
    it("should throw an Error if  a <rect> has a width and/or height <= 0", function() {
      expect(() => rect(10,5,-10,10) ).toThrow(new Error("Width less or equal to 0") );
      expect(() => rect(10,5,10,-10) ).toThrow(new Error("Height less or equal to 0") );
      expect(() => rect(10,5,-10,-10) ).toThrow(new Error("Size less or equal to 0") );
    });
    it("should throw an Error if  a <circle> has a radius <= 0", function() {
      expect(() => circle(10,5,0) ).toThrow(new Error("Radius less or equal to 0") );
    });
  });
  // Create a rectangle with many attributes
    describe("Create a Test SVG with a rectangle", function() {
    let el;
    beforeEach(function() {
      const sketch = svg(100,100,[0,0,100,100]);
      attributes(sketch,['id','test']);
      sketch.style.margin = "10px";
      el = rect(10,10,80,30);
      const txt = text(15,30,'Hello World','Verdana',14);
      attributes(el,['fill','blue','stroke','pink','stroke-width',5,'fill-opacity',0.1,'stroke-opacity',0.9]);
      append(sketch,el);
      append(sketch,txt);
      append(document.body,sketch);
    });
    it("should get a `fill-opacity` attribute equal to 0.1", function() {
      console.log(attribute(el,'fill-opacity'));
      expect(attribute(el,"fill-opacity")).toBe("0.1");
    });
  });
  
});


