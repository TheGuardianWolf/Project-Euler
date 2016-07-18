function findPermutations(input) {
  var permArr = [],
  usedChars = [];

  function permute(input) {
    var i, ch;
    for (i = 0; i < input.length; i++) {
      if (permArr.length === 1000000) {
        break;
      }
      ch = input.splice(i, 1)[0];
      usedChars.push(ch);
      if (input.length === 0) {
        permArr.push(usedChars.slice());
      }
      permute(input);
      input.splice(i, 0, ch);
      usedChars.pop();
    }
    return permArr;
  }
  return permute(input);
}


console.log(findPermutations([0,1,2,3,4,5,6,7,8,9])[999999].join(''));
