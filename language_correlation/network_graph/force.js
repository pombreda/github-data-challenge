var scaleNode = function(node) {
//  return Math.log(node.size * node.size) / Math.log(2);
  return Math.sqrt(node.size) / 20;
};

var w = 1200,
    h = 900;

var vis = d3.select("body").append("svg:svg")
    .attr("width", w)
    .attr("height", h);

d3.json('graph.json', function(json) {
    var force = self.force = d3.layout.force()
        .nodes(json.nodes)
        .links(json.links)
        .gravity(.05)
        .distance(500)
        .charge(-1000)
        .size([w, h])
        .start();

    var link = vis.selectAll("line.link")
        .data(json.links)
        .enter().append("svg:line")
          .attr("class", "link")
          .attr("x1", function(d) { return d.source.x; })
          .attr("y1", function(d) { return d.source.y; })
          .attr("x2", function(d) { return d.target.x; })
          .attr("y2", function(d) { return d.target.y; })
          .style("stroke-width", function(d) { return (d.value/5); });

    var node = vis.selectAll("g.node")
        .data(json.nodes)
      .enter().append("svg:g")
        .attr("class", "node")
        .call(force.drag);

    node.append("svg:circle")
        .attr("fill", "red")
        .attr("x", "-8px")
        .attr("y", "-8px")
        .attr("r", function(d) { return scaleNode(d); });

    node.append("svg:text")
        .attr("class", "nodetext")
        .attr("dx", function(d) { return 5+scaleNode(d); })
        .attr("dy", 0)
        .text(function(d) { return d.name });

    force.on("tick", function() {
      link.attr("x1", function(d) { return d.source.x; })
          .attr("y1", function(d) { return d.source.y; })
          .attr("x2", function(d) { return d.target.x; })
          .attr("y2", function(d) { return d.target.y; });

      node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
    });
});
