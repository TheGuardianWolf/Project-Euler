module.exports = function (num) {

    var half = Math.floor(num / 2), // Ensures a whole number <= num.
        array = [1], // 1 will be a part of every solution.
        i, j;

    // Determine our increment value for the loop and starting point.
    num % 2 === 0 ? (i = 2, j = 1) : (i = 3, j = 2);

    for (i; i <= half; i += j) {
        num % i === 0 ? array.push(i) : false;
    }

    array.push(num);

    return array;
};
