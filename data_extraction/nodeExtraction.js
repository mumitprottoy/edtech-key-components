/*
Extracting learning materials from publicly accessible source over the internet.
Materials are organized by chapters. Chapters have multiple layers (topic, sub-topic etc.)
Denoting each layer as Node
*/

[...document.getElementsByClassName('position-relative')].forEach(element => element.remove());
// selcting the parentElements of the data by class
const chapterUlList = [...document.getElementsByClassName('p-md-0 ps-md-3 p-3 myList')];
// the site I chose had 5 node layers
const nodeType = ['Chapter', 'Topic', 'Section', 'Sub-Section', 'Micro-Section'];

// a recursive function to make multi-layerd map
const extractNode = (ulList, depth = 0) => {
    let nodeList = [];

    ulList.forEach(ul => {
        const a = ul.children[0].getElementsByTagName('a')[0];
        nodeList.push({
            nodeType: nodeType[depth],
            title: a.innerText.trim(),
            url: a.href.trim(),
            note: "",
            childNodes: extractNode([...ul.children].slice(1), depth + 1)
        })
    })

    return nodeList;
}
