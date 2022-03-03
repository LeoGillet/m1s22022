describe("Pie and Donut charts", function() {
    describe("create(...)", function() {
        it("Create ('rect')", function () {
            const el = create('rect');
            expect(el instanceof SVGRectElement).toBe(true);
        });
        it("Create ('svg')", function() {
            const el = create('svg');
            expect(el instanceof SVGElement).toBe(true);
        });
    });
    describe("attribute(...)", function() {
        let el;
        beforeEach(function() {
            el = create('rect');
            attribute(el, "color", "150");
        });
        it("attribute(el, 'color', 150)", function() {
            expect(el.getAttribute('color')).toBe("150");
        });
        it("attribute(el, 'color')", function () {
            expect(attribute(el, 'color')).toBe("150");
        });
    });
    describe("attributes(...)", function() {
        let el;
        beforeEach(function() {
            el = create('rect');
            let arr = ['color', 150, 'width', 30];
            attributes(el, arr);
        });
        it("attributes(el,arr) -- color", function() {
            expect(el.getAttribute('color')).toBe("150");
        });
        it("attributes(el,arr) -- width", function() {
            expect(el.getAttribute('width')).toBe("30");
        });
    })
});

