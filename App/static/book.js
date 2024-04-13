
async function getBookData(){
    const response = await fetch('/api/books');
    return response.json();
}

function loadBookTable(books){
    const table = document.querySelector('#bookresult');
    for(let book of books){
        table.innerHTML += `<tr>
            <td>${book.id}</td>
            <td>${book.name}</td>
        </tr>`;
    }
}

async function book(){
    const books = await getBookData();
    loadBookTable(books);
}

book();