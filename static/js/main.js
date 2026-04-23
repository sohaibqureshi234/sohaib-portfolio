// Cursor blob
const blob = document.getElementById('cursorBlob');
document.addEventListener('mousemove', e => {
  blob.style.transform = `translate(${e.clientX}px, ${e.clientY}px) translate(-50%, -50%)`;
});

// Navbar scroll effect
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 60);
});

// Mobile menu
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');
hamburger.addEventListener('click', () => {
  mobileMenu.classList.toggle('open');
});
document.querySelectorAll('.mobile-link').forEach(link => {
  link.addEventListener('click', () => mobileMenu.classList.remove('open'));
});

// Scroll reveal
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// Stagger reveal for grid children
const staggerObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const children = entry.target.querySelectorAll('.skill-group, .project-card, .timeline-item');
      children.forEach((child, i) => {
        setTimeout(() => child.classList.add('visible'), i * 80);
      });
      staggerObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.05 });

document.querySelectorAll('.skills-grid, .projects-grid, .timeline').forEach(el => {
  el.querySelectorAll('.skill-group, .project-card, .timeline-item').forEach(child => {
    child.classList.add('reveal');
  });
  staggerObserver.observe(el);
});
