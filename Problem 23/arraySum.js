Array.prototype.sum = function() {
  return this.reduce(function(prev, curr) {
    return prev + curr;
  });
};

module.exports = Array.prototype.sum;
