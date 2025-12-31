---
layout: homepage
title: Leituras
permalink: /reading/
author_profile: false
---

<style>
/* Fixed navigation bar */
.masthead {
  position: fixed !important;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: #ffffff !important;
}
body {
  padding-top: 70px;
}

/* Hamburger menu color - match titles */
.greedy-nav__toggle .navicon,
.greedy-nav__toggle .navicon::before,
.greedy-nav__toggle .navicon::after {
  background: #000000 !important;
}
.greedy-nav__toggle:hover .navicon,
.greedy-nav__toggle:hover .navicon::before,
.greedy-nav__toggle:hover .navicon::after {
  background: #0066cc !important;
}
.search__toggle { color: #000000 !important; }
.search__toggle:hover { color: #0066cc !important; }
.search__toggle svg { fill: #000000 !important; }
.search__toggle:hover svg { fill: #0066cc !important; }

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

.reading-wrapper {
  font-family: var(--font-body);
  background: var(--background);
  color: var(--foreground);
  line-height: 1.6;
  margin: -2rem;
}

.reading-wrapper h1, .reading-wrapper h2, .reading-wrapper h3 {
  font-family: var(--font-body);
  font-weight: 700;
  line-height: 1.2;
  color: var(--foreground);
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }
.max-w-6xl { max-width: 72rem; margin: 0 auto; }

/* Hero Section */
.hero-reading {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  padding: 4rem 0;
  text-align: center;
  border-bottom: 1px solid var(--border);
}

.hero-reading h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--foreground);
}

.hero-reading p {
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
  font-size: 1.75rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: var(--foreground);
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.section-title .icon {
  font-size: 1.5rem;
}

/* Reading Grid */
.reading-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.reading-card {
  background: #ffffff;
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
}

.reading-card:hover {
  box-shadow: 0 4px 12px rgba(0, 102, 204, 0.1);
}

.reading-card a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  display: block;
  margin-bottom: 0.25rem;
}

.reading-card a:hover {
  text-decoration: underline;
}

.reading-card .author {
  color: var(--text-secondary);
  font-size: 0.85rem;
  font-style: italic;
}

/* Category Section */
.category-section {
  margin-bottom: 3rem;
}

/* Responsive - Mobile First */
@media (max-width: 480px) {
  .reading-wrapper { margin: -1rem; }
  .container { padding: 0 1rem; }
  .hero-reading { padding: 2rem 0; }
  .hero-reading h1 { font-size: 1.5rem; }
  .hero-reading p { font-size: 1rem; }
  .section { padding: 2rem 0; }
  .section-title { font-size: 1.25rem; gap: 0.5rem; }
  .section-title .icon { font-size: 1.25rem; }
  .reading-grid { grid-template-columns: 1fr; gap: 0.75rem; }
  .reading-card { padding: 1rem; }
  .reading-card a { font-size: 0.9rem; }
  .reading-card .author { font-size: 0.8rem; }
  .category-section { margin-bottom: 2rem; }
}

@media (min-width: 481px) and (max-width: 768px) {
  .reading-wrapper { margin: -1.5rem; }
  .hero-reading h1 { font-size: 1.75rem; }
  .section { padding: 2.5rem 0; }
  .section-title { font-size: 1.5rem; }
  .reading-grid { grid-template-columns: 1fr; }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .hero-reading h1 { font-size: 2rem; }
  .section { padding: 3rem 0; }
}
</style>

<div class="reading-wrapper">

<section class="hero-reading">
  <div class="container">
    <h1>Recursos de Pesquisa</h1>
    <p>Materiais de apoio para orientandos e pesquisadores</p>
  </div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <p style="color: var(--text-secondary); text-align: center; margin-bottom: 3rem;">Algumas sugestões, sem uma ordem específica (algumas delas retiradas de <a href="https://gustavopinto.org" target="_blank" style="color: var(--primary);">gustavopinto.org</a>)</p>

    <div class="category-section">
      <h2 class="section-title"> Trabalho de Conclusão de Curso</h2>
      <div class="reading-grid">
        <div class="reading-card">
          <a href="/assets/docs/TCC.pdf" target="_blank">Guia de Sobrevivência do TCC</a>
          <div class="author">por Carla Rocha</div>
        </div>
      </div>
    </div>

    <div class="category-section">
      <h2 class="section-title"> Leitura Obrigatória</h2>
      <div class="reading-grid">
        <div class="reading-card">
          <a href="https://youtube.com/playlist?list=PLFFHHqnY3q2FLjtGKYuI-V-z9u7jzBOb_" target="_blank">Talk like a BOSS - rodas de conversas</a>
          <div class="author">por Big Open Source Sibling (BOSS)</div>
        </div>
        <div class="reading-card">
          <a href="https://www.slideshare.net/cameraculture/raskar-phd-and-ms-thesis-guidance" target="_blank">Orientação para Tese de Doutorado e Mestrado</a>
          <div class="author">por Ramesh Raskar</div>
        </div>
        <div class="reading-card">
          <a href="https://www.nature.com/articles/d41586-018-02404-4" target="_blank">Como escrever um artigo de primeira classe</a>
          <div class="author">por Virginia Gewin</div>
        </div>
        <div class="reading-card">
          <a href="https://homes.cs.washington.edu/~mernst/advice/" target="_blank">Conselhos para pesquisadores e estudantes</a>
          <div class="author">por Michael Ernst</div>
        </div>
        <div class="reading-card">
          <a href="http://matt.might.net/articles/grad-student-resolutions/" target="_blank">12 resoluções para estudantes de pós-graduação</a>
          <div class="author">por Matt Might</div>
        </div>
        <div class="reading-card">
          <a href="https://www.scielo.br/pdf/clin/v69n3/1807-5932-clin-69-03-153.pdf" target="_blank">Escrevendo artigos científicos como falante nativo de inglês</a>
          <div class="author">Dicas para falantes de português</div>
        </div>
        <div class="reading-card">
          <a href="https://ieeexplore.ieee.org/document/799955" target="_blank">Métodos qualitativos em estudos empíricos de ES</a>
          <div class="author">IEEE</div>
        </div>
        <div class="reading-card">
          <a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006914" target="_blank">Dez regras simples para laboratórios mais saudáveis</a>
          <div class="author">PLOS Computational Biology</div>
        </div>
      </div>
    </div>

    <div class="category-section">
      <h2 class="section-title"> Escrita de Artigos</h2>
      <div class="reading-grid">
        <div class="reading-card">
          <a href="https://users.ece.cmu.edu/~koopman/essays/abstract.html" target="_blank">Como Escrever um Resumo</a>
          <div class="author">por Philip Koopman</div>
        </div>
        <div class="reading-card">
          <a href="http://sarahnadi.org/writing-papers/" target="_blank">Escrevendo Artigos Acadêmicos</a>
          <div class="author">por Sarah Nadi</div>
        </div>
        <div class="reading-card">
          <a href="http://www.cis.famu.edu/~cen5055joe/Administrative/HowToWrite_ResearchPaper.pdf" target="_blank">Escrevendo Boas Pesquisas em Engenharia de Software</a>
          <div class="author">por Mary Shaw</div>
        </div>
        <div class="reading-card">
          <a href="https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper" target="_blank">Como escrever um ótimo artigo de pesquisa</a>
          <div class="author">por Simon Peyton Jones</div>
        </div>
      </div>
    </div>

    <div class="category-section">
      <h2 class="section-title"> Apresentações</h2>
      <div class="reading-grid">
        <div class="reading-card">
          <a href="https://www.microsoft.com/en-us/research/academic-program/give-great-research-talk" target="_blank">Como fazer uma ótima apresentação de pesquisa</a>
          <div class="author">por Simon Peyton Jones</div>
        </div>
        <div class="reading-card">
          <a href="http://andreas-zeller.blogspot.com.br/2013/10/summarizing-your-presentation-with.html" target="_blank">Resumindo sua apresentação com mini slides</a>
          <div class="author">por Andreas Zeller</div>
        </div>
      </div>
    </div>

    <div class="category-section">
      <h2 class="section-title"> Rejeições</h2>
      <div class="reading-grid">
        <div class="reading-card">
          <a href="https://medium.com/@cfiesler/tenured-professor-rogers-talks-about-imposter-syndrome-229e0a546ac1" target="_blank">Professor Titular Rogers Fala Sobre: Síndrome do Impostor</a>
          <div class="author">por Casey Fiesler</div>
        </div>
      </div>
    </div>

    <div class="category-section">
      <h2 class="section-title"> Tópicos Gerais</h2>
      <div class="reading-grid">
        <div class="reading-card">
          <a href="https://medium.com/@lappisunbfga/what-i-wish-i-knew-before-starting-my-first-chatbot-project-66e5208f77dd" target="_blank">O que eu gostaria de saber antes de começar meu primeiro projeto de Chatbot</a>
          <div class="author">por Carla Rocha</div>
        </div>
        <div class="reading-card">
          <a href="https://medium.com/@lappisunbfga/desafios-ensino-de-ti-em-tempo-de-pandemia-o-futuro-é-colaborativo-e7aa183bb3d7" target="_blank">Desafios do ensino de TI em tempos de pandemia</a>
          <div class="author">por Carla Rocha</div>
        </div>
      </div>
    </div>

  </div></div>
</section>

</div>
