// The file fills in the verse data obtained from a database

// Define fetch call parameters
// Initial origin "http://0.0.0.0:8000/display/"
let url = window.origin + "/display/";
let options = {
    method: "POST",
    cache: "no-cache",
    headers: {
        "content-type": "application/json"
    },
};

const section = document.querySelector("div.card");
const card_group = document.querySelector("section.card-group");

// Fetches the verses data from the flask server
fetch(url, options)
    .then(response => {
        return response.json();
    })
    .then(verse_list => {
        let theme_names = get_themes(verse_list);
        let cards = theme_names.map(theme => {
            let data = {
                theme: theme,
                verses: get_verses(theme, verse_list),
            };
            return data;
        });
        // Adds all cards to the DOM
        cards.forEach(card => {
            add_card(card_group, card);
        });
    })
    .catch(error => {
        console.log(error);
    });

// Adds the specified card to the list of cards
function add_card(card_group, card) {
    let section = document.createElement("section");
    section.setAttribute("class", "card border-0 m-1");
    let header = document.createElement("h4");
    header.setAttribute("class", "card-header bg-secondary text-light");
    header.innerText = card.theme;
    section.appendChild(header);
    let ul = document.createElement("ul");
    ul.setAttribute("class", "list-group py-2");
    section.appendChild(ul);

    card.verses.forEach(verse => {
        let li = document.createElement("li");
        li.setAttribute("class", "list-group-item scripture-styles");
        ul.appendChild(li);

        let api_bible_content = document.createElement("div");
        api_bible_content.setAttribute("class", "api-bible-content px-3 py-2");
        li.appendChild(api_bible_content);
        api_bible_content.innerHTML = verse.content;

        let ref_div = document.createElement("div");
        ref_div.setAttribute("class", "d-flex justify-content-end");
        let p = document.createElement("p");
        p.innerText = verse.reference;
        ref_div.appendChild(p);
        li.appendChild(ref_div);

    });
    card_group.appendChild(section);
}


// Returns an array of themes
function get_themes(verse_list) {
    let themes = [];
    verse_list.forEach(verse => {
        if (themes.includes(verse.theme) === false) {
            themes.push(verse.theme);
        }
    });
    return themes;
};

// Returns an array of verses
function get_verses(theme, verse_list) {
    let verses = [];
    verse_list.forEach((verse) => {
        if (verse.theme === theme) {
            verses.push({ content: verse.verse, reference: verse.reference });
        }
    });
    return verses;
};