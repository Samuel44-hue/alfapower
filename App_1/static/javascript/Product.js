document.addEventListener("DOMContentLoaded", () => {
    // Hide all products initially
    filterProducts('');
});

function filterProducts(category) {
    const products = document.querySelectorAll('.product');
    const solarInverterSubsections = document.getElementById('solarInverterSubsections');

    if (category === 'si') {
        solarInverterSubsections.style.display = 'block';
    } else {
        solarInverterSubsections.style.display = 'none';
    }

    products.forEach(product => {
        if (category && (category === 'all' || product.classList.contains(category))) {
            product.closest('a').style.display = 'block';
        } else {
            product.closest('a').style.display = 'none';
        }
    });
}
