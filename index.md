---
layout: single
title: false
author_profile: false
permalink: /
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
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
/* Modern CSS Variables */
:root {
  --primary-color: #667eea;
  --secondary-color: #764ba2;
  --accent-color: #f093fb;
  --text-dark: #2c3e50;
  --text-light: #6c757d;
  --bg-light: #f8f9fa;
  --shadow: 0 10px 30px rgba(0,0,0,0.1);
  --shadow-hover: 0 20px 40px rgba(0,0,0,0.15);
}

/* Hero Section */
.hero-section {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 50%, var(--accent-color) 100%);
  color: white;
  padding: 4rem 2rem;
  border-radius: 20px;
  margin: -2rem -1rem 3rem -1rem;
  position: relative;
  overflow: hidden;
  box-shadow: var(--shadow);
}

.hero-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="50" cy="50" r="1" fill="%23ffffff" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
  animation: float 20s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-10px) rotate(1deg); }
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  background: linear-gradient(45deg, #fff, #f0f8ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
  from { text-shadow: 0 0 10px rgba(255,255,255,0.5); }
  to { text-shadow: 0 0 20px rgba(255,255,255,0.8), 0 0 30px rgba(255,255,255,0.4); }
}

.hero-subtitle {
  font-size: 1.3rem;
  margin-bottom: 2rem;
  opacity: 0.9;
  line-height: 1.6;
}

.hero-cta {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.cta-button {
  padding: 1rem 2rem;
  border: none;
  border-radius: 50px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.cta-primary {
  background: rgba(255,255,255,0.2);
  color: white;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.3);
}

.cta-primary:hover {
  background: rgba(255,255,255,0.3);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}

/* Feature Cards */
.features-section {
  margin: 4rem 0;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: var(--shadow);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  border: 1px solid #e9ecef;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
}

.feature-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: var(--shadow-hover);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  display: block;
}

.feature-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 1rem;
}

.feature-description {
  color: var(--text-light);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.feature-link {
  color: var(--primary-color);
  text-decoration: none;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}

.feature-link:hover {
  color: var(--secondary-color);
  transform: translateX(5px);
}

/* Stats Section */
.stats-section {
  background: linear-gradient(135deg, var(--bg-light) 0%, #e9ecef 100%);
  padding: 3rem 2rem;
  border-radius: 16px;
  margin: 3rem 0;
  text-align: center;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.stat-item {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  transition: all 0.3s ease;
}

.stat-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}

.stat-number {
  font-size: 2.5rem;
  font-weight: bold;
  background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  display: block;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: var(--text-light);
  font-weight: 500;
}

/* Partners Section */
.partners-section {
  margin: 4rem 0;
  text-align: center;
}

.partners-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
  align-items: center;
}

.partner-logo {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
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

/* Contact Section */
.contact-section {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
  color: white;
  padding: 3rem 2rem;
  border-radius: 16px;
  text-align: center;
  margin: 3rem 0;
}

.contact-section h3 {
  color: white;
  margin-bottom: 1rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-section {
    padding: 3rem 1.5rem;
    margin: -1rem -0.5rem 2rem -0.5rem;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-subtitle {
    font-size: 1.1rem;
  }
  
  .hero-cta {
    flex-direction: column;
    align-items: center;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
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
    padding: 1.5rem;
  }
}
</style>

<div class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">Bem-vindas e Bem-vindos! 👋</h1>
    <p class="hero-subtitle">
      Professora na <strong>Faculdade de Engenharia de Software (UnB)</strong> e coordenadora do laboratório <strong>LAPPIS</strong>. 
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
  <h2 style="text-align: center; margin-bottom: 3rem; color: var(--text-dark);">🚀 Áreas de Atuação</h2>
  
  <div class="features-grid">
    <div class="feature-card">
      <span class="feature-icon">🔬</span>
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
      <span class="feature-icon">🤖</span>
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
      <span class="feature-icon">💻</span>
      <h3 class="feature-title">Software Livre</h3>
      <p class="feature-description">
        Todo o software desenvolvido no laboratório é software livre. 
        Promovemos colaboração aberta e compartilhamento de conhecimento.
      </p>
      <a href="https://www.lappis.rocks" class="feature-link">
        LAPPIS →
      </a>
    </div>
    
    <div class="feature-card">
      <span class="feature-icon">🎓</span>
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
  <h3>📊 Impacto e Números</h3>
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
  <h3 style="color: var(--text-dark); margin-bottom: 2rem;">🤝 Parcerias e Reconhecimentos</h3>
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
      <img src="/images/logo-lappis.png" alt="LAPPIS" />
    </div>
    <div class="partner-logo">
      <img src="/images/unb.png" alt="UnB" />
    </div>
  </div>
</section>

<section class="contact-section">
  <h3>💬 Vamos Colaborar?</h3>
  <p style="margin-bottom: 2rem; font-size: 1.1rem; opacity: 0.9;">
    Se você busca orientação acadêmica, tem interesses semelhantes ou procura colaborações 
    em projetos inovadores, estou aberta a novas parcerias!
  </p>
  <a href="mailto:caguiar@unb.br" class="cta-button cta-primary" style="background: rgba(255,255,255,0.2); color: white;">
    📧 caguiar@unb.br
  </a>
</section>
