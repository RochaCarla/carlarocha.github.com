---
layout: single
author_profile: false
title: Projetos de Pesquisa
permalink: /projects/
header:
  overlay_color: "#5e72e4"
  overlay_filter: "0.5"
  overlay_image: /assets/images/projects-header.jpg
  actions:
    - label: "Ver Lattes"
      url: "http://lattes.cnpq.br/2831991076751452"
      class: "btn btn--light-outline btn--large"
excerpt: "Pesquisa aplicada em desenvolvimento de software livre e ciência de dados"
---

<style>
.projects-intro {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2rem;
  border-radius: 12px;
  margin-bottom: 2rem;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.projects-intro h2 {
  color: white;
  margin-bottom: 1rem;
  font-size: 1.8rem;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.project-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  transition: all 0.3s ease;
  border: 1px solid #e9ecef;
  position: relative;
  overflow: hidden;
}

.project-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #667eea, #764ba2);
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}

.project-card h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
  font-size: 1.3rem;
  font-weight: 600;
}

.project-card p {
  color: #6c757d;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.project-status {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
  margin-bottom: 1rem;
}

.status-active {
  background: #d4edda;
  color: #155724;
}

.status-completed {
  background: #cce5ff;
  color: #004085;
}

.project-links {
  margin-top: 1rem;
}

.project-links a {
  display: inline-block;
  margin-right: 0.5rem;
  margin-bottom: 0.5rem;
  padding: 0.4rem 1rem;
  background: #f8f9fa;
  color: #495057;
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.85rem;
  transition: all 0.2s ease;
}

.project-links a:hover {
  background: #667eea;
  color: white;
  text-decoration: none;
}

.stats-section {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 12px;
  margin: 2rem 0;
  text-align: center;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.stat-item {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.stat-number {
  font-size: 2rem;
  font-weight: bold;
  color: #667eea;
  display: block;
}

.stat-label {
  color: #6c757d;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

@media (max-width: 768px) {
  .projects-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .projects-intro {
    padding: 1.5rem;
  }
  
  .projects-intro h2 {
    font-size: 1.5rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .stat-item {
    padding: 1rem;
  }
  
  .stat-number {
    font-size: 1.5rem;
  }
}

@media (max-width: 480px) {
  .project-card {
    padding: 1rem;
  }
  
  .stats-section {
    padding: 1.5rem;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="projects-intro">
  <h2>🔬 Sobre Minha Pesquisa</h2>
  <p>Faço parte de diversos projetos de pesquisa, tanto com grupos de pesquisa quanto com departamentos de Pesquisa e Desenvolvimento (P&D) de empresas. Participo do grupo de pesquisa com <a href="http://dgp.cnpq.br/dgp/espelhogrupo/633486" style="color: #fff; text-decoration: underline;">IME-USP</a> "Sistemas de Software, Ciência e Engenharia de Dados e Computação de Alto Desempenho".</p>
  
  <p>Atuo como uma das coordenadoras do laboratório de pesquisa aplicada <a href="https://www.lappis.rocks" style="color: #fff; text-decoration: underline;">LAPPIS</a>, onde tenho a oportunidade de liderar várias iniciativas de pesquisa aplicada em colaboração com agências governamentais e empresas privadas.</p>
</div>

<div class="stats-section">
  <h3>📊 Impacto da Pesquisa</h3>
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
  </div>
</div>

## 🚀 Projetos Principais

<div class="projects-grid">
  
  <div class="project-card">
    <div class="project-status status-active">Ativo</div>
    <h3>LAPPIS - Laboratório de Pesquisa Aplicada</h3>
    <p>Coordenação de laboratório focado em pesquisa aplicada em desenvolvimento de software livre, com colaborações entre universidade, governo e empresas privadas.</p>
    <div class="project-links">
      <a href="https://www.lappis.rocks">🌐 Website</a>
      <a href="https://github.com/lappis-unb">📦 GitHub</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-status status-active">Ativo</div>
    <h3>Sistemas de Software e Ciência de Dados</h3>
    <p>Participação no grupo de pesquisa IME-USP focado em sistemas de software, engenharia de dados e computação de alto desempenho.</p>
    <div class="project-links">
      <a href="http://dgp.cnpq.br/dgp/espelhogrupo/633486">🔗 CNPq</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-status status-active">Ativo</div>
    <h3>Projetos de P&D Empresarial</h3>
    <p>Colaboração com departamentos de Pesquisa e Desenvolvimento de empresas em projetos de inovação tecnológica e desenvolvimento de software.</p>
    <div class="project-links">
      <a href="#">📋 Detalhes</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-status status-active">Ativo</div>
    <h3>Iniciativas Governamentais</h3>
    <p>Liderança de projetos de pesquisa aplicada em colaboração com agências governamentais, focando em soluções de software livre para o setor público.</p>
    <div class="project-links">
      <a href="#">🏛️ Projetos</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-status status-active">Ativo</div>
    <h3>Supervisão de Bolsistas</h3>
    <p>Orientação e supervisão de mais de 70 bolsas de pesquisa, contribuindo para a formação de novos pesquisadores na área de engenharia de software.</p>
    <div class="project-links">
      <a href="#">👥 Equipe</a>
    </div>
  </div>

  <div class="project-card">
    <div class="project-status status-completed">Concluído</div>
    <h3>Projetos de Software Livre</h3>
    <p>Desenvolvimento e contribuição para diversos projetos de software livre, promovendo a colaboração aberta e o compartilhamento de conhecimento.</p>
    <div class="project-links">
      <a href="#">💻 Repositórios</a>
    </div>
  </div>

</div>

---

## 📚 Mais Informações

Para detalhes completos sobre publicações, projetos e colaborações, consulte meu **[Currículo Lattes](http://lattes.cnpq.br/2831991076751452)**.

*A maioria dos projetos de pesquisa aplicada em que estou engajada está focada no desenvolvimento de software, sendo distribuído como Software Livre.*
