document.addEventListener('DOMContentLoaded', function() {
  const themeToggle = document.getElementById('themeToggle');
  const body = document.body;
  
  // Verifica o tema salvo no localStorage
  const savedTheme = localStorage.getItem('theme') || 'dark';
  if (savedTheme === 'light') {
    body.classList.add('theme-light');
  }

  // Atualiza o ícone do botão
  function updateIcon() {
    const isLight = body.classList.contains('theme-light');
    themeToggle.innerHTML = isLight ? '<i class="fas fa-moon"></i>' : '<i class="fas fa-sun"></i>';
  }

  // Alterna entre temas
  themeToggle.addEventListener('click', function() {
    body.classList.toggle('theme-light');
    const isLight = body.classList.contains('theme-light');
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
    updateIcon();
  });

  // Inicializa o ícone
  updateIcon();
});
