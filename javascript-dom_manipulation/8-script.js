fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then((response) => {
        if (!response.ok) {
            throw new Error(response.status);
        }
        return response.json();
    }).then((data) => {
        // console.log(data);
        const tag = document.getElementById("hello");
        tag.textContent = data.hello;
}).catch((error) => console.error(`Fetch problema: ${error.message}`));