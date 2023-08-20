let availableProducts = suggestions;
// console.log('Hello FlipKart Members!');   
// console.log(availableProducts);

// Search Box
const resultsBox = document.querySelector(".result-box");
const inputBox = document.getElementById("input-box");

inputBox.onkeyup = function() {
    let results = [];
    let input = inputBox.value;
    if (input.length) {
        results = availableProducts.filter((keyword) => {
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
    if (results.length > 1) {
        const content = results.map((list) => {
            return "<li onclick=selectInput(this)>" + list + "</li>";
        });
        resultsBox.innerHTML = '<ul >' + content.join('') + '</ul>';
    }
}

function selectInput(element){
    let selectResult = element.textContent;
    inputBox.value = selectResult;
    resultsBox.innerHTML = '';
    document.getElementById("input-box").focus();
}





// // Collaborative AutoComplete
// const collaborativeResults = document.querySelector(".result-box");
// const collaborativeInputs = document.getElementById("search-autocomplete");

// // Hybrid AutoComplete
// const hybridResults = document.querySelector(".result-box");
// const hybridInputs = document.getElementById("search-autocomplete");

