window.onload = function(){ 
    // Content Based AutoComplete
    let availableContents = productNames;
    // console.log(availableContents);
    const contentResults = document.querySelector(".content-result");
    const contentInputs = document.getElementById("content-autocomplete");


    contentInputs.onkeyup = function() {
        let results = [];
        let input = contentInputs.value;
        if (input.length) {
            results = availableContents.filter((keyword) => {
                return keyword.toLowerCase().includes(input.toLowerCase());
            });
            // const top25Results = results.slice(0, 25);

        }
        display(results.slice(0, 25));

        if (results.length === 0) {
            contentResults.innerHTML = '';
        }
    }

    function display(results){
        if (results.length > 1) {
            const content = results.map((list) => {
                return "<li onclick = selectContent(this)>" + list + "</li>";
            });
            contentResults.innerHTML = '<ul >' + content.join('') + '</ul>';
        }
    }
};

function selectContent(element){
    let selectResult = element.textContent;
    const contentResults = document.querySelector(".content-result");
    const contentInputs = document.getElementById("content-autocomplete");
    contentInputs.value = selectResult;
    contentResults.innerHTML = '';
    document.getElementById("content-autocomplete").focus();
}
