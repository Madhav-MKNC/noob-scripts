let stopScrolling = false;

function infiniteScroll() {
    if (stopScrolling) return;

    window.scrollBy(0, window.innerHeight); // Scrolls down by one viewport height

    setTimeout(infiniteScroll, 100); // Calls the function again after 100 milliseconds
}

// Start the infinite scroll
infiniteScroll();

// Set a timeout to stop scrolling after 5 minutes (300,000 milliseconds)
setTimeout(() => {
    stopScrolling = true;
    console.log('Stopped scrolling after 5 minutes');
}, 300000);
