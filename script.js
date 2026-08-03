const links = document.querySelectorAll('.top-nav a');
const sections = Array.from(document.querySelectorAll('main section'));
const highlightActiveLink = () => {
  let currentSection = '';
  sections.forEach((section) => {
    const sectionTop = section.offsetTop - 120;
    if (window.scrollY >= sectionTop) currentSection = section.id;
  });
  links.forEach((link) => link.classList.toggle('active', link.getAttribute('href') === `#${currentSection}`));
};
window.addEventListener('scroll', highlightActiveLink);
window.addEventListener('load', highlightActiveLink);
