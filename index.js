// 'use strict'

// Using jQuery to check if the html doc is in a ready state i.e. DOM loaded
$(document).ready(function () {
    let artist_images = $("img")

    artist_images.hover(function () {
        artist_images.eq(1).attr("src", "images/nicki_minaj.jpg")
        artist_images.eq(1).attr("class", "img-thumbnail")
    })


})



// setInterval(200, change_pic)