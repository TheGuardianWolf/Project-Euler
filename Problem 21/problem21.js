function properDivisors(num) {

    var half = Math.floor(num / 2), // Ensures a whole number <= num.
        str = [1], // 1 will be a part of every solution.
        i, j;

    // Determine our increment value for the loop and starting point.
    num % 2 === 0 ? (i = 2, j = 1) : (i = 3, j = 2);

    for (i; i <= half; i += j) {
        num % i === 0 ? str.push(i) : false;
    }
    return str;
}

function arraySum(array) {
  return array.reduce(function(prev, curr) {
    return prev + curr;
  });
}

var numbers = [{},{
  amicable : false,
  properDivisors : [],
  divisorSum : 0
}];

var amicable = [];

for (var i = 2; i < 10000; i++) {
  numbers[i] = {};
  numbers[i].properDivisors = properDivisors(i);
  numbers[i].divisorSum = arraySum(numbers[i].properDivisors);
}

for (var i = 2; i < 10000; i++) {
  if (!numbers[i].amicable) {
    if (numbers[numbers[i].divisorSum] && numbers[numbers[i].divisorSum].divisorSum === i && numbers[i].divisorSum !== i) {
      numbers[i].amicable = true;
      numbers[numbers[i].divisorSum].amicable = true;
      console.log(i.toString() + ' paired with ' + numbers[i].divisorSum.toString());
      amicable.push(i);
    }
  }
  else {
    amicable.push(i);
  }
}

console.log('Sum is ' + arraySum(amicable).toString());
