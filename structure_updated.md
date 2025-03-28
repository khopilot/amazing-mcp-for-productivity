# Structure du dossier MCP Servers pour Cursor

Cette structure organise les 30 serveurs MCP (Model Context Protocol) pour Cursor en trois catégories principales : développement web, ingénierie IA et productivité.

```
mcp_servers_for_cursor/
├── README.md                      # Documentation principale
├── serveurs_mcp_info.md           # Informations sur les 10 serveurs MCP initiaux
├── nouveaux_serveurs_info.md      # Informations sur les 11 serveurs MCP ajoutés (2e phase)
├── serveurs_mcp_productivite.md   # Informations sur les 10 serveurs MCP de productivité (3e phase)
├── structure.md                   # Ce fichier décrivant la structure
├── validation.md                  # Guide de validation des configurations
├── web_development/               # Serveurs MCP pour le développement web (10)
│   ├── combined_web_mcp.json      # Configuration combinée des serveurs web initiaux
│   ├── combined_web_mcp_extended.json # Configuration combinée de tous les serveurs web
│   ├── firecrawl_mcp.json         # Configuration pour Firecrawl
│   ├── github_mcp.json            # Configuration pour GitHub
│   ├── vercel_mcp.json            # Configuration pour Vercel
│   ├── figma_context_mcp.json     # Configuration pour Figma Context
│   ├── stripe_mcp.json            # Configuration pour Stripe
│   ├── contentful_mcp.json        # Configuration pour Contentful
│   ├── mongodb_mcp.json           # Configuration pour MongoDB
│   ├── sentry_mcp.json            # Configuration pour Sentry
│   ├── playwright_mcp.json        # Configuration pour Playwright
│   └── firebase_mcp.json          # Configuration pour Firebase
├── ai_engineering/                # Serveurs MCP pour l'ingénierie IA (10)
│   ├── combined_ai_mcp.json       # Configuration combinée des serveurs IA initiaux
│   ├── combined_ai_mcp_extended.json # Configuration combinée de tous les serveurs IA
│   ├── magic_mcp.json             # Configuration pour Magic
│   ├── opik_mcp.json              # Configuration pour Opik
│   ├── browserbase_mcp.json       # Configuration pour Browserbase
│   ├── postgresql_mcp.json        # Configuration pour PostgreSQL
│   ├── qdrant_mcp.json            # Configuration pour Qdrant
│   ├── screenshotone_mcp.json     # Configuration pour ScreenshotOne
│   ├── stabilityai_mcp.json       # Configuration pour Stability AI
│   ├── huggingface_mcp.json       # Configuration pour Hugging Face
│   ├── agentql_mcp.json           # Configuration pour AgentQL
│   ├── hyperbrowser_mcp.json      # Configuration pour Hyperbrowser
│   └── magicai_mcp.json           # Configuration pour Magic AI Agent
└── productivity/                  # Serveurs MCP pour la productivité (10)
    ├── combined_productivity_mcp.json # Configuration combinée des serveurs de productivité
    ├── jira_mcp.json              # Configuration pour Jira
    ├── asana_mcp.json             # Configuration pour Asana
    ├── notion_mcp.json            # Configuration pour Notion
    ├── slack_mcp.json             # Configuration pour Slack
    ├── google_workspace_mcp.json  # Configuration pour Google Workspace
    ├── azure_devops_mcp.json      # Configuration pour Azure DevOps
    ├── google_ads_mcp.json        # Configuration pour Google Ads
    ├── osp_marketing_mcp.json     # Configuration pour OSP Marketing Tools
    ├── timezone_mcp.json          # Configuration pour Timezone
    └── zapier_mcp.json            # Configuration pour Zapier
```

## Organisation des serveurs MCP

### Développement Web (10 serveurs)
- **Collection initiale** : Firecrawl, GitHub, Vercel, Figma Context, Stripe
- **Nouveaux serveurs** : Contentful, MongoDB, Sentry, Playwright, Firebase

### Ingénierie IA (10 serveurs)
- **Collection initiale** : Magic, Opik, Browserbase, PostgreSQL, Qdrant
- **Nouveaux serveurs** : ScreenshotOne, Stability AI, Hugging Face, AgentQL, Hyperbrowser, Magic AI Agent

### Productivité (10 serveurs)
- **Gestion de projet** : Jira, Asana
- **Collaboration** : Notion, Slack
- **Outils bureautiques** : Google Workspace
- **Développement** : Azure DevOps
- **Marketing** : Google Ads, OSP Marketing Tools
- **Utilitaires** : Timezone
- **Automatisation** : Zapier

## Fichiers de configuration combinés

Pour faciliter l'utilisation de plusieurs serveurs MCP simultanément, trois fichiers de configuration combinés sont fournis :

1. `web_development/combined_web_mcp_extended.json` - Tous les serveurs de développement web
2. `ai_engineering/combined_ai_mcp_extended.json` - Tous les serveurs d'ingénierie IA
3. `productivity/combined_productivity_mcp.json` - Tous les serveurs de productivité

Ces fichiers permettent d'activer rapidement tous les serveurs d'une catégorie sans avoir à configurer chaque serveur individuellement.
