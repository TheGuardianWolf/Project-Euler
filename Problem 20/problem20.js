var datejs = require('datejs');

var sundays = 0;

for (var year = 1901; year <= 2000; year++) {
    for (var month = 1; month <= 12; month++) {
        if ((Date.parse(year.toString() + '/' + month.toString() + '/1')).is().sunday()) {
            sundays++;
        }
    }
}

console.log(sundays);
