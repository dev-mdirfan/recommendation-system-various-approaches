let availableKeywords = suggestions;

// console.log('howdy');   
// console.log(availableKeywords);

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
    display(results.slice(0, 25));

    if (results.length === 0) {
        resultsBox.innerHTML = '';
    }
}


function display(results){
    const content = results.map((list) => {
        return "<li onclick=selectInput(this)>" + list + "</li>";
    });
    resultsBox.innerHTML = '<ul >' + content.join('') + '</ul>';
}

function selectInput(element){
    let selectResult = element.textContent;
    inputBox.value = selectResult;
    resultsBox.innerHTML = '';
}
