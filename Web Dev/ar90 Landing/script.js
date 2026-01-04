document.addEventListener("DOMContentLoaded", function () {
  // Dark Mode Toggle
  const toggleButton = document.getElementById("toggle-dark");
  toggleButton.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    toggleButton.textContent = document.body.classList.contains("dark") ? "☀️" : "🌙";
  });

  // Fade-in Animation on Scroll
  const fadeElements = document.querySelectorAll(".fade-in-up");
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("animate");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  fadeElements.forEach(el => observer.observe(el));

  // Highlight Active Nav Link
  const currentPage = window.location.pathname.split("/").pop();
  document.querySelectorAll("nav a").forEach(link => {
    if (link.getAttribute("href") === currentPage) {
      link.classList.add("active");
    }
  });

  // Form Handling
  const form = document.getElementById("signup-form");
  if (form) {
    const responseBox = document.getElementById("form-response");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const emailInput = form.querySelector("input[type='email']");
      const email = emailInput.value.trim();

      if (email === "") {
        responseBox.textContent = "Please enter a valid email.";
        responseBox.style.color = "#ff6f61";
        return;
      }

      responseBox.textContent = `Thanks! You’ll be notified at ${email}`;
      responseBox.style.color = "limegreen";
      form.reset();
    });
  }

  // Buy Now Modal Handler
  const buyNowLinks = document.querySelectorAll("a[href='#contact']");
  const modal = document.getElementById("purchase-modal");
  const closeBtn = document.getElementById("close-modal");

  buyNowLinks.forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      modal.style.display = "flex";
    });
  });

  if (closeBtn && modal) {
    closeBtn.addEventListener("click", () => {
      modal.style.display = "none";
    });

    window.addEventListener("click", (e) => {
      if (e.target === modal) {
        modal.style.display = "none";
      }
    });
  }
});

// Loader Handler
window.addEventListener("load", () => {
  const loader = document.getElementById("loader-wrapper");
  if (loader) loader.style.display = "none";
});
