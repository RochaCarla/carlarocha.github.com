---
layout: homepage
title: Publicações
permalink: /publications/
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

.pub-wrapper {
  font-family: var(--font-body);
  background: var(--background);
  color: var(--foreground);
  line-height: 1.6;
  margin: -2rem;
}

.pub-wrapper h1, .pub-wrapper h2, .pub-wrapper h3 {
  font-family: var(--font-body);
  font-weight: 700;
  line-height: 1.2;
  color: var(--foreground);
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }
.max-w-6xl { max-width: 72rem; margin: 0 auto; }

/* Hero Section */
.hero-pub {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  padding: 4rem 0;
  text-align: center;
  border-bottom: 1px solid var(--border);
}

.hero-pub h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--foreground);
}

.hero-pub p {
  font-size: 1.125rem;
  color: var(--text-secondary);
  max-width: 600px;
  margin: 0 auto 2rem auto;
}

/* Stats Grid */
.stats-grid {
  display: flex;
  justify-content: center;
  gap: 3rem;
  margin-top: 2rem;
}

.stat-item {
  text-align: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--primary);
  display: block;
}

.stat-label {
  font-size: 0.9rem;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.1em;
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

/* External Links */
.external-links {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: 2rem;
}

.external-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--primary);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
}

.external-link:hover {
  background: var(--primary-dark);
  color: white;
}

/* Publication Cards */
.pub-grid {
  display: grid;
  gap: 1.5rem;
}

.pub-card {
  background: #ffffff;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
  position: relative;
}

.pub-card:hover {
  box-shadow: 0 8px 24px rgba(0, 102, 204, 0.1);
}

.pub-card.highlight {
  border-left: 4px solid var(--primary);
}

.pub-card .badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: var(--primary);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.pub-card .year {
  color: var(--primary);
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.pub-card .title {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--foreground);
  margin-bottom: 0.5rem;
  line-height: 1.4;
}

.pub-card .authors {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.pub-card .venue {
  color: var(--text-secondary);
  font-size: 0.85rem;
  font-style: italic;
  margin-bottom: 0.75rem;
}

.pub-card .citations {
  display: inline-block;
  background: var(--card-bg);
  color: var(--primary);
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.8rem;
  font-weight: 600;
}

/* Year Section */
.year-group {
  margin-bottom: 3rem;
}

.year-title {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.year-title h3 {
  font-size: 1.5rem;
  color: var(--foreground);
  margin: 0;
}

.year-title .count {
  background: var(--primary);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.8rem;
  font-weight: 600;
}

/* Info Section */
.info-text {
  color: var(--text-secondary);
  font-size: 1rem;
  line-height: 1.7;
  max-width: 800px;
}

.info-text a {
  color: var(--primary);
  text-decoration: none;
}

.info-text a:hover {
  text-decoration: underline;
}

/* Responsive */
@media (max-width: 768px) {
  .hero-pub h1 { font-size: 2rem; }
  .stats-grid { flex-direction: column; gap: 1.5rem; }
  .stat-number { font-size: 2rem; }
  .external-links { flex-direction: column; align-items: center; }
  .section { padding: 3rem 0; }
}
</style>

<div class="pub-wrapper">

<section class="hero-pub">
  <div class="container">
    <h1>Publicações Científicas</h1>
    <p>Produção acadêmica em Engenharia de Software, DevOps, MLOps e Software Livre</p>
    <div class="stats-grid">
      <div class="stat-item">
        <span class="stat-number">955</span>
        <span class="stat-label">Citações</span>
      </div>
      <div class="stat-item">
        <span class="stat-number">10</span>
        <span class="stat-label">Índice h</span>
      </div>
      <div class="stat-item">
        <span class="stat-number">10</span>
        <span class="stat-label">Índice i10</span>
      </div>
    </div>
    <div class="external-links">
      <a href="https://scholar.google.com/citations?user=_y8XHnAAAAAJ&hl=pt-BR" class="external-link" target="_blank">📊 Google Scholar</a>
      <a href="http://lattes.cnpq.br/2831991076751452" class="external-link" target="_blank">📋 Currículo Lattes</a>
      <a href="https://books.apple.com/us/author/carla-rocha/id522601238" class="external-link" target="_blank">📚 Apple Books</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Sobre</span></div>
    <div class="info-text">
      <p>Sou membro ativo do grupo de pesquisa em <a href="http://dgp.cnpq.br/dgp/espelhogrupo/633486" target="_blank">Sistemas de Software, Ciência e Engenharia de Dados e Computação de Alto Desempenho</a> vinculado ao Instituto de Matemática e Estatística da Universidade de São Paulo (IME-USP).</p>
      <p>Atualmente participo do programa de mestrado profissionalizante <a href="https://ppca.unb.br" target="_blank">PPCA</a> na Universidade de Brasília (UnB). Além disso, atuo como coordenadora do laboratório de pesquisa aplicada <a href="https://lablivre.unb.br/" target="_blank">Lab Livre</a>, um espaço de referência na UnB para estudos e pesquisas em áreas tecnológicas de vanguarda.</p>
    </div>
  </div></div>
</section>

<section class="section" style="background: #f8f9fa;">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Destaques</span></div>
    <h2 class="section-title">Publicações de Alto Impacto</h2>
    <div class="pub-grid">
      <div class="pub-card highlight">
        <span class="badge">743 citações</span>
        <div class="year">2019 • ACM Computing Surveys</div>
        <div class="title">A survey of DevOps concepts and challenges</div>
        <div class="authors">L Leite, C Rocha, F Kon, D Milojicic, P Meirelles</div>
        <div class="venue">ACM Computing Surveys (CSUR) 52 (6), 1-35</div>
      </div>
      <div class="pub-card highlight">
        <span class="badge">33 citações</span>
        <div class="year">2019 • OpenSym</div>
        <div class="title">FLOSS FAQ chatbot project reuse: how to allow nonexperts to develop a chatbot</div>
        <div class="authors">ART de Lacerda, CSR Aguiar</div>
        <div class="venue">Proceedings of the 15th International Symposium on Open Collaboration</div>
      </div>
      <div class="pub-card highlight">
        <span class="badge">29 citações</span>
        <div class="year">2021 • ICSE-SEET</div>
        <div class="title">Qualifying software engineers undergraduates in DevOps</div>
        <div class="authors">I Alves, C Rocha</div>
        <div class="venue">IEEE/ACM 43rd International Conference on Software Engineering</div>
      </div>
    </div>
  </div></div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Produção</span></div>
    <h2 class="section-title">Lista Completa de Publicações</h2>
    
    <div class="year-group">
      <div class="year-title"><h3>2025</h3><span class="count">4</span></div>
      <div class="pub-grid">
        <div class="pub-card">
          <div class="year">Revista do Serviço Público (ENAP)</div>
          <div class="title"><a href="https://revista.enap.gov.br/index.php/RSP/article/view/10305" target="_blank">Colaboração multissetorial para desenvolvimento e manutenção de soluções tecnológicas de participação</a></div>
          <div class="authors">CSR Aguiar, I Alves, L Gomes, B Pinos, L Bellix, H Parra</div>
          <span class="citations">Novo</span>
        </div>
        <div class="pub-card">
          <div class="year">Conference Paper</div>
          <div class="title">From Pre-labeling to Production: Engineering Lessons from a Machine Learning Pipeline in the Public Sector</div>
          <div class="authors">C Rocha et al.</div>
          <span class="citations">Novo</span>
        </div>
        <div class="pub-card">
          <div class="year">Conference Paper</div>
          <div class="title">Semantic Clustering of Civic Proposals: A Case Study on Brazil's National Participation Platform</div>
          <div class="authors">C Rocha et al.</div>
          <span class="citations">1 citação</span>
        </div>
        <div class="pub-card">
          <div class="year">Technical Report</div>
          <div class="title">Plataforma de Integração de Sistemas Estruturantes da Execução Financeira Federal</div>
          <div class="authors">C Rocha et al.</div>
          <span class="citations">Novo</span>
        </div>
      </div>
    </div>

    <div class="year-group">
      <div class="year-title"><h3>2024</h3><span class="count">1</span></div>
      <div class="pub-grid">
        <div class="pub-card">
          <div class="year">Journal of Systems and Software</div>
          <div class="title">Harmonizing DevOps taxonomies—A grounded theory study</div>
          <div class="authors">J Díaz, J Pérez, I Alves, F Kon, L Leite, P Meirelles, C Rocha</div>
          <span class="citations">23 citações</span>
        </div>
      </div>
    </div>

    <div class="year-group">
      <div class="year-title"><h3>2023</h3><span class="count">5</span></div>
      <div class="pub-grid">
        <div class="pub-card">
          <div class="year">IEEE Transactions on Engineering Management</div>
          <div class="title">Practices for managing machine learning products: A multivocal literature review</div>
          <div class="authors">I Alves, LAF Leite, P Meirelles, F Kon, CSR Aguiar</div>
          <span class="citations">15 citações</span>
        </div>
        <div class="pub-card">
          <div class="year">IEEE Transactions on Engineering Management</div>
          <div class="title">When technical solutions are not enough: using software concepts to analyze challenges at delivery processes</div>
          <div class="authors">TP Vidigal, W Prodanov, CSR Aguiar</div>
          <span class="citations">1 citação</span>
        </div>
        <div class="pub-card">
          <div class="year">Conference Paper</div>
          <div class="title">Trans Perspective in Software Engineering</div>
          <div class="authors">M Joranhezon, FM Fleury, C Rocha</div>
          <span class="citations">2 citações</span>
        </div>
        <div class="pub-card">
          <div class="year">arXiv preprint</div>
          <div class="title">Harmonizing DevOps Taxonomies—Theory Operationalization and Testing</div>
          <div class="authors">I Alves, J Pérez, J Díaz, D López-Fernández, M Pais, F Kon, C Rocha</div>
          <span class="citations">2 citações</span>
        </div>
      </div>
    </div>

    <div class="year-group">
      <div class="year-title"><h3>2021</h3><span class="count">2</span></div>
      <div class="pub-grid">
        <div class="pub-card">
          <div class="year">ICSE-SEET</div>
          <div class="title">Qualifying software engineers undergraduates in DevOps—challenges of introducing technical and non-technical concepts</div>
          <div class="authors">I Alves, C Rocha</div>
          <span class="citations">29 citações</span>
        </div>
        <div class="pub-card">
          <div class="year">IFIP OSS Conference</div>
          <div class="title">OSS Scripting System for Game Development in Rust</div>
          <div class="authors">PDS da Silva, RO Campos, C Rocha</div>
          <span class="citations">3 citações</span>
        </div>
      </div>
    </div>

    <div class="year-group">
      <div class="year-title"><h3>2019</h3><span class="count">3</span></div>
      <div class="pub-grid">
        <div class="pub-card">
          <div class="year">ACM Computing Surveys</div>
          <div class="title">A survey of DevOps concepts and challenges</div>
          <div class="authors">L Leite, C Rocha, F Kon, D Milojicic, P Meirelles</div>
          <span class="citations">743 citações</span>
        </div>
        <div class="pub-card">
          <div class="year">OpenSym</div>
          <div class="title">FLOSS FAQ chatbot project reuse: how to allow nonexperts to develop a chatbot</div>
          <div class="authors">ART de Lacerda, CSR Aguiar</div>
          <span class="citations">33 citações</span>
        </div>
        <div class="pub-card">
          <div class="year">ICCSA</div>
          <div class="title">A students' perspective of native and cross-platform approaches for mobile application development</div>
          <div class="authors">P Meirelles, CSR Aguiar, F Assis, R Siqueira, A Goldman</div>
          <span class="citations">21 citações</span>
        </div>
      </div>
    </div>

    <div class="year-group">
      <div class="year-title"><h3>2016</h3><span class="count">2</span></div>
      <div class="pub-grid">
        <div class="pub-card">
          <div class="year">Universitas Psychologica</div>
          <div class="title">A influência da intensidade emocional no reconhecimento de emoções em faces por crianças brasileiras</div>
          <div class="authors">JS Rocha Aguiar, AI de Paiva Silva, CS Rocha Aguiar, N Torro-Alves, W Cristina de Souza</div>
          <span class="citations">16 citações</span>
        </div>
      </div>
    </div>

    <div class="year-group">
      <div class="year-title"><h3>2014-2015</h3><span class="count">3</span></div>
      <div class="pub-grid">
        <div class="pub-card">
          <div class="year">SPIE 2015</div>
          <div class="title">Development of simulation interfaces for evaluation task with physiological data and virtual reality</div>
          <div class="authors">MR Miranda, H Costa, L Oliveira, T Bernardes, C Aguiar, C Miosso, A Rocha</div>
          <span class="citations">3 citações</span>
        </div>
        <div class="pub-card">
          <div class="year">SPIE 2014</div>
          <div class="title">Embodiments, visualizations, and immersion with enactive affective systems</div>
          <div class="authors">D Domingues, CJ Miosso, SF Rodrigues, CSR Aguiar, TF Lucena, M Miranda, AF Rocha, R Raskar</div>
          <span class="citations">19 citações</span>
        </div>
      </div>
    </div>

    <div class="year-group">
      <div class="year-title"><h3>2007</h3><span class="count">3</span></div>
      <div class="pub-grid">
        <div class="pub-card">
          <div class="year">SBAI</div>
          <div class="title">Planejamento de trajetória para o robô omni utilizando o algoritmo mapa de rotas probabilístico</div>
          <div class="authors">BV Adôrno, CSR Aguiar, GA Borges</div>
          <span class="citations">10 citações</span>
        </div>
        <div class="pub-card">
          <div class="year">IEEE/RSJ IROS</div>
          <div class="title">3D datasets segmentation based on local attribute variation</div>
          <div class="authors">CSR Aguiar, S Druon, A Crosnier</div>
          <span class="citations">6 citações</span>
        </div>
        <div class="pub-card">
          <div class="year">CGIV</div>
          <div class="title">Hierarchical segmentation for unstructured and unfiltered range images</div>
          <div class="authors">CSR Aguiar, S Druon, A Crosnier</div>
          <span class="citations">2 citações</span>
        </div>
      </div>
    </div>

  </div></div>
</section>

</div>



