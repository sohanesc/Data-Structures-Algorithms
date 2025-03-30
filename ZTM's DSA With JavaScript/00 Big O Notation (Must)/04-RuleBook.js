//#Rule 1 (Worst Case) -- For loop in Javascript.
const nemo = ["nemo"];

function findNemo1(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === "nemo") {
      console.log("Found NEMO!");
    }
  }
}

findNemo1(nemo);

//#Rule 2 (Remove Constants)
function printFirstItemThenFirstHalfThenSayHi100Times(items) {
  console.log(items[0]);

  var middleIndex = Math.floor(items.length / 2);
  var index = 0;

  while (index < middleIndex) {
    console.log(items[index]);
    index++;
  }

  for (var i = 0; i < 100; i++) {
    console.log("hi");
  }
}

//#Rule 3 (Different Terms For Inputs)
//Log all pairs of array

const boxes = ["a", "b", "c", "d", "e"];
function logAllPairsOfArray(array) {
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      console.log(array[i], array[j]);
    }
  }
}

logAllPairsOfArray(boxes); // O(n^2)

//#4 (Drop Non Dominants)
function printAllNumbersThenAllPairSums(numbers) {
  console.log("these are the numbers:");
  numbers.forEach(function (number) {
    console.log(number);
  });

  console.log("and these are their sums:");
  numbers.forEach(function (firstNumber) {
    numbers.forEach(function (secondNumber) {
      console.log(firstNumber + secondNumber);
    });
  });
}

printAllNumbersThenAllPairSums([1, 2, 3, 4, 5]); // O(n^2)

//#5 Space complexity O(1)
function boooo(n) {
  for (let i = 0; i < n; i++) {
    console.log("booooo");
  }
}

// #6 Space complexity O(n)
function arrayOfHiNTimes(n) {
  var hiArray = [];
  for (let i = 0; i < n; i++) {
    hiArray[i] = "hi";
  }
  return hiArray;
}

arrayOfHiNTimes(6);
