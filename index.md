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
    - label: "📧 Contato"
      url: "mailto:caguiar@unb.br"
      class: "btn btn--primary btn--large"
    - label: "🔬 Projetos"
      url: "/projects/"
      class: "btn btn--light-outline btn--large"
---

<style>
/* UnB Official Colors CSS Variables */
:root {
  --unb-blue: #003366;
  --unb-green: #006633;
  --primary-color: #003366;
  --secondary-color: #006633;
  --accent-color: #004d99;
  --text-dark: #2c3e50;
  --text-light: #6c757d;
  --bg-light: #f8f9fa;
  --shadow: 0 10px 30px rgba(0,0,0,0.1);
  --shadow-hover: 0 20px 40px rgba(0,0,0,0.15);
}

/* Formal Hero Section with Highlighted Photo */
.hero-section {
  background: linear-gradient(rgba(0,51,102,0.85), rgba(0,51,102,0.85)), url('/images/lab.png');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  color: white;
  padding: 3rem 2rem;
  border-radius: 0;
  margin: -2rem -1rem 2rem -1rem;
  position: relative;
  border-left: 6px solid var(--unb-green);
  box-shadow: 0 4px 20px rgba(0,51,102,0.15);
}

.hero-section::after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 100px;
  height: 100%;
  background: var(--unb-green);
  opacity: 0.15;
  clip-path: polygon(0 0, 100% 0, 80% 100%, 0% 100%);
}

.hero-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at 70% 30%, transparent 30%, rgba(0,51,102,0.3) 70%);
  pointer-events: none;
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 800px;
  margin: 0 auto;
  text-align: left;
}

.hero-title {
  font-size: 2.8rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  color: white;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.hero-subtitle {
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  opacity: 0.95;
  line-height: 1.5;
  font-weight: 400;
}

.hero-cta {
  display: flex;
  gap: 1rem;
  justify-content: flex-start;
  flex-wrap: wrap;
  margin-top: 1.5rem;
}

.cta-button {
  padding: 0.8rem 1.8rem;
  border: 2px solid white;
  border-radius: 4px;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.95rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.cta-primary {
  background: transparent;
  color: white;
}

.cta-primary:hover {
  background: white;
  color: var(--unb-blue);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(255,255,255,0.2);
}

/* Feature Cards */
.features-section {
  margin: 2.5rem 0;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.feature-card {
  background: white;
  padding: 1.5rem;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0,51,102,0.08);
  transition: all 0.3s ease;
  position: relative;
  border: 1px solid #e9ecef;
  border-left: 4px solid var(--unb-blue);
}

.feature-card:nth-child(even) {
  border-left-color: var(--unb-green);
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0,51,102,0.12);
  border-left-width: 6px;
}

.feature-icon {
  display: none;
}

.feature-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 0.8rem;
}

.feature-description {
  color: var(--text-light);
  line-height: 1.5;
  margin-bottom: 1rem;
}

.feature-link {
  color: var(--unb-blue);
  text-decoration: none;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}

.feature-link:hover {
  color: var(--unb-green);
  transform: translateX(5px);
}

/* Stats Section */
.stats-section {
  background: var(--bg-light);
  padding: 2rem;
  border-radius: 4px;
  margin: 2rem 0;
  text-align: center;
  border: 1px solid #dee2e6;
  position: relative;
}

.stats-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--unb-blue);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.stat-item {
  background: white;
  padding: 1.5rem;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: all 0.3s ease;
}

.stat-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--unb-blue);
  display: block;
  margin-bottom: 0.5rem;
}

.stat-item:nth-child(even) .stat-number {
  color: var(--unb-green);
}

.stat-label {
  color: var(--text-light);
  font-weight: 500;
}

/* Partners Section */
.partners-section {
  margin: 2.5rem 0;
  text-align: center;
}

.partners-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
  align-items: center;
}

.partner-logo {
  background: white;
  padding: 1rem;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.partner-logo:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}

.partner-logo img {
  max-width: 100%;
  max-height: 80px;
  object-fit: contain;
}

/* Formal Contact Section */
.contact-section {
  background: var(--unb-green);
  color: white;
  padding: 2.5rem 2rem;
  border-radius: 4px;
  text-align: center;
  margin: 2rem 0;
  position: relative;
}

.contact-section::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 80px;
  height: 100%;
  background: var(--unb-blue);
  opacity: 0.15;
  clip-path: polygon(20% 0%, 100% 0%, 100% 100%, 0% 100%);
}

.contact-section h3 {
  color: white;
  margin-bottom: 1rem;
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
    <h1 class="hero-title">Bem-vindas e Bem-vindos! 👋</h1>
    <p class="hero-subtitle">
      Professora na <strong>Faculdade de Engenharia de Software (UnB)</strong> e coordenadora do laboratório <strong>Lab Livre</strong>. 
      Especialista em desenvolvimento ágil, DevOps, aspectos humanos do software e machine learning.
    </p>
    <div class="hero-cta">
      <a href="mailto:caguiar@unb.br" class="cta-button cta-primary">
        📧 Entre em Contato
      </a>
      <a href="/projects/" class="cta-button cta-primary">
        🔬 Ver Projetos
      </a>
    </div>
  </div>
</div>

<section class="features-section">
  <h2 style="text-align: center; margin-bottom: 2rem; color: var(--unb-blue); font-weight: 600; font-size: 1.8rem;">Áreas de Atuação</h2>
  
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
  <h3 style="color: var(--unb-blue); font-weight: 600;">Impacto e Números</h3>
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
  <h3 style="color: var(--unb-blue); margin-bottom: 2rem; font-weight: 600;">Parcerias e Reconhecimentos</h3>
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
  </div>
</section>

<section class="contact-section">
  <h3 style="font-weight: 600;">Vamos Colaborar?</h3>
  <p style="margin-bottom: 2rem; font-size: 1.1rem; opacity: 0.9;">
    Se você busca orientação acadêmica, tem interesses semelhantes ou procura colaborações 
    em projetos inovadores, estou aberta a novas parcerias!
  </p>
  <a href="mailto:caguiar@unb.br" class="cta-button cta-primary" style="background: rgba(255,255,255,0.2); color: white;">
    📧 caguiar@unb.br
  </a>
</section>
