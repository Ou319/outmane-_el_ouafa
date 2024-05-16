let slider = document.querySelector(".slider");
let list = document.querySelector(".list");
let prev = document.querySelector(".prev");
let back = document.querySelector(".pack");

prev.onclick = function() {
    showiimg('next');
}
back.onclick = function() {
    showiimg('back');
}

function showiimg(type) {
    let items = list.querySelectorAll(".item");
    let item, img;

    if (type === 'next') {
        item = items[0];
        list.appendChild(item); // Move first item to the end
    } else if (type === 'back') {
        item = items[items.length - 1];
        list.insertBefore(item, list.firstChild); // Move last item to the beginning
    }

    // Remove the 'active' class from all images
    items.forEach(it => {
        let image = it.querySelector("img");
        if (image) {
            image.classList.remove("active");
        }
    });

    // Force a reflow to restart the transition
    void item.offsetWidth;

    // Adding the active class to the current image
    img = item.querySelector("img");
    if (img) {
        img.classList.add("active");
    }
}
