---
layout: single
title: false
author_profile: true
permalink: /
header:
  overlay_color: "#003366"
  overlay_filter: "0.3"
  overlay_image: /images/lab.png
  actions:
    - label: "Contato"
      url: "mailto:caguiar@unb.br"
      class: "btn btn--primary btn--large"
    - label: "Projetos"
      url: "/projects/"
      class: "btn btn--light-outline btn--large"
---

<style>
/* Clean Academic Design System */
:root {
  --primary-color: #333333;
  --secondary-color: #666666;
  --accent-color: #0066cc;
  --text-dark: #333333;
  --text-medium: #666666;
  --text-light: #999999;
  --bg-white: #ffffff;
  --bg-light: #fafafa;
  --border-light: #e0e0e0;
  --shadow-subtle: 0 1px 3px rgba(0,0,0,0.1);
  --shadow-medium: 0 2px 8px rgba(0,0,0,0.1);
}

/* Reset and Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: var(--text-dark);
  background: var(--bg-white);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* Hero Section - NetLab Style */
.hero-section {
  background: var(--bg-white);
  padding: 4rem 0;
  text-align: center;
  border-bottom: 1px solid var(--border-light);
}

.hero-title {
  font-size: 2rem;
  font-weight: 400;
  color: var(--primary-color);
  margin-bottom: 1.5rem;
  line-height: 1.3;
}

.hero-subtitle {
  font-size: 1.2rem;
  color: var(--text-medium);
  max-width: 800px;
  margin: 0 auto 2rem auto;
  line-height: 1.6;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 0.7rem 1.5rem;
  border: 1px solid var(--primary-color);
  background: var(--primary-color);
  color: white;
  text-decoration: none;
  border-radius: 3px;
  font-weight: 400;
  font-size: 0.9rem;
  transition: all 0.2s ease;
}

.btn-secondary {
  background: transparent;
  color: var(--primary-color);
}

.btn:hover {
  background: var(--secondary-color);
  border-color: var(--secondary-color);
}

.btn-secondary:hover {
  background: var(--primary-color);
  color: white;
}

/* Research Areas Section */
.research-section {
  padding: 4rem 0;
  background: var(--bg-light);
}

.section-title {
  font-size: 2rem;
  font-weight: 400;
  color: var(--primary-color);
  text-align: center;
  margin-bottom: 2.5rem;
}

.research-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.research-card {
  background: var(--bg-white);
  padding: 2rem;
  border: 1px solid var(--border-light);
  transition: all 0.2s ease;
}

.research-card:hover {
  border-color: var(--accent-color);
  box-shadow: var(--shadow-subtle);
}

.research-title {
  font-size: 1.2rem;
  font-weight: 500;
  color: var(--primary-color);
  margin-bottom: 1rem;
}

.research-description {
  color: var(--text-medium);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.research-link {
  color: var(--accent-color);
  text-decoration: none;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: color 0.2s ease;
}

.research-link:hover {
  color: var(--primary-color);
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }
  
  .section-title {
    font-size: 1.6rem;
  }
  
  .research-grid,
  .publications-grid,
  .books-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .hero-buttons {
    flex-direction: column;
    align-items: center;
  }
  
  .container {
    padding: 0 1rem;
  }
}

/* Publications Section - NetLab Style */
.publications-section {
  padding: 4rem 0;
  background: var(--bg-white);
}

.publications-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.publication-item {
  background: var(--bg-white);
  border: 1px solid var(--border-light);
  padding: 2rem;
  transition: all 0.2s ease;
  position: relative;
}

.publication-item:hover {
  border-color: var(--accent-color);
  box-shadow: var(--shadow-subtle);
}

.publication-item.featured {
  border-left: 3px solid var(--accent-color);
  background: var(--bg-white);
}

.publication-item.featured::before {
  content: 'Destaque';
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: var(--accent-color);
  color: white;
  padding: 0.2rem 0.6rem;
  border-radius: 3px;
  font-size: 0.7rem;
  font-weight: 500;
}

.pub-title {
  font-size: 1.1rem;
  font-weight: 500;
  color: var(--primary-color);
  margin-bottom: 0.8rem;
  line-height: 1.4;
}

.pub-authors {
  color: var(--text-medium);
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.pub-venue {
  color: var(--text-medium);
  font-style: italic;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.pub-meta {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.pub-year {
  background: var(--bg-light);
  color: var(--text-dark);
  padding: 0.2rem 0.6rem;
  border-radius: 3px;
  font-size: 0.8rem;
  font-weight: 400;
}

.pub-citations {
  background: var(--text-medium);
  color: white;
  padding: 0.2rem 0.6rem;
  border-radius: 3px;
  font-size: 0.8rem;
  font-weight: 500;
}

.pub-link {
  color: var(--accent-color);
  text-decoration: none;
  font-weight: 500;
  margin-top: 1rem;
  display: inline-block;
  transition: color 0.2s ease;
}

.pub-link:hover {
  color: var(--primary-color);
}

/* Books Section */
.books-section {
  padding: 4rem 0;
  background: var(--bg-light);
}

.books-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.book-item {
  background: var(--bg-white);
  border: 1px solid var(--border-light);
  padding: 2rem;
  transition: all 0.2s ease;
  position: relative;
  border-left: 3px solid var(--accent-color);
}

.book-item:hover {
  border-color: var(--primary-color);
  box-shadow: var(--shadow-subtle);
}

.book-title {
  font-size: 1.2rem;
  font-weight: 500;
  color: var(--primary-color);
  margin-bottom: 0.8rem;
  line-height: 1.4;
}

.book-authors {
  color: var(--text-medium);
  font-size: 0.9rem;
  margin-bottom: 1rem;
  font-style: italic;
}

.book-description {
  color: var(--text-medium);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.book-meta {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin-bottom: 1.5rem;
}

.book-year {
  background: var(--bg-light);
  color: var(--text-dark);
  padding: 0.2rem 0.6rem;
  border-radius: 3px;
  font-size: 0.8rem;
  font-weight: 400;
}

.book-type {
  background: var(--accent-color);
  color: white;
  padding: 0.2rem 0.6rem;
  border-radius: 3px;
  font-size: 0.8rem;
  font-weight: 500;
}

.book-link {
  color: var(--accent-color);
  text-decoration: none;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  transition: color 0.2s ease;
}

.book-link:hover {
  color: var(--primary-color);
  text-decoration: underline;
}

.book-item.featured-project {
  border-left: 3px solid var(--primary-color);
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
}

.project-features {
  margin: 1.5rem 0;
  padding: 1rem;
  background: var(--bg-light);
  border-radius: 3px;
}

.feature-item {
  color: var(--text-medium);
  font-size: 0.9rem;
  margin: 0.5rem 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.feature-item::before {
  content: '';
  width: 4px;
  height: 4px;
  background: var(--accent-color);
  border-radius: 50%;
  flex-shrink: 0;
}

.book-status {
  background: #28a745;
  color: white;
  padding: 0.2rem 0.6rem;
  border-radius: 3px;
  font-size: 0.8rem;
  font-weight: 500;
}

.project-links {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.book-link.primary {
  background: var(--accent-color);
  color: white;
  padding: 0.6rem 1.2rem;
  border-radius: 3px;
  text-decoration: none;
  font-weight: 500;
  transition: background 0.2s ease;
}

.book-link.primary:hover {
  background: var(--primary-color);
  text-decoration: none;
}

.book-link.secondary {
  background: transparent;
  color: var(--accent-color);
  border: 1px solid var(--accent-color);
  padding: 0.6rem 1.2rem;
  border-radius: 3px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.2s ease;
}

.book-link.secondary:hover {
  background: var(--accent-color);
  color: white;
  text-decoration: none;
}

.book-item.featured-book {
  border-left: 4px solid var(--accent-color);
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  position: relative;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}

.book-badge {
  position: absolute;
  top: -10px;
  right: 20px;
  background: var(--accent-color);
  color: white;
  padding: 0.4rem 1rem;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 600;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.book-highlights {
  margin: 1.5rem 0;
  padding: 1.5rem;
  background: var(--bg-light);
  border-radius: 6px;
  border-left: 3px solid var(--accent-color);
}

.highlight-item {
  color: var(--text-dark);
  font-size: 0.95rem;
  margin: 0.8rem 0;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  font-weight: 500;
}

.book-link.featured {
  background: linear-gradient(135deg, var(--accent-color) 0%, var(--primary-color) 100%);
  color: white;
  padding: 0.8rem 1.5rem;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  box-shadow: 0 3px 12px rgba(0,0,0,0.15);
}

.book-link.featured:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.2);
  text-decoration: none;
}

/* Fixed Navigation */
.masthead {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  z-index: 1000 !important;
  background: var(--bg-white) !important;
  border-bottom: 1px solid var(--border-light) !important;
  box-shadow: var(--shadow-subtle) !important;
  transition: all 0.2s ease !important;
}

/* Adjust body padding to account for fixed header */
body {
  padding-top: 80px !important;
}

/* Ensure proper spacing for the main content */
.page__content {
  margin-top: 0 !important;
}

/* Style the navigation links */
.masthead__menu {
  background: transparent !important;
}

.masthead__menu-item {
  color: var(--text-dark) !important;
}

.masthead__menu-item:hover {
  color: var(--accent-color) !important;
}

</style>

<!-- Hero Section -->
<section class="hero-section">
  <div class="container">
    <h1 class="hero-title">Produzindo evidências científicas em Engenharia de Software</h1>
    <p class="hero-subtitle">
      Professora na <strong>Faculdade de Engenharia de Software (UnB)</strong> e coordenadora do <strong>Lab Livre</strong>. 
      Pesquisa dedicada ao desenvolvimento de soluções tecnológicas com impacto social, promovendo software livre, práticas ágeis e inovação no setor público.
    </p>
    <div class="hero-buttons">
      <a href="/projects/" class="btn">Projetos de Pesquisa</a>
      <a href="/publications/" class="btn btn-secondary">Publicações</a>
      <a href="mailto:caguiar@unb.br" class="btn btn-secondary">Contato</a>
    </div>
  </div>
</section>

<!-- Research Areas Section -->
<section class="research-section">
  <div class="container">
    <h2 class="section-title">Linhas de Pesquisa</h2>
    <div class="research-grid">
      <div class="research-card">
        <h3 class="research-title">Engenharia de Software e DevOps</h3>
        <p class="research-description">
          Pesquisa em práticas de desenvolvimento ágil, integração contínua, 
          e metodologias de engenharia de software para o setor público.
        </p>
        <a href="/projects/" class="research-link">Ver Projetos →</a>
      </div>
      
      <div class="research-card">
        <h3 class="research-title">Inteligência Artificial e Dados</h3>
        <p class="research-description">
          Desenvolvimento de soluções de IA para detecção de desinformação, 
          análise de dados governamentais e sistemas inteligentes.
        </p>
        <a href="/projects/thinkads" class="research-link">ThinkAds →</a>
      </div>
      
      <div class="research-card">
        <h3 class="research-title">Tecnologias Cívicas</h3>
        <p class="research-description">
          Plataformas de participação digital, transparência governamental 
          e ferramentas para fortalecimento da democracia.
        </p>
        <a href="/projects/ecossistemas" class="research-link">Brasil Participativo →</a>
      </div>
      
      <div class="research-card">
        <h3 class="research-title">Software Livre e Inovação Pública</h3>
        <p class="research-description">
          Promoção do software livre no setor público, desenvolvimento 
          colaborativo e transferência de tecnologia.
        </p>
        <a href="https://www.lappis.rocks" class="research-link">Lab Livre →</a>
      </div>
    </div>
  </div>
</section>

<!-- Publications Section -->
<section class="publications-section">
  <div class="container">
    <h2 class="section-title">Publicações em Destaque</h2>
    <div class="publications-grid">
      <div class="publication-item featured">
        <h3 class="pub-title">A Survey of DevOps Concepts and Challenges</h3>
        <p class="pub-authors">L Leite, C Rocha, F Kon, D Milojicic, P Meirelles</p>
        <p class="pub-venue">ACM Computing Surveys (CSUR), Volume 52, Número 6</p>
        <div class="pub-meta">
          <span class="pub-year">2019</span>
          <span class="pub-citations">676 citações</span>
        </div>
        <a href="https://scholar.google.com/citations?view_op=view_citation&hl=pt-BR&user=_y8XHnAAAAAJ&citation_for_view=_y8XHnAAAAAJ:u-x6o8ySG0sC" class="pub-link" target="_blank">Ver publicação →</a>
      </div>
      
      <div class="publication-item">
        <h3 class="pub-title">Qualifying Software Engineers Undergraduates in DevOps</h3>
        <p class="pub-authors">I Alves, C Rocha</p>
        <p class="pub-venue">2021 IEEE/ACM 43rd International Conference on Software Engineering: Software Engineering Education and Training (ICSE-SEET)</p>
        <div class="pub-meta">
          <span class="pub-year">2021</span>
          <span class="pub-citations">26 citações</span>
        </div>
        <a href="https://scholar.google.com/citations?view_op=view_citation&hl=pt-BR&user=_y8XHnAAAAAJ&citation_for_view=_y8XHnAAAAAJ:YsMSGLbcyi4C" class="pub-link" target="_blank">Ver publicação →</a>
      </div>
      
      <div class="publication-item">
        <h3 class="pub-title">Harmonizing DevOps Taxonomies—A Grounded Theory Study</h3>
        <p class="pub-authors">J Díaz, J Pérez, I Alves, F Kon, L Leite, P Meirelles, C Rocha</p>
        <p class="pub-venue">Journal of Systems and Software, Volume 208</p>
        <div class="pub-meta">
          <span class="pub-year">2024</span>
          <span class="pub-citations">18 citações</span>
        </div>
        <a href="/publications/" class="pub-link">Ver todas as publicações →</a>
      </div>
    </div>
  </div>
</section>

<!-- Books Section -->
<section class="books-section">
  <div class="container">
    <h2 class="section-title">Livros</h2>
    <p style="text-align: center; color: var(--text-medium); margin-bottom: 3rem; font-size: 1.1rem;">
      Publicações que abordam temas fundamentais para a modernização do setor público através de tecnologia e software livre.
    </p>
    <div class="books-grid">
      <div class="book-item featured-book">
        <div class="book-badge">📖 Guia Prático</div>
        <h3 class="book-title">GovHub - Um guia prático para integração e qualificação de dados públicos</h3>
        <p class="book-authors">Carla Rocha, Lab Livre UnB, IPEA</p>
        <p class="book-description">
          Guia completo que apresenta metodologias e ferramentas práticas para transformar dados governamentais dispersos 
          em informações estratégicas, promovendo transparência e decisões baseadas em evidências no setor público.
        </p>
        <div class="book-meta">
          <span class="book-year">2025</span>
          <span class="book-type">Livro</span>
          <span class="book-status">Disponível</span>
        </div>
        <a href="https://gov-hub.io/land/dist/index.html#" class="book-link featured" target="_blank">📖 Baixar Guia →</a>
      </div>
      
      <div class="book-item featured-book">
        <div class="book-badge">📚 Livro</div>
        <h3 class="book-title">Dinheiro Público Código Público - Modernizando a Infraestrutura Pública com Software Livre</h3>
        <p class="book-description">
          Obra fundamental sobre a aplicação de software livre no setor público, apresentando técnicas de aprendizagem experiencial, 
          mentoria e estratégias para modernização da infraestrutura governamental através de soluções abertas e colaborativas.
        </p>
        <div class="book-meta">
          <span class="book-year">2023</span>
          <span class="book-type">E-book</span>
          <span class="book-status">Disponível</span>
        </div>
        <a href="https://download.fsfe.org/campaigns/pmpc/PMPC-Modernising-with-Free-Software.pt_br.pdf" class="book-link featured" target="_blank">📚 Ler Online →</a>
      </div>
    </div>
  </div>
</section>

<!-- Contact Section -->
<section class="contact-section" style="background: var(--bg-light); padding: 4rem 0; text-align: center;">
  <div class="container">
    <h2 class="section-title">Contato</h2>
    <p style="font-size: 1.1rem; color: var(--text-medium); max-width: 600px; margin: 0 auto 2rem auto;">
      Para colaborações acadêmicas, orientações ou parcerias em projetos de pesquisa.
    </p>
    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
      <a href="mailto:caguiar@unb.br" class="btn">caguiar@unb.br</a>
      <a href="https://scholar.google.com/citations?user=_y8XHnAAAAAJ&hl=pt-BR" class="btn btn-secondary" target="_blank">Google Scholar</a>
      <a href="http://lattes.cnpq.br/2831991076751452" class="btn btn-secondary" target="_blank">Currículo Lattes</a>
    </div>
  </div>
</section>
