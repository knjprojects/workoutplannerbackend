
async function getReviewData(){
    const response = await fetch('/api/reviews');
    return response.json();
}

function loadReviewTable(reviews){
    const table = document.querySelector('#reviewresult');
    for(let review of reviews){
        table.innerHTML += `<tr>
            <td>${review.id}</td>
            <td>${review.name}</td>
        </tr>`;
    }
}

async function review(){
    const reviews = await getReviewData();
    loadReviewTable(reviews);
}

review();