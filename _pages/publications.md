---
layout: single
author_profile: true
title: Publicações
permalink: /publications/
---

<style>
/* Publications Page Styling */
.publications-header {
  background: linear-gradient(135deg, #003366 0%, #006633 100%);
  color: white;
  padding: 2rem;
  border-radius: 8px;
  margin-bottom: 2rem;
  text-align: center;
}

.publications-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}

.stat-item {
  background: rgba(255,255,255,0.1);
  padding: 1rem;
  border-radius: 6px;
  text-align: center;
}

.stat-number {
  font-size: 1.8rem;
  font-weight: bold;
  display: block;
}

.stat-label {
  font-size: 0.9rem;
  opacity: 0.9;
}

.year-section {
  margin: 2.5rem 0;
  border-left: 4px solid #003366;
  padding-left: 1.5rem;
}

.year-title {
  color: #003366;
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.year-count {
  background: #006633;
  color: white;
  padding: 0.2rem 0.6rem;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: normal;
}

.publication-item {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1rem;
  transition: all 0.2s ease;
  position: relative;
}

.publication-item:hover {
  border-color: #003366;
  box-shadow: 0 4px 12px rgba(0,51,102,0.1);
}

/* High-impact publications (50+ citations) */
.publication-item.high-impact {
  background: linear-gradient(135deg, #fff8e1 0%, #f3e5f5 100%);
  border: 2px solid #ff6f00;
  box-shadow: 0 6px 20px rgba(255,111,0,0.15);
}

.publication-item.high-impact::before {
  content: '🏆 HIGH IMPACT';
  position: absolute;
  top: -8px;
  right: 15px;
  background: #ff6f00;
  color: white;
  padding: 0.2rem 0.8rem;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.5px;
}

/* Very high-impact publications (100+ citations) */
.publication-item.very-high-impact {
  background: linear-gradient(135deg, #fff3e0 0%, #fce4ec 100%);
  border: 3px solid #d32f2f;
  box-shadow: 0 8px 25px rgba(211,47,47,0.2);
}

.publication-item.very-high-impact::before {
  content: '⭐ BREAKTHROUGH';
  background: #d32f2f;
}

/* Journal publications */
.publication-item.journal {
  border-left: 6px solid #006633;
  background: linear-gradient(135deg, #f1f8e9 0%, #e8f5e8 100%);
}

.publication-item.journal .pub-venue::before {
  content: '📖 ';
  color: #006633;
  font-weight: bold;
}

/* Conference publications */
.publication-item.conference .pub-venue::before {
  content: '🎤 ';
  color: #666;
}

.pub-title {
  color: #003366;
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  line-height: 1.3;
}

.pub-authors {
  color: #6c757d;
  font-size: 0.95rem;
  margin-bottom: 0.5rem;
}

.pub-venue {
  color: #495057;
  font-style: italic;
  margin-bottom: 0.5rem;
}

.pub-citations {
  background: #006633;
  color: white;
  padding: 0.2rem 0.6rem;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 500;
  display: inline-block;
}

.external-links {
  display: flex;
  gap: 1rem;
  margin: 1.5rem 0;
  flex-wrap: wrap;
}

.external-link {
  background: #003366;
  color: white;
  padding: 0.8rem 1.5rem;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 500;
  transition: background 0.2s ease;
}

.external-link:hover {
  background: #006633;
  color: white;
}

@media (max-width: 768px) {
  .publications-header {
    padding: 1.5rem;
  }
  
  .publications-stats {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .year-section {
    padding-left: 1rem;
  }
  
  .publication-item {
    padding: 1rem;
  }
}
</style>

<div class="publications-header">
  <h1>Publicações Científicas</h1>
  <p>Professora na Faculdade de Engenharia de Software (UnB) e coordenadora do laboratório Lab Livre</p>
  
  <div class="publications-stats">
    <div class="stat-item">
      <span class="stat-number">868</span>
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
</div>

Sou membro ativo do grupo de pesquisa em [Sistemas de Software, Ciência e Engenharia de Dados e Computação de Alto Desempenho](http://dgp.cnpq.br/dgp/espelhogrupo/633486) vinculado ao Instituto de Matemática e Estatística da Universidade de São Paulo (IME-USP).

Atualmente participo do programa de mestrado profissionalizante [PPCA](https://ppca.unb.br) na Universidade de Brasília (UnB).

Além disso, atuo como coordenadora do laboratório de pesquisa aplicada [Lab Livre](https://www.lappis.rocks), um espaço de referência na UnB para estudos e pesquisas em áreas tecnológicas de vanguarda.

<div class="external-links">
  <a href="https://scholar.google.com/citations?user=_y8XHnAAAAAJ&hl=pt-BR" class="external-link" target="_blank">
    📊 Google Scholar
  </a>
  <a href="http://lattes.cnpq.br/2831991076751452" class="external-link" target="_blank">
    📋 Currículo Lattes
  </a>
</div>

---

## Lista Completa de Publicações

<div class="year-section">
  <h2 class="year-title">2024 <span class="year-count">1</span></h2>
  
  <div class="publication-item journal">
    <div class="pub-title">Harmonizing DevOps taxonomies—A grounded theory study</div>
    <div class="pub-authors">J Díaz, J Pérez, I Alves, F Kon, L Leite, P Meirelles, C Rocha</div>
    <div class="pub-venue">Journal of Systems and Software 208, 111908</div>
    <span class="pub-citations">18 citações</span>
  </div>
</div>

<div class="year-section">
  <h2 class="year-title">2023 <span class="year-count">4</span></h2>
  
  <div class="publication-item journal">
    <div class="pub-title">Practices for managing machine learning products: A multivocal literature review</div>
    <div class="pub-authors">I Alves, LAF Leite, P Meirelles, F Kon, CSR Aguiar</div>
    <div class="pub-venue">IEEE Transactions on Engineering Management 71, 7425-7455</div>
    <span class="pub-citations">13 citações</span>
  </div>
  
  <div class="publication-item">
    <div class="pub-title">Practices for Managing Machine Learning Products: a Multivocal Literature Review</div>
    <div class="pub-authors">L Leite, PRM Meirelles, F Kon, C Rocha</div>
    <div class="pub-venue">Authorea Preprints</div>
    <span class="pub-citations">3 citações</span>
  </div>
  
  <div class="publication-item journal">
    <div class="pub-title">When technical solutions are not enough: using software concepts to analyze challenges at delivery processes between mixed-signal IC team members</div>
    <div class="pub-authors">TP Vidigal, W Prodanov, CSR Aguiar</div>
    <div class="pub-venue">IEEE Transactions on Engineering Management 71, 1744-1756</div>
    <span class="pub-citations">1 citação</span>
  </div>
  
  <div class="publication-item">
    <div class="pub-title">Harmonizing DevOps Taxonomies--Theory Operationalization and Testing</div>
    <div class="pub-authors">I Alves, J Pérez, J Díaz, D López-Fernández, M Pais, F Kon, C Rocha</div>
    <div class="pub-venue">arXiv preprint arXiv:2302.00033</div>
    <span class="pub-citations">1 citação</span>
  </div>
</div>

<div class="year-section">
  <h2 class="year-title">2021 <span class="year-count">2</span></h2>
  
  <div class="publication-item conference">
    <div class="pub-title">Qualifying software engineers undergraduates in devops-challenges of introducing technical and non-technical concepts in a project-oriented course</div>
    <div class="pub-authors">I Alves, C Rocha</div>
    <div class="pub-venue">2021 IEEE/ACM 43rd International Conference on Software Engineering: Software Engineering Education and Training (ICSE-SEET)</div>
    <span class="pub-citations">26 citações</span>
  </div>
  
  <div class="publication-item conference">
    <div class="pub-title">OSS Scripting System for Game Development in Rust</div>
    <div class="pub-authors">PDS da Silva, RO Campos, C Rocha</div>
    <div class="pub-venue">IFIP International Conference on Open Source Systems, 51-58</div>
    <span class="pub-citations">3 citações</span>
  </div>
</div>

<div class="year-section">
  <h2 class="year-title">2019 <span class="year-count">3</span></h2>
  
  <div class="publication-item journal very-high-impact">
    <div class="pub-title">A survey of DevOps concepts and challenges</div>
    <div class="pub-authors">L Leite, C Rocha, F Kon, D Milojicic, P Meirelles</div>
    <div class="pub-venue">ACM computing surveys (CSUR) 52 (6), 1-35</div>
    <span class="pub-citations">676 citações</span>
  </div>
  
  <div class="publication-item conference">
    <div class="pub-title">FLOSS FAQ chatbot project reuse: how to allow nonexperts to develop a chatbot</div>
    <div class="pub-authors">ART de Lacerda, CSR Aguiar</div>
    <div class="pub-venue">Proceedings of the 15th International Symposium on Open Collaboration, 1-8</div>
    <span class="pub-citations">31 citações</span>
  </div>
  
  <div class="publication-item conference">
    <div class="pub-title">A students' perspective of native and cross-platform approaches for mobile application development</div>
    <div class="pub-authors">P Meirelles, CSR Aguiar, F Assis, R Siqueira, A Goldman</div>
    <div class="pub-venue">International Conference on Computational Science and Its Applications, 586-601</div>
    <span class="pub-citations">21 citações</span>
  </div>
</div>

<div class="year-section">
  <h2 class="year-title">2016 <span class="year-count">2</span></h2>
  
  <div class="publication-item journal">
    <div class="pub-title">A influência da intensidade emocional no reconhecimento de emoções em faces por crianças brasileiras</div>
    <div class="pub-authors">JS Rocha Aguiar, AI de Paiva Silva, CS Rocha Aguiar, N Torro-Alves, W Cristina de Souza</div>
    <div class="pub-venue">Universitas Psychologica 15 (SPE5), 1-9</div>
    <span class="pub-citations">16 citações</span>
  </div>
  
  <div class="publication-item journal">
    <div class="pub-title">The importance of emotional intensity on the recognition of facial emotions by Brazilian children</div>
    <div class="pub-authors">JS Rocha Aguiar, AI de Paiva Silva, CS Rocha Aguiar, N Torro-Alves, W Cristina de Souza</div>
    <div class="pub-venue">Universitas Psychologica 15 (spe5), 1-9</div>
    <span class="pub-citations">2 citações</span>
  </div>
</div>

<div class="year-section">
  <h2 class="year-title">2015 <span class="year-count">1</span></h2>
  
  <div class="publication-item conference">
    <div class="pub-title">Development of simulation interfaces for evaluation task with the use of physiological data and virtual reality applied to a vehicle simulator</div>
    <div class="pub-authors">MR Miranda, H Costa, L Oliveira, T Bernardes, C Aguiar, C Miosso, A Rocha</div>
    <div class="pub-venue">The Engineering Reality of Virtual Reality 2015 9392, 49-61</div>
    <span class="pub-citations">3 citações</span>
  </div>
</div>

### 2014

- **Embodiments, visualizations, and immersion with enactive affective systems**. *D Domingues, CJ Miosso, SF Rodrigues, CSR Aguiar, TF Lucena, M Miranda, AF Rocha, R Raskar*. The Engineering Reality of Virtual Reality 2014 9012, 151-163. **19 citações**

- **Metodologia para Usar Dados Fisiológicos e Realidade Virtual em Ergonomia do Produto Aplicados a um Simulador Veicular**. *M MIRANDA, H Costa, L Oliveira, T Bernardes, C Aguiar, C Miosso, A Rocha*. Artigo publicado na ABERGO. **1 citação**

### 2007

- **Planejamento de trajetória para o robô omni utilizando o algoritmo mapade rotas probabilístico**. *BV Adôrno, CSR Aguiar, GA Borges*. VIII Simpósio Brasileiro de Automação Inteligente 1, 1-6. **10 citações**

- **3D datasets segmentation based on local attribute variation**. *CSR Aguiar, S Druon, A Crosnier*. 2007 IEEE/RSJ International Conference on Intelligent Robots and Systems. **6 citações**

- **Hierarchical segmentation for unstructured and unfiltered range images**. *CSR Aguiar, S Druon, A Crosnier*. Computer Graphics, Imaging and Visualisation (CGIV 2007), 261-267. **2 citações**

### 2005

- **Estimação de parâmetros geométricos de um robô móvel omnidirecional**. *CSR Aguiar, FMGSA Oliveira, GA Borges*. VII Simpósio Brasileiro de Automação Inteligente/II IEEE Latin-American Robotics Symposium. **4 citações**

### 2003

- **A Educação Física no Jardim de Infância e no 1º CEB: características e contextos de formação**. *L Rocha, RC Campos, C Rocha*. Educare Aprender 1. **10 citações**

### Artigos de Revistas

-  **A survey of DevOps concepts and challenges**. *Autores:* Leonardo Leite, Carla Rocha, Fabio Kon, Dejan Milojicic, Paulo Meirelles. *Revista:* ACM Computing Surveys (CSUR). *Volume:* 52. *Número:* 6. *Páginas:* 1-35. *Ano:* 2019. *Editora:* ACM New York, NY, USA. **450 citações até 2023**.
    
- **Harmonizing Devops Taxonomies–a Grounded Theory Study**. *J Díaz, J Pérez, I Alves, F Kon, L Leite, P Meirelles, C Rocha*. *Journal of Systems and Software (JSS)*. *2024*.

- **Harmonizing DevOps Taxonomies--Theory Operationalization and Testing**. *J Díaz, J Pérez, I Alves, F Kon, L Leite, P Meirelles, C Rocha*. arXiv preprint arXiv:2302.00033, 2023.

- **Practices for Managing Machine Learning Products: A Multivocal Literature Review**. *I Alves, LAF Leite, P Meirelles, F Kon, CSR Aguiar*. *IEEE Transactions on Engineering Management*. *2023*.
  
- **When Technical Solutions aren’t Enough: Using Software Concepts to Analyse Challenges at Delivery Processes between Mixed-Signal IC Team Members**. *T Pereira Vidigal, W Prodanov, C Rocha*. *IEEE Transactions on Engineering Management*. *2023*.
  
-  **A influência da intensidade emocional no reconhecimento de emoções em faces por crianças brasileiras**. *Autores:* Juliana Silva Rocha Aguiar, Ana Idalina de Paiva Silva, Carla Silva Rocha Aguiar, Nelson Torro-Alves, Wânia Cristina de Souza. *Revista:* Universitas Psychologica. *Volume:* 15. *Número:* SPE5. *Páginas:* 1-9. *Ano:* 2016.


-  **The importance of emotional intensity on the recognition of facial emotions by Brazilian children**. *Autores:* Juliana Silva Rocha Aguiar, Ana Idalina de Paiva Silva, Carla Silva Rocha Aguiar, Nelson Torro-Alves, Wânia Cristina de Souza. *Revista:* Universitas Psychologica. *Volume:* 15. *Número:* spe5. *Páginas:* 1-9. *Ano:* 2016.






### Conference Papers

-  **Qualifying software engineers undergraduates in DevOps-challenges of introducing technical and non-technical concepts in a project-oriented course**. *Autores:* Isaque Alves, Carla Rocha. *Evento:* 2021 IEEE/ACM 43rd International Conference on Software Engineering: Software Engineering Education and Training (ICSE-SEET). *Páginas:* 144-153. *Ano:* 2021. *Editora:* IEEE.

-  **A students’ perspective of native and cross-platform approaches for mobile application development**. *Autores:* Paulo Meirelles, Carla SR Aguiar, Felipe Assis, Rodrigo Siqueira, Alfredo Goldman. *Conferência:* Computational Science and Its Applications–ICCSA 2019: 19th International Conference, Saint Petersburg, Russia, July 1–4, 2019, Proceedings, Part V 19. *Páginas:* 586-601. *Ano:* 2019. *Editora:* Springer International Publishing.

- **OSS Scripting System for Game Development in Rust**. *PDS da Silva, RO Campos, C Rocha*. *Open Source Systems: 17th IFIP WG 2.13 International Conference, OSS 2021 …*. *2021*.
  
-  **FLOSS FAQ chatbot project reuse: how to allow nonexperts to develop a chatbot**. *Autores:* Arthur RT de Lacerda, Carla SR Aguiar *Evento:* Proceedings of the 15th International Symposium on Open Collaboration. *Páginas:* 1-8. *Ano:* 2019.

- **Assuring the Evolvability of Legacy Systems in Devops Transformation/Adoption: Insights of an Experience Report**. *Á Alves, C Rocha*. *Brazilian Workshop on Agile Methods, 32-53*. *2021*.

- **Planejamento de trajetória para o robô omni utilizando o algoritmo mapade rotas probabilístico**. *Autores:* Bruno Vilhena Adôrno, Carla Silva Rocha Aguiar, Geovany Araújo Borges. *Publicação:* VIII Simpósio Brasileiro de Automação Inteligente. *Volume:* 1. *Páginas:* 1-6. *Ano:* 2007. 

- **3D datasets segmentation based on local attribute variation**. *Autores:* Carla Silva Rocha Aguiar, Sébastien Druon, André Crosnier. *Publicação:* 2007 IEEE/RSJ International Conference on Intelligent Robots and Systems. *Páginas:* 3205-3210. *Ano:* 2007. *Editora:* IEEE.

- **Development of simulation interfaces for evaluation task with the use of physiological data and virtual reality applied to a vehicle simulator**. *MR Miranda, H Costa, L Oliveira, T Bernardes, C Aguiar, C Miosso, ...*. *The Engineering Reality of Virtual Reality 2015 9392, 49-61*. *2015*.
  
- **Embodiments, visualizations, and immersion with enactive affective systems**. *Autores:* Diana Domingues, Cristiano Jacques Miosso, Suélia F Rodrigues, Carla Silva Rocha Aguiar, Tiago F Lucena, Mateus Miranda, Adson F Rocha, Ramesh Raskar. *Publicação:* The Engineering Reality of Virtual Reality 2014. *Volume:* 9012. *Páginas:* 151-163. *Ano:* 2014. *Editora:* SPIE.

- **Estimação de parâmetros geométricos de um robô móvel omnidirecional**. *Autores:* Carla Silva Rocha Aguiar, Flávia Maria GSA Oliveira, Geovany Araújo Borges. *Publicação:* VII Simpósio Brasileiro de Automação Inteligente/II IEEE Latin-American Robotics Symposium, São Luis. *Páginas:* 1-8. *Ano:* 2005.

- **Hierarchical segmentation for unstructured and unfiltered range images**. *Autores:* Carla Silva Rocha Aguiar, Sébastien Druon, André Crosnier. *Publicação:* Computer Graphics, Imaging and Visualisation (CGIV 2007. *Páginas:* 261-267. *Ano:* 2007. *Editora:* IEEE.

-  **Criterion independent hierarchical segmentation for unstructured 3D datasets-Application to range images**. *Autores:* Carla Aguiar, Sébastien Druon, André Crosnier. *Evento:* IROS'07: Intelligent Robots and Systems.*Ano:* 2007.
 
- **Pairwise region-based scan alignment**. *Autores:* Carla Silva Rocha Aguiar, Sébastien Druon, André Crosnier. *Publicação:* 2009 IEEE/RSJ International Conference on Intelligent Robots and Systems. *Páginas:* 4047-4053. *Ano:* 2009. *Editora:* IEEE.

- **Contextual Sentiment Analysis with Untrained Annotators**. *Autores:* Lucas A Silva, Carla R Aguiar. *Revista:* International Journal of Computer and Information Engineering. *Volume:* 8. *Número:* 3. *Páginas:* 435-440. *Ano:* 2014.

### Outras Publicações

-  **Agile Methods: 10th Brazilian Workshop, WBMA 2019, Belo Horizonte, Brazil, September 11, 2019, Revised Selected Papers**. *Autores:* Paulo Meirelles, Maria Augusta Nelson, Carla Rocha.  *Ano:* 2019. *Editora:* Springer Nature.

-  **Trans Perspective in Software Engineering**. *Autores:* Marina Joranhezon, Fabıola Malta Fleury, Carla Rocha. *Ano:* 2023 . *Editora:* Não especificada.

- **Camera calibration for 3D localization: application to beating heart motion estimation**. *Autores:* Carla SILVA ROCHA AGUIAR AGUIAR, Philippe POIGNET, Jean TRIBOULET.

- **Recalage de données 3D denses**. *Autores:* Sébastien Druon, Carla Aguiar, Marie-José Aldon, André Crosnier.



