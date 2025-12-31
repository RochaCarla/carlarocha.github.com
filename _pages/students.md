---
layout: homepage
title: Oportunidades
permalink: /students/
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

.students-wrapper {
  font-family: var(--font-body);
  background: var(--background);
  color: var(--foreground);
  line-height: 1.6;
  margin: -2rem;
}

.students-wrapper h1, .students-wrapper h2, .students-wrapper h3 {
  font-family: var(--font-body);
  font-weight: 700;
  line-height: 1.2;
  color: var(--foreground);
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }
.max-w-6xl { max-width: 72rem; margin: 0 auto; }

/* Hero Section */
.hero-students {
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  padding: 4rem 0;
  text-align: center;
  border-bottom: 1px solid var(--border);
}

.hero-students h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--foreground);
}

.hero-students p {
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

.section-desc {
  color: var(--text-secondary);
  font-size: 1rem;
  line-height: 1.7;
  margin-bottom: 2rem;
}

/* Skills Grid */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.skill-card {
  background: #ffffff;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
}

.skill-card:hover {
  box-shadow: 0 8px 24px rgba(0, 102, 204, 0.1);
}

.skill-card h3 {
  color: var(--primary);
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.skill-card p {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin: 0;
}

/* CTA Section */
.cta-section {
  background: var(--primary);
  color: white;
  padding: 3rem;
  border-radius: 1rem;
  text-align: center;
  margin-top: 2rem;
}

.cta-section h3 {
  color: white;
  margin-bottom: 1rem;
}

.cta-section p {
  opacity: 0.9;
  margin-bottom: 1.5rem;
}

.cta-button {
  display: inline-block;
  background: white;
  color: var(--primary);
  padding: 0.75rem 2rem;
  border-radius: 0.5rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s ease;
}

.cta-button:hover {
  background: #f0f0f0;
  transform: translateY(-2px);
}

/* Student Cards */
.students-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}

.student-card {
  background: #ffffff;
  border-radius: 0.75rem;
  padding: 1rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
}

.student-card:hover {
  box-shadow: 0 4px 12px rgba(0, 102, 204, 0.1);
}

.student-card .name {
  font-weight: 600;
  color: var(--foreground);
  font-size: 0.95rem;
}

.student-card .level {
  color: var(--primary);
  font-size: 0.8rem;
  font-weight: 500;
}

.student-card.highlight {
  background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%);
  border: 2px dashed var(--primary);
}

/* Research Topics */
.research-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.research-card {
  background: #ffffff;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  border-left: 4px solid var(--primary);
}

.research-card h3 {
  color: var(--foreground);
  font-size: 1.1rem;
  margin-bottom: 0.75rem;
}

.research-card .question {
  color: var(--text-secondary);
  font-size: 0.9rem;
  font-style: italic;
  margin-bottom: 0.75rem;
}

.research-card .skills {
  display: inline-block;
  background: var(--card-bg);
  color: var(--primary);
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.8rem;
  font-weight: 500;
}

/* Responsive - Mobile First */
@media (max-width: 480px) {
  .students-wrapper { margin: -1rem; }
  .container { padding: 0 1rem; }
  .hero-students { padding: 2rem 0; }
  .hero-students h1 { font-size: 1.5rem; }
  .hero-students p { font-size: 1rem; }
  .section { padding: 2rem 0; }
  .section-title { font-size: 1.5rem; }
  .skills-grid { grid-template-columns: 1fr; gap: 1rem; }
  .skill-card { padding: 1rem; }
  .skill-card h3 { font-size: 1rem; }
  .students-grid { grid-template-columns: 1fr; gap: 0.75rem; }
  .student-card { padding: 0.75rem; }
  .student-card .name { font-size: 0.9rem; }
  .research-grid { grid-template-columns: 1fr; gap: 1rem; }
  .research-card { padding: 1rem; }
  .cta-section { padding: 1.5rem; }
  .cta-button { padding: 0.6rem 1.5rem; font-size: 0.9rem; }
}

@media (min-width: 481px) and (max-width: 768px) {
  .students-wrapper { margin: -1.5rem; }
  .hero-students h1 { font-size: 1.75rem; }
  .section { padding: 2.5rem 0; }
  .section-title { font-size: 1.75rem; }
  .skills-grid { grid-template-columns: 1fr; }
  .students-grid { grid-template-columns: repeat(2, 1fr); }
  .research-grid { grid-template-columns: 1fr; }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .hero-students h1 { font-size: 2rem; }
  .section { padding: 3rem 0; }
  .skills-grid { grid-template-columns: repeat(2, 1fr); }
  .students-grid { grid-template-columns: repeat(3, 1fr); }
  .research-grid { grid-template-columns: 1fr; }
}

@media (max-width: 480px) {
  .students-grid { grid-template-columns: 1fr; }
}
</style>

<div class="students-wrapper">

<section class="hero-students">
  <div class="container">
    <h1>Oportunidades de Pesquisa</h1>
    <p>Junte-se ao nosso grupo de pesquisa em software livre e inovação tecnológica</p>
  </div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Bolsas</span></div>
    <h2 class="section-title">Oportunidades no Lab Livre</h2>
    <p class="section-desc">Estou sempre em busca de indivíduos talentosos interessados em fazer parte do meu grupo de pesquisa, em diferentes níveis acadêmicos: desde estudantes de graduação (para programas de iniciação científica e projetos de pesquisa) até candidatos a mestrado e doutorado.</p>
    
    <div class="skills-grid">
      <div class="skill-card">
        <h3>Ciência de Dados</h3>
        <p>Expertise em limpeza de dados e geração automatizada de relatórios (pdf, html).</p>
      </div>
      <div class="skill-card">
        <h3>Engenharia de Dados</h3>
        <p>Capacidade na criação de Dags no Airflow e automação de processamento de dados.</p>
      </div>
      <div class="skill-card">
        <h3>Software Livre Decidim</h3>
        <p>Conhecimento em Ruby on Rails e criação de módulos para esta plataforma.</p>
      </div>
      <div class="skill-card">
        <h3>Python</h3>
        <p>Proficiência em Python e interesse em contribuir para projetos de código aberto.</p>
      </div>
      <div class="skill-card">
        <h3>Front-end</h3>
        <p>Habilidades em HTML, CSS e Javascript para criar interfaces atrativas e funcionais.</p>
      </div>
      <div class="skill-card">
        <h3>Pesquisa</h3>
        <p>Capacidade na redação de artigos científicos embasados e relevantes.</p>
      </div>
      <div class="skill-card">
        <h3>Jornalismo</h3>
        <p>Experiência ou formação na área jornalística para comunicação e divulgação.</p>
      </div>
      <div class="skill-card">
        <h3>Design</h3>
        <p>Habilidades criativas para contribuir com design de interfaces e materiais gráficos.</p>
      </div>
      <div class="skill-card">
        <h3>DevOps</h3>
        <p>Conhecimento em práticas de DevOps para otimização e implementação de processos.</p>
      </div>
    </div>

    <div class="cta-section">
      <h3>Pronto para se juntar ao nosso time?</h3>
      <p>Junte-se a nós para contribuir com projetos inovadores e fazer parte de uma comunidade de pesquisa e desenvolvimento de software livre.</p>
      <a href="mailto:caguiar@unb.br" class="cta-button">Entre em contato: caguiar@unb.br</a>
    </div>
  </div></div>
</section>

<section class="section" style="background: #f8f9fa;">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Orientandos</span></div>
    <h2 class="section-title">Alunos Atuais</h2>
    <div class="students-grid">
      <div class="student-card">
        <div class="name">Isaque Alves</div>
        <div class="level">Doutorado</div>
      </div>
      <div class="student-card">
        <div class="name">Bruna Pinos</div>
        <div class="level">Mestrado</div>
      </div>
      <div class="student-card">
        <div class="name">Alax Alves</div>
        <div class="level">Mestrado</div>
      </div>
      <div class="student-card">
        <div class="name">Arthur José B. O. Assis</div>
        <div class="level">Graduação</div>
      </div>
      <div class="student-card highlight">
        <div class="name">Você?</div>
        <div class="level">Candidate-se!</div>
      </div>
    </div>
    <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 1.5rem; font-style: italic;">Os bolsistas dos projetos de pesquisa não estão listados aqui, e sim nos repositórios de cada projeto.</p>
  </div></div>
</section>

<section class="section">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Alumni</span></div>
    <h2 class="section-title">Ex-alunos</h2>
    <div class="students-grid">
      <div class="student-card"><div class="name">Ivon Miranda Santos</div><div class="level">Mestrado</div></div>
      <div class="student-card"><div class="name">Leonardo Silva Gomes</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Tiago Vidigal</div><div class="level">Mestrado</div></div>
      <div class="student-card"><div class="name">Gabriel Filipe M. Araujo</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Giovana Vitor Dionísio</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Hérya Rodrigues</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Youssef M. Y. Falaneh</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Gabriela Barrozo Guedes</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Fabíola Malta Fleury</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Marina Joranhezon</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Rodrigo Oliveira Campos</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Eduardo Nunes</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Guilherme G. Lacerda</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">João Pedro Sconetto</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Indiara Duarte</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Rafaella O. F. Junqueira</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Lorrany dos S. Azevedo</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Filipe C. H. Barcelos</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Lucas Dutra F. Nascimento</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Caio Vinícius F. Araújo</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Geison de Souza Oliveira</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Marcos Nery Borges Junior</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Igor Araujo de Sousa</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Shayane Marques Alcantara</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Matheus Silva Pereira</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Felipe Campos de Almeida</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Mar Akin Dantas Silva</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Abdul Hannan</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Heitor Marques Simões Barbosa</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Carolina Barbosa Brito</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Laura Pinos de Oliveira</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Ana Beatriz Ferreira dos Santos</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Breno Yuri Barbosa Gomes</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Gabriel Pessoa Zaranza</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Juan Pablo Ricarte de Barros</div><div class="level">Graduação</div></div>
      <div class="student-card"><div class="name">Leonardo Lago Moreno</div><div class="level">Graduação</div></div>
    </div>
  </div></div>
</section>

<section class="section" style="background: #f8f9fa;">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Temas</span></div>
    <h2 class="section-title">Interesses de Pesquisa</h2>
    <p class="section-desc">Aqui estão alguns temas nos quais tenho interesse em pesquisar/colaborar. Meu objetivo atual é que esses trabalhos gerem artigos para serem publicados em eventos de impacto para a comunidade de Engenharia de Software.</p>
    
    <div class="research-grid">
      <div class="research-card">
        <h3>Programas de Mentoria para Grupos Sub-representados</h3>
        <p class="question">Quais são os desafios para envolver grupos sub-representados em programas de mentoria?</p>
        <span class="skills">Scripts, Pró-atividade</span>
      </div>
      <div class="research-card">
        <h3>Comportamento de Estudantes em Open Source</h3>
        <p class="question">Que tipo de contribuições são feitas por estudantes? Projetos de sala de aula? Estágios? Hackathons?</p>
        <span class="skills">Scripts, Pró-atividade</span>
      </div>
      <div class="research-card">
        <h3>Ensino de DevOps</h3>
        <p class="question">Teoria sobre estruturas/educação de equipes DevOps</p>
        <span class="skills">Scripts, Pró-atividade</span>
      </div>
      <div class="research-card">
        <h3>Migração Multicloud em DevOps</h3>
        <p class="question">Quais são os desafios e requisitos de arquitetura para permitir soluções multicloud?</p>
        <span class="skills">Scripts, Python</span>
      </div>
      <div class="research-card">
        <h3>ML para Análise de Dados</h3>
        <p class="question">Desenvolvimento de ferramentas para facilitar que cientistas de dados explorem dados em contextos específicos</p>
        <span class="skills">Python, ML</span>
      </div>
      <div class="research-card">
        <h3>Engenharia de Dados em Pipelines</h3>
        <p class="question">Desenvolvimento de pipeline para processar vários bancos de dados em paralelo usando fluxo de dados</p>
        <span class="skills">Python, Airflow</span>
      </div>
      <div class="research-card">
        <h3>MLOps</h3>
        <p class="question">Quais são as barreiras para adotar práticas e automação de MLOps?</p>
        <span class="skills">Scripts, DevOps</span>
      </div>
      <div class="research-card">
        <h3>Ensino de Engenharia de Software</h3>
        <p class="question">Quais as boas práticas para o aprendizado ativo em Engenharia de Software?</p>
        <span class="skills">Pesquisa, Educação</span>
      </div>
    </div>
  </div></div>
</section>

</div>
