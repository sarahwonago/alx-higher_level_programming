#!/usr/bin/node
function findSecondLargestInteger (args) {
  if (args.length < 3) {
    return 0;
  }

  let largest = 0;
  let secondLargest = 0;

  for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i]);

    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }

  return secondLargest;
}

const args = process.argv;

const result = findSecondLargestInteger(args);
console.log(result);
