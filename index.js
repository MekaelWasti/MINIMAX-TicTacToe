var playerTurn = ["X", "O"];
var player = 0;
gameEnd = false;

window.addEventListener("DOMContentLoaded", () => {
  const tiles = Array.from(document.querySelectorAll(".boardTile"));

  console.log("TILE ARRAY", tiles);

  tiles.forEach((tile, index) => {
    tile.addEventListener("click", () => userAction(tile, index));
  });

  const playAgainButton = document.querySelector(".reset");
  playAgainButton.addEventListener("click", () => resetGame(tiles));
});

const userAction = (tile, index) => {
  console.log(tile.style);
  console.log(player);
  var turn = "boardTilePlayer" + playerTurn[player];

  if (
    !tile.classList.contains("boardTilePlayerX") &&
    !tile.classList.contains("boardTilePlayerO")
  ) {
    tile.classList.add(turn);
    if (player == 0) {
      player = 1;
    } else if (player == 1) {
      player = 0;
    }
  }

  fetchData(index);
  AIMove = getDict();
  console.log(`RESPONSE::::: ${AIMove}`);
};

const resetGame = (tiles) => {
  tiles.forEach((tile, index) => {
    tile.classList.remove("boardTilePlayerX");
    tile.classList.remove("boardTilePlayerO");
    player = 0;
  });
};

function fetchData(tileIndex) {
  fetch("http://127.0.0.1:5000/receiver", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
      Accept: "application/json",
    },
    // Strigify the payload into JSON:
    // body: JSON.stringify(String(tileIndex)),
    body: JSON.stringify({
      UserMove: String(tileIndex + 1),
      AIMove: "",
      GameEnded: gameEnd,
    }),
  })
    .then((res) => {
      if (res.ok) {
        return res.json();
      } else {
        alert("something is wrong");
      }
    })
    .then((jsonResponse) => {
      // Log the response data in the console
      // console.log(jsonResponse);
    })
    .catch((err) => console.error(err));

  console.log(tileIndex);
}

async function getDict() {
  const response = await fetch("http://127.0.0.1:5000/sender", {
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  });
  const text = await response.text();
  // const text = await response.json();
  console.log(text);

  // console.log(JSON.parse(text));
}

// async function recieveData() {
//   let result = await fetch("http://127.0.0.1:5000/sender", {
//     headers: {
//       "Content-Type": "application/json",
//       Accept: "application/json",
//     },
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       console.log(data);
//       return data;
//     });
//   console.log("RESULT");
//   console.log(result);
// }

// async function fetchYER() {
//   let response = await fetch("http://127.0.0.1:5000/sender");
//   let data = await response.json();
//   data = JSON.stringify(data);
//   data = JSON.parse(data);
//   console.log(data);
//   return data.text;
// }

// while (!gameEnd) {
//   console.log("User Select A Tile");
// }
