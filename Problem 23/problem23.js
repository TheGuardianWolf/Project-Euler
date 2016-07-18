var factorsOf = require('./factorsOf');
var arraySum = require('./arraySum');

var numbers = [{},{
  abundant : false,
  isSum : false
}];
var abundant = [];
var sum = 0;

var i, j;

for (i = 2; i <= 28123; i++) {
  numbers[i] = {};
  numbers[i].abundant = factorsOf(i).slice(0,-1).sum() > i;
  numbers[i].isSum = false;
  if (numbers[i].abundant) {
    abundant.push(i);
  }
}

var reduction = function(val, test) {
  if (val + test <= 28123) {
    numbers[val + test].isSum = true;
  }
  return val;
};

var map = function(val) {
  if (val * 2 <= 28123) {
    numbers[val * 2].isSum = true;
  }
};

for (i = 0; i < abundant.length - 2; i++) {
  abundant.slice(i).reduce(reduction);
  abundant.slice(i).map(map);
}

for (i = 1; i < numbers.length; i++) {
  if (!numbers[i].isSum) {
    sum += i;
  }
}

console.log(sum);
