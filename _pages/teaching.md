---
layout: homepage
title: Aulas
permalink: /teaching/
author_profile: false
---

<style>
/* Design System - Azul */
:root {
  --primary: #0066cc;
  --primary-dark: #004499;
  --primary-light: #0088ee;
  --background: #FFFFFF;
  --foreground: #000000;
  --text-secondary: #666666;
  --border: #e0e0e0;
  --card-bg: #f5f5f5;
  --font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}

.teaching-wrapper {
  font-family: var(--font-body);
  background: var(--background);
  color: var(--foreground);
  line-height: 1.6;
  margin: -2rem;
}

.teaching-wrapper h1, .teaching-wrapper h2, .teaching-wrapper h3 {
  font-family: var(--font-body);
  font-weight: 700;
  line-height: 1.2;
  color: var(--foreground);
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }
.max-w-6xl { max-width: 72rem; margin: 0 auto; }

/* Hero Section */
.hero-teaching {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  padding: 4rem 0;
  text-align: center;
  border-bottom: 1px solid var(--border);
}

.hero-teaching h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--foreground);
}

.hero-teaching p {
  font-size: 1.125rem;
  color: var(--text-secondary);
  max-width: 600px;
  margin: 0 auto;
}

/* Section Styles */
.section { padding: 4rem 0; }

.section-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.section-line { height: 3px; width: 3rem; background: var(--primary); border-radius: 2px; }

.section-label {
  color: var(--primary);
  font-size: 0.875rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  font-weight: 600;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: var(--foreground);
}

.section-desc {
  color: var(--text-secondary);
  font-size: 1rem;
  line-height: 1.7;
  margin-bottom: 2rem;
  max-width: 800px;
}

/* Methodology Grid */
.methodology-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-top: 2rem;
}

.methodology-card {
  background: #ffffff;
  border-radius: 1rem;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  text-align: center;
  transition: all 0.3s ease;
}

.methodology-card:hover {
  box-shadow: 0 8px 24px rgba(0, 102, 204, 0.1);
}

.methodology-card .icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.methodology-card h3 {
  color: var(--foreground);
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.methodology-card p {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin: 0;
}

/* Course Image */
.course-image {
  text-align: center;
  margin: 2rem 0;
}

.course-image img {
  max-width: 100%;
  border-radius: 1rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.course-image p {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin-top: 1rem;
  font-style: italic;
}

/* Semester Grid */
.semester-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.semester-card {
  background: #ffffff;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
}

.semester-card:hover {
  box-shadow: 0 4px 12px rgba(0, 102, 204, 0.1);
}

.semester-card.current {
  border: 2px solid var(--primary);
}

.semester-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.semester-header h3 {
  margin: 0;
  font-size: 1.25rem;
}

.semester-badge {
  background: var(--primary);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.course-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.course-item {
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--border);
}

.course-item:last-child {
  border-bottom: none;
}

.course-item a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 500;
}

.course-item a:hover {
  text-decoration: underline;
}

/* Other Courses */
.other-courses {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 1.5rem;
}

.other-course-card {
  background: var(--card-bg);
  border-radius: 0.75rem;
  padding: 1rem;
  text-align: center;
}

.other-course-card a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 500;
}

/* Responsive - Mobile First */
@media (max-width: 480px) {
  .teaching-wrapper { margin: -1rem; }
  .container { padding: 0 1rem; }
  .hero-teaching { padding: 2rem 0; }
  .hero-teaching h1 { font-size: 1.5rem; }
  .hero-teaching p { font-size: 1rem; }
  .section { padding: 2rem 0; }
  .section-title { font-size: 1.5rem; }
  .section-desc { font-size: 0.9rem; }
  .methodology-grid { grid-template-columns: 1fr; gap: 1rem; }
  .methodology-card { padding: 1.25rem; }
  .methodology-card .icon { font-size: 2rem; }
  .methodology-card h3 { font-size: 1.1rem; }
  .semester-grid { grid-template-columns: 1fr; gap: 1rem; }
  .semester-card { padding: 1rem; }
  .semester-header h3 { font-size: 1.1rem; }
  .other-courses { grid-template-columns: 1fr; gap: 0.75rem; }
}

@media (min-width: 481px) and (max-width: 768px) {
  .teaching-wrapper { margin: -1.5rem; }
  .hero-teaching h1 { font-size: 1.75rem; }
  .section { padding: 2.5rem 0; }
  .section-title { font-size: 1.75rem; }
  .methodology-grid { grid-template-columns: repeat(2, 1fr); }
  .semester-grid { grid-template-columns: 1fr; }
  .other-courses { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .hero-teaching h1 { font-size: 2rem; }
  .section { padding: 3rem 0; }
  .methodology-grid { grid-template-columns: repeat(2, 1fr); }
  .semester-grid { grid-template-columns: 1fr; }
  .other-courses { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
  .hero-teaching h1 { font-size: 2rem; }
  .methodology-grid { grid-template-columns: 1fr; }
  .other-courses { grid-template-columns: 1fr; }
  .section { padding: 3rem 0; }
}
</style>

<div class="teaching-wrapper">

<section class="hero-teaching">
  <div class="container">
    <h1>Metodologia de Ensino</h1>
    <p>Aprendizagem experiencial através de projetos reais</p>
  </div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Filosofia</span></div>
    <p class="section-desc">Eu adoto <strong>Modelos de Aprendizagem Experiencial</strong> com cursos orientados a projetos e Living Labs no laboratório de pesquisa. Neste modelo, os alunos passam por uma 'jornada de descoberta', onde compreendem as lições e conceitos por meio do processo experiencial de chegar lá.</p>
    <p class="section-desc">Os estudantes desenvolvem projetos de software com clientes reais ou conjuntos de dados reais. Todos os artefatos produzidos durante os cursos são de código aberto, e os alunos têm acesso ao material e código de semestres anteriores.</p>
    
    <div class="methodology-grid">
      <div class="methodology-card">
        <h3>Projetos Reais</h3>
        <p>Desenvolvimento com clientes reais e dados abertos</p>
      </div>
      <div class="methodology-card">
        <h3>Código Aberto</h3>
        <p>Todos os artefatos são open source e acessíveis para futuras turmas</p>
      </div>
      <div class="methodology-card">
        <h3>Comunidades</h3>
        <p>Contribuição para projetos como Debian, Kubernetes e Rocket.Chat</p>
      </div>
    </div>

    <div class="course-image">
      <img src="/images/gpp_mds.png" alt="Estudantes em aula prática" />
      <p>Estudantes desenvolvendo projetos em metodologia ágil</p>
    </div>
  </div></div>
</section>

<section class="section" style="background: #f8f9fa;">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Disciplinas</span></div>
    
    <div class="semester-grid">
      <div class="semester-card current">
        <div class="semester-header">
          <h3>2025.2</h3>
          <span class="semester-badge">Atual</span>
        </div>
        <ul class="course-list">
          <li class="course-item"><a href="/teaching/mds">Métodos de Desenvolvimento de Software (MDS)</a></li>
          <li class="course-item"><a href="https://github.com/fga-gces" target="_blank">Gerência de Configuração e Evolução de Software (GCES)</a></li>
          <li class="course-item"><a href="https://unb-sistemas-de-machine-learning.github.io/Disciplina/" target="_blank">Sistemas de Machine Learning</a></li>
        </ul>
      </div>
      <div class="semester-card">
        <div class="semester-header"><h3>2025.1</h3></div>
        <ul class="course-list">
          <li class="course-item"><a href="/teaching/mds">Métodos de Desenvolvimento de Software (MDS)</a></li>
          <li class="course-item"><a href="https://github.com/fga-gces" target="_blank">Gerência de Configuração e Evolução de Software (GCES)</a></li>
        </ul>
      </div>
      <div class="semester-card">
        <div class="semester-header"><h3>2024.1</h3></div>
        <ul class="course-list">
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2024.1-MDS-DOCS/" target="_blank">Métodos de Desenvolvimento de Software</a></li>
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2024.1-EPS-DOCS/" target="_blank">Engenharia de Produto de Software</a></li>
        </ul>
      </div>
      <div class="semester-card">
        <div class="semester-header"><h3>2023.2</h3></div>
        <ul class="course-list">
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2023.2-MDS-DOCS/" target="_blank">Métodos de Desenvolvimento de Software</a></li>
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2023.2-EPS-DOCS/" target="_blank">Engenharia de Produto de Software</a></li>
        </ul>
      </div>
      <div class="semester-card">
        <div class="semester-header"><h3>2023.1</h3></div>
        <ul class="course-list">
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2023.1-MDS-DOCS/" target="_blank">Métodos de Desenvolvimento de Software</a></li>
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2023.1-EPS-DOCS/" target="_blank">Engenharia de Produto de Software</a></li>
        </ul>
      </div>
      <div class="semester-card">
        <div class="semester-header"><h3>2022.2</h3></div>
        <ul class="course-list">
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2022.2-MDS-DOCS/" target="_blank">Métodos de Desenvolvimento de Software</a></li>
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2022.2-EPS-DOCS/" target="_blank">Engenharia de Produto de Software</a></li>
        </ul>
      </div>
      <div class="semester-card">
        <div class="semester-header"><h3>2022.1</h3></div>
        <ul class="course-list">
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2022.1-MDS-DOCS/" target="_blank">Métodos de Desenvolvimento de Software</a></li>
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2022.1-EPS-DOCS/" target="_blank">Engenharia de Produto de Software</a></li>
        </ul>
      </div>
      <div class="semester-card">
        <div class="semester-header"><h3>2021.1 - 2021.2</h3></div>
        <ul class="course-list">
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2021.2-MDS-DOCS/" target="_blank">Métodos de Desenvolvimento de Software</a></li>
          <li class="course-item"><a href="https://fga-eps-mds.github.io/2021.2-EPS-DOCS/" target="_blank">Engenharia de Produto de Software</a></li>
        </ul>
      </div>
    </div>
  </div></div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Repositórios</span></div>
    
    <div class="other-courses">
      <div class="other-course-card">
        <a href="/teaching/mds">📚 MDS - Métodos de Desenvolvimento</a>
      </div>
      <div class="other-course-card">
        <a href="https://github.com/fga-gces" target="_blank">⚙️ GCES - Gerência de Configuração</a>
      </div>
      <div class="other-course-card">
        <a href="https://github.com/PPCA-CS" target="_blank">🎓 Software Development - Masters</a>
      </div>
      <div class="other-course-card">
        <a href="https://github.com/unb-Sistemas-de-Machine-learning" target="_blank">🤖 Sistemas de Machine Learning</a>
      </div>
    </div>

    <p style="color: var(--text-secondary); margin-top: 2rem;"><strong>Outras disciplinas ministradas:</strong> Computação Gráfica, Engenharia de Produto, Introdução à Engenharia de Software</p>
  </div></div>
</section>

</div>


