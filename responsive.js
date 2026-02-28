document.addEventListener("DOMContentLoaded", function () {
  const btn = document.getElementById("mobile-menu-btn");
  const links = document.querySelector(".nav-links");

  if (!btn || !links) {
    console.log("Navbar elements not found");
    return;
  }

  btn.addEventListener("click", function (e) {
    e.stopPropagation();
    links.classList.toggle("mobile-active");
  });

  // Close menu when clicking outside
  document.addEventListener("click", function (e) {
    if (!btn.contains(e.target) && !links.contains(e.target)) {
      links.classList.remove("mobile-active");
    }
  });
});
