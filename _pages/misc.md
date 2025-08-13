---
layout: single
title: Participação
permalink: /misc/
author_profile: true
---

<style>
/* Misc Page Styling */
.page-header {
  background: linear-gradient(135deg, #003366 0%, #006633 100%);
  color: white;
  padding: 2.5rem 2rem;
  border-radius: 8px;
  margin-bottom: 2rem;
  text-align: center;
}

.page-header h1 {
  margin: 0 0 0.5rem 0;
  font-size: 2.2rem;
  font-weight: 600;
}

.page-header p {
  margin: 0;
  font-size: 1.1rem;
  opacity: 0.9;
}

.participation-section {
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 2rem;
  margin: 2rem 0;
  border-left: 6px solid #003366;
  transition: all 0.2s ease;
}

.participation-section:hover {
  border-left-color: #006633;
  box-shadow: 0 4px 12px rgba(0,102,51,0.1);
}

.participation-section h2 {
  color: #003366;
  margin-top: 0;
  font-size: 1.6rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.participation-section .icon {
  font-size: 1.8rem;
  color: #006633;
}

.participation-list {
  list-style: none;
  padding: 0;
  margin: 1rem 0;
  counter-reset: participation-counter;
}

.participation-item {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 6px;
  padding: 1.2rem;
  margin: 1rem 0;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
  counter-increment: participation-counter;
}

.participation-item::before {
  content: counter(participation-counter);
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 40px;
  background: #006633;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.1rem;
  transform: translateX(-40px);
  transition: transform 0.2s ease;
}

.participation-item:hover::before {
  transform: translateX(0);
}

.participation-item:hover {
  background: white;
  border-color: #006633;
  box-shadow: 0 2px 8px rgba(0,102,51,0.1);
  padding-left: 3rem;
}

.participation-item a {
  color: #003366;
  text-decoration: none;
  font-weight: 500;
}

.participation-item a:hover {
  color: #006633;
}

.highlight-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.highlight-card {
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.2s ease;
  border-top: 4px solid #003366;
}

.highlight-card:hover {
  border-top-color: #006633;
  box-shadow: 0 4px 12px rgba(0,102,51,0.1);
  transform: translateY(-2px);
}

.highlight-card .icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  display: block;
  color: #006633;
}

.highlight-card h3 {
  color: #003366;
  margin-bottom: 1rem;
  font-size: 1.3rem;
}

@media (max-width: 768px) {
  .page-header {
    padding: 2rem 1rem;
  }
  
  .page-header h1 {
    font-size: 1.8rem;
  }
  
  .participation-section {
    padding: 1.5rem;
  }
  
  .highlight-grid {
    grid-template-columns: 1fr;
  }
  
  .participation-item {
    padding: 1rem;
  }
  
  .participation-item:hover {
    padding-left: 2.5rem;
  }
}
</style>

<div class="page-header">
  <h1>Participação & Contribuições</h1>
  <p>Engajamento em comunidades, eventos e projetos de impacto</p>
</div>

<div class="highlight-grid">
  <div class="highlight-card">
    <span class="icon">🎯</span>
    <h3>Liderança</h3>
    <p>Co-fundadora BOSS e coordenação de eventos acadêmicos</p>
  </div>
  
  <div class="highlight-card">
    <span class="icon">🎤</span>
    <h3>Palestras</h3>
    <p>Apresentações em eventos nacionais e internacionais</p>
  </div>
  
  <div class="highlight-card">
    <span class="icon">🔓</span>
    <h3>Open Source</h3>
    <p>Desenvolvimento e manutenção de projetos de código aberto</p>
  </div>
</div>

<div class="participation-section">
  <h2><span class="icon">🏆</span>Principais Participações</h2>
  <ol class="participation-list">
    <li class="participation-item">
      Co-fundadora <a href="https://www.youtube.com/c/BigOpenSourceSibling" target="_blank">BOSS</a>
    </li>
    <li class="participation-item">
      Co-apresentadora <a href="https://youtube.com/playlist?list=PLFFHHqnY3q2FLjtGKYuI-V-z9u7jzBOb_" target="_blank">Talk Like a BOSS - rodas de conversas</a> pela Big Open Source Sibling (BOSS)
    </li>
    <li class="participation-item">
      Co-apresentadora <a href="https://youtu.be/zynynEynpk8" target="_blank">Mini Lab Livre Conf</a>
    </li>
    <li class="participation-item">
      Organizadora <a href="https://github.com/lappis-unb/MiniLappisConf" target="_blank">Mini Lab Livre Conf</a>
    </li>
    <li class="participation-item">
      Co-presidente do programa <a href="http://www.agilebrazil.com/2021/wbma" target="_blank">WBMA - Agile Brazil 2021</a>
    </li>
    <li class="participation-item">
      Coordenador de Publicidade <a href="http://www.agilebrazil.com/2019/docs/en/wbma/" target="_blank">WBMA - Agile Brazil 2019</a>
    </li>
    <li class="participation-item">
      Palestrante na <a href="https://youtu.be/MlGYHl3Iyyg" target="_blank">Campus Party 2020</a>
    </li>
    <li class="participation-item">
      Comitê científico <a href="https://covidas-unb.github.io/InfoGerais/" target="_blank">CoVidas UnB Hackathon 2020</a>
    </li>
    <li class="participation-item">
      Membro do Comitê de Gestão Estratégica de Campus Inteligente e Sustentável (CGECIS) da Universidade de Brasília
    </li>
    <li class="participation-item">
      Membro do Conselho Editorial da <a href="https://revistadarcy.unb.br" target="_blank">Revista Darcy</a>
    </li>
    <li class="participation-item">
      Já fui coordenadora do curso de Engenharia de Software na UnB
    </li>
  </ol>
</div>

<div class="participation-section">
  <h2><span class="icon">🎤</span>Apresentações</h2>
  <ul class="participation-list">
    <li class="participation-item">
      <a href="https://docs.google.com/presentation/d/1bAOZ0gLjEIwOLhkRhakvaXG1_FP4fGuHYMVhEc72w7M/edit?usp=sharing" target="_blank">Introdução à BOSS</a>
      <div class="author">Presentation Guadec 2021</div>
    </li>
    <li class="participation-item">
      <a href="https://docs.google.com/presentation/d/1c0bLbdfj8ztAvIQz3MNYSp0I6zjUhQDO4k3aqQianEU/edit?usp=sharing" target="_blank">Introdução a uma arquitetura de Chatbot Open Source</a>
      <div class="author">Apresentação Campus Party 2019</div>
    </li>
    <li class="participation-item">
      <a href="https://docs.google.com/presentation/d/1xFwBtiMU08lOgSGFG4s9QpUZF80Ei5HENvTPN1VffGs/edit?usp=sharing" target="_blank">Formando inovadores através de Open Source</a>
      <div class="author">Apresentação Campus Party 2020</div>
    </li>
  </ul>
</div>

<div class="participation-section">
  <h2><span class="icon">🔓</span>Software Livre</h2>
  
  <p>Nossos projetos de pesquisa seguem a prática do uso de licenças de software livre sempre que há necessidade de desenvolvimento. Todos os nossos projetos de software são disponibilizados na organização do laboratório no GitLab/GitHub (lappis-unb). Abaixo, estão alguns dos projetos desenvolvidos pelo nosso laboratório.</p>

  <div class="project-grid">
    <div class="project-card">
      <h3><a href="https://gitlab.com/lappis-unb/decidimbr" target="_blank">Brasil Participativo</a></h3>
      <p>Plataforma de participação social baseada no Decidim para engajamento cidadão.</p>
    </div>
    
    <div class="project-card">
      <h3><a href="https://github.com/lappis-unb/rasa-ptbr-boilerplate" target="_blank">Chatbot Boilerplate for Brazilian Portuguese</a></h3>
      <p>Arquitetura boilerplate de um produto chatbot utilizando o framework Rasa, configurado para a língua Portuguesa.</p>
    </div>
    
    <div class="project-card">
      <h3><a href="https://github.com/Escola-em-Casa" target="_blank">Escola em Casa</a></h3>
      <p>Concede acesso gratuito, através de dados patrocinados, aos recursos necessários para a realização do ensino à distância da Secretaria de Educação do Distrito Federal.</p>
    </div>
    
    <div class="project-card">
      <h3><a href="https://github.com/lappis-unb/realtimecardgame" target="_blank">Real time Card Game</a></h3>
      <p>Jogo de carta real time utilizando a engine de jogos Unity3D. Utilizado para aprendizagem de desenvolvimento de jogos.</p>
    </div>
    
    <div class="project-card">
      <h3><a href="https://github.com/fga-eps-mds" target="_blank">POC OSS projects</a></h3>
      <p>Projetos de software desenvolvido por estudantes de graduação em Engenharia de Software.</p>
    </div>
    
    <div class="project-card">
      <h3><a href="https://github.com/BOSS-BigOpenSourceSibling/" target="_blank">BOSS Organization</a></h3>
      <p>Organização com todo o material de apoio do programa de mentoria Big Open Source Siblings.</p>
    </div>
  </div>

  <div class="translation-highlight">
    <h3>Tradução FSFE</h3>
    <p>O time do Lab Livre traduziu para o português brasileiro a publicação "Public Money Public Code – Modernising Public Infrastructure with Free Software" da Free Software Foundation Europe.</p>
    <p>A tradução em português é intitulada: <a href="https://download.fsfe.org/campaigns/pmpc/PMPC-Modernising-with-Free-Software.pt_br.pdf" target="_blank"><strong>Dinheiro Público Código Público - Modernizando a Infraestrutura Pública com Software Livre</strong></a></p>
    
    <div class="publication-image">
      <img src="/images/publico.png" alt="Dinheiro Público Código Publico - Modernizando a Infraestrutura Pública com Software Livre" />
    </div>
  </div>
</div>
