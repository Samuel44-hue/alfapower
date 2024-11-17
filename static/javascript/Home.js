function filterProducts(category) {
    let products = document.getElementsByClassName('product');

    for (let i = 0; i < products.length; i++) {
        products[i].style.display = 'none';
        if (category === 'all' || products[i].classList.contains(category)) {
            products[i].style.display = 'block';
        }
    }
}

window.onload = function () {
    filterProducts('all');
};
// --------------------------------------------------------------------
function animateCountUp(counter) {
    const updateCount = () => {
        const target = +counter.getAttribute('data-target');
        const current = +counter.innerText.replace('+', '');
        const increment = target / 100;

        if (current < target) {
            counter.innerText = `${Math.ceil(current + increment)}+`;
            setTimeout(updateCount, 50);
        } else {
            counter.innerText = `${target}+`;
        }
    };

    updateCount();
}

function createObserver() {
    const counters = document.querySelectorAll('.num');

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                animateCountUp(counter);
                observer.unobserve(counter);
            }
        });
    }, {
        threshold: 0.5
    });
    counters.forEach(counter => {
        observer.observe(counter);
    });
}

document.addEventListener('DOMContentLoaded', createObserver);


