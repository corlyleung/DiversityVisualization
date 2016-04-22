data = [{
  name: "A",
  value: 1,
  value2: 2
}, {
  name: "B",
  value: 4,
  value2: 5
}, {
  name: "C",
  value: 7,
  value2: 9
}, {
  name: "D",
  value: 2,
  value2: 7
}, {
  name: "E",
  value: 1,
  value2: 1
}, {
  name: "F",
  value: 5,
  value2: 2
}]

var margin = {
    top: 30,
    right: 10,
    bottom: 10,
    left: 10
  },
  width = 500 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

var x = d3.scale.linear()
  .range([0, width])

var y = d3.scale.ordinal()
  .rangeRoundBands([0, height], .2);

var xAxis = d3.svg.axis()
  .scale(x)
  .orient("top");

var svg = d3.select("body").append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

x.domain([-10, 10])
y.domain(data.map(function(d) {
  return d.name;
}));

svg.selectAll(".bar")
  .data(data)
  .enter().append("rect")
  .attr("class", "bar")
  .attr("x", function(d) {
    return x(Math.min(0, d.value));
  })
  .attr("y", function(d) {
    return y(d.name);
  })
  .attr("width", function(d) {
    return Math.abs(x(d.value) - x(0));
  })
  .attr("height", y.rangeBand());

svg.selectAll(".bar2")
  .data(data)
  .enter().append("rect")
  .attr("class", "bar2")
  .attr("x", function(d) {
    return x(Math.min(0, -d.value2));
  })
  .attr("y", function(d) {
    return y(d.name);
  })
  .attr("width", function(d) {
    return Math.abs(x(-d.value2) - x(0));
  })
  .attr("height", y.rangeBand());


svg.append("g")
  .attr("class", "x axis")
  .call(xAxis);

svg.append("g")
  .attr("class", "y axis")
  .append("line")
  .attr("x1", x(0))
  .attr("x2", x(0))
  .attr("y2", height);


function type(d) {
  d.value = +d.value;
  return d;
}
