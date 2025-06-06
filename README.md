# 30 Meilleurs Serveurs MCP pour Cursor

Ce dépôt contient une collection soigneusement sélectionnée des 30 meilleurs serveurs MCP (Model Context Protocol) pour Cursor, organisés en trois catégories principales : développement web, ingénierie IA et productivité.

## Qu'est-ce que MCP?

Le Model Context Protocol (MCP) est un standard ouvert conçu pour faciliter l'interaction entre les grands modèles de langage (LLM) et des sources de données ou outils externes. Il fournit une méthode standardisée permettant aux modèles d'IA de se connecter à diverses sources de données et outils, évitant ainsi les implémentations personnalisées qui causent de la fragmentation.

MCP agit comme une interface universelle (comparable à un port USB-C pour les applications d'IA), standardisant la façon dont les applications fournissent du contexte aux LLM. Ce protocole représente un changement fondamental dans la façon dont nous construisons des applications agentiques, passant de connexions isolées et propriétaires à un écosystème ouvert et connecté.

## Contenu du dépôt

```
mcp_servers_for_cursor/
├── serveurs_mcp_info.md       # Documentation détaillée sur les 10 serveurs MCP initiaux
├── nouveaux_serveurs_info.md  # Documentation détaillée sur les 11 serveurs MCP ajoutés (2e phase)
├── serveurs_mcp_productivite.md # Documentation détaillée sur les 10 serveurs MCP de productivité (3e phase)
├── structure_updated.md       # Description de la structure du dossier
├── validation.md              # Validation des configurations
├── web_development/           # Serveurs MCP pour le développement web
│   ├── firecrawl_mcp.json     # Configuration pour Firecrawl (web scraping)
│   ├── github_mcp.json        # Configuration pour GitHub
│   ├── vercel_mcp.json        # Configuration pour Vercel API
│   ├── figma_context_mcp.json # Configuration pour Figma Context
│   ├── stripe_mcp.json        # Configuration pour Stripe
│   ├── contentful_mcp.json    # Configuration pour Contentful (NOUVEAU)
│   ├── mongodb_mcp.json       # Configuration pour MongoDB (NOUVEAU)
│   ├── sentry_mcp.json        # Configuration pour Sentry (NOUVEAU)
│   ├── playwright_mcp.json    # Configuration pour Playwright (NOUVEAU)
│   ├── firebase_mcp.json      # Configuration pour Firebase (NOUVEAU)
│   ├── combined_web_mcp.json  # Configuration combinée des serveurs web initiaux
│   └── combined_web_mcp_extended.json # Configuration combinée de tous les serveurs web
├── ai_engineering/            # Serveurs MCP pour l'ingénierie IA
│   ├── magic_mcp.json         # Configuration pour Magic (IA générative)
│   ├── opik_mcp.json          # Configuration pour Opik (suivi d'expériences)
│   ├── browserbase_mcp.json   # Configuration pour Browserbase (automatisation)
│   ├── postgresql_mcp.json    # Configuration pour PostgreSQL
│   ├── qdrant_mcp.json        # Configuration pour Qdrant (recherche vectorielle)
│   ├── screenshotone_mcp.json # Configuration pour ScreenshotOne (NOUVEAU)
│   ├── stabilityai_mcp.json   # Configuration pour Stability AI (NOUVEAU)
│   ├── huggingface_mcp.json   # Configuration pour Hugging Face (NOUVEAU)
│   ├── agentql_mcp.json       # Configuration pour AgentQL (NOUVEAU)
│   ├── hyperbrowser_mcp.json  # Configuration pour Hyperbrowser (NOUVEAU)
│   ├── magicai_mcp.json       # Configuration pour Magic AI Agent (NOUVEAU)
│   ├── combined_ai_mcp.json   # Configuration combinée des serveurs IA initiaux
│   └── combined_ai_mcp_extended.json # Configuration combinée de tous les serveurs IA
└── productivity/              # Serveurs MCP pour la productivité (NOUVEAU)
    ├── jira_mcp.json          # Configuration pour Jira
    ├── asana_mcp.json         # Configuration pour Asana
    ├── notion_mcp.json        # Configuration pour Notion
    ├── slack_mcp.json         # Configuration pour Slack
    ├── google_workspace_mcp.json # Configuration pour Google Workspace
    ├── azure_devops_mcp.json  # Configuration pour Azure DevOps
    ├── google_ads_mcp.json    # Configuration pour Google Ads
    ├── osp_marketing_mcp.json # Configuration pour OSP Marketing Tools
    ├── timezone_mcp.json      # Configuration pour Timezone
    ├── zapier_mcp.json        # Configuration pour Zapier
    └── combined_productivity_mcp.json # Configuration combinée des serveurs de productivité
```

## Serveurs MCP inclus

### Pour le développement web (10 serveurs)

#### Collection initiale
1. **Firecrawl MCP** - Solution complète de web scraping
2. **GitHub MCP** - Gestion de dépôts et intégration avec l'API GitHub
3. **Vercel API MCP** - Gestion des déploiements et des projets Vercel
4. **Figma Context MCP** - Intégration des designs Figma dans le flux de développement
5. **Stripe MCP** - Intégration des paiements et gestion des clients

#### Nouveaux serveurs
6. **Contentful MCP** - Gestion de contenu CMS structuré
7. **MongoDB MCP** - Interaction avec les bases de données NoSQL MongoDB
8. **Sentry MCP** - Monitoring et suivi des erreurs d'application
9. **Playwright MCP** - Automatisation des tests UI et API
10. **Firebase MCP** - Authentification et services Firebase

### Pour l'ingénierie IA (10 serveurs)

#### Collection initiale
1. **Magic MCP** - Capacités d'IA générative (images, texte, code)
2. **Opik MCP** - Suivi d'expériences pour les projets de machine learning
3. **Browserbase MCP** - Automatisation de navigateur cloud
4. **PostgreSQL MCP** - Accès aux bases de données pour l'analyse de données
5. **Qdrant MCP** - Recherche vectorielle pour les applications d'IA sémantique

#### Nouveaux serveurs
6. **ScreenshotOne MCP** - Capture et analyse d'écrans de sites web
7. **Stability AI MCP** - Génération et édition d'images haute qualité
8. **Hugging Face MCP** - Accès aux modèles, datasets et espaces Hugging Face
9. **AgentQL MCP** - Extraction de données structurées à partir du web
10. **Hyperbrowser MCP** - Navigateurs cloud pour les agents IA
11. **Magic AI Agent MCP** - Création de composants UI à partir de descriptions en langage naturel

### Pour la productivité (10 serveurs)

#### Gestion de projet et collaboration
1. **Jira MCP** - Suivi des problèmes, planification des sprints et gestion de projet
2. **Asana MCP** - Gestion des tâches et des projets
3. **Notion MCP** - Création et modification de pages, gestion des bases de données
4. **Slack MCP** - Communication d'équipe et gestion des canaux

#### Outils bureautiques et développement
5. **Google Workspace MCP** - Intégration avec Gmail, Calendar et Drive
6. **Azure DevOps MCP** - Gestion des projets, des éléments de travail et des pipelines CI/CD

#### Marketing et analytique
7. **Google Ads MCP** - Analyse des données publicitaires et des campagnes
8. **OSP Marketing Tools MCP** - Création et optimisation de contenu technique

#### Utilitaires et automatisation
9. **Timezone MCP** - Conversion de fuseaux horaires et calculs de temps localisés
10. **Zapier MCP** - Intégration avec plus de 7000 applications et automatisation de tâches

## Guide d'installation

### Prérequis

Avant d'ajouter des serveurs MCP, assurez-vous d'avoir installé les outils nécessaires :

- **Node.js** (≥ v18, LTS recommandé)
- **Python** (pour certains serveurs comme PostgreSQL MCP)
- **UV** (pour les serveurs Python)
- **Cursor** (dernière version)

### Installation de Node.js et npx

**Pour Windows :**
1. Téléchargez l'installateur depuis [nodejs.org](https://nodejs.org/)
2. Exécutez l'installateur et suivez les instructions
3. Vérifiez l'installation en ouvrant l'invite de commande et en tapant :
   ```
   node --version
   npx --version
   ```

**Pour macOS :**
1. Avec Homebrew (recommandé) :
   ```
   brew install node
   ```
2. Vérifiez l'installation dans le Terminal :
   ```
   node --version
   npx --version
   ```

### Installation de Python et UV

**Pour Windows :**
1. Téléchargez et installez Python depuis [python.org](https://python.org)
2. Ouvrez l'invite de commande et installez UV :
   ```
   pip install uv
   ```
3. Vérifiez l'installation :
   ```
   uv --version
   ```

**Pour macOS :**
1. Avec Homebrew :
   ```
   brew install python
   pip3 install uv
   ```
2. Vérifiez l'installation :
   ```
   uv --version
   ```

## Configuration des serveurs MCP dans Cursor

Cursor prend en charge deux approches principales pour configurer les serveurs MCP :

### Emplacements de configuration

Vous pouvez placer les configurations MCP à l'un de ces deux emplacements :

1. **Configuration de projet** : Créez un fichier `.cursor/mcp.json` dans votre répertoire de projet pour définir les serveurs MCP qui ne devraient être disponibles que dans ce projet spécifique.

2. **Configuration globale** : Créez un fichier `~/.cursor/mcp.json` dans votre répertoire personnel pour rendre les serveurs MCP disponibles dans tous vos projets Cursor.

### Comment configurer un serveur MCP

1. Choisissez les serveurs MCP qui correspondent à vos besoins
2. Copiez le fichier de configuration JSON correspondant depuis ce dépôt
3. Placez-le dans le dossier `.cursor/` (configuration de projet) ou `~/.cursor/` (configuration globale)
4. Renommez le fichier en `mcp.json`
5. Remplacez les valeurs d'API fictives (`your_api_key_here`, etc.) par vos propres clés d'API
6. Redémarrez Cursor pour activer les serveurs MCP

### Exemple : Configuration de Zapier MCP

1. Obtenez une URL MCP depuis [zapier.com/mcp](https://zapier.com/mcp)
2. Copiez le fichier `productivity/zapier_mcp.json` dans votre dossier `.cursor/`
3. Renommez-le en `mcp.json`
4. Modifiez le fichier pour inclure votre URL MCP :
   ```json
   {
     "mcpServers": {
       "zapier": {
         "command": "npx",
         "args": ["-y", "zapier-mcp-server"],
         "env": {
           "ZAPIER_MCP_URL": "votre_url_zapier_mcp_ici"
         }
       }
     }
   }
   ```
5. Redémarrez Cursor

### Configuration combinée

Si vous souhaitez utiliser plusieurs serveurs MCP simultanément, vous pouvez utiliser les fichiers combinés fournis :

- `web_development/combined_web_mcp_extended.json` - Pour tous les serveurs de développement web
- `ai_engineering/combined_ai_mcp_extended.json` - Pour tous les serveurs d'ingénierie IA
- `productivity/combined_productivity_mcp.json` - Pour tous les serveurs de productivité

Ou créer votre propre combinaison en fusionnant les configurations individuelles.

## Utilisation des serveurs MCP dans Cursor

Une fois configurés, vous pouvez utiliser les serveurs MCP de deux façons :

### Utilisation implicite

Cursor détectera automatiquement quand un serveur MCP peut être utile et suggérera son utilisation. Par exemple, si vous demandez à Cursor de rechercher des informations sur un site web, il pourrait suggérer d'utiliser Firecrawl MCP.

### Utilisation explicite

Vous pouvez également mentionner explicitement l'outil MCP que vous souhaitez utiliser dans vos prompts :

- "Utilise Firecrawl pour extraire des données de ce site web : example.com"
- "Utilise Magic MCP pour générer une image de placeholder pour cette section"
- "Utilise GitHub MCP pour rechercher des exemples de code d'authentification OAuth"
- "Utilise Jira MCP pour créer un ticket pour ce bug"
- "Utilise Zapier MCP pour automatiser l'envoi d'emails quand un commit est fait"

### Mode Yolo

## Vérification des serveurs MCP

Un script `validate_mcp_servers.py` est fourni pour vérifier si les paquets référencés dans les fichiers `*_mcp.json` existent sur npm ou PyPI. Exécutez :

```
python3 validate_mcp_servers.py
```

Le script parcourt tous les fichiers de configuration et indique `OK` si le paquet est disponible ou `MISSING` sinon. Les outils basés sur `npx` sont vérifiés sur npm, tandis que ceux exécutés via `uv run python -m` sont validés sur PyPI.


Pour une exécution automatique sans demande d'approbation, vous pouvez activer le "Mode Yolo" dans les paramètres de Cursor. Cela permet à l'agent d'exécuter des outils MCP sans demander votre approbation explicite pour chaque utilisation.

## Dépannage

### Problèmes courants et solutions

1. **Le serveur MCP n'apparaît pas dans Cursor**
   - Vérifiez que le fichier `mcp.json` est correctement placé
   - Assurez-vous que la syntaxe JSON est valide
   - Redémarrez Cursor

2. **Erreurs d'exécution du serveur MCP**
   - Vérifiez que vous avez installé les prérequis (Node.js, Python, UV)
   - Assurez-vous que les clés API sont valides
   - Consultez les logs de Cursor pour plus de détails

3. **Problème avec Browserbase MCP**
   - Ajustez le chemin dans `args` en fonction de votre installation locale

## Ressources supplémentaires

- [Documentation officielle MCP](https://mcp.anthropic.com/)
- [Cursor Directory](https://cursor.directory/mcp)
- [Awesome MCP Servers](https://github.com/awesome-mcp/awesome-mcp-servers)
- [Awesome MCP Clients](https://github.com/awesome-mcp/awesome-mcp-clients)
- [Zapier MCP](https://zapier.com/mcp)

## Licence

Ce dépôt est fourni à titre informatif et éducatif. Les serveurs MCP individuels peuvent avoir leurs propres licences et conditions d'utilisation. Veuillez consulter la documentation de chaque serveur pour plus de détails.

## Contact

Si vous avez des questions, souhaitez collaborer ou discuter de projets liés à l'IA, au développement web ou à l'utilisation de MCP avec Cursor, n'hésitez pas à me contacter :

**Nicolas Delrieu**
*AI Full Stack Senior Developer & Formateur*

*   **Email:** [nicolas@angkor-intelligence.com](mailto:nicolas@angkor-intelligence.com)
*   **Téléphone:** +855 92 332 554
*   **LinkedIn:** [linkedin.com/in/nicolas-delrieu-a61a60224](https://www.linkedin.com/in/nicolas-delrieu-a61a60224)
*   **Telegram:** [Contacter sur Telegram](https://t.me/+85592332554)
*   **GitHub:** [khopilot](https://github.com/khopilot) *(Assuming this is your GitHub profile based on the prompt)*

**Expertise:**
*   Intelligence Artificielle
*   Développement Web
*   Machine Learning
*   Prompt Engineering
*   React/Next.js
*   Python

---

Pour des informations détaillées sur les serveurs MCP initiaux, consultez le fichier [serveurs_mcp_info.md](./serveurs_mcp_info.md).
Pour des informations détaillées sur les nouveaux serveurs MCP pour le développement web et l'ingénierie IA, consultez le fichier [nouveaux_serveurs_info.md](./nouveaux_serveurs_info.md).
Pour des informations détaillées sur les serveurs MCP de productivité, consultez le fichier [serveurs_mcp_productivite.md](./serveurs_mcp_productivite.md).
