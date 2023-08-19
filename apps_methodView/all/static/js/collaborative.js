window.onload = function(){ 
    // Content Based AutoComplete
    let availableCollaborative = productIds;
    // console.log(availableCollaborative);
    const contentResults = document.querySelector(".collaborative-result");
    const contentInputs = document.getElementById("collaborative-autocomplete");


    contentInputs.onkeyup = function() {
        let results = [];
        let input = contentInputs.value;
        if (input.length) {
            results = availableCollaborative.filter((keyword) => {
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
        const content = results.map((list) => {
            return "<li onclick = selectCollaborative(this)>" + list + "</li>";
        });
        contentResults.innerHTML = '<ul >' + content.join('') + '</ul>';
    }
};

function selectCollaborative(element){
    let selectResult = element.textContent;
    const contentResults = document.querySelector(".collaborative-result");
    const contentInputs = document.getElementById("collaborative-autocomplete");
    contentInputs.value = selectResult;
    contentResults.innerHTML = '';
    document.getElementById("collaborative-autocomplete").focus();
}
