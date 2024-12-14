fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then((response) => {
        if (!response.ok) {
            throw new Error(response.status);
        }
        return response.json();
    }).then((data) => {
        // console.log(data);
        const titles = data.results.map(movie => movie.title);
        const list = document.getElementById("list_movies");

        for ( const title of titles) {
            item = document.createElement("li");
            item.textContent = title;
            list.appendChild(item);
        }
        
}).catch((error) => console.error(`Fetch problema: ${error.message}`));