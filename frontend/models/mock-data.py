"""
Fichier contenant des données fictives pour le prototype en dark mode.
"""

# Données fictives pour les fiches de poste
JOBS_DATA = [
    {
        "id": 1,
        "titre": "Développeur Full Stack",
        "departement": "Technologie",
        "type": "CDI",
        "localisation": "Paris",
        "description": """Nous recherchons un développeur full stack expérimenté pour rejoindre notre équipe et travailler sur nos applications web et mobiles.
        
**Missions principales:**
- Développer des fonctionnalités front-end et back-end
- Participer à la conception technique des projets
- Assurer la maintenance et l'amélioration continue des applications
- Collaborer avec les designers et les product managers

**Compétences requises:**
- JavaScript, React, Node.js
- HTML/CSS, responsive design
- SQL et NoSQL databases
- Git, CI/CD
""",
        "salaire": "45 000€ - 55 000€ selon expérience",
        "date_publication": "12/04/2025",
        "competences_requises": ["JavaScript", "React", "Node.js", "HTML/CSS", "SQL", "Git"]
    },
    {
        "id": 2,
        "titre": "Chef de Projet Marketing",
        "departement": "Marketing",
        "type": "CDI",
        "localisation": "Lyon",
        "description": """Responsable de la planification, du développement et de l'exécution des campagnes marketing pour nos produits et services.
        
**Missions principales:**
- Élaborer et mettre en œuvre des stratégies marketing
- Gérer les budgets des campagnes et analyser leur ROI
- Coordonner les différentes équipes impliquées
- Suivre les KPIs et optimiser les performances

**Compétences requises:**
- Expérience en marketing digital
- Maîtrise des outils d'analyse marketing
- Excellentes capacités de communication
- Sens de l'organisation et gestion de projet
""",
        "salaire": "50 000€ - 60 000€ selon expérience",
        "date_publication": "15/04/2025",
        "competences_requises": ["Marketing Digital", "Analyse Marketing", "Communication", "Gestion de Projet"]
    },
    {
        "id": 3,
        "titre": "Data Scientist",
        "departement": "Data & Analytics",
        "type": "CDI",
        "localisation": "Toulouse",
        "description": """Analyser de grands ensembles de données et créer des modèles prédictifs pour aider à la prise de décision commerciale.
        
**Missions principales:**
- Collecter, traiter et analyser des données complexes
- Développer des modèles d'apprentissage automatique
- Présenter les résultats d'analyse aux parties prenantes
- Collaborer avec les équipes produit et technique

**Compétences requises:**
- Python, R, SQL
- Machine Learning et statistiques
- Data visualization (Tableau, PowerBI)
- Bonnes compétences en communication
""",
        "salaire": "55 000€ - 65 000€ selon expérience",
        "date_publication": "10/04/2025",
        "competences_requises": ["Python", "R", "SQL", "Machine Learning", "Tableau", "PowerBI"]
    },
    {
        "id": 4,
        "titre": "Ingénieur DevOps",
        "departement": "Infrastructure",
        "type": "CDI",
        "localisation": "Bordeaux",
        "description": """Responsable de l'infrastructure cloud, de l'automatisation du déploiement et de la mise en place des pipelines CI/CD.
        
**Missions principales:**
- Concevoir et maintenir notre infrastructure cloud
- Automatiser les processus de déploiement
- Optimiser les performances et la sécurité
- Implémenter les meilleures pratiques DevOps

**Compétences requises:**
- AWS, Azure ou GCP
- Docker, Kubernetes
- Terraform, Ansible
- Linux, scripting (Python, Bash)
""",
        "salaire": "48 000€ - 58 000€ selon expérience",
        "date_publication": "18/04/2025",
        "competences_requises": ["AWS", "Docker", "Kubernetes", "Terraform", "Linux", "Python"]
    }
]

# Données fictives pour les candidats
CANDIDATES_DATA = [
    {
        "id": 1,
        "nom": "Martin",
        "prenom": "Sophie",
        "email": "sophie.martin@example.com",
        "telephone": "0123456789",
        "competences": ["JavaScript", "React", "Node.js", "Python"],
        "experience": "5 ans d'expérience en développement web",
        "mobilite": "Région",
        "teletravail": "Hybride",
        "poste": "Développeur Full Stack",
        "matching": "95%"
    },
    {
        "id": 2,
        "nom": "Dubois",
        "prenom": "Thomas",
        "email": "thomas.dubois@example.com",
        "telephone": "0234567890",
        "competences": ["Marketing Digital", "Gestion de Projet", "SEO/SEM"],
        "experience": "8 ans dans divers postes marketing",
        "mobilite": "France",
        "teletravail": "Sur site uniquement",
        "poste": "Chef de Projet Marketing",
        "matching": "87%"
    },
    {
        "id": 3,
        "nom": "Leroy",
        "prenom": "Emma",
        "email": "emma.leroy@example.com",
        "telephone": "0345678901",
        "competences": ["Python", "R", "Machine Learning", "SQL"],
        "experience": "3 ans en analyse de données",
        "mobilite": "International",
        "teletravail": "Télétravail complet",
        "poste": "Data Scientist",
        "matching": "92%"
    },
    {
        "id": 4,
        "nom": "Bernard",
        "prenom": "Alexandre",
        "email": "alex.bernard@example.com",
        "telephone": "0456789012",
        "competences": ["AWS", "Docker", "Kubernetes", "Terraform"],
        "experience": "6 ans en infrastructure cloud",
        "mobilite": "France",
        "teletravail": "Hybride",
        "poste": "Ingénieur DevOps",
        "matching": "89%"
    },
    {
        "id": 5,
        "nom": "Moreau",
        "prenom": "Julie",
        "email": "julie.moreau@example.com",
        "telephone": "0567890123",
        "competences": ["HTML/CSS", "JavaScript", "React", "Vue.js"],
        "experience": "4 ans en développement frontend",
        "mobilite": "Région",
        "teletravail": "Hybride",
        "poste": "Développeur Front-End",
        "matching": "83%"
    }
]

# Données fictives pour les candidatures
APPLICATIONS_DATA = [
    {
        "id": 1,
        "job_id": 1,
        "candidate_id": 1,
        "message": "Je suis très intéressé par ce poste qui correspond parfaitement à mes compétences.",
        "statut": "Soumise",
        "date_soumission": "15/04/2025 10:30:00"
    },
    {
        "id": 2,
        "job_id": 2,
        "candidate_id": 2,
        "message": "Avec mon expérience en marketing, je pense pouvoir apporter une réelle valeur ajoutée.",
        "statut": "En cours d'analyse",
        "date_soumission": "16/04/2025 14:45:00"
    },
    {
        "id": 3,
        "job_id": 3,
        "candidate_id": 3,
        "message": "Passionnée par l'analyse de données, je souhaite mettre mes compétences à votre service.",
        "statut": "Entretien programmé",
        "date_soumission": "12/04/2025 09:15:00"
    },
    {
        "id": 4,
        "job_id": 4,
        "candidate_id": 4,
        "message": "Je suis convaincu que mon expérience en gestion d'infrastructure cloud serait un atout pour votre équipe.",
        "statut": "Soumise",
        "date_soumission": "19/04/2025 16:20:00"
    }
]