---
layout: single
author_profile: true
title: Leituras
permalink: /reading/
---

<style>
/* Reading Page Styling */
.page-header {
  background: #f8f9fa;
  color: #333;
  padding: 2rem;
  border: 1px solid #e0e0e0;
  margin-bottom: 2rem;
  text-align: center;
}

.page-header h1 {
  margin: 0 0 0.5rem 0;
  font-size: 1.8rem;
  font-weight: 400;
  color: #333;
}

.page-header p {
  margin: 0;
  font-size: 1rem;
  color: #666;
}

.reading-section {
  background: #fff;
  border: 1px solid #e0e0e0;
  padding: 1.5rem;
  margin: 2rem 0;
  border-left: 3px solid #666;
  transition: border-color 0.2s ease;
}

.reading-section:hover {
  border-color: #333;
}

.reading-section h2 {
  color: #333;
  margin-top: 0;
  font-size: 1.4rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.reading-section .icon {
  font-size: 1.8rem;
  color: #666;
}

.reading-list {
  list-style: none;
  padding: 0;
  margin: 1rem 0;
  counter-reset: reading-counter;
}

.reading-item {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 6px;
  padding: 1.2rem;
  margin: 1rem 0;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
  counter-increment: reading-counter;
}

.reading-item::before {
  content: counter(reading-counter);
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

.reading-item:hover::before {
  transform: translateX(0);
}

.reading-item:hover {
  background: white;
  border-color: #006633;
  box-shadow: 0 2px 8px rgba(0,102,51,0.1);
  padding-left: 3rem;
}

.reading-item a {
  color: #003366;
  text-decoration: none;
  font-weight: 500;
  font-size: 1.1rem;
  display: block;
}

.reading-item a:hover {
  color: #006633;
}

.reading-item .author {
  margin: 0.5rem 0 0 0;
  color: #6c757d;
  font-size: 0.95rem;
  font-style: italic;
}

.intro-text {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 2rem 0;
  text-align: center;
  font-size: 1.1rem;
  color: #495057;
}

@media (max-width: 768px) {
  .page-header {
    padding: 2rem 1rem;
  }
  
  .page-header h1 {
    font-size: 1.8rem;
  }
  
  .reading-section {
    padding: 1.5rem;
  }
  
  .reading-item {
    padding: 1rem;
  }
  
  .reading-item:hover {
    padding-left: 2.5rem;
  }
}
</style>

<div class="page-header">
  <h1>Recursos de Pesquisa</h1>
  <p>Materiais de apoio para orientandos e pesquisadores</p>
</div>

<div class="intro-text">
  <p>Algumas sugestões, sem uma ordem específica (algumas delas retiradas de <a href="https://gustavopinto.org" target="_blank">gustavopinto.org</a>):</p>
</div>

<div class="reading-section">
  <h2><span class="icon">🎓</span>Trabalho de Conclusão de Curso (TCC)</h2>
  <ol class="reading-list">
    <li class="reading-item">
      <a href="/assets/docs/TCC.pdf" target="_blank">Guia de Sobrevivência do TCC</a>
      <div class="author">por Carla Rocha</div>
    </li>
  </ol>
</div>

<div class="reading-section">
  <h2><span class="icon">📚</span>Leitura Obrigatória</h2>
  <ol class="reading-list">
    <li class="reading-item">
      <a href="https://youtube.com/playlist?list=PLFFHHqnY3q2FLjtGKYuI-V-z9u7jzBOb_" target="_blank">Talk like a BOSS - rodas de conversas</a>
      <div class="author">por Big Open Source Sibling (BOSS)</div>
    </li>
    <li class="reading-item">
      <a href="https://www.slideshare.net/cameraculture/raskar-phd-and-ms-thesis-guidance?fbclid=IwAR1ECIl-T96IyK5X2BAIY3tm1nqP9fSaL9HN0oWWuYkw0mmQZ-5q1XYl0X4" target="_blank">Orientação para Tese de Doutorado e Mestrado</a>
      <div class="author">por Ramesh Raskar</div>
    </li>
    <li class="reading-item">
      <a href="https://www.nature.com/articles/d41586-018-02404-4" target="_blank">Como escrever um artigo de primeira classe</a>
      <div class="author">por Virginia Gewin</div>
    </li>
    <li class="reading-item">
      <a href="https://homes.cs.washington.edu/~mernst/advice/" target="_blank">Conselhos para pesquisadores e estudantes</a>
      <div class="author">por Michael Ernst</div>
    </li>
    <li class="reading-item">
      <a href="http://matt.might.net/articles/grad-student-resolutions/" target="_blank">12 resoluções para estudantes de pós-graduação</a>
      <div class="author">por Matt Might</div>
    </li>
    <li class="reading-item">
      <a href="https://www.scielo.br/pdf/clin/v69n3/1807-5932-clin-69-03-153.pdf" target="_blank">Escrevendo artigos científicos como um falante nativo de inglês: dez melhores dicas para falantes de português</a>
    </li>
    <li class="reading-item">
      <a href="https://ieeexplore.ieee.org/document/799955" target="_blank">Métodos qualitativos em estudos empíricos de engenharia de software</a>
    </li>
    <li class="reading-item">
      <a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006914" target="_blank">Dez regras simples para laboratórios de pesquisa mais saudáveis</a>
    </li>
  </ol>
</div>

<div class="reading-section">
  <h2><span class="icon">✍️</span>Escrita de Artigos</h2>
  <ol class="reading-list">
    <li class="reading-item">
      <a href="https://users.ece.cmu.edu/~koopman/essays/abstract.html" target="_blank">Como Escrever um Resumo</a>
      <div class="author">por Philip Koopman</div>
    </li>
    <li class="reading-item">
      <a href="http://sarahnadi.org/writing-papers/" target="_blank">Escrevendo Artigos Acadêmicos</a>
      <div class="author">por Sarah Nadi</div>
    </li>
    <li class="reading-item">
      <a href="http://www.cis.famu.edu/~cen5055joe/Administrative/HowToWrite_ResearchPaper.pdf" target="_blank">Escrevendo Boas Pesquisas em Engenharia de Software</a>
      <div class="author">por Mary Shaw</div>
    </li>
    <li class="reading-item">
      <a href="https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper" target="_blank">Como escrever um ótimo artigo de pesquisa</a>
      <div class="author">por Simon Peyton Jones</div>
    </li>
  </ol>
</div>

<div class="reading-section">
  <h2><span class="icon">🎤</span>Apresentações</h2>
  <ol class="reading-list">
    <li class="reading-item">
      <a href="https://www.microsoft.com/en-us/research/academic-program/give-great-research-talk" target="_blank">Como fazer uma ótima apresentação de pesquisa</a>
      <div class="author">por Simon Peyton Jones</div>
    </li>
    <li class="reading-item">
      <a href="http://andreas-zeller.blogspot.com.br/2013/10/summarizing-your-presentation-with.html" target="_blank">Resumindo sua apresentação com mini slides</a>
      <div class="author">por Andreas Zeller</div>
    </li>
  </ol>
</div>

<div class="reading-section">
  <h2><span class="icon">💪</span>Rejeições</h2>
  <ol class="reading-list">
    <li class="reading-item">
      <a href="https://medium.com/@cfiesler/tenured-professor-rogers-talks-about-imposter-syndrome-229e0a546ac1" target="_blank">Professor Titular Rogers Fala Sobre: Síndrome do Impostor</a>
      <div class="author">por Casey Fiesler</div>
    </li>
  </ol>
</div>

<div class="reading-section">
  <h2><span class="icon">🌟</span>Tópicos Gerais</h2>
  <ol class="reading-list">
    <li class="reading-item">
      <a href="https://medium.com/@lappisunbfga/what-i-wish-i-knew-before-starting-my-first-chatbot-project-66e5208f77dd" target="_blank">O que eu gostaria de saber antes de começar meu primeiro projeto de Chatbot</a>
      <div class="author">por Carla Rocha</div>
    </li>
    <li class="reading-item">
      <a href="https://medium.com/@lappisunbfga/desafios-ensino-de-ti-em-tempo-de-pandemia-o-futuro-é-colaborativo-e7aa183bb3d7" target="_blank">Desafios do ensino de TI em tempos de pandemia — O Futuro é Colaborativo</a>
      <div class="author">por Carla Rocha</div>
    </li>
  </ol>
</div>
