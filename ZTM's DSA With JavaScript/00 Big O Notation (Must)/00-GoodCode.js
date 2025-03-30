const nemo = ["dory", "nemo", "nemo", "bruce", "nemo"];

function findNemo(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === "nemo") {
      console.log("Found NEMO!");
      //   return; // Exit code after one occourance
    }
  }
}

findNemo(nemo);
