# Structure du dossier MCP Servers pour Cursor

Ce dossier contient une collection des 10 meilleurs serveurs MCP (Model Context Protocol) pour Cursor, organisés pour faciliter leur utilisation en tant que développeur web et ingénieur IA.

## Organisation du dossier

```
mcp_servers_for_cursor/
├── serveurs_mcp_info.md       # Documentation détaillée sur tous les serveurs MCP
├── web_development/           # Serveurs MCP pour le développement web
│   ├── firecrawl_mcp.json     # Configuration pour Firecrawl (web scraping)
│   ├── github_mcp.json        # Configuration pour GitHub
│   ├── vercel_mcp.json        # Configuration pour Vercel API
│   ├── figma_context_mcp.json # Configuration pour Figma Context
│   └── stripe_mcp.json        # Configuration pour Stripe
└── ai_engineering/            # Serveurs MCP pour l'ingénierie IA
    ├── magic_mcp.json         # Configuration pour Magic (IA générative)
    ├── opik_mcp.json          # Configuration pour Opik (suivi d'expériences)
    ├── browserbase_mcp.json   # Configuration pour Browserbase (automatisation)
    ├── postgresql_mcp.json    # Configuration pour PostgreSQL
    └── qdrant_mcp.json        # Configuration pour Qdrant (recherche vectorielle)
```

## Comment utiliser ces fichiers

1. Choisissez les serveurs MCP qui correspondent à vos besoins
2. Copiez les fichiers de configuration JSON correspondants dans votre dossier `.cursor/` (pour une configuration spécifique au projet) ou `~/.cursor/` (pour une configuration globale)
3. Renommez le fichier en `mcp.json`
4. Remplacez les valeurs d'API par vos propres clés d'API
5. Redémarrez Cursor pour activer les serveurs MCP

Pour plus de détails sur chaque serveur MCP et ses fonctionnalités, consultez le fichier `serveurs_mcp_info.md`.
