// File: process.js
// The file contains code to manipulate DOM with information obtained from the flask server

// Original origin http://0.0.0.0:8000
let origin = window.origin;
let button = document.getElementById("button");
let process_url = origin + "/process/";
let addverse_url = origin + "/addverse/";


// Gives the flask server instructions on which information to fetch and supply
let bible_request = { bibleInfo: "books"};

// Prepares data to send a first POST request to the flask server
let book_select = document.getElementById("book-select");
let fetching_message = document.querySelector("select#book-select > option");
fetching_message.innerText = "Fetching books ...";
fetching_message.style.color = "green";
let options = {
    method: "POST",
    cache: "no-cache",
    headers: {
        "content-type": "application/json"
    },
    body: JSON.stringify(bible_request)
};


// Fetches books from the flask server
fetch(process_url, options)
.then(response => {
    return response.json();
})
.then(bible_data => {
    bible_request.version = bible_data.version;
    let books = bible_data.books;
    let option;
    book_select.removeChild(fetching_message);
    books.forEach(book => {
        option = document.createElement("option");
        option.setAttribute("value", book.id);
        option.innerText = book.name;
        book_select.append(option);
    });
    book_select.size = 3;
    book_select.removeAttribute("disabled");
})
.catch(error => {
    console.log(error);
});


// Fetches book chapters and allows selection of a chapter
let chapter_select = document.getElementById("chapter-select");
book_select.onchange = function () {

    book_select.setAttribute("disabled", "");
    bible_request.bibleInfo = "chapters";
    bible_request.selected_book = book_select.value;

    options = {
        method: "POST",
        cache: "no-cache",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify(bible_request)
    };

    fetching_message = document.querySelector("select#chapter-select > option");
    fetching_message.innerText = "Fetching chapters ...";
    fetching_message.style.color = "green";
    
    // Fetches chapters from the flask server
    fetch(process_url, options)
    .then(response => {
        return response.json();
    })
    .then(bible_data => {
        let chapters = bible_data.chapters;
        let option;
        chapter_select.removeChild(fetching_message);
        chapters.forEach(chapter => {
            option = document.createElement("option");
            option.setAttribute("value", chapter.id);
            option.innerText = chapter.number;
            chapter_select.append(option);
        });
        chapter_select.size = 3;
        chapter_select.removeAttribute("disabled");
    })
    .catch(error => {
        console.log(error);
    });
}



// Fetches book verses and allows selection of a verse
let verse_select = document.getElementById("verse-select");
chapter_select.onchange = function () {

    chapter_select.setAttribute("disabled", "");
    bible_request.bibleInfo = "verses";
    bible_request.selected_chapter = chapter_select.value;

    options = {
        method: "POST",
        cache: "no-cache",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify(bible_request)
    };

    fetching_message = document.querySelector("select#verse-select > option");
    fetching_message.innerText = "Fetching verses ...";
    fetching_message.style.color = "green";
    
    // Fetches verses from the flask server
    fetch(process_url, options)
    .then(response => {
        return response.json();
    })
    .then(bible_data => {
        let verses = bible_data.verses;
        let option;
        verse_select.removeChild(fetching_message);
        verses.forEach(verse => {
            option = document.createElement("option");
            option.setAttribute("value", verse.id);
            option.innerText = verse.number;
            verse_select.append(option);
        });
        verse_select.size = 3;
        verse_select.removeAttribute("disabled");
    })
    .catch(error => {
        console.log(error);
    });
}


// Fetches a verse value and allows viewing and submission of the verse
let par_verse = document.getElementById("bible-verse");
let theme_box = document.getElementById("theme-box");
verse_select.onchange = function () {
    let bible_verse_group = document.getElementById("bible-verse-group");
    bible_verse_group.setAttribute("style", "display: inherit;");
    verse_select.setAttribute("disabled", "");
    bible_request.bibleInfo = "verse";
    bible_request.selected_verse = verse_select.value;

    options = {
        method: "POST",
        cache: "no-cache",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify(bible_request)
    };

    fetching_message = par_verse;
    fetching_message.innerText = "Fetching the verse ...";
    fetching_message.style.color = "green";
    
    // Fetches a verse from the flask server
    fetch(process_url, options)
    .then(response => {
        return response.json();
    })
    .then(bible_data => {
        bible_request.verse = bible_data.verse;
        bible_request.reference = bible_data.reference;
        bible_request.fums = bible_data.meta.fums;
        fetching_message.innerText = "";
        par_verse.style.color = "black";
        par_verse.innerHTML = bible_data.verse;
        button.removeAttribute("disabled");
        button.insertAdjacentHTML("afterend", bible_data.meta.fums);
        theme_box.removeAttribute("disabled");
    })
    .catch(error => {
        console.log(error);
    });
}

// When the submit button is clicked, post data to the route for upload
button.onclick = function () {
    bible_request.theme = theme_box.value;
    options = {
        method: "POST",
        cache: "no-cache",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify(bible_request)
    };
    // Fetches a route to redirect to from the flask server
    fetch(addverse_url, options)
    .then(response => {
        return response.json();
    })
    .then(data => {
        // Redirects a user to the home page
        window.location.replace(origin + data.redirect_url);
    })
    .catch(error => {
        console.log(error);
    });
}