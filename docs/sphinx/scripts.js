Array.from(document.querySelectorAll("img"))
  .filter((img) => img.hasAttribute("height"))
  .forEach((img) => {
    img.style.height = img.getAttribute("height").concat("px");
  });

Array.from(document.querySelectorAll(".toctree-checkbox")).forEach(
  (section) => {
    if (!section.checked) {
      section.click();
    }
  },
);
