#!/usr/bin/env node

const https = require('https');
const fs = require('fs');
const path = require('path');

const ORG = 'unb-mds';
const TOKEN = process.env.GH_TOKEN || process.env.GITHUB_TOKEN;
const EXCLUDE_USERS = ['RochaCarla', 'carlarocha'];

if (!TOKEN) {
  console.error('❌ Erro: GH_TOKEN ou GITHUB_TOKEN não definido.');
  console.error('Execute: export GH_TOKEN="seu_token_aqui"');
  process.exit(1);
}

function githubRequest(endpoint) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'api.github.com',
      path: endpoint,
      headers: {
        'User-Agent': 'MDS-Graph-Miner',
        'Authorization': `token ${TOKEN}`,
        'Accept': 'application/vnd.github.v3+json'
      }
    };

    https.get(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        if (res.statusCode === 200) {
          resolve(JSON.parse(data));
        } else {
          reject(new Error(`GitHub API error: ${res.statusCode} - ${data}`));
        }
      });
    }).on('error', reject);
  });
}

async function getAllPages(endpoint) {
  let allData = [];
  let page = 1;
  
  while (true) {
    const separator = endpoint.includes('?') ? '&' : '?';
    const data = await githubRequest(`${endpoint}${separator}per_page=100&page=${page}`);
    if (data.length === 0) break;
    allData = allData.concat(data);
    page++;
    if (data.length < 100) break;
  }
  
  return allData;
}

async function mine() {
  console.log(`🔍 Minerando dados da organização ${ORG}...`);
  
  // Buscar repositórios
  console.log('📦 Buscando repositórios...');
  const repos = await getAllPages(`/orgs/${ORG}/repos`);
  console.log(`   Encontrados ${repos.length} repositórios`);
  
  const contributorsByRepo = {};
  const contributorData = {};
  
  // Buscar contribuidores de cada repo
  for (const repo of repos) {
    process.stdout.write(`\r🔄 Processando: ${repo.name.padEnd(40)}`);
    
    try {
      const contributors = await githubRequest(`/repos/${ORG}/${repo.name}/contributors?per_page=100`);
      contributorsByRepo[repo.name] = contributors
          .map(c => c.login)
          .filter(login => !EXCLUDE_USERS.includes(login));
      
      for (const c of contributors.filter(c => !EXCLUDE_USERS.includes(c.login))) {
        if (!contributorData[c.login]) {
          contributorData[c.login] = {
            id: c.login,
            avatar: c.avatar_url,
            url: c.html_url,
            repos: []
          };
        }
        contributorData[c.login].repos.push(repo.name);
      }
    } catch (e) {
      // Repo vazio ou sem acesso
    }
    
    // Rate limiting
    await new Promise(r => setTimeout(r, 100));
  }
  
  console.log('\n✅ Coleta finalizada!');
  
  // Construir nós
  const nodes = Object.values(contributorData).map(c => ({
    id: c.id,
    avatar: c.avatar,
    url: c.url,
    repoCount: c.repos.length,
    repos: c.repos
  }));
  
  // Construir arestas (contribuidores que trabalharam no mesmo repo)
  const edges = [];
  const edgeSet = new Set();
  
  for (const [repoName, contributors] of Object.entries(contributorsByRepo)) {
    for (let i = 0; i < contributors.length; i++) {
      for (let j = i + 1; j < contributors.length; j++) {
        const [a, b] = [contributors[i], contributors[j]].sort();
        const key = `${a}-${b}`;
        
        if (!edgeSet.has(key)) {
          edgeSet.add(key);
          edges.push({
            source: a,
            target: b,
            repos: [repoName]
          });
        } else {
          const edge = edges.find(e => 
            (e.source === a && e.target === b) || 
            (e.source === b && e.target === a)
          );
          if (edge && !edge.repos.includes(repoName)) {
            edge.repos.push(repoName);
          }
        }
      }
    }
  }
  
  const graphData = {
    nodes,
    edges,
    metadata: {
      organization: ORG,
      totalContributors: nodes.length,
      totalConnections: edges.length,
      totalRepos: repos.length,
      minedAt: new Date().toISOString()
    }
  };
  
  // Salvar
  const outputPath = path.join(__dirname, 'graph-data.json');
  fs.writeFileSync(outputPath, JSON.stringify(graphData, null, 2));
  
  console.log(`\n📊 Estatísticas:`);
  console.log(`   - Contribuidores: ${nodes.length}`);
  console.log(`   - Conexões: ${edges.length}`);
  console.log(`   - Repositórios: ${repos.length}`);
  console.log(`\n💾 Dados salvos em: ${outputPath}`);
}

mine().catch(err => {
  console.error('\n❌ Erro:', err.message);
  process.exit(1);
});
