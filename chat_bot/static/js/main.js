function show_hide(lshow, lhide) {
    lshow.forEach(e => {
        $(e).show()
    });
    lhide.forEach(e => {
        $(e).hide()
    });
}