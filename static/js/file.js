const walletLink = document.querySelector('.wallet-link');
const walletBox = document.querySelector('.wallet-box');
//const addMoneyBtn = document.querySelector('.add-money-btn');

// Show the wallet box when the wallet link is clicked
walletLink.addEventListener('click', (event) => {
  event.preventDefault();
  walletBox.style.display = 'block';
});

const addMoneyBtn = document.querySelector('.btn.btn-primary.add-money-btn');

// Add money when the add money button is clicked
// addMoneyBtn.addEventListener('click', (event) => {
//   event.preventDefault();
//   const amount = document.querySelector('#amount').value;
//   console.log("shubham ------",amount)
//   // Do something with the amount value, such as sending it to the server
//   walletBox.style.display = 'none';
// });

addMoneyBtn.addEventListener('click', (event) => {
  event.preventDefault();
  const amount = document.querySelector('#amount').value;
  console.log("shubham ------",amount);

  // Make an API call to send the amount to the server
  fetch('http://localhost:5000/add_funds', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ form: { amount } })
  })
  .then(response => {
    if (response.ok) {
      // Handle successful response
      console.log('Money added successfully');
      walletBox.style.display = 'none';
    } else {
      // Handle error response
      console.error('Error adding money');
    }
  })
  .catch(error => {
    console.error('Error adding money:', error);
  });
});

// Hide the wallet box when clicked outside of it
document.addEventListener('click', (event) => {
  if (!walletLink.contains(event.target) && !walletBox.contains(event.target)) {
    walletBox.style.display = 'none';
  }
});
