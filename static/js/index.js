var textInput = document.getElementById("textInput");
var scoreButton = document.getElementById('scoreButton');
var banner = document.getElementById('userScore');
var needle = document.getElementById("needle");
var maxScore = 100;

function showScore() {
  // Get the score number from the input
  var userScoreInput = document.getElementById("textInput").value
  userScore.innerHTML = userScoreInput;
  console.log("entered: " + userScoreInput);
  
  // Find percent out of max score
  var scorePercent = userScoreInput / maxScore;
  console.log("score percent out of max: " + scorePercent);
  
  // Find angle to animate to -- between 0 and 90
  var needleAngle = scorePercent * 90
  console.log("needle angle: " + needleAngle);
  
  // Write angle to transform rotate amount
  needle.style.setProperty('--needle-position', needleAngle)
}
// visulaize the data
scoreButton.addEventListener("click", showScore);


