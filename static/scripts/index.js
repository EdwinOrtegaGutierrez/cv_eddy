const btn = document.querySelector('.btn');
btn.addEventListener('click', function() {
    const imgHeight = document.querySelector('.presentation img').offsetHeight;
    window.scrollTo({
        top: document.querySelector('.presentation img').offsetTop + imgHeight + 800,
        behavior: 'smooth'
    });
});