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


// /////////////////////////////////////////////////////////////////////////////

let availableKeywords = [
    "keyword1",
    "keyword2",
    "keyword3",
    // ... (other keywords)
    "blueberry",
];

const resultsBox = document.querySelector(".result-box");
const inputBox = document.getElementById("input-box");

function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

inputBox.oninput = function() {
    let results = [];
    let input = inputBox.value.trim();
    if (input.length) {
        const escapedInput = escapeRegExp(input);
        const regex = new RegExp(escapedInput, 'i'); // Match anywhere within the keyword
        results = availableKeywords.filter((keyword) => regex.test(keyword));
    }
    display(results);

    if (results.length === 0) {
        resultsBox.innerHTML = '';
    }
};

function display(results) {
    const content = results.map((keyword) => {
        return `<li onclick="selectInput(this)">${keyword}</li>`;
    });
    resultsBox.innerHTML = '<ul>' + content.join('') + '</ul>';
}

function selectInput(element) {
    let selectResult = element.textContent;
    inputBox.value = selectResult;
    resultsBox.innerHTML = '';
}

////////////////////////////////////////////////////////////////////////



$(document).ready(function () {
    let availableKeywords = [
        "keyword1",
        "keyword2",
        "keyword3",
        // ... (other keywords)
        "blueberry",
    ];

    const resultsBox = $(".result-box");
    const inputBox = $("#input-box");

    function escapeRegExp(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    inputBox.on("input", function () {
        let results = [];
        let input = inputBox.val().trim();
        if (input.length) {
            const escapedInput = escapeRegExp(input);
            const regex = new RegExp(escapedInput, 'i'); // Match input anywhere
            results = availableKeywords.filter((keyword) => regex.test(keyword));
        }
        display(results);

        if (results.length === 0) {
            resultsBox.html('');
        }
    });

    function display(results) {
        const content = results.map((keyword) => {
            return `<li>${keyword}</li>`;
        });
        resultsBox.html('<ul>' + content.join('') + '</ul>');
    }

    resultsBox.on("click", "li", function () {
        let selectResult = $(this).text();
        inputBox.val(selectResult);
        resultsBox.html('');
    });
});



