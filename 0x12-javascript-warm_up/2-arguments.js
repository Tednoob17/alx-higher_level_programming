#!/usr/bin/node
const arg = process.argv.length;
/*
if (arg === 2) {
	console.log("No argument")
}else if (arg === 3) {
	console.log("Argument found")
} else {
	console.log("Arguments found")
}
*/
console.log(arg === 2 ? 'No argument' : arg === 3 ?  'Argument found' : 'Arguments found');
