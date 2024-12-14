fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    .then((response) => {
        if (!response.ok) {
            throw new Error(response.status);
        }
        return response.json();
    }).then((data) => {
        // console.log(data);
        const tag = document.getElementById("character");
        tag.textContent = data.name;
}).catch((error) => console.error(`Fetch problema: ${error.message}`));