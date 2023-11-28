document.addEventListener('DOMContentLoaded', function () {
    const cartButton = document.getElementById('cart-button');
    const cartContent = document.getElementById('cart-content');
  
    cartButton.addEventListener('click', function () {
      if (cartContent.style.display === 'block') {
        cartContent.style.display = 'none';
      } else {
        cartContent.style.display = 'block';
      }
    });
  
    // Cierra el carrito si se hace clic fuera de él
    document.addEventListener('click', function (event) {
      if (!cartButton.contains(event.target) && !cartContent.contains(event.target)) {
        cartContent.style.display = 'none';
      }
    });
  });
  