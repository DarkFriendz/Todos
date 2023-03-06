// Vars
const search = document.getElementById("search");
const searchDate = document.getElementById("searchDate");
const select = document.getElementById("select");

// Select 
select.addEventListener("change", function() {
    const rows = document.getElementById("Table").rows;
    for (let i = 0; i < rows.length; i++) {
        if(i >= 1) {
            rows[i].style.display = "table-row";
        }
    }
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
            for (let i = 0; i < rows.length; i++) {
                if(i >= 1) {
                    if(rows[i].className != "Done") {
                        rows[i].style.display = "none";
                    }
                }
            }
        break;
        case 'notdone':
            search.style.display = "none";
            searchDate.style.display = "none";
            for (let i = 0; i < rows.length; i++) {
                if(i >= 1) {
                    if(rows[i].className == "Done") {
                        rows[i].style.display = "none";
                    }
                }
            }
        break;
        case 'expired':
            search.style.display = "none";
            searchDate.style.display = "none";
            for (let i = 0; i < rows.length; i++) {
                if(i >= 1) {
                    if(rows[i].className != "Expired") {
                        rows[i].style.display = "none";
                    }
                }
            }
        break;
    }
});

// Search Input

search.addEventListener("input", function() {
    const value = search.value.toLowerCase();
    const rows = document.getElementById("Table").rows;
    
    if(select.value == 'title') {
        for (let i = 0; i < rows.length; i++) {
            if(i >= 1) {
                if (rows[i].cells[1].textContent.toLowerCase().indexOf(value) !== -1) {
                    rows[i].style.display = "table-row";
                } else {
                    rows[i].style.display = "none";
                }
            }
        }
    } else if(select.value == 'description') {
        for (let i = 0; i < rows.length; i++) {
            if(i >= 1) {
                if (rows[i].cells[2].textContent.toLowerCase().indexOf(value) !== -1) {
                    rows[i].style.display = "table-row";
                } else {
                    rows[i].style.display = "none";
                }
            }
        }
    }
});

// Search Date

searchDate.addEventListener("change", function() {
    const rows = document.getElementById("Table").rows;
    for (let i = 0; i < rows.length; i++) {
        if(i >= 1) {
            if (rows[i].cells[3].textContent == searchDate.value.split("T")[0]) {
                rows[i].style.display = "table-row";
            } else {
                rows[i].style.display = "none";
            }
        }
    }
});