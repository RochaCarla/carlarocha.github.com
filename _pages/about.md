---
layout: homepage
title: Bio
permalink: /about/
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

.about-wrapper {
  font-family: var(--font-body);
  background: var(--background);
  color: var(--foreground);
  line-height: 1.6;
  margin: -2rem;
}

.about-wrapper h1, .about-wrapper h2, .about-wrapper h3 {
  font-family: var(--font-body);
  font-weight: 700;
  line-height: 1.2;
  color: var(--foreground);
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }
.max-w-6xl { max-width: 72rem; margin: 0 auto; }

/* Hero Section */
.hero-about {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  padding: 4rem 0;
  text-align: center;
  border-bottom: 1px solid var(--border);
}

.hero-about h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--foreground);
}

.hero-about p {
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

/* Bio Text */
.bio-text {
  color: var(--text-secondary);
  font-size: 1.05rem;
  line-height: 1.8;
  max-width: 800px;
}

.bio-text a {
  color: var(--primary);
  text-decoration: none;
}

.bio-text a:hover {
  text-decoration: underline;
}

/* Links Grid */
.links-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.link-card {
  background: #ffffff;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  text-align: center;
  transition: all 0.3s ease;
}

.link-card:hover {
  box-shadow: 0 8px 24px rgba(0, 102, 204, 0.1);
}

.link-card .icon {
  font-size: 2rem;
  margin-bottom: 0.75rem;
}

.link-card h3 {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.link-card a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 500;
}

.link-card a:hover {
  text-decoration: underline;
}

.link-card p {
  color: var(--text-secondary);
  font-size: 0.85rem;
  margin: 0;
}

/* Contact Card */
.contact-card {
  background: var(--primary);
  color: white;
  border-radius: 1rem;
  padding: 2rem;
  text-align: center;
}

.contact-card h3 {
  color: white;
  margin-bottom: 1rem;
}

.contact-card a {
  color: white;
  font-size: 1.25rem;
  font-weight: 600;
}

/* Responsive - Mobile First */
@media (max-width: 480px) {
  .about-wrapper { margin: -1rem; }
  .container { padding: 0 1rem; }
  .hero-about { padding: 2rem 0; }
  .hero-about h1 { font-size: 1.5rem; }
  .hero-about p { font-size: 1rem; }
  .section { padding: 2rem 0; }
  .section-title { font-size: 1.5rem; }
  .bio-text { font-size: 0.95rem; line-height: 1.7; }
  .links-grid { grid-template-columns: 1fr; gap: 1rem; }
  .link-card { padding: 1rem; }
  .link-card .icon { font-size: 1.5rem; }
  .link-card h3 { font-size: 1rem; }
  .contact-card { padding: 1.5rem; }
  .contact-card h3 { font-size: 1.1rem; }
  .contact-card a { font-size: 1rem; }
}

@media (min-width: 481px) and (max-width: 768px) {
  .about-wrapper { margin: -1.5rem; }
  .hero-about h1 { font-size: 1.75rem; }
  .section { padding: 2.5rem 0; }
  .section-title { font-size: 1.75rem; }
  .links-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .hero-about h1 { font-size: 2rem; }
  .section { padding: 3rem 0; }
  .links-grid { grid-template-columns: repeat(2, 1fr); }
}
</style>

<div class="about-wrapper">

<section class="hero-about">
  <div class="container">
    <h1>Carla Rocha</h1>
    <p>Professora na Universidade de Brasília • Pesquisadora em Engenharia de Software</p>
  </div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">English</span></div>
    <h2 class="section-title">Biography</h2>
    <div class="bio-text">
      <p>Dr. Carla Rocha is an adjunct professor at the <a href="http://www.unb.br" target="_blank">University of Brasília (UnB)</a>, where she holds a PhD in Computer Science from the Laboratoire d'Informatique, de Robotique et de Microélectronique de Montpellier (<a href="http://lirmm.fr" target="_blank">LIRMM</a>). Her areas of expertise span across multiple aspects of Software Engineering, including Open Source Software communities and contributors, Human Aspects of Software Engineering, Empirical Software Engineering, and Mining Software Repositories techniques.</p>
      <p>She is also a coordinator of the research group <a href="https://lablivre.unb.br/" target="_blank">Lab Livre</a>, one of the founding members of the <a href="https://github.com/BOSS-BigOpenSourceSibling/" target="_blank">Big Open Source Siblings (BOSS)</a> mentorship program, and has collaborated on research projects with institutions such as CCSL (IME-USP), LARA (UnB), Secretaria Especial da Cultura, the Media Lab at MIT, and C2RMF (Louvre Museum).</p>
    </div>
  </div></div>
</section>

<section class="section" style="background: #f8f9fa;">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Português</span></div>
    <h2 class="section-title">Biografia</h2>
    <div class="bio-text">
      <p>Dr. Carla Rocha é professora assistente na Universidade de Brasília (UnB), onde obteve um doutorado em Ciência da Computação no Laboratoire d'Informatique, de Robotique et de Microélectronique de Montpellier (LIRMM). Suas áreas de especialização abrangem diversos aspectos da Engenharia de Software, incluindo comunidades e contribuidores de Software Livre, Aspectos Humanos da Engenharia de Software, Engenharia de Software Empírica, DevOps e MLOps.</p>
      <p>Ela também é coordenadora do grupo de pesquisa <a href="https://lablivre.unb.br/" target="_blank">Lab Livre</a>, uma das membros fundadoras do programa de mentoria Big Open Source Siblings (BOSS), e colaborou em projetos de pesquisa com instituições como CCSL (IME-USP), LARA (UnB), Secretaria Especial da Cultura, Media Lab no MIT e C2RMF (Museu do Louvre).</p>
      <p>As pesquisas da Carla Rocha são abrangentes e incluem tópicos como desenvolvimento de software livre, ecossistemas de software livre, mentoria, o movimento DevOps e sistemas de software com módulos de aprendizado de máquina. Além de suas atividades acadêmicas, ela lidera o projeto de colaboração <strong>Brasil Participativo</strong> em parceria com o Governo Federal Brasileiro, envolvendo aproximadamente 70 colaboradores de diversas áreas.</p>
    </div>
  </div></div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Links</span></div>
    <h2 class="section-title">Grupos de Pesquisa & Redes</h2>
    
    <div class="links-grid">
      <div class="link-card">
        <div class="icon">🔬</div>
        <h3>Lab Livre @ UnB</h3>
        <a href="https://lablivre.unb.br/" target="_blank">lablivre.unb.br</a>
        <p>Laboratório de pesquisa aplicada</p>
      </div>
      <div class="link-card">
        <div class="icon">🐙</div>
        <h3>GitHub</h3>
        <a href="https://github.com/lappis-unb" target="_blank">github.com/lappis-unb</a>
        <p>Repositórios do laboratório</p>
      </div>
      <div class="link-card">
        <div class="icon">🦊</div>
        <h3>GitLab</h3>
        <a href="https://gitlab.com/lappis-unb" target="_blank">gitlab.com/lappis-unb</a>
        <p>Projetos do laboratório</p>
      </div>
      <div class="link-card">
        <div class="icon">👥</div>
        <h3>BOSS</h3>
        <a href="https://github.com/BOSS-BigOpenSourceSibling/" target="_blank">Big Open Source Siblings</a>
        <p>Programa de mentoria</p>
      </div>
      <div class="link-card">
        <div class="icon">📊</div>
        <h3>Google Scholar</h3>
        <a href="https://scholar.google.com/citations?user=_y8XHnAAAAAJ&hl=en" target="_blank">CarlaRocha</a>
        <p>Publicações acadêmicas</p>
      </div>
      <div class="link-card">
        <div class="icon">🎓</div>
        <h3>IME-USP</h3>
        <a href="http://dgp.cnpq.br/dgp/espelhogrupo/633486" target="_blank">Grupo de Pesquisa</a>
        <p>Sistemas de Software e Dados</p>
      </div>
    </div>

    <div class="contact-card" style="margin-top: 2rem;">
      <h3>📧 Entre em Contato</h3>
      <a href="mailto:caguiar@unb.br">caguiar@unb.br</a>
    </div>
  </div></div>
</section>

</div>



