var playerTurn = ["X", "O"];
var player = 0;

window.addEventListener("DOMContentLoaded", () => {
  const tiles = Array.from(document.querySelectorAll(".boardTile"));

  console.log(tiles[0]);

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
    body: JSON.stringify(String(tileIndex)),
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
      console.log(jsonResponse);
    })
    .catch((err) => console.error(err));

  console.log(tileIndex);
}
