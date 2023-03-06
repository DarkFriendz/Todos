// Vars
const search = document.getElementById("search");
const searchDate = document.getElementById("searchDate");
const select = document.getElementById("select");

// Select 
select.addEventListener("change", function() {
    switch(select.value) {
        case 'title':
            search.style.display = "block";
            searchDate.style.display = "none";
        break;
        case 'description':
            search.style.display = "block";
            searchDate.style.display = "none";
        break;
        case 'date':
            search.style.display = "none";
            searchDate.style.display = "block";
        break;
        case 'done':
            search.style.display = "none";
            searchDate.style.display = "none";
        break;
        case 'notdone':
            search.style.display = "none";
            searchDate.style.display = "none";
        break;
        case 'expired':
            search.style.display = "none";
            searchDate.style.display = "none";
        break;
    }
});

// Search Input

search.addEventListener("input", function() {
    const value = search.value.toLowerCase();
    const rows = document.getElementById("Table").rows;

    for (let i = 0; i < rows.length; i++) {
        if(i >= 1) {
            console.log(rows[i]);
        }
    }
});