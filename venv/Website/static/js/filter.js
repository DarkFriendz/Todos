// consts
const filter = document.getElementById("filter")
const Search = document.getElementById("Search")
const SearchDate = document.getElementById("SearchDate")

// Filter
filter.addEventListener("change", function() {
    const tableRows = document.querySelectorAll("#table tbody tr");
    for (const row of tableRows) {
        row.style.display = "table-row"
    }

    if (filter.value != 0) {
        if (filter.value != 3) {
            Search.style.display = "block"
            SearchDate.style.display = "none"
        } else {
            Search.style.display = "none"
            SearchDate.style.display = "block"
        }
    } else {
        Search.style.display = "none"
        SearchDate.style.display = "none"

        if (filter.selectedIndex != 2) {
            const tableRows = document.querySelectorAll("#table tbody tr");
            for (const row of tableRows) {
                if(row.id != "") {
                    if (row.cells[0].children[0].checked != false) {
                        row.style.display = "table-row"
                    } else {
                        row.style.display = "none"
                    }
                }
            }
        } else {
            const tableRows = document.querySelectorAll("#table tbody tr");
            for (const row of tableRows) {
                if(row.id != "") {
                    if (row.cells[0].children[0].checked != true) {
                        row.style.display = "table-row"
                    } else {
                        row.style.display = "none"
                    }
                }
            }
        }
    }
})

// Search Text
Search.addEventListener("input", function() {
    const tableRows = document.querySelectorAll("#table tbody tr");
    const value = Search.value.trim().toLowerCase()
    for (const row of tableRows) {
        if(row.id != "") {
            if (value != 0) {
                if (value != "") {
                    const filterValue = row.cells[filter.value].textContent.trim().toLowerCase()
                    const match = filterValue.includes(value)
                    row.style.display = match ? "": "none";
                } else {
                    row.style.display = "table-row"
                }
            } else {
                row.style.display = "table-row"
            }
        }
    }
})

//Search Date
SearchDate.addEventListener("input", function() {
    const date = SearchDate.value.split(/-/g)
    const dateFormat = `${date[2]}/${date[1]}/${date[0]}`

    const tableRows = document.querySelectorAll("#table tbody tr");
    for (const row of tableRows) {
        if(row.id != "") {
            if (row.cells[3].textContent != 'Vazio') {
                if (row.cells[3].textContent == dateFormat) {
                    row.style.display = "table-row"
                } else {
                    row.style.display = "none"
                }
            } else {
                row.style.display = "none"
            }
        }
    }
})