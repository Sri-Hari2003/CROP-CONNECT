import { initializeApp } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";
  import { getDatabase,ref,set,get,child } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-database.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyAx_FCwv2EZOTrqyc7QLP8sKK5Z4TboNbU",
    authDomain: "agricult-x.firebaseapp.com",
    databaseURL: "https://agricult-x-default-rtdb.firebaseio.com",
    projectId: "agricult-x",
    storageBucket: "agricult-x.appspot.com",
    messagingSenderId: "219714777253",
    appId: "1:219714777253:web:ba14c8481ea57389fddd4c"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const db = getDatabase(app);

document.getElementById("submit").addEventListener('click', function(e){
e.preventDefault();
set(ref(db, 'user/' + document.getElementById("email").value.split("@")[0]),
{
email: document.getElementById("email").value,
password: document.getElementById("password").value

});
alert("Login Sucessfull  !");
})


document.getElementById("submit1").addEventListener('click', function(e){
  e.preventDefault();
  set(ref(db, 'new user/' + document.getElementById("email1").value.split("@")[0]),
  {
  name: document.getElementById("name").value,
  email: document.getElementById("email1").value,
  password: document.getElementById("password1").value
  
  });
  alert("Login Sucessfull  !");
  })