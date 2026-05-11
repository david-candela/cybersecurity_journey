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

document.addEventListener('DOMContentLoaded', function () {
  if (!('IntersectionObserver' in window)) return;
  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.setAttribute('data-visible', '');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );
  document.querySelectorAll('[data-animate]').forEach(function (el) {
    observer.observe(el);
  });
});
