document.querySelector("#myButton").onclick = function () {
  const h1 = document.querySelector("#myH1");
  console.log(h1.style);
  h1.style.color = "red";
};


// ---------------------------------------------------------
document.querySelector(".reset").onclick = function () {
  const element = document.querySelector(".boardTile");
  console.log(element.style);
  element.style.backgroundColor = "red";
};
