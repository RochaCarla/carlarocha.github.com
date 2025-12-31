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
    <img src="/lost+found/ghlp4.png" alt="Carla Rocha" style="width: 180px; height: 180px; border-radius: 50%; object-fit: cover; margin-bottom: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    <h1>Carla Rocha</h1>
    <p>Professora na Universidade de Brasília • Pesquisadora em Engenharia de Software</p>
  </div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Português</span></div>
    <h2 class="section-title">Biografia</h2>
    <div class="bio-text">
      <p>Carla Silva Rocha Aguiar é professora e pesquisadora em Engenharia de Software na Universidade de Brasília (UnB) e coordenadora do <a href="https://lablivre.unb.br/" target="_blank">Lab Livre</a> – Laboratório de Competência em Software Livre. Atua em projetos de pesquisa e desenvolvimento nas áreas de DevOps, engenharia de dados, plataformas digitais e software livre, com foco em impacto social e inovação no setor público. Possui ampla experiência em parcerias com órgãos governamentais, integração de sistemas, arquitetura de dados e formação de estudantes por meio de projetos práticos e colaborativos.</p>
    </div>
    <h3 class="section-title" style="margin-top: 2rem;">Biografia Longa</h3>
    <div class="bio-text">
      <p>Carla Rocha é professora e pesquisadora em Engenharia de Software na Universidade de Brasília (UnB). É coordenadora do <a href="https://lablivre.unb.br/" target="_blank">Lab Livre</a> – Laboratório de Competência em Software Livre, onde desenvolve e lidera projetos de pesquisa, desenvolvimento e inovação com foco em software livre, DevOps, MLOps, engenharia de dados, plataformas digitais participativas e ecossistemas sociotécnicos.</p>
      <p>Sua atuação combina pesquisa acadêmica de alto impacto, formação de estudantes e desenvolvimento de soluções tecnológicas voltadas ao interesse público. Possui produção científica com publicações em periódicos e conferências nacionais e internacionais de alto impacto na área de Engenharia de Software, Sistemas de Informação e Computação Aplicada, contribuindo para o avanço do estado da arte em temas como organização de times DevOps, ecossistemas de software livre, engenharia de dados e plataformas digitais.</p>
      <p>Coordena e participa de projetos estratégicos em parceria com órgãos do Governo Federal, instituições públicas, privadas e sociedade civil, envolvendo integração de sistemas estruturantes, arquitetura de dados, interoperabilidade, plataformas de participação digital e uso responsável de inteligência artificial no setor público.</p>
      <p>Além da pesquisa e do desenvolvimento tecnológico, atua fortemente na formação orientada à experiência, coordenando disciplinas e projetos integradores, mentorando estudantes em iniciativas de extensão, hackathons e programas de inovação, e contribuindo ativamente para a construção de comunidades e ecossistemas colaborativos.</p>
    </div>
  </div></div>
</section>

<section class="section" style="background: #f8f9fa;">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">English</span></div>
    <h2 class="section-title">Biography</h2>
    <div class="bio-text">
      <p>Carla Silva Rocha Aguiar is a professor and researcher in Software Engineering at the University of Brasília (UnB) and coordinator of <a href="https://lablivre.unb.br/" target="_blank">Lab Livre</a> – Free Software Competence Laboratory. She works on research and development projects in DevOps, data engineering, digital platforms, and free software, with a focus on social impact and innovation in the public sector. She has extensive experience in partnerships with government agencies, systems integration, data architecture, and student training through practical and collaborative projects.</p>
    </div>
    <h3 class="section-title" style="margin-top: 2rem;">Extended Biography</h3>
    <div class="bio-text">
      <p>Carla Rocha is a professor and researcher in Software Engineering at the University of Brasília (UnB). She is the coordinator of <a href="https://lablivre.unb.br/" target="_blank">Lab Livre</a> – Free Software Competence Laboratory, where she develops and leads research, development, and innovation projects focused on free software, DevOps, MLOps, data engineering, participatory digital platforms, and sociotechnical ecosystems.</p>
      <p>Her work combines high-impact academic research, student training, and the development of technological solutions aimed at the public interest. She has scientific publications in high-impact national and international journals and conferences in the fields of Software Engineering, Information Systems, and Applied Computing, contributing to the advancement of the state of the art in topics such as DevOps team organization, free software ecosystems, data engineering, and digital platforms.</p>
      <p>She coordinates and participates in strategic projects in partnership with Federal Government agencies and public institutions, involving integration of structural systems, data architecture, interoperability, digital platforms, and responsible use of artificial intelligence in the public sector.</p>
      <p>Beyond research and technological development, she is strongly engaged in experience-oriented education, coordinating courses and integrative projects, mentoring students in extension initiatives, hackathons, and innovation programs, and actively contributing to the building of collaborative communities and ecosystems.</p>
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
        <h3>GitHub</h3>
        <a href="https://github.com/lablivre-unb" target="_blank">https://github.com/lablivre-unb</a>
        <p>Repositórios do laboratório</p>
      </div>
      <div class="link-card">
        <h3>GitLab</h3>
        <a href="https://gitlab.com/lappis-unb" target="_blank">gitlab.com/lappis-unb</a>
        <p>Projetos do laboratório</p>
      </div>
      <div class="link-card">
        <h3>BOSS</h3>
        <a href="https://github.com/BOSS-BigOpenSourceSibling/" target="_blank">Big Open Source Siblings</a>
        <p>Programa de mentoria</p>
      </div>
      <div class="link-card">
        <h3>Google Scholar</h3>
        <a href="https://scholar.google.com/citations?user=_y8XHnAAAAAJ&hl=en" target="_blank">CarlaRocha</a>
        <p>Publicações acadêmicas</p>
      </div>
      <div class="link-card">
        <h3>IME-USP</h3>
        <a href="http://dgp.cnpq.br/dgp/espelhogrupo/633486" target="_blank">Grupo de Pesquisa</a>
        <p>Sistemas de Software e Dados</p>
      </div>
    </div>

    <div class="contact-card" style="margin-top: 2rem;">
      <a href="mailto:caguiar@unb.br">caguiar@unb.br</a>
    </div>
  </div></div>
</section>

</div>



