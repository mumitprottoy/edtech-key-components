/*
Extracting Question Bank from exposed api over the internet.
Extracted 15+ questions (Subject: English)
*/

// the source site is csrf-protected. 
// This script needs to be executed in the console of the browser (devtools)

let dataSet = [];
// the source is paginated, each page yielding 20 questions
// total 778 pages available
const totalPages = 778;
let _url = new URL(document.location.toString());


async function fetchQuestionSet(_url) {
    const response = await fetch(_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFTOKEN': csrftoken,
        },
        body: JSON.stringify({})
    });

    const questionSet = await response.json();
    dataSet.push(questionSet);
}


async function iterate() {
    for (var i = 0; i < totalPages; i++) {
        const pageNum = (i + 1).toString();
        _url.searchParams.set('page', pageNum);
        await fetchQuestionSet(_url);
    }

    console.log(dataSet);
}


iterate();