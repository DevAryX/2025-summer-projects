$(document).ready(function () {
  let currentInput = "";
  const display = $("#display");
  const historyList = $("#history-list");

  // Dark mode
  if (localStorage.getItem("darkMode") === "true") {
    $("body").addClass("dark");
  }

  // Load history
  const history = JSON.parse(localStorage.getItem("calcHistory") || "[]");
  history.forEach(entry => {
    historyList.append(`<li>${entry}</li>`);
  });

  function addToHistory(entry) {
    history.push(entry);
    if (history.length > 50) history.shift();
    localStorage.setItem("calcHistory", JSON.stringify(history));
    historyList.append(`<li>${entry}</li>`);
  }

  $(".btn").not(".clear, #equals, .toggle-mode, .clear-history, .toggle-sci").on("click", function () {
    const value = $(this).text();
    const lastChar = currentInput.slice(-1);

    if ("+-*/.".includes(value) && "+-*/.".includes(lastChar)) return;
    if (currentInput === "" && "+*/.".includes(value)) return;
    if (value === "." && /(\.\d*|\d*\.\d*)$/.test(currentInput.split(/[\+\-\*\/]/).pop())) return;

    currentInput += value;
    display.val(currentInput);
  });

  $("#equals").on("click", function () {
    try {
      const result = math.evaluate(currentInput);
      const expression = `${currentInput} = ${result}`;
      display.val(result);
      addToHistory(expression);
      currentInput = result.toString();
    } catch {
      display.val("Error");
      currentInput = "";
    }
  });

  $(".clear").on("click", function () {
    currentInput = "";
    display.val("");
  });

  $(".toggle-mode").on("click", function () {
    $("body").toggleClass("dark");
    localStorage.setItem("darkMode", $("body").hasClass("dark"));
  });

  $(".clear-history").on("click", function () {
    localStorage.removeItem("calcHistory");
    historyList.empty();
  });

  $(".toggle-sci").on("click", function () {
    $(".sci-mode").toggleClass("show");
  });

  $(document).on("keydown", function (e) {
    const key = e.key;

    if (!isNaN(key) || "+-*/().%".includes(key)) {
      const lastChar = currentInput.slice(-1);

      if ("+-*/.".includes(key) && "+-*/.".includes(lastChar)) return;
      if (currentInput === "" && "+*/.".includes(key)) return;
      if (key === "." && /(\.\d*|\d*\.\d*)$/.test(currentInput.split(/[\+\-\*\/]/).pop())) return;

      currentInput += key;
      display.val(currentInput);
    } else if (key === "Enter") {
      $("#equals").click();
    } else if (key === "Backspace") {
      currentInput = currentInput.slice(0, -1);
      display.val(currentInput);
    } else if (key === "Escape") {
      currentInput = "";
      display.val("");
    }
  });
});
