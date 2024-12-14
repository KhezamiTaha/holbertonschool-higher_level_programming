document.getElementById("add_item").addEventListener("click", function () {
    const list = document.querySelector(".my_list");

    item = document.createElement("li");
    item.textContent = "Itemiii";

    list.appendChild(item);
})