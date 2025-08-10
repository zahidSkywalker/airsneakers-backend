// Paste this into your Air Sneaker HTML before </body>
// Replace API_BASE with your Render backend API root (no trailing slash)
const API_BASE = "https://your-backend.onrender.com/api";

async function loadProductsInto(selector='#product-grid') {
  const res = await fetch(`${API_BASE}/products/`);
  const products = await res.json();
  const grid = document.querySelector(selector);
  if (!grid) return;
  grid.innerHTML = '';
  products.forEach(p => {
    const html = `
      <article class="glass rounded-xl p-4 w-64 flex flex-col justify-between hover:shadow-yellow-400/50 hover:shadow-lg transition-shadow">
        <div class="product-img-container mb-4">
          <img src="${p.image_primary}" class="primary rounded-xl" />
          ${p.image_secondary ? `<img src="${p.image_secondary}" class="secondary rounded-xl" />` : ''}
        </div>
        <h3 class="text-white font-semibold text-lg mb-1">${p.name}</h3>
        <p class="text-yellow-400 font-bold text-xl mb-2">৳${p.price}</p>
        <button class="order-btn bg-yellow-400 text-black text-center py-2 rounded-lg font-semibold hover:bg-yellow-500 transition" data-id="${p.id}">Order Now</button>
      </article>
    `;
    grid.insertAdjacentHTML('beforeend', html);
  });
  document.querySelectorAll('.order-btn').forEach(b=>{
    b.addEventListener('click', ()=> startCheckout(b.dataset.id));
  });
}

async function startCheckout(productId) {
  const name = prompt("Enter your name:");
  const email = prompt("Enter your email:");
  const phone = prompt("Enter your phone:");
  const address = prompt("Enter your address:");
  if(!name || !email || !phone || !address) {
    alert('All fields are required.');
    return;
  }
  const orderData = {
    customer_name: name,
    email: email,
    phone: phone,
    address: address,
    items: [{product_id: parseInt(productId), qty: 1}],
    total_amount: 0
  };
  const res = await fetch(`${API_BASE}/checkout/`, {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify(orderData)
  });
  const data = await res.json();
  if(data.payment && data.payment.GatewayPageURL) {
    window.location.href = data.payment.GatewayPageURL;
  } else {
    console.log('Checkout response:', data);
    alert('Could not initiate payment. Check console for details.');
  }
}

// auto-load when script loaded if #product-grid exists
document.addEventListener('DOMContentLoaded', ()=> loadProductsInto());
