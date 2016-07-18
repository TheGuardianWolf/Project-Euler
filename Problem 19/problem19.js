var fs = require('fs');

var data = fs.readFileSync('text.txt');

var triangle = data.toString().split('\r\n').map(function(i) {
  return i.split(' ').map(function(j) {
    return parseInt(j);
  });
});

var reduced = triangle.reduceRight(function(previousValue, currentValue, index, array) {
  return currentValue.map(function(val, i) {
    return Math.max(
      val + previousValue[i],
      val + previousValue[i + 1]);
  });
});

console.log(triangle);
console.log(reduced);
