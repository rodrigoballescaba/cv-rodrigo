// Reproduce la conversación del teléfono una vez al entrar en pantalla.
(function () {
  var chat = document.querySelector(".chat");
  if (!chat) return;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var steps = Array.prototype.slice.call(chat.querySelectorAll(".msg:not(.typing)"));
  var typing = chat.querySelector(".typing");
  var timers = [];

  function reset() {
    timers.forEach(clearTimeout);
    timers = [];
    steps.forEach(function (el) { el.classList.remove("in"); });
    typing.classList.remove("show");
  }

  function play() {
    reset();
    var t = 400;
    steps.forEach(function (el) {
      var isBot = el.classList.contains("bot");
      if (isBot) {
        timers.push(setTimeout(function () {
          chat.insertBefore(typing, el);
          typing.classList.add("show");
        }, t));
        t += 1100;
      }
      timers.push(setTimeout(function () {
        typing.classList.remove("show");
        el.classList.add("in");
      }, t));
      t += el.classList.contains("tool") ? 700 : 1000;
    });
  }

  if (reduce) {
    steps.forEach(function (el) { el.classList.add("in"); });
    return;
  }

  var replay = document.querySelector(".replay");
  if (replay) replay.addEventListener("click", play);

  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) { play(); io.disconnect(); }
    }, { threshold: 0.4 });
    io.observe(chat);
  } else {
    play();
  }
})();
