# Les 10 Meilleurs Serveurs MCP pour Cursor

Ce document présente une compilation des meilleurs serveurs MCP (Model Context Protocol) que vous pouvez utiliser avec Cursor pour améliorer votre productivité en tant que développeur web et ingénieur IA.

## Qu'est-ce que MCP?

Le Model Context Protocol (MCP) est un standard ouvert conçu pour faciliter l'interaction entre les grands modèles de langage (LLM) et des sources de données ou outils externes. Il fournit une méthode standardisée permettant aux modèles d'IA de se connecter à diverses sources de données et outils, évitant ainsi les implémentations personnalisées qui causent de la fragmentation.

MCP agit comme une interface universelle (comparable à un port USB-C pour les applications d'IA), standardisant la façon dont les applications fournissent du contexte aux LLM. Ce protocole représente un changement fondamental dans la façon dont nous construisons des applications agentiques, passant de connexions isolées et propriétaires à un écosystème ouvert et connecté.

## Serveurs MCP pour le Développement Web

### 1. Firecrawl MCP

**Description**: Firecrawl est une solution complète de web scraping qui améliore votre flux de travail de développement en fournissant un accès direct au contenu web directement dans votre IDE.

**Fonctionnalités principales**:
- Extraction de contenu structuré à partir de sites web
- Recherche et extraction de contenu à partir de résultats de recherche
- Crawling profond avec contraintes de profondeur et de domaine configurables
- Extraction structurée de données spécifiques

**Cas d'utilisation**:
- Recherche sur les produits ou services concurrents
- Collecte de données pour des projets de machine learning
- Extraction d'informations à partir de sites de documentation
- Surveillance des changements de contenu sur plusieurs sites web

**Configuration dans Cursor**:
```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "@firecrawl/mcp-server"],
      "env": {
        "FIRECRAWL_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### 2. GitHub MCP

**Description**: Fournit un accès direct aux fonctionnalités de GitHub, permettant de gérer des dépôts, des fichiers et d'interagir avec l'API GitHub.

**Fonctionnalités principales**:
- Gestion de dépôts
- Opérations sur les fichiers
- Recherche de code
- Gestion des issues et pull requests

**Cas d'utilisation**:
- Automatisation des tâches GitHub
- Recherche de code dans des dépôts
- Création et gestion d'issues

**Configuration dans Cursor**:
```json
{
  "mcpServers": {
    "github-tools": {
      "command": "npx",
      "args": ["-y", "mcp-github"],
      "env": {
        "GITHUB_TOKEN": "your-github-token"
      }
    }
  }
}
```

### 3. Vercel API MCP

**Description**: Intègre l'API Vercel pour permettre la gestion des déploiements et des projets Vercel directement depuis Cursor.

**Fonctionnalités principales**:
- Gestion des déploiements
- Configuration des projets
- Surveillance des performances
- Accès aux logs et métriques

**Cas d'utilisation**:
- Déploiement d'applications web
- Surveillance des performances des applications
- Gestion des environnements de développement

**Configuration dans Cursor**:
```json
{
  "mcpServers": {
    "vercel": {
      "command": "npx",
      "args": ["-y", "vercel-mcp-server"],
      "env": {
        "VERCEL_API_TOKEN": "your_vercel_api_token"
      }
    }
  }
}
```

### 4. Figma Context MCP

**Description**: Comble le fossé entre vos ressources de design dans Figma et votre environnement de développement, permettant aux développeurs de créer, accéder, visualiser et analyser les designs Figma directement dans Cursor.

**Fonctionnalités principales**:
- Accès aux designs Figma
- Extraction des spécifications de design
- Extraction des schémas de couleurs et détails typographiques
- Compréhension des relations entre composants

**Cas d'utilisation**:
- Implémentation de designs depuis Figma
- Vérification des spécifications de design et mesures
- Extraction des schémas de couleurs pour le développement frontend

**Configuration dans Cursor**:
```json
{
  "mcpServers": {
    "figma-context": {
      "command": "npx",
      "args": ["-y", "figma-context-mcp"],
      "env": {
        "FIGMA_API_KEY": "your_figma_api_key",
        "FIGMA_FILE_ID": "your_figma_file_id"
      }
    }
  }
}
```

### 5. Stripe MCP

**Description**: Permet d'interagir avec l'API Stripe pour gérer les paiements, les clients et les abonnements directement depuis votre environnement de développement.

**Fonctionnalités principales**:
- Gestion des paiements
- Gestion des clients et abonnements
- Accès aux rapports et analyses
- Traitement des webhooks

**Cas d'utilisation**:
- Intégration de systèmes de paiement
- Gestion des abonnements
- Analyse des données de paiement

**Configuration dans Cursor**:
```json
{
  "mcpServers": {
    "stripe": {
      "command": "npx",
      "args": ["-y", "stripe-mcp-server"],
      "env": {
        "STRIPE_API_KEY": "your_stripe_api_key"
      }
    }
  }
}
```

## Serveurs MCP pour l'Ingénierie IA

### 1. Magic MCP

**Description**: Apporte des capacités d'IA générative directement dans votre environnement de développement, permettant de générer des images, d'effectuer des transformations de texte et d'autres opérations basées sur l'IA sans changer de contexte.

**Fonctionnalités principales**:
- Génération d'images
- Transformations de texte
- Création d'échantillons de code à partir de descriptions en langage naturel
- Résumé de contenu pour la documentation

**Cas d'utilisation**:
- Création d'images placeholder pendant le développement frontend
- Génération d'illustrations pour la documentation
- Transformation de texte dans divers formats ou styles
- Création de code à partir de descriptions en langage naturel

**Configuration dans Cursor**:
```json
{
  "mcpServers": {
    "magic": {
      "command": "npx",
      "args": ["-y", "@21st/magic-mcp"],
      "env": {
        "OPENAI_API_KEY": "your_openai_api_key_here"
      }
    }
  }
}
```

### 2. Opik MCP

**Description**: Intègre des capacités de suivi d'expériences directement dans votre environnement de développement, alimenté par Comet ML. Ce serveur aide les scientifiques de données et les ingénieurs en machine learning à gérer, visualiser et suivre leurs expériences ML sans quitter leur contexte de codage.

**Fonctionnalités principales**:
- Suivi des métriques d'entraînement de modèles
- Comparaison de différentes exécutions d'expériences
- Visualisation des performances de modèles
- Collaboration avec les membres de l'équipe sur des projets ML

**Cas d'utilisation**:
- Projets de machine learning
- Suivi des métriques d'entraînement
- Comparaison d'expériences
- Visualisation des performances de modèles

**Configuration dans Cursor**:
```json
{
  "mcpServers": {
    "opik": {
      "command": "npx",
      "args": ["-y", "@comet-ml/opik-mcp"],
      "env": {
        "COMET_API_KEY": "your_comet_api_key_here"
      }
    }
  }
}
```

### 3. Browserbase MCP

**Description**: Apporte de puissantes capacités d'automatisation de navigateur cloud directement dans votre environnement de développement, permettant d'interagir avec des sites web de manière programmatique, de gérer du contenu rendu par JavaScript, des systèmes de connexion et des éléments de page dynamiques.

**Fonctionnalités principales**:
- Gestion de sessions de navigateur
- Navigation et interaction avec des sites web
- Capture de screenshots
- Exécution de JavaScript dans le contexte du navigateur
- Extraction de contenu depuis des pages rendues

**Cas d'utilisation**:
- Tests d'applications web sur différents scénarios
- Automatisation d'interactions répétitives avec des sites web
- Capture de représentations visuelles d'éléments web
- Extraction de données depuis des sites utilisant beaucoup de JavaScript
- Débogage de problèmes côté client

**Configuration dans Cursor**:
```json
{
  "mcpServers": {
    "browserbase": {
      "command": "node",
      "args": ["path/to/mcp-server-browserbase/browserbase/dist/index.js"],
      "env": {
        "BROWSERBASE_API_KEY": "your_api_key_here",
        "BROWSERBASE_PROJECT_ID": "your_project_id_here"
      }
    }
  }
}
```

### 4. PostgreSQL MCP

**Description**: Fournit un accès en lecture seule aux bases de données PostgreSQL, permettant aux LLM d'inspecter les schémas de base de données et d'exécuter des requêtes en lecture seule.

**Fonctionnalités principales**:
- Inspection des schémas de base de données
- Exécution de requêtes en lecture seule
- Analyse de données

**Cas d'utilisation**:
- Exploration de données pour des projets de machine learning
- Analyse de données pour des insights
- Génération de rapports basés sur des données

**Configuration dans Cursor**:
```json
{
  "mcpServers": {
    "database-query": {
      "command": "uv",
      "args": ["run", "python", "-m", "mcp_database_tool"],
      "env": {
        "DB_CONNECTION_STRING": "your-connection-string"
      }
    }
  }
}
```

### 5. Qdrant MCP

**Description**: Permet d'implémenter une mémoire sémantique en utilisant le moteur de recherche vectorielle Qdrant, idéal pour les applications d'IA nécessitant une recherche sémantique.

**Fonctionnalités principales**:
- Stockage et recherche de vecteurs
- Recherche sémantique
- Clustering et classification

**Cas d'utilisation**:
- Systèmes de recommandation
- Recherche sémantique dans de grands corpus de texte
- Applications de RAG (Retrieval Augmented Generation)
- Systèmes de question-réponse basés sur des documents

**Configuration dans Cursor**:
```json
{
  "mcpServers": {
    "qdrant": {
      "command": "npx",
      "args": ["-y", "qdrant-mcp-server"],
      "env": {
        "QDRANT_URL": "your_qdrant_url",
        "QDRANT_API_KEY": "your_qdrant_api_key"
      }
    }
  }
}
```

## Comment utiliser les serveurs MCP dans Cursor

1. **Installation des prérequis**:
   - Node.js (≥ v18, LTS recommandé)
   - Python (pour certains serveurs)
   - UV (pour les serveurs Python)

2. **Configuration des serveurs MCP**:
   - Créez un fichier `.cursor/mcp.json` dans votre répertoire de projet (configuration spécifique au projet)
   - Ou créez un fichier `~/.cursor/mcp.json` dans votre répertoire personnel (configuration globale)
   - Ajoutez les configurations des serveurs MCP que vous souhaitez utiliser

3. **Utilisation dans Cursor**:
   - Une fois configurés, vous pouvez demander à l'agent Cursor d'utiliser les outils MCP
   - Cursor identifiera automatiquement le besoin et utilisera le serveur requis
   - Vous pouvez également mentionner explicitement l'outil à utiliser dans vos prompts

4. **Mode Yolo**:
   - Pour une exécution automatique sans demande d'approbation, vous pouvez activer le "Mode Yolo" dans les paramètres de Cursor
   - Cela permet à l'agent d'exécuter des outils MCP sans demander votre approbation explicite pour chaque utilisation
