document.addEventListener('DOMContentLoaded', function () {
  var title = document.querySelector('.md-header__title');
  if (!title) return;

  var link = document.createElement('a');
  link.href = 'https://david-candela.github.io/cybersecurity_journey/cv/';
  link.className = 'cv-header-link';
  link.textContent = 'My CV';
  link.setAttribute('target', '_blank');
  link.setAttribute('rel', 'noopener noreferrer');
  link.setAttribute('aria-label', 'My CV (opens in a new tab)');

  title.insertAdjacentElement('afterend', link);
});
