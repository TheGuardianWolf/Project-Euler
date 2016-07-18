var fs = require('fs');

var data = fs.readFileSync('names.txt');

var nameSums = JSON.parse('[' + data.toString() + ']')
  .sort()
  .reduce(function(prev, curr, index) {
    return prev += (index + 1) * curr.split('')
    .reduce(function(total, letter) {
      return total + letter.charCodeAt(0) - 64;
    }, 0);
  }, 0);

console.log(nameSums);
