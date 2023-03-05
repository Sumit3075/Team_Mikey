async function basiclogin (email, password) {
  const response = await zlFetch.post(loginEndpoint, {
    auth: {
      username: email,
      password: password
    },
    
  })
}

// Text to type
var text = "";

// Set up the typing effect
var i = 0;
var speed = 50; // Time between typing each character in milliseconds
var typingEffect = setInterval(function() {
if (i < text.length) {
  document.querySelector(".typing-text").innerHTML += text.charAt(i);
  i++;
} else {
  clearInterval(typingEffect);
}
}, speed);


var autoType = document.getElementById('auto-type');
var textArray = ['We are on Mars!!!', 'Want to eat something??', 'Then, What are waiting for..... ORDER NOW'];
var index = 0;

function type() {
var text = textArray[index];
autoType.innerHTML = text.substring(0, autoType.innerHTML.length + 1);
if (autoType.innerHTML === text) {
  setTimeout(function() {
    erase();
  }, 2000);
} else {
  setTimeout(type, 100);
}
}

function erase() {
autoType.innerHTML = autoType.innerHTML.substring(0, autoType.innerHTML.length - 1);
if (autoType.innerHTML === '') {
  index++;
  if (index >= textArray.length) {
    index = 0;
  }
  setTimeout(type, 1000);
} else {
  setTimeout(erase, 50);
  }
}

type();