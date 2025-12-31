---
layout: homepage
title: Participação
permalink: /misc/
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

.misc-wrapper {
  font-family: var(--font-body);
  background: var(--background);
  color: var(--foreground);
  line-height: 1.6;
  margin: -2rem;
}

.misc-wrapper h1, .misc-wrapper h2, .misc-wrapper h3 {
  font-family: var(--font-body);
  font-weight: 700;
  line-height: 1.2;
  color: var(--foreground);
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }
.max-w-6xl { max-width: 72rem; margin: 0 auto; }

/* Hero Section */
.hero-misc {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  padding: 4rem 0;
  text-align: center;
  border-bottom: 1px solid var(--border);
}

.hero-misc h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--foreground);
}

.hero-misc p {
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
  margin-bottom: 2rem;
  color: var(--foreground);
}

/* Highlight Cards */
.highlight-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-bottom: 2rem;
}

.highlight-card {
  background: #ffffff;
  border-radius: 1rem;
  padding: 2rem;
  text-align: center;
  border: none;
  transition: all 0.3s ease;
}

.highlight-card:hover {
  border-color: var(--primary);
  box-shadow: 0 8px 30px rgba(0, 102, 204, 0.1);
}

.highlight-card .icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  display: block;
}

.highlight-card h3 {
  color: var(--foreground);
  margin-bottom: 0.5rem;
  font-size: 1.25rem;
}

.highlight-card p {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin: 0;
}

/* Participation List */
.participation-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.participation-item {
  background: #ffffff;
  border: none;
  border-radius: 0.75rem;
  padding: 1.25rem;
  transition: all 0.3s ease;
}

.participation-item:hover {
  border-color: var(--primary);
}

.participation-item a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 500;
}

.participation-item a:hover {
  text-decoration: underline;
}

.participation-item .desc {
  color: var(--text-secondary);
  font-size: 0.85rem;
  margin-top: 0.25rem;
}

/* Project Grid */
.project-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.project-card {
  background: #ffffff;
  border: none;
  border-radius: 1rem;
  padding: 1.5rem;
  transition: all 0.3s ease;
}

.project-card:hover {
  border-color: var(--primary);
  box-shadow: 0 4px 20px rgba(0, 102, 204, 0.1);
}

.project-card h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
}

.project-card h3 a {
  color: var(--primary);
  text-decoration: none;
}

.project-card h3 a:hover {
  text-decoration: underline;
}

.project-card p {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin: 0;
  line-height: 1.5;
}

/* Translation Highlight */
.translation-highlight {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  border: none;
  border-radius: 1rem;
  padding: 2rem;
  margin-top: 2rem;
  text-align: center;
}

.translation-highlight h3 {
  color: var(--primary);
  margin-bottom: 1rem;
}

.translation-highlight p {
  color: var(--text-secondary);
  margin-bottom: 1rem;
}

.translation-highlight a {
  color: var(--primary);
}

.publication-image {
  margin-top: 1.5rem;
}

.publication-image img {
  max-width: 300px;
  border-radius: 0.5rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

/* Responsive */
@media (max-width: 768px) {
  .hero-misc h1 { font-size: 2rem; }
  .highlight-grid { grid-template-columns: 1fr; }
  .participation-grid { grid-template-columns: 1fr; }
  .project-grid { grid-template-columns: 1fr; }
  .section { padding: 3rem 0; }
}
</style>

<div class="misc-wrapper">

<section class="hero-misc">
  <div class="container">
    <h1>Participação & Contribuições</h1>
    <p>Engajamento em comunidades, eventos e projetos de impacto</p>
  </div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <div class="highlight-grid">
      <div class="highlight-card">
        <h3>Liderança</h3>
        <p>Co-fundadora BOSS e coordenação de eventos acadêmicos e projetos de pesquisa</p>
      </div>
      <div class="highlight-card">
        <h3>Palestras</h3>
        <p>Apresentações em eventos nacionais e internacionais</p>
      </div>
      <div class="highlight-card">
        <h3>Open Source</h3>
        <p>Desenvolvimento e manutenção de projetos de código aberto</p>
      </div>
    </div>
  </div></div>
</section>

<section class="section" style="background: #f8f9fa;">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Participações</span></div>
    <h2 class="section-title">Principais Participações</h2>
    <div class="participation-grid">
      <div class="participation-item">
        <a href="https://www.youtube.com/c/BigOpenSourceSibling" target="_blank">Co-fundadora BOSS</a>
        <div class="desc">Big Open Source Sibling - Programa de mentoria</div>
      </div>
      <div class="participation-item">
        <a href="https://youtube.com/playlist?list=PLFFHHqnY3q2FLjtGKYuI-V-z9u7jzBOb_" target="_blank">Talk Like a BOSS</a>
        <div class="desc">Rodas de conversas pela BOSS</div>
      </div>
      <div class="participation-item">
        <a href="https://youtu.be/zynynEynpk8" target="_blank">Mini Lab Livre Conf</a>
        <div class="desc">Co-apresentadora e organizadora</div>
      </div>
      <div class="participation-item">
        <a href="http://www.agilebrazil.com/2021/wbma" target="_blank">WBMA - Agile Brazil 2021</a>
        <div class="desc">Co-presidente do programa</div>
      </div>
      <div class="participation-item">
        <a href="https://youtu.be/MlGYHl3Iyyg" target="_blank">Campus Party 2020</a>
        <div class="desc">Palestrante</div>
      </div>
      <div class="participation-item">
        <a href="https://covidas-unb.github.io/InfoGerais/" target="_blank">CoVidas UnB Hackathon 2020</a>
        <div class="desc">Comitê científico</div>
      </div>
      <div class="participation-item">
        <a href="https://revistadarcy.unb.br" target="_blank">Revista Darcy</a>
        <div class="desc">Membro do Conselho Editorial</div>
      </div>
      <div class="participation-item">
        <span style="color: var(--foreground); font-weight: 500;">CGECIS - UnB</span>
        <div class="desc">Comitê de Gestão Estratégica de Campus Inteligente</div>
      </div>
    </div>
  </div></div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Apresentações</span></div>
    <h2 class="section-title">Palestras e Talks</h2>
    <div class="participation-grid">
      <div class="participation-item">
        <a href="https://docs.google.com/presentation/d/1bAOZ0gLjEIwOLhkRhakvaXG1_FP4fGuHYMVhEc72w7M/edit?usp=sharing" target="_blank">Introdução à BOSS</a>
        <div class="desc">Guadec 2021</div>
      </div>
      <div class="participation-item">
        <a href="https://docs.google.com/presentation/d/1c0bLbdfj8ztAvIQz3MNYSp0I6zjUhQDO4k3aqQianEU/edit?usp=sharing" target="_blank">Arquitetura de Chatbot Open Source</a>
        <div class="desc">Campus Party 2019</div>
      </div>
      <div class="participation-item">
        <a href="https://docs.google.com/presentation/d/1xFwBtiMU08lOgSGFG4s9QpUZF80Ei5HENvTPN1VffGs/edit?usp=sharing" target="_blank">Formando inovadores através de Open Source</a>
        <div class="desc">Campus Party 2020</div>
      </div>
    </div>
  </div></div>
</section>

<section class="section" style="background: #f8f9fa;">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Open Source</span></div>
    <h2 class="section-title">Software Livre</h2>
    <p style="color: var(--text-secondary); margin-bottom: 2rem;">Nossos projetos de pesquisa seguem a prática do uso de licenças de software livre. Todos os projetos são disponibilizados na organização do laboratório no GitLab/GitHub.</p>
    
    <div class="project-grid">
      <div class="project-card">
        <h3><a href="https://gitlab.com/lappis-unb/decidimbr" target="_blank">Brasil Participativo</a></h3>
        <p>Plataforma de participação social baseada no Decidim para engajamento cidadão.</p>
      </div>
      <div class="project-card">
        <h3><a href="https://github.com/lappis-unb/rasa-ptbr-boilerplate" target="_blank">Chatbot Boilerplate PT-BR</a></h3>
        <p>Arquitetura boilerplate de chatbot utilizando Rasa, configurado para Português.</p>
      </div>
      <div class="project-card">
        <h3><a href="https://github.com/Escola-em-Casa" target="_blank">Escola em Casa</a></h3>
        <p>Acesso gratuito aos recursos de ensino à distância da Secretaria de Educação do DF.</p>
      </div>
      <div class="project-card">
        <h3><a href="https://github.com/lappis-unb/realtimecardgame" target="_blank">Real time Card Game</a></h3>
        <p>Jogo de carta real time utilizando Unity3D para aprendizagem.</p>
      </div>
      <div class="project-card">
        <h3><a href="https://github.com/fga-eps-mds" target="_blank">POC OSS Projects</a></h3>
        <p>Projetos de software por estudantes de Engenharia de Software.</p>
      </div>
      <div class="project-card">
        <h3><a href="https://github.com/BOSS-BigOpenSourceSibling/" target="_blank">BOSS Organization</a></h3>
        <p>Material de apoio do programa de mentoria Big Open Source Siblings.</p>
      </div>
    </div>

    <div class="translation-highlight">
      <h3>Tradução FSFE</h3>
      <p>O time do Lab Livre/LAPPIS traduziu para o português brasileiro a publicação "Public Money Public Code – Modernising Public Infrastructure with Free Software" da Free Software Foundation Europe.</p>
      <p><a href="https://download.fsfe.org/campaigns/pmpc/PMPC-Modernising-with-Free-Software.pt_br.pdf" target="_blank"><strong>Dinheiro Público Código Público - Modernizando a Infraestrutura Pública com Software Livre</strong></a></p>
      <div class="publication-image">
        <img src="/images/publico.png" alt="Dinheiro Público Código Público" />
      </div>
    </div>
  </div></div>
</section>

</div>
