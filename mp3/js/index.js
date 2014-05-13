function main() {
    console.log("JS file loaded!");
    d3.json('data/cindas_data.json', function(data) {
        data = _.map(data, function(elem) {
            return {name: elem.word, value: elem.freq};
        });
        histogram("#main", data);
    });

}
function histogram(id, data) {
    // Get size of container and set some defaults.
    var width = $(id).width() || 900;
    var height = $(id).height() || 200;

    // A few colors to mess with
    var color = d3.scale.category10();
    // Insert a new SVG element (our chart)
    var chart = d3.select(id)
            .append("svg")
            .attr("width", width)
            .attr("height", height);

    // this is our scale for the x-axis. We use this to scale the chart to
    // the width of our space, regardless of the number of buckets.
    var x = d3.scale.linear()
            .domain([0, data.length])
            .range([0, width]);
    // We also want a scale for our y-axis so we can make the height of the bars
    // relative to the largest bar in our dataset
    var y = d3.scale.linear()
            .domain([0, d3.max(data, function(d) { return d.value; })])
            .range([0, height]);

    // The g elements represent a data point.
    var g = chart.selectAll("g")
            .data(data)
            .enter()
            .append("g");

    // Each g element has a rectangle that is our bar
    g.append("rect")
        .attr("x", function(d, i) { return x(i);})
        .attr("y", function(d) {return height - y(d.value) - 25;})
        .style("fill", function(d, i) { return color(i); })
        .attr("width", width/data.length)
        .attr("height", function(d) { return y(d.value); });

    // and a text element describing the bar
    g.append("text")
        .attr("x", function(d, i) { return x(i) + width / data.length / 4;})
        .attr("y", function(d) {return height - 5;})
        .style("fill", "black")
        .text(function(d) {return d.name; });
}
