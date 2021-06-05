// 'use strict'

// Using jQuery to check if the html doc is in a ready state i.e. DOM loaded
// $document.ready(function () {
//     $.
// })


let artist_images = $("img")
let imgs_num = artist_images.length

// artist_img.hover(function () {
//     artist_img.eq(1).attr("src", "images/nicki_minaj.jpg")
//     artist_img.setAttribute("class", "img-thumbnail")
// })


function change_pic() {
    let random_num = Math.floor(Math.random() * imgs_num)
    console.log(artist_images.eq(Number(random_num)))
    // artist_images.eq(0).attr("src", artist_images.eq(Number(random_num)))
    // artist_images.attr("class", "img-thumbnail")
}
change_pic()
// setInterval(200, change_pic)