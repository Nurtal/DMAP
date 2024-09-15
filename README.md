# Disease MAP

## Overview
Playing with the concept


## Idee en vrac
- Approche orientée objet
- Extraction des faits à partir des p-values (quantification robustesse des faits ?)
- moteur d'inférence
- **Réseaux bayésien**

## Histoires
- Utilisation du NLP sur des publis pour construire un réseau bayesien du SjS + Utilisation du réseau pour estimer STARS / ESSDAI
- Base du réseau construit via NLP, cible constitué par un facteur défini (diagnostic, SSA, ESSDAI ...), learning structure via algo génétique, poids avec backpropagation ?  

## Feedback
 - Les outils types spacy sont chouettes pour extraires des relations dans les phrases simples mais pas dans les trucs torturés des publis : Utilisation de LLM pour simplifier & clarifier le contenu -> spacy pour extraire à partir de phrases simples et courtes


## Approche Via Reseau Bayesien
### Plan

-------     -----------------------       ------------------------------------        -----------------
| TXT |---> | Reformulation (LLM) |-----> | Parse (NLP & Spacy, langchain ?) |------> | Build Network |
-------     -----------------------       ------------------------------------        -----------------
