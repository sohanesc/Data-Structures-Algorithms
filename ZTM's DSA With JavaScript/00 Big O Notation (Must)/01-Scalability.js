const nemo = ["nemo", "dory", "nemo", "bruce", "nemo"];
const large = new Array(100).fill("nemo");

function findNemo(array) {
  let t0 = performance.now();
  for (let i = 0; i < array.length; i++) {
    if (array[i] === "nemo") {
      console.log("Found NEMO!");
    }
  }

  let t1 = performance.now(); // performance.now() returns the current time in miliseconds
  console.log(`Call to find Nemo took ${t1 - t0} miliseconds.`);
}

// findNemo(nemo);
findNemo(large);
