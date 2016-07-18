var sequenceLength = 0;

for (var i = 1000; i > 1; i--) {
    if (sequenceLength >= i) {
        break;
    }

    var foundRemainders = [];
    var value = 1;
    var position = 0;

    while ((foundRemainders[value] === undefined || foundRemainders[value] === 0) && value !== 0) {
        foundRemainders[value] = position;
        value *= 10;
        value %= i;
        position++;
    }

    if (position - foundRemainders[value] > sequenceLength) {
        sequenceLength = position - foundRemainders[value];
    }
    console.log(i);
}
