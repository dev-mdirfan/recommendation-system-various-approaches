let availableKeywords = [
    "keyword1",
    "keyword2",
    "keyword3",
    "keyword4",
    "keyword5",
    "keyword6",
    "keyword7",
    "keyword8",
    "keyword9",
    "keyword10",
    "keyword10",
    "keyword10",
    "keyword10",
    "keyword10",
    'apple',
    'banana',
    'orange',
    'pineapple',
    'grape',
    'strawberry',
    'blueberry',
    'apple pie where to buy in singapore 2021',
];

const resultsBox = document.querySelector(".result-box");
const inputBox = document.getElementById("input-box");

// Write a function that takes in a string and returns a list of matching keywords
inputBox.onkeyup = function() {
    let results = [];
    let input = inputBox.value;
    if (input.length) {
        results = availableKeywords.filter((keyword) => {
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
        // const top25Results = results.slice(0, 25);

    }
    display(results);

    if (results.length === 0) {
        resultsBox.innerHTML = '';
    }
}


function display(results){
    const content = results.map((list) => {
        return "<li onclick=selectInput(this)>" + list + "</li>";
    });
    resultsBox.innerHTML = '<ul>' + content.join('') + '</ul>';
}

function selectInput(element){
    let selectResult = element.textContent;
    inputBox.value = selectResult;
    resultsBox.innerHTML = '';
}
