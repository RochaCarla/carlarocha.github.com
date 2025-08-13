---
layout: single
author_profile: true
title: Aulas
permalink: /teaching/
---

<style>
/* Teaching Page Styling */
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

.teaching-philosophy {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 2rem;
  margin: 2rem 0;
  border-left: 6px solid #003366;
}

.teaching-philosophy h2 {
  color: #003366;
  margin-top: 0;
  font-size: 1.6rem;
  font-weight: 600;
}

.methodology-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.methodology-item {
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.2s ease;
}

.methodology-item:hover {
  border-color: #006633;
  box-shadow: 0 4px 12px rgba(0,102,51,0.1);
  transform: translateY(-2px);
}

.methodology-item h3 {
  color: #003366;
  margin-bottom: 1rem;
}

.methodology-item .icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  display: block;
}

.course-image {
  text-align: center;
  margin: 2rem 0;
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  border: 1px solid #e9ecef;
}

.course-image img {
  max-width: 100%;
  height: auto;
  border-radius: 6px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.semester-section {
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  border-left: 4px solid #006633;
}

.semester-section h2 {
  color: #003366;
  margin-top: 0;
  font-size: 1.4rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.semester-badge {
  background: #006633;
  color: white;
  padding: 0.2rem 0.8rem;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: normal;
}

.course-list {
  list-style: none;
  padding: 0;
  margin: 1rem 0;
}

.course-item {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 6px;
  padding: 1rem;
  margin: 0.8rem 0;
  transition: all 0.2s ease;
}

.course-item:hover {
  border-color: #003366;
  background: white;
  box-shadow: 0 2px 8px rgba(0,51,102,0.1);
}

.course-item a {
  color: #003366;
  text-decoration: none;
  font-weight: 500;
}

.course-item a:hover {
  color: #006633;
}

@media (max-width: 768px) {
  .page-header {
    padding: 2rem 1rem;
  }
  
  .page-header h1 {
    font-size: 1.8rem;
  }
  
  .methodology-grid {
    grid-template-columns: 1fr;
  }
  
  .semester-section {
    padding: 1rem;
  }
}
</style>

<div class="page-header">
  <h1>Metodologia de Ensino</h1>
  <p>Aprendizagem experiencial através de projetos reais</p>
</div>

<div class="teaching-philosophy">
  <h2>Filosofia Educacional</h2>
  
  <p>Eu adoto <strong>Modelos de Aprendizagem Experiencial</strong> com cursos orientados a projetos. Neste modelo, os alunos passam por uma 'jornada de descoberta', onde compreendem as lições e conceitos por meio do processo experiencial de chegar lá.</p>

  <p>Os estudantes desenvolvem projetos de software com clientes reais ou conjuntos de dados reais. Todos os artefatos produzidos durante os cursos são de código aberto, e os alunos têm acesso ao material e código de semestres anteriores. Os estudantes também têm a experiência de contribuir para comunidades de Código Aberto maiores, como Debian, Kubernetes, Rocket.Chat e Noosfero.</p>
</div>

<div class="methodology-grid">
  <div class="methodology-item">
    <span class="icon">🎯</span>
    <h3>Projetos Reais</h3>
    <p>Desenvolvimento com clientes reais e conjuntos de dados autênticos</p>
  </div>
  
  <div class="methodology-item">
    <span class="icon">🔓</span>
    <h3>Código Aberto</h3>
    <p>Todos os artefatos são open source e acessíveis para futuras turmas</p>
  </div>
  
  <div class="methodology-item">
    <span class="icon">🌐</span>
    <h3>Comunidades</h3>
    <p>Contribuição para projetos como Debian, Kubernetes e Rocket.Chat</p>
  </div>
</div>

<div class="course-image">
  <img src="/images/gpp_mds.png" alt="Estudantes em aula prática" />
  <p><em>Estudantes desenvolvendo projetos em metodologia ágil</em></p>
</div>

<div class="semester-section">
  <h2>2024.1 <span class="semester-badge">Atual</span></h2>
  <ul class="course-list">
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2024.1-MDS-DOCS/" target="_blank">
        Métodos de Desenvolvimento de Software
      </a>
    </li>
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2024.1-EPS-DOCS/" target="_blank">
        Engenharia de Produto de Software
      </a>
    </li>
  </ul>
</div>

<div class="semester-section">
  <h2>2023.2</h2>
  <ul class="course-list">
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2023.2-MDS-DOCS/" target="_blank">
        Métodos de Desenvolvimento de Software
      </a>
    </li>
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2023.2-EPS-DOCS/" target="_blank">
        Engenharia de Produto de Software
      </a>
    </li>
  </ul>
</div>

<div class="semester-section">
  <h2>2023.1</h2>
  <ul class="course-list">
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2023.1-MDS-DOCS/" target="_blank">
        Métodos de Desenvolvimento de Software
      </a>
    </li>
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2023.1-EPS-DOCS/" target="_blank">
        Engenharia de Produto de Software
      </a>
    </li>
  </ul>
</div>

<div class="semester-section">
  <h2>2022.2</h2>
  <ul class="course-list">
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2022.2-MDS-DOCS/" target="_blank">
        Métodos de Desenvolvimento de Software
      </a>
    </li>
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2022.2-EPS-DOCS/" target="_blank">
        Engenharia de Produto de Software
      </a>
    </li>
  </ul>
</div>

<div class="semester-section">
  <h2>2022.1</h2>
  <ul class="course-list">
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2022.1-MDS-DOCS/" target="_blank">
        Métodos de Desenvolvimento de Software
      </a>
    </li>
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2022.1-EPS-DOCS/" target="_blank">
        Engenharia de Produto de Software
      </a>
    </li>
  </ul>
</div>

<div class="semester-section">
  <h2>2021.2</h2>
  <ul class="course-list">
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2021.2-MDS-DOCS/" target="_blank">
        Métodos de Desenvolvimento de Software
      </a>
    </li>
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2021.2-EPS-DOCS/" target="_blank">
        Engenharia de Produto de Software
      </a>
    </li>
  </ul>
</div>

<div class="semester-section">
  <h2>2021.1</h2>
  <ul class="course-list">
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2021.1-MDS-DOCS/" target="_blank">
        Métodos de Desenvolvimento de Software
      </a>
    </li>
    <li class="course-item">
      <a href="https://fga-eps-mds.github.io/2021.1-EPS-DOCS/" target="_blank">
        Engenharia de Produto de Software
      </a>
    </li>
  </ul>
</div>

## 2021.1 
1. [Software Development Methods - Métodos de Desenvolvimento de Software (MDS)](/teaching/mds)
1. [Software Configuration Management and Evolution- Gerência de Configuração e Evolução de Software(GCES)](https://github.com/fga-gces)
1. [Software Development - Masters](https://github.com/PPCA-CS)

## 2020.2 
1. [Software Development Methods - Métodos de Desenvolvimento de Software (MDS)](/teaching/mds)
1. [Software Configuration Management and Evolution - Gerência de Configuração e Evolução de Software(GCES)](https://github.com/fga-gces)

## 2020.1 
1. [Software Development Methods - Métodos de Desenvolvimento de Software (MDS)](/teaching/mds)
1. [Software Configuration Management and Evolution - Gerência de Configuração e Evolução de Software(GCES)](https://github.com/fga-gces)


## Before 2020
I also teach Computer Graphics, Product Engineering, and Introduction to Software Engineering.


