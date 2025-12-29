---
layout: homepage
title: false
author_profile: false
permalink: /
---

<style>
/* Design System - Azul */
:root {
  /* Cor Principal - Azul */
  --primary: #0066cc;
  --primary-dark: #004499;
  --primary-light: #0088ee;
  
  /* Cores Base */
  --background: #FFFFFF;
  --foreground: #000000;
  --text-secondary: #666666;
  --text-muted: #999999;
  --border: #e0e0e0;
  --card-bg: #f5f5f5;
  
  /* Tipografia */
  --font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  
  /* Gradientes - Azul */
  --gradient-primary: linear-gradient(135deg, #0066cc 0%, #0088ee 100%);
}

.home-wrapper {
  font-family: var(--font-body);
  background: var(--background);
  color: var(--foreground);
  line-height: 1.6;
  margin: -2rem;
}

.home-wrapper h1, .home-wrapper h2, .home-wrapper h3 {
  font-family: var(--font-body);
  font-weight: 700;
  line-height: 1.2;
  color: var(--foreground);
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }

.text-gradient {
  background: var(--primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

.btn-elegant {
  display: inline-flex;
  align-items: center;
  padding: 0.875rem 1.75rem;
  font-size: 0.9rem;
  font-weight: 600;
  border-radius: 0.5rem;
  transition: all 0.3s ease;
  border: none;
}

.btn-primary {
  background: var(--primary);
  color: white;
  box-shadow: 0 4px 20px rgba(0, 102, 204, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(0, 102, 204, 0.4);
  color: white;
}

.btn-outline {
  background: transparent;
  color: var(--primary);
  border: 2px solid var(--primary);
}

.btn-outline:hover {
  background: rgba(0, 102, 204, 0.1);
  color: var(--primary);
}

/* Hero */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  position: relative;
  overflow: hidden;
  background: #FFFFFF;
  padding-top: 5rem;
}

.hero-bg-circle {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
}

.hero-bg-circle-1 {
  top: 5rem; right: 5rem;
  width: 24rem; height: 24rem;
  background: rgba(0, 102, 204, 0.06);
  animation: float 6s ease-in-out infinite;
}

.hero-bg-circle-2 {
  bottom: 5rem; left: 5rem;
  width: 18rem; height: 18rem;
  background: rgba(0, 136, 238, 0.08);
  animation: float 6s ease-in-out infinite 0.3s;
}

.hero-content {
  position: relative;
  z-index: 10;
  max-width: 56rem;
  margin: 0 auto;
  text-align: center;
  padding: 3rem 1.5rem;
}

.hero-subtitle {
  color: var(--primary);
  font-size: 0.875rem;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: #000000;
}

@media (min-width: 768px) { .hero-title { font-size: 4rem; } }

.hero-bio {
  font-size: 1.125rem;
  color: #333333;
  max-width: 42rem;
  margin: 0 auto 2.5rem;
  line-height: 1.8;
}

.hero-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}

.hero-stats {
  margin-top: 4rem;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  max-width: 42rem;
  margin-left: auto;
  margin-right: auto;
}

@media (min-width: 640px) { .hero-stats { grid-template-columns: repeat(4, 1fr); } }

.hero-stat-number {
  font-family: var(--font-display);
  font-size: 2rem;
  font-weight: 700;
}

.hero-stat-label {
  color: #666666;
  font-size: 0.875rem;
  margin-top: 0.5rem;
}

.scroll-indicator {
  position: absolute;
  bottom: 2.5rem;
  left: 50%;
  transform: translateX(-50%);
}

.scroll-indicator-inner {
  width: 1.5rem;
  height: 2.5rem;
  border: 2px solid rgba(160, 174, 192, 0.3);
  border-radius: 9999px;
  display: flex;
  justify-content: center;
}

.scroll-indicator-dot {
  width: 0.25rem;
  height: 0.75rem;
  background: var(--primary);
  border-radius: 9999px;
  margin-top: 0.5rem;
  animation: bounce 1.5s ease-in-out infinite;
}

/* Sections */
.section { padding: 6rem 0; }

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
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: var(--foreground);
}

.section-desc {
  color: var(--text-secondary);
  font-size: 1.125rem;
  max-width: 42rem;
  margin-bottom: 3rem;
  line-height: 1.7;
}

.max-w-6xl { max-width: 72rem; margin: 0 auto; }

/* Lab Photo Section */
.lab-photo {
  background: #FFFFFF;
  padding: 1rem 0 3rem 0;
}

.lab-photo-container {
  max-width: 100%;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
}

.lab-photo-img {
  width: 100%;
  height: auto;
  display: block;
}

/* Research - Lab Livre Style */
.research { 
  background: #FFFFFF;
  padding: 5rem 0;
}

.research .section-title {
  color: #000000;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 3rem;
  text-align: center;
}

.research-grid {
  display: grid;
  gap: 2.5rem 3.5rem;
  grid-template-columns: 1fr;
  max-width: 1200px;
  margin: 0 auto;
}

@media (min-width: 768px) { 
  .research-grid { 
    grid-template-columns: repeat(2, 1fr); 
  } 
}

.research-card {
  padding: 0;
  background: transparent;
  border: none;
  text-align: left;
  transition: transform 0.3s ease;
}

.research-card:hover {
  transform: translateY(-3px);
}

.research-icon {
  display: none;
}

.research-title {
  font-family: var(--font-body);
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: #000000;
  text-decoration: underline;
  text-decoration-thickness: 3px;
  text-underline-offset: 8px;
}

.research-card .research-title {
  text-decoration-color: var(--primary);
}

.research-desc {
  color: #000000;
  font-size: 1rem;
  margin-bottom: 0;
  line-height: 1.6;
}

.research-link {
  display: none;
}

/* Publications - Lab Livre Style (news-card) */
.publications { 
  background: #FFFFFF; 
  padding: 5rem 0;
}

.publications .section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #000000;
  text-align: center;
  margin-bottom: 3rem;
}

.publications-grid { 
  display: grid; 
  gap: 1.5rem;
  max-width: 1200px;
  margin: 0 auto;
}

@media (min-width: 768px) { .publications-grid { grid-template-columns: repeat(3, 1fr); } }

.pub-card {
  background: #ffffff;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.pub-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.pub-card-header {
  position: relative;
  height: 180px;
  background: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  overflow: hidden;
}

.pub-card-icon {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 4rem;
  color: rgba(255, 255, 255, 0.9);
}

.pub-card-icon img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.pub-card-body {
  padding: 30px;
  flex: 1;
  display: flex;
  flex-direction: column;
  background: #f5f5f5;
  position: relative;
}

/* Simple Publication Card (no image) */
.pub-card-simple {
  background: transparent;
  padding: 1rem 0;
  border: none;
}

.pub-card-simple:hover .pub-title a {
  color: var(--primary);
}

.section-more {
  text-align: center;
  margin-top: 2rem;
}

.section-more-link {
  color: var(--primary);
  font-weight: 600;
  text-decoration: none;
  font-size: 1rem;
  transition: color 0.3s ease;
}

.section-more-link:hover {
  color: var(--primary-dark);
  text-decoration: underline;
}

.pub-card-date {
  font-size: 14px;
  color: #666666;
  margin: 0 0 12px 0;
  font-weight: 400;
}

.pub-title {
  font-size: 18px;
  font-weight: 700;
  line-height: 1.4;
  color: var(--primary);
  margin: 0 0 12px 0;
  flex: 1;
}

.pub-title a {
  color: var(--primary);
  text-decoration: none;
  transition: color 0.3s ease;
}

.pub-title a:hover {
  color: var(--primary-dark);
  text-decoration: underline;
}

.pub-card-description {
  font-size: 14px;
  font-weight: 400;
  line-height: 1.6;
  color: #666666;
  margin: 0 0 20px 0;
}

.pub-card-arrow {
  align-self: flex-end;
  color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  transition: transform 0.3s ease;
}

.pub-card-arrow a {
  color: var(--primary);
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pub-card:hover .pub-card-arrow {
  transform: translateX(5px);
}

/* Legacy pub-card styles for compatibility */
.pub-card.featured { border-left: 4px solid var(--primary); }

.pub-badge {
  display: inline-block;
  background: var(--primary);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.pub-authors { color: #666666; font-size: 0.9rem; margin-bottom: 0.5rem; }

.pub-venue { color: #666666; font-style: italic; font-size: 0.875rem; margin-bottom: 1rem; }

.pub-meta {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #e0e0e0;
}

.pub-citations { font-family: var(--font-body); font-size: 1.25rem; font-weight: 700; color: var(--primary); }

.pub-citations-label { color: #666666; font-size: 0.75rem; }

.pub-link { color: var(--primary); font-weight: 600; font-size: 0.875rem; margin-left: auto; }
.pub-link:hover { color: var(--primary-dark); text-decoration: underline; }

/* Courses */
.courses { background: #ffffff; }

.courses-grid {
  display: grid;
  gap: 1.5rem;
}

@media (min-width: 768px) { .courses-grid { grid-template-columns: repeat(3, 1fr); } }

.course-card {
  background: #ffffff;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
  text-decoration: none;
  display: block;
}

.course-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 102, 204, 0.15);
  border-color: var(--primary);
}

.course-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.course-card h3 {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--foreground);
  margin-bottom: 0.75rem;
  line-height: 1.3;
}

.course-card p {
  color: var(--text-secondary);
  font-size: 0.9rem;
  line-height: 1.5;
  margin-bottom: 1rem;
}

.course-link {
  color: var(--primary);
  font-weight: 600;
  font-size: 0.9rem;
}

.course-card:hover .course-link {
  text-decoration: underline;
}

/* Projects */
.projects { background: #FFFFFF; }

.projects-grid { display: grid; gap: 2rem; }

@media (min-width: 768px) { .projects-grid { grid-template-columns: repeat(2, 1fr); } }

.project-card {
  border-radius: 1rem;
  overflow: hidden;
  background: #FFFFFF;
  border: none;
  transition: all 0.5s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.project-card:hover {
  border-color: var(--primary);
  box-shadow: 0 8px 24px rgba(0, 102, 204, 0.15);
}

.project-header {
  background: var(--primary);
  padding: 1.5rem;
  color: white;
}

.project-badge {
  display: inline-block;
  background: rgba(255, 255, 255, 0.2);
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
}

.project-header h3 {
  font-family: var(--font-body);
  font-size: 1.25rem;
  font-weight: 700;
}

.project-content { padding: 1.5rem; }

.project-authors { color: #666666; font-size: 0.9rem; font-style: italic; margin-bottom: 1rem; }

.project-desc { color: #666666; font-size: 0.9rem; margin-bottom: 1.5rem; }

.project-meta { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.5rem; }

.project-tag {
  padding: 0.25rem 0.75rem;
  font-size: 0.75rem;
  background: #f0f0f0;
  color: #333333;
  border-radius: 0.375rem;
}

.project-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--primary);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.project-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 102, 204, 0.3);
  color: white;
}

/* Contact */
.contact { background: #FFFFFF; }

.contact-grid { display: grid; gap: 3rem; }

@media (min-width: 1024px) { .contact-grid { grid-template-columns: 1fr 1fr; } }

.contact-info-list { display: flex; flex-direction: column; gap: 1.5rem; }

.contact-info-item { display: flex; align-items: center; gap: 1rem; transition: color 0.3s ease; text-decoration: none; color: inherit; }

.contact-info-item:hover { color: var(--primary); }

.contact-info-icon {
  width: 3rem;
  height: 3rem;
  border-radius: 0.75rem;
  background: var(--card-bg);
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
}

.contact-info-label { font-size: 0.875rem; color: var(--text-secondary); }

.contact-info-value { font-weight: 600; color: var(--foreground); }

.social-links { display: flex; gap: 1rem; margin-top: 2rem; }

.social-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  background: var(--card-bg);
  border: none;
  font-size: 0.9rem;
  color: var(--text-secondary);
  text-decoration: none;
  transition: all 0.3s ease;
}

.social-link:hover {
  border-color: var(--primary);
  background: rgba(0, 102, 204, 0.1);
  color: var(--primary);
}

/* Contact Compact Layout */
.contact-compact {
  text-align: center;
}

.contact-info-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 1rem;
}

.contact-info-row .contact-info-item {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  background: var(--card-bg);
  border: none;
  text-decoration: none;
  color: var(--foreground);
  transition: all 0.3s ease;
}

.contact-info-row .contact-info-item:hover {
  border-color: var(--primary);
  color: var(--primary);
}

.contact-info-row .contact-info-icon {
  font-size: 1rem;
}

.contact-info-row .contact-info-value {
  font-size: 0.9rem;
  font-weight: 500;
}

.contact-subtitle {
  color: var(--text-secondary);
  font-size: 1rem;
  text-align: center;
  margin-bottom: 1.5rem;
}

.contact-link {
  color: var(--primary);
  text-decoration: none;
  font-size: 0.95rem;
  transition: color 0.3s ease;
}

.contact-link:hover {
  color: var(--primary-dark);
  text-decoration: underline;
}

/* Footer Logos */
.footer-logos {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 3rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
}

.footer-logo-link {
  display: flex;
  align-items: center;
  opacity: 0.7;
  transition: opacity 0.3s ease;
}

.footer-logo-link:hover {
  opacity: 1;
}

.footer-logo {
  height: 50px;
  width: auto;
}

.contact-box {
  padding: 2rem;
  border-radius: 1rem;
  background: var(--card-bg);
  border: none;
}

.contact-box-title {
  font-family: var(--font-body);
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--foreground);
}

.contact-box-desc { color: var(--text-secondary); margin-bottom: 1.5rem; line-height: 1.6; }

.footer-bar {
  margin-top: 4rem;
  padding-top: 2rem;
  border-top: 1px solid var(--border);
  text-align: center;
}

.footer-copyright { color: var(--text-secondary); font-size: 0.875rem; }

/* Responsive - Mobile First */
@media (max-width: 480px) {
  .home-wrapper { margin: -1rem; }
  .container { padding: 0 1rem; }
  .hero { min-height: auto; padding: 3rem 0 2rem 0; }
  .hero-content { padding: 1.5rem 1rem; }
  .hero-title { font-size: 1.75rem; }
  .hero-subtitle { font-size: 0.75rem; letter-spacing: 0.2em; }
  .hero-bio { font-size: 1rem; margin-bottom: 1.5rem; }
  .hero-buttons { flex-direction: column; gap: 0.75rem; }
  .btn-elegant { width: 100%; justify-content: center; padding: 0.75rem 1.25rem; }
  .hero-stats { grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 2rem; }
  .hero-stat-number { font-size: 1.5rem; }
  .hero-stat-label { font-size: 0.75rem; }
  .scroll-indicator { display: none; }
  .section { padding: 2.5rem 0; }
  .section-title { font-size: 1.5rem; }
  .section-desc { font-size: 1rem; margin-bottom: 2rem; }
  .research-grid { gap: 1.5rem; }
  .research-title { font-size: 1.25rem; }
  .research-desc { font-size: 0.9rem; }
  .publications-grid { gap: 1rem; }
  .pub-card-simple { padding: 0.75rem 0; }
  .pub-title { font-size: 1rem; }
  .pub-card-date { font-size: 0.8rem; }
  .pub-card-description { font-size: 0.85rem; }
  .projects-grid { gap: 1.5rem; }
  .project-header { padding: 1rem; }
  .project-header h3 { font-size: 1.1rem; }
  .project-content { padding: 1rem; }
  .project-desc { font-size: 0.85rem; }
  .project-link { padding: 0.6rem 1rem; font-size: 0.85rem; }
  .courses-grid { grid-template-columns: 1fr; gap: 1rem; }
  .course-card { padding: 1.25rem; }
  .course-icon { font-size: 2rem; }
  .course-card h3 { font-size: 1rem; }
  .contact-info-row { flex-direction: column; gap: 0.75rem; }
  .footer-logos { flex-direction: column; gap: 1.5rem; }
  .footer-logo { height: 40px; }
  .lab-photo { padding: 0.5rem 0 2rem 0; }
}

@media (min-width: 481px) and (max-width: 768px) {
  .home-wrapper { margin: -1.5rem; }
  .hero { min-height: auto; padding: 4rem 0 3rem 0; }
  .hero-title { font-size: 2.25rem; }
  .hero-stats { grid-template-columns: repeat(2, 1fr); }
  .section { padding: 3rem 0; }
  .section-title { font-size: 1.75rem; }
  .research-grid { grid-template-columns: 1fr; }
  .publications-grid { grid-template-columns: 1fr; }
  .projects-grid { grid-template-columns: 1fr; }
  .courses-grid { grid-template-columns: 1fr; }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .hero-title { font-size: 3rem; }
  .section { padding: 4rem 0; }
  .research-grid { grid-template-columns: repeat(2, 1fr); }
}
</style>

<div class="home-wrapper">

<section class="hero">
  <div class="hero-bg-circle hero-bg-circle-1"></div>
  <div class="hero-bg-circle hero-bg-circle-2"></div>
  <div class="container">
    <div class="hero-content">
      <p class="hero-subtitle">Professora de Engenharia de Software</p>
      <h1 class="hero-title">Profa. Carla <span class="text-gradient">Rocha</span></h1>
      <p class="hero-bio">Professora no curso de Engenharia de Software (UnB) e coordenadora do <a href="https://lablivre.unb.br/" target="_blank">Lab Livre</a>. Pesquisa dedicada ao desenvolvimento de soluções tecnológicas com impacto social, promovendo software livre, práticas ágeis e inovação no setor público.</p>
    </div>
  </div>
</section>

<section class="section lab-photo">
  <div class="container"><div class="max-w-6xl">
    <div class="lab-photo-container">
      <a href="https://lablivre.unb.br/" target="_blank"><img src="/images/lab.png" alt="Lab Livre - Equipe" class="lab-photo-img"></a>
    </div>
  </div></div>
</section>

<section class="section research">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Linhas de Pesquisa</span></div>
    <div class="research-grid">
      <article class="research-card">
        <h3 class="research-title">DevOps</h3>
        <p class="research-desc">Estudo e aplicação de práticas, estruturas de times que integram desenvolvimento e operações para melhorar a entrega contínua, qualidade e confiabilidade de software.</p>
      </article>
      <article class="research-card">
        <h3 class="research-title">MLOps</h3>
        <p class="research-desc">Pesquisa sobre processos, ferramentas e automações para desenvolvimento, implantação, monitoramento e governança de modelos de aprendizado de máquina em produção.</p>
      </article>
      <article class="research-card">
        <h3 class="research-title">Engenharia de Dados</h3>
        <p class="research-desc">Investigação de arquiteturas, pipelines e governança de dados para coleta, integração, qualidade e análise em larga escala.</p>
      </article>
      <article class="research-card">
        <h3 class="research-title">Aprendizado por Experiência</h3>
        <p class="research-desc">Abordagens de ensino e formação baseadas na prática, experimentação e resolução de problemas reais em contextos acadêmicos e profissionais.</p>
      </article>
      <article class="research-card">
        <h3 class="research-title">Metodologia de Co-desenvolvimento</h3>
        <p class="research-desc">Métodos colaborativos de desenvolvimento de software envolvendo pesquisadores, estudantes, usuários e parceiros institucionais.</p>
      </article>
      <article class="research-card">
        <h3 class="research-title">Ecossistemas de Software Livre</h3>
        <p class="research-desc">Estudo da dinâmica técnica, organizacional e social de comunidades e plataformas de software livre, com foco em sustentabilidade e impacto.</p>
      </article>
      <article class="research-card">
        <h3 class="research-title">Participação Digital</h3>
        <p class="research-desc">Pesquisa sobre tecnologias e métodos para ampliar, qualificar e analisar a participação cidadã em processos digitais de tomada de decisão.</p>
      </article>
    </div>
    <div class="section-more">
      <a href="/projects/" class="section-more-link">Saiba mais →</a>
    </div>
  </div></div>
</section>

<section class="section publications">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Produção Científica</span></div>
    <div class="publications-grid">
      <article class="pub-card-simple">
        <p class="pub-card-date">ACM Computing Surveys, 2019</p>
        <h3 class="pub-title"><a href="https://dl.acm.org/doi/abs/10.1145/3359981" target="_blank">A Survey of DevOps Concepts and Challenges</a></h3>
        <p class="pub-card-description">L Leite, C Rocha, F Kon, D Milojicic, P Meirelles. Artigo com mais de 676 citações investigando desafios de DevOps.</p>
      </article>
      <article class="pub-card-simple">
        <p class="pub-card-date">IEEE/ACM ICSE-SEET, 2021</p>
        <h3 class="pub-title"><a href="/publications/" target="_blank">Qualifying Software Engineers Undergraduates in DevOps</a></h3>
        <p class="pub-card-description">I Alves, C Rocha. Metodologia de qualificação de engenheiros de software em práticas DevOps. 26 citações.</p>
      </article>
      <article class="pub-card-simple">
        <p class="pub-card-date">Journal of Systems and Software, 2024</p>
        <h3 class="pub-title"><a href="/publications/" target="_blank">Harmonizing DevOps Taxonomies—A Grounded Theory Study</a></h3>
        <p class="pub-card-description">J Díaz, J Pérez, I Alves, F Kon, L Leite, P Meirelles, C Rocha. Estudo sobre taxonomias DevOps. 18 citações.</p>
      </article>
    </div>
    <div class="section-more">
      <a href="/publications/" class="section-more-link">Saiba mais →</a>
    </div>
  </div></div>
</section>

<section class="section courses">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Ensino</span></div>
    <div class="courses-grid">
      <a href="https://mds.lappis.rocks/" target="_blank" class="course-card">
        <h3>Métodos de Desenvolvimento de Software</h3>
        <p>Metodologias ágeis, práticas de desenvolvimento e gestão de projetos de software.</p>
        <span class="course-link">Acessar →</span>
      </a>
      <a href="https://github.com/FGA-GCES" target="_blank" class="course-card">
        <h3>Gerência de Configuração e Evolução de Software</h3>
        <p>Controle de versão, integração contínua, DevOps e evolução de sistemas.</p>
        <span class="course-link">Acessar →</span>
      </a>
      <a href="https://unb-sistemas-de-machine-learning.github.io/Disciplina/" target="_blank" class="course-card">
        <h3>Sistemas de Machine Learning</h3>
        <p>MLOps, pipelines de ML, deploy e monitoramento de modelos em produção.</p>
        <span class="course-link">Acessar →</span>
      </a>
    </div>
    <div class="section-more">
      <a href="/teaching/" class="section-more-link">Ver todas as disciplinas →</a>
    </div>
  </div></div>
</section>

<section class="section projects">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Livros</span></div>
    <p class="section-desc">Obras fundamentais para a modernização do setor público através de tecnologia e software livre.</p>
    <div class="projects-grid">
      <article class="project-card"><div class="project-header" style="padding: 0;"><img src="{{ site.baseurl }}/images/livro.png" alt="GovHub" style="width: 100%; height: 100%; object-fit: cover;"></div><div class="project-content"><p class="project-authors">Carla Rocha, Lab Livre UnB, IPEA</p><h3 style="margin-bottom: 0.5rem;">GovHub - Um guia prático para integração e qualificação de dados públicos</h3><p class="project-desc">Guia completo que apresenta metodologias e ferramentas práticas para transformar dados governamentais dispersos em informações estratégicas.</p><div class="project-meta"><span class="project-tag">2025</span><span class="project-tag">Livro</span><span class="project-tag">Disponível</span></div><a href="https://gov-hub.io/govhub/ebook-viewer/" class="project-link" target="_blank">📖 Acessar Guia →</a></div></article>
      <article class="project-card"><div class="project-header" style="padding: 0;"><img src="{{ site.baseurl }}/images/publico.png" alt="Dinheiro Público Código Público" style="width: 100%; height: 100%; object-fit: cover;"></div><div class="project-content"><h3 style="margin-bottom: 0.5rem;">Dinheiro Público Código Público - Modernizando a Infraestrutura Pública</h3><p class="project-desc">Obra fundamental sobre a aplicação de software livre no setor público, apresentando técnicas de aprendizagem experiencial e estratégias para modernização governamental.</p><div class="project-meta"><span class="project-tag">2023</span><span class="project-tag">E-book</span><span class="project-tag">FSFE</span></div><a href="https://download.fsfe.org/campaigns/pmpc/PMPC-Modernising-with-Free-Software.pt_br.pdf" class="project-link" target="_blank">📚 Ler Online →</a></div></article>
    </div>
  </div></div>
</section>

<section class="section contact" style="padding: 3rem 0;">
  <div class="container"><div class="max-w-6xl">
    <div class="section-header"><div class="section-line"></div><span class="section-label">Contato</span></div>
    <h2 class="section-title" style="margin-bottom: 1rem;">Vamos Colaborar?</h2>
    <p class="contact-subtitle">Oportunidades de Pesquisa: mestrado, doutorado e iniciação científica</p>
    <div class="contact-compact">
      <div class="contact-info-row">
        <a href="mailto:caguiar@unb.br" class="contact-link">✉️ caguiar@unb.br</a>
        <a href="https://scholar.google.com/citations?user=_y8XHnAAAAAJ&hl=pt-BR" target="_blank" class="contact-link">📊 Scholar</a>
        <a href="https://github.com/RochaCarla" target="_blank" class="contact-link">💻 GitHub</a>
      </div>

    </div>
  </div></div>
</section>

</div>
