---
layout: posts
author_profile: false
permalink: /projects/
sidebar: false
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
  border-bottom: 1px solid #e0e0e0 !important;
}
.masthead__inner-wrap {
  max-width: 1200px !important;
  padding: 0 1.5rem !important;
}
.greedy-nav a { color: #000000 !important; }
.greedy-nav a:hover { color: #0066cc !important; }
.greedy-nav .visible-links a:before { background: #0066cc !important; }
.site-title { color: #000000 !important; font-weight: 700 !important; }
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
.search__toggle {
  color: #000000 !important;
}
.search__toggle:hover {
  color: #0066cc !important;
}
.search__toggle svg {
  fill: #000000 !important;
}
.search__toggle:hover svg {
  fill: #0066cc !important;
}

/* Hide sidebar - both sides */
.sidebar, .author__avatar, .author__content, .author__urls-wrapper,
.sidebar__right, .sidebar__left, .toc, .toc__menu {
  display: none !important;
}
#main {
  margin-left: 0 !important;
  margin-right: 0 !important;
  padding-left: 1rem !important;
  padding-right: 1rem !important;
  max-width: 100% !important;
}
.page {
  float: none !important;
  width: 100% !important;
  padding-right: 0 !important;
}
.page__inner-wrap {
  max-width: 900px;
  margin: 0 auto;
}
/* Enhanced Mobile-First Responsive Design */

/* Base styles - Mobile first approach */
.page__content {
  max-width: 100%;
  padding: 1rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  margin: 0.5rem 0;
  overflow-wrap: break-word;
  word-wrap: break-word;
}

.page__title {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  line-height: 1.3;
  color: #2c3e50;
  text-align: center;
}

.page__content p {
  line-height: 1.6;
  margin-bottom: 1.5rem;
  text-align: left;
  font-size: 0.9rem;
  color: #333;
}

.page__content a {
  color: #667eea;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s ease;
  word-break: break-word;
}

.page__content a:hover {
  color: #764ba2;
  text-decoration: underline;
}

/* Ensure proper spacing and readability on mobile */
.page__content {
  line-height: 1.6;
}

/* Better text wrapping for long URLs and text */
.page__content a[href] {
  overflow-wrap: break-word;
  word-wrap: break-word;
  hyphens: auto;
}

/* Tablet styles */
@media (min-width: 481px) and (max-width: 768px) {
  .page__content {
    padding: 1.5rem;
    margin: 0.75rem 0;
  }
  
  .page__title {
    font-size: 1.8rem;
  }
  
  .page__content p {
    font-size: 0.95rem;
  }
}

/* Desktop styles */
@media (min-width: 769px) {
  .page__content {
    padding: 2rem;
    margin: 1rem 0;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .page__title {
    font-size: 2.2rem;
    text-align: left;
  }
  
  .page__content p {
    font-size: 1rem;
    text-align: justify;
  }
}

/* Large desktop styles */
@media (min-width: 1200px) {
  .page__content {
    max-width: 900px;
    padding: 2.5rem;
  }
  
  .page__title {
    font-size: 2.5rem;
  }
  
  .page__content p {
    font-size: 1.1rem;
  }
}

/* Fix for very small screens */
@media (max-width: 320px) {
  .page__content {
    padding: 0.75rem;
    margin: 0.25rem 0;
  }
  
  .page__title {
    font-size: 1.3rem;
  }
  
  .page__content p {
    font-size: 0.85rem;
  }
}

/* Improve touch targets for mobile */
@media (max-width: 768px) {
  .page__content a {
    padding: 0.2rem 0;
    display: inline-block;
    min-height: 44px;
    line-height: 1.4;
  }
}

/* Better sidebar handling on mobile */
@media (max-width: 768px) {
  .sidebar {
    display: none;
  }
  
  #main {
    margin-left: 0 !important;
  }
  
  .archive {
    width: 100% !important;
    padding: 0 !important;
  }
}

/* Ensure proper viewport handling */
.page {
  width: 100%;
  overflow-x: hidden;
}

/* Better spacing for mobile reading */
@media (max-width: 768px) {
  .page__content p:last-child {
    margin-bottom: 2rem;
  }
}

/* Hero Section */
.hero-proj {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  padding: 3rem 1.5rem;
  text-align: center;
  border-bottom: 1px solid #e0e0e0;
  margin: -2rem calc(-50vw + 50%) 2rem calc(-50vw + 50%);
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  margin-top: -2rem;
  margin-bottom: 2rem;
}

.hero-proj h1 {
  font-size: 2rem;
  margin-bottom: 0.75rem;
  color: #000;
  font-weight: 700;
}

.hero-proj p {
  font-size: 1rem;
  color: #666;
  max-width: 600px;
  margin: 0 auto 1.5rem auto;
}

.external-links {
  display: flex;
  justify-content: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.external-link {
  display: inline-flex;
  align-items: center;
  padding: 0.6rem 1.25rem;
  background: #0066cc;
  color: white !important;
  text-decoration: none !important;
  border-radius: 0.5rem;
  font-weight: 500;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.external-link:hover {
  background: #004499;
  transform: translateY(-2px);
  color: white !important;
}

@media (max-width: 768px) {
  .hero-proj { padding: 2rem 1rem; }
  .hero-proj h1 { font-size: 1.5rem; }
  .external-links { flex-direction: column; align-items: center; }
}
</style>

<div class="hero-proj">
  <h1>Projetos de Pesquisa</h1>
  <p>Pesquisa aplicada em Engenharia de Dados, Participação Digital, DevOps, MLOps e Software Livre</p>
  <div class="external-links">
    <a href="https://lablivre.unb.br/" class="external-link" target="_blank">Lab Livre</a>
    <a href="http://lattes.cnpq.br/2831991076751452" class="external-link" target="_blank">Currículo Lattes</a>
    <a href="https://summerofcode.withgoogle.com/archive/2024/organizations/lappis" class="external-link" target="_blank">GSoC 2024</a>
  </div>
</div>

Faço parte diversos projetos de pesquisa, tanto com grupos de pesquisa quanto com departamentos de Pesquisa e Desenvolvimento (P&D) de empresas. Participo do grupo de pesquisa com [IME-USP](http://dgp.cnpq.br/dgp/espelhogrupo/633486) "Sistemas de Software, Ciência e Engenharia de Dados e Computação de Alto Desempenho".

Atuo como uma das coordenadoras do laboratório de pesquisa aplicada [LAPPIS](https://lablivre.unb.br/), onde tenho a oportunidade de liderar várias iniciativas de pesquisa aplicada em colaboração com agências governamentais e empresas privadas. Ao longo do meu percurso, supervisionei mais de 70 bolsas de pesquisa.

A maioria dos projetos pesquisa aplicada em que estou engajada está focada no desenvolvimento de software, sendo distribuído como Software Livre. Apresento aqui os principais projetos ativos e passados. Para mais detalhes, entre no [Lattes](http://lattes.cnpq.br/2831991076751452).

Em 2024, o LAPPIS foi selecionado como organização participante do [Google Summer of Code (GSoC) 2024](https://summerofcode.withgoogle.com/archive/2024/organizations/lappis), programa global do Google que conecta estudantes a projetos de código aberto. Esta participação reforça nosso compromisso com a comunidade de Software Livre e a formação de novos desenvolvedores.
