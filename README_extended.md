# Guide des serveurs MCP pour Cursor

Ce dossier contient une collection étendue de 20 serveurs MCP (Model Context Protocol) pour Cursor, organisés en deux catégories principales : développement web et ingénierie IA.

## Qu'est-ce que MCP ?

Le Model Context Protocol (MCP) est un protocole ouvert qui permet aux modèles d'IA comme Claude d'interagir avec des outils et services externes. Dans Cursor, les serveurs MCP permettent d'étendre les capacités de l'éditeur en lui donnant accès à diverses sources de données et fonctionnalités.

## Structure du dossier

```
mcp_servers_for_cursor/
├── README.md                      # Ce fichier
├── serveurs_mcp_info.md           # Informations détaillées sur les 10 serveurs MCP initiaux
├── nouveaux_serveurs_info.md      # Informations détaillées sur les 11 serveurs MCP ajoutés
├── structure.md                   # Description de la structure du dossier
├── validation.md                  # Guide de validation des configurations
├── web_development/               # Serveurs MCP pour le développement web
│   ├── combined_web_mcp.json      # Configuration combinée des serveurs web initiaux
│   ├── combined_web_mcp_extended.json # Configuration combinée de tous les serveurs web
│   ├── firecrawl_mcp.json         # Configuration pour Firecrawl
│   ├── github_mcp.json            # Configuration pour GitHub
│   ├── vercel_mcp.json            # Configuration pour Vercel
│   ├── figma_context_mcp.json     # Configuration pour Figma Context
│   ├── stripe_mcp.json            # Configuration pour Stripe
│   ├── contentful_mcp.json        # Configuration pour Contentful (NOUVEAU)
│   ├── mongodb_mcp.json           # Configuration pour MongoDB (NOUVEAU)
│   ├── sentry_mcp.json            # Configuration pour Sentry (NOUVEAU)
│   ├── playwright_mcp.json        # Configuration pour Playwright (NOUVEAU)
│   └── firebase_mcp.json          # Configuration pour Firebase (NOUVEAU)
└── ai_engineering/                # Serveurs MCP pour l'ingénierie IA
    ├── combined_ai_mcp.json       # Configuration combinée des serveurs IA initiaux
    ├── combined_ai_mcp_extended.json # Configuration combinée de tous les serveurs IA
    ├── magic_mcp.json             # Configuration pour Magic
    ├── opik_mcp.json              # Configuration pour Opik
    ├── browserbase_mcp.json       # Configuration pour Browserbase
    ├── postgresql_mcp.json        # Configuration pour PostgreSQL
    ├── qdrant_mcp.json            # Configuration pour Qdrant
    ├── screenshotone_mcp.json     # Configuration pour ScreenshotOne (NOUVEAU)
    ├── stabilityai_mcp.json       # Configuration pour Stability AI (NOUVEAU)
    ├── huggingface_mcp.json       # Configuration pour Hugging Face (NOUVEAU)
    ├── agentql_mcp.json           # Configuration pour AgentQL (NOUVEAU)
    ├── hyperbrowser_mcp.json      # Configuration pour Hyperbrowser (NOUVEAU)
    └── magicai_mcp.json           # Configuration pour Magic AI Agent (NOUVEAU)
```

## Comment utiliser ces serveurs MCP

1. Ouvrez Cursor et accédez aux paramètres (Settings)
2. Naviguez vers Features > MCP
3. Cliquez sur "+ Add New MCP Server"
4. Copiez le contenu du fichier JSON correspondant au serveur que vous souhaitez ajouter
5. Collez-le dans la configuration et sauvegardez

Pour utiliser plusieurs serveurs simultanément, vous pouvez utiliser les fichiers de configuration combinés :
- `combined_web_mcp_extended.json` pour tous les serveurs de développement web
- `combined_ai_mcp_extended.json` pour tous les serveurs d'ingénierie IA

## Serveurs MCP pour le développement web

### Collection initiale
1. **Firecrawl** - Transformation de sites web entiers en données pour LLM
2. **GitHub** - Interaction avec l'API GitHub pour la gestion de code
3. **Vercel** - Déploiement et gestion d'applications sur Vercel
4. **Figma Context** - Accès aux données de design Figma pour l'implémentation précise
5. **Stripe** - Interaction avec l'API Stripe pour les paiements

### Nouveaux serveurs
6. **Contentful** - Gestion de contenu CMS structuré
7. **MongoDB** - Interaction avec les bases de données NoSQL MongoDB
8. **Sentry** - Monitoring et suivi des erreurs d'application
9. **Playwright** - Automatisation des tests UI et API
10. **Firebase** - Authentification et services Firebase

## Serveurs MCP pour l'ingénierie IA

### Collection initiale
1. **Magic** - Agent IA pour le développement
2. **Opik** - Intégration avec Comet ML pour le suivi d'expériences
3. **Browserbase** - Automatisation de navigateur cloud pour les LLM
4. **PostgreSQL** - Accès en lecture seule aux bases de données PostgreSQL
5. **Qdrant** - Implémentation de mémoire sémantique avec recherche vectorielle

### Nouveaux serveurs
6. **ScreenshotOne** - Capture et analyse d'écrans de sites web
7. **Stability AI** - Génération et édition d'images haute qualité
8. **Hugging Face** - Accès aux modèles, datasets et espaces Hugging Face
9. **AgentQL** - Extraction de données structurées à partir du web
10. **Hyperbrowser** - Navigateurs cloud pour les agents IA
11. **Magic AI Agent** - Création de composants UI à partir de descriptions en langage naturel

## Remarques importantes

- Chaque serveur MCP nécessite généralement une clé API ou un token d'authentification
- Remplacez les valeurs "your_xxx_here" par vos propres clés API
- Certains serveurs peuvent nécessiter une configuration supplémentaire
- Consultez les fichiers `serveurs_mcp_info.md` et `nouveaux_serveurs_info.md` pour plus de détails sur chaque serveur

Pour plus d'informations sur le protocole MCP, visitez [cursor.directory/mcp](https://cursor.directory/mcp)
