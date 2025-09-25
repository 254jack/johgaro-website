document.addEventListener("DOMContentLoaded", () => {
  const logo = document.getElementById("logo");
  const triggerPoint = 170;

  window.addEventListener("scroll", () => {
    if (window.scrollY >= triggerPoint) {
      logo.classList.add("logo-scrolled");
    } else {
      logo.classList.remove("logo-scrolled");
    }
  });
});
