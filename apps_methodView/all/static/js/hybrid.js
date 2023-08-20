window.onload = function(){ 
    // Content Based AutoComplete
    let availableHybrids1 = userIds;
    // console.log(availableCollaborative);
    const contentResults1 = document.querySelector(".hybrid1-result");
    const contentInputs1 = document.getElementById("hybrid1-autocomplete");


    contentInputs1.onkeyup = function() {
        let results = [];
        let input = contentInputs1.value;
        if (input.length) {
            results = availableHybrids1.filter((keyword) => {
                return keyword.toLowerCase().includes(input.toLowerCase());
            });
            // const top25Results = results.slice(0, 25);

        }
        display(results.slice(0, 25));

        if (results.length === 0) {
            contentResults1.innerHTML = '';
        }
    }


    function display(results){
        if (results.length > 1) {
            const content = results.map((list) => {
                return "<li onclick = selectHybrid1(this)>" + list + "</li>";
            });
            contentResults1.innerHTML = '<ul >' + content.join('') + '</ul>';
        }
    }


// /////////////////////////////////////////////////////////////////////////

    // Content Based AutoComplete
    let availableHybrids2 = productIds2;
    // console.log(availableCollaborative);
    const contentResults2 = document.querySelector(".hybrid2-result");
    const contentInputs2 = document.getElementById("hybrid2-autocomplete");


    contentInputs2.onkeyup = function() {
        let results = [];
        let input = contentInputs2.value;
        if (input.length) {
            results = availableHybrids2.filter((keyword) => {
                return keyword.toLowerCase().includes(input.toLowerCase());
            });
            // const top25Results = results.slice(0, 25);

        }
        display(results.slice(0, 25));

        if (results.length === 0) {
            contentResults2.innerHTML = '';
        }
    }


    function display(results){
        if (results.length > 1) {
            const content = results.map((list) => {
                return "<li onclick = selectHybrid2(this)>" + list + "</li>";
            });
            contentResults2.innerHTML = '<ul >' + content.join('') + '</ul>';
        }
    }

};

function selectHybrid2(element){
    let selectResult = element.textContent;
    const contentResults2 = document.querySelector(".hybrid2-result");
    const contentInputs2 = document.getElementById("hybrid2-autocomplete");
    contentInputs2.value = selectResult;
    contentResults2.innerHTML = '';
    document.getElementById("hybrid2-autocomplete").focus();
}

function selectHybrid1(element){
    let selectResult = element.textContent;
    const contentResults1 = document.querySelector(".hybrid1-result");
    const contentInputs1 = document.getElementById("hybrid1-autocomplete");
    contentInputs1.value = selectResult;
    contentResults1.innerHTML = '';
    document.getElementById("hybrid1-autocomplete").focus();
}

