---
layout: single
title: false
author_profile: false
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
/* Academic Color Palette */
:root {
  --unb-blue: #1e3a5f;
  --unb-green: #2d5a3d;
  --primary-color: #1e3a5f;
  --secondary-color: #2d5a3d;
  --accent-color: #34495e;
  --text-dark: #2c3e50;
  --text-medium: #34495e;
  --text-light: #7f8c8d;
  --bg-light: #fafbfc;
  --bg-white: #ffffff;
  --border-light: #e1e8ed;
  --shadow-subtle: 0 2px 8px rgba(0,0,0,0.06);
  --shadow-medium: 0 4px 16px rgba(0,0,0,0.08);
  --shadow-hover: 0 8px 24px rgba(0,0,0,0.12);
}

/* Container for wider content */
.wide-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* Academic Hero Section */
.hero-section {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--accent-color) 100%);
  color: white;
  padding: 3rem 2rem;
  border-radius: 0;
  margin: -2rem -1rem 2rem -1rem;
  position: relative;
  border-bottom: 4px solid var(--unb-green);
  box-shadow: var(--shadow-medium);
}

.hero-section::after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 60px;
  height: 100%;
  background: var(--unb-green);
  opacity: 0.1;
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 1200px;
  margin: 0 auto;
  text-align: left;
}

.hero-title {
  font-size: 2.4rem;
  font-weight: 300;
  margin-bottom: 1.5rem;
  color: white;
  line-height: 1.3;
  letter-spacing: -0.01em;
  font-family: 'Georgia', 'Times New Roman', serif;
}

.hero-subtitle {
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
  opacity: 0.9;
  line-height: 1.6;
  font-weight: 300;
  max-width: 700px;
}

.hero-cta {
  display: flex;
  gap: 1rem;
  justify-content: flex-start;
  flex-wrap: wrap;
  margin-top: 1.5rem;
}

.cta-button {
  padding: 0.75rem 1.5rem;
  border: 1px solid rgba(255,255,255,0.3);
  border-radius: 2px;
  font-weight: 400;
  text-decoration: none;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
  letter-spacing: 0.3px;
}

.cta-primary {
  background: rgba(255,255,255,0.15);
  color: white;
  backdrop-filter: blur(10px);
  border-color: rgba(255,255,255,0.4);
}

.cta-primary:hover {
  background: rgba(255,255,255,0.25);
  border-color: rgba(255,255,255,0.7);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* Academic Feature Cards */
.features-section {
  margin: 2rem 0;
  padding: 0;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin: 1.5rem 0;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
  padding: 0 2rem;
}

.feature-card {
  background: var(--bg-white);
  padding: 2rem;
  border-radius: 2px;
  box-shadow: var(--shadow-subtle);
  transition: all 0.2s ease;
  position: relative;
  border: 1px solid var(--border-light);
  border-top: 3px solid var(--primary-color);
}

.feature-card:nth-child(even) {
  border-top-color: var(--unb-green);
}

.feature-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
}

.feature-icon {
  display: none;
}

.feature-title {
  font-size: 1.2rem;
  font-weight: 500;
  color: var(--text-dark);
  margin-bottom: 1rem;
  font-family: 'Georgia', 'Times New Roman', serif;
}

.feature-description {
  color: var(--text-medium);
  line-height: 1.6;
  margin-bottom: 1rem;
  font-size: 0.95rem;
}

.feature-link {
  color: var(--primary-color);
  text-decoration: none;
  font-weight: 400;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  transition: all 0.2s ease;
  font-size: 0.9rem;
  border-bottom: 1px solid transparent;
}

.feature-link:hover {
  color: var(--unb-green);
  border-bottom-color: var(--unb-green);
}

/* Academic Stats Section */
.stats-section {
  background: var(--bg-light);
  padding: 2rem 2rem;
  border-radius: 2px;
  margin: 2rem 0;
  text-align: center;
  border: 1px solid var(--border-light);
  position: relative;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.stats-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--primary-color) 0%, var(--unb-green) 100%);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.stat-item {
  background: var(--bg-white);
  padding: 2rem 1.5rem;
  border-radius: 2px;
  box-shadow: var(--shadow-subtle);
  transition: all 0.2s ease;
  border: 1px solid var(--border-light);
}

.stat-item:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-medium);
}

.stat-number {
  font-size: 2.2rem;
  font-weight: 300;
  color: var(--primary-color);
  display: block;
  margin-bottom: 0.5rem;
  font-family: 'Georgia', 'Times New Roman', serif;
}

.stat-item:nth-child(even) .stat-number {
  color: var(--unb-green);
}

.stat-label {
  color: var(--text-medium);
  font-weight: 400;
  font-size: 0.9rem;
}

/* Academic Partners Section */
.partners-section {
  margin: 2rem 0;
  text-align: center;
  padding: 0;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.partners-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
  align-items: center;
  padding: 0 2rem;
}

.partner-logo {
  background: var(--bg-white);
  padding: 1.5rem;
  border-radius: 2px;
  box-shadow: var(--shadow-subtle);
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--border-light);
}

.partner-logo:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-medium);
}

.partner-logo img {
  max-width: 100%;
  max-height: 70px;
  object-fit: contain;
  filter: grayscale(20%);
  transition: filter 0.2s ease;
}

.partner-logo:hover img {
  filter: grayscale(0%);
}

/* Academic Contact Section */
.contact-section {
  background: linear-gradient(135deg, var(--unb-green) 0%, var(--primary-color) 100%);
  color: white;
  padding: 2.5rem 2rem;
  border-radius: 2px;
  text-align: center;
  margin: 2rem 0;
  position: relative;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.contact-section h3 {
  color: white;
  margin-bottom: 1.5rem;
  font-family: 'Georgia', 'Times New Roman', serif;
  font-weight: 400;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-section {
    padding: 2rem 1.5rem;
    margin: -1rem -0.5rem 1.5rem -0.5rem;
  }
  
  .hero-content {
    text-align: center;
  }
  
  .hero-title {
    font-size: 2.2rem;
  }
  
  .hero-subtitle {
    font-size: 1.1rem;
  }
  
  .hero-cta {
    justify-content: center;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 0.8rem;
  }
  
  .partners-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 2rem;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .feature-card, .stat-item {
    padding: 1rem;
  }
}
</style>

<div class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">Bem-vindas e Bem-vindos!</h1>
    <p class="hero-subtitle">
      Professora na <strong>Faculdade de Engenharia de Software (UnB)</strong> e coordenadora do laboratório <strong>Lab Livre</strong>. 
      Especialista em desenvolvimento ágil, DevOps, aspectos humanos do software e machine learning.
    </p>
    <div class="hero-cta">
      <a href="mailto:caguiar@unb.br" class="cta-button cta-primary">
        Entre em Contato
      </a>
      <a href="/projects/" class="cta-button cta-primary">
        Ver Projetos
      </a>
    </div>
  </div>
</div>

<section class="features-section">
  <div style="max-width: 1200px; margin: 0 auto; padding: 0 2rem;">
    <h2 style="text-align: center; margin-bottom: 1.5rem; color: var(--primary-color); font-weight: 400; font-size: 1.8rem; font-family: 'Georgia', 'Times New Roman', serif;">Áreas de Atuação</h2>
  </div>
  
  <div class="features-grid">
    <div class="feature-card">
      <h3 class="feature-title">Pesquisa Aplicada</h3>
      <p class="feature-description">
        Coordeno diversos projetos de pesquisa aplicada em práticas de desenvolvimento de software ágil, 
        DevOps e aspectos humanos do desenvolvimento.
      </p>
      <a href="/projects/" class="feature-link">
        Ver Projetos →
      </a>
    </div>
    
    <div class="feature-card">
      <h3 class="feature-title">Machine Learning</h3>
      <p class="feature-description">
        Desenvolvimento de produtos de machine learning e pesquisa em ciência de dados 
        aplicada a sistemas de software.
      </p>
      <a href="https://dgp.cnpq.br/dgp/espelhogrupo/633486" class="feature-link">
        Grupo IME-USP →
      </a>
    </div>
    
    <div class="feature-card">
      <h3 class="feature-title">Software Livre</h3>
      <p class="feature-description">
        Todo o software desenvolvido no laboratório é software livre. 
        Promovemos colaboração aberta e compartilhamento de conhecimento.
      </p>
      <a href="https://www.lappis.rocks" class="feature-link">
        Lab Livre →
      </a>
    </div>
    
    <div class="feature-card">
      <h3 class="feature-title">Orientação Acadêmica</h3>
      <p class="feature-description">
        Supervisiono bolsas de pesquisa e participo do mestrado acadêmico PPCA. 
        Aberta a novas parcerias e colaborações.
      </p>
      <a href="http://PPCA.unb.br" class="feature-link">
        PPCA →
      </a>
    </div>
  </div>
</section>

<section class="stats-section">
  <h3 style="color: var(--primary-color); font-weight: 400; font-family: 'Georgia', 'Times New Roman', serif;">Impacto e Números</h3>
  <div class="stats-grid">
    <div class="stat-item">
      <span class="stat-number">70+</span>
      <div class="stat-label">Bolsas Supervisionadas</div>
    </div>
    <div class="stat-item">
      <span class="stat-number">15+</span>
      <div class="stat-label">Projetos Ativos</div>
    </div>
    <div class="stat-item">
      <span class="stat-number">100%</span>
      <div class="stat-label">Software Livre</div>
    </div>
    <div class="stat-item">
      <span class="stat-number">2024</span>
      <div class="stat-label">Google Summer of Code</div>
    </div>
  </div>
</section>

<section class="partners-section">
  <div style="padding: 0 2rem;">
    <h3 style="color: var(--primary-color); margin-bottom: 1.5rem; font-weight: 400; font-family: 'Georgia', 'Times New Roman', serif;">Parcerias e Reconhecimentos</h3>
  </div>
  <div class="partners-grid">
    <div class="partner-logo">
      <img src="/images/gsoc.png" alt="Google Summer of Code" />
    </div>
    <div class="partner-logo">
      <img src="/images/BrasilParticipativo.png" alt="Brasil Participativo" />
    </div>
    <div class="partner-logo">
      <img src="/images/boss.png" alt="BOSS" />
    </div>
    <div class="partner-logo">
      <img src="/images/BadgesPhaseThreeWinner.png" alt="GNOME" />
    </div>
    <div class="partner-logo">
      <img src="/images/logo-lappis.png" alt="Lab Livre" />
    </div>
    <div class="partner-logo">
      <img src="/images/unb.png" alt="UnB" />
    </div>
    <div class="partner-logo">
      <a href="https://gov-hub.io/" target="_blank">
        <img src="/images/img-infos-gov.jpg" alt="GovHub" />
      </a>
    </div>
  </div>
</section>

<section class="contact-section">
  <h3 style="font-weight: 600;">Vamos Colaborar?</h3>
  <p style="margin-bottom: 2rem; font-size: 1.1rem; opacity: 0.9;">
    Se você busca orientação acadêmica, tem interesses semelhantes ou procura colaborações 
    em projetos inovadores, estou aberta a novas parcerias!
  </p>
  <a href="mailto:caguiar@unb.br" class="cta-button cta-primary" style="background: rgba(255,255,255,0.25); color: white; border-color: rgba(255,255,255,0.5);">
    📧 caguiar@unb.br
  </a>
</section>
