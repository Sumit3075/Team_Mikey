const questions = document.querySelectorAll('.question');
const prevBtn = document.querySelector('#prev-btn');
const nextBtn = document.querySelector('#next-btn');
const submitBtn = document.querySelector('#submit-btn');
let currentQuestion = 0;

showQuestion(currentQuestion);

function showQuestion(index) {
  questions[currentQuestion].classList.add('hidden');
  questions[index].classList.remove('hidden');
  currentQuestion = index;
  if (currentQuestion === 0) {
    prevBtn.disabled = true;
  } else {
    prevBtn.disabled = false;
  }
  if (currentQuestion === questions.length - 1) {
    nextBtn.classList.add('hidden');
    submitBtn.classList.remove('hidden');
  } else {
    nextBtn.classList.remove('hidden');
    submitBtn.classList.add('hidden');
  }
}

prevBtn.addEventListener('click', () => {
  showQuestion(currentQuestion - 1);
});

nextBtn.addEventListener('click', () => {
  showQuestion(currentQuestion + 1);
});

submitBtn.addEventListener('click', () => {
  const form = document.querySelector('#mcq-form');
  const formData = new FormData(form);
  const answers = {};
  for (let [key, value] of formData.entries()) {
    answers[key] = value;
  }
  console.log(answers);
});


