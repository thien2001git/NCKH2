function show_hide(lshow, lhide) {
    lshow.forEach(e => {
        $(e).show()
    });
    lhide.forEach(e => {
        $(e).hide()
    });
}

if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}