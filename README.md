# 🗺️ Roadmap — Black-Scholes Options Pricer

Combinaison lecture **Hull (Options, Futures & Other Derivatives)** + implémentation Python, organisée en 4 phases sur ~4 semaines.

---

## Phase 1 — Foundations & Setup

### Étape 1 · Mécanique des options `~5h`

| 📖 Hull Ch.10 | 💻 Code — Setup |
|---|---|
| Call/Put, exercice, style américain vs européen | Créer le repo GitHub |
| Cotation en pratique, positions longue/courte | Arborescence `src/`, `requirements.txt` |

### Étape 2 · Propriétés des prix d'options `~5h`

| 📖 Hull Ch.11 | 💻 Code — Vérification parité |
|---|---|
| Bornes supérieures/inférieures des prix | Écrire un test unitaire qui vérifie |
| Démonstration rigoureuse de la parité Call-Put | la relation `C − P = S₀e⁻ᵍᵀ − Ke⁻ʳᵀ` |

---

## Phase 2 — Modèles de Pricing

### Étape 3 · Arbre Binomial CRR `~6h`

| 📖 Hull Ch.13 | 💻 Code — `binomial_crr.py` |
|---|---|
| Probabilités risque-neutre, backward induction | Construire l'arbre à N pas |
| Paramètres `u`, `d`, `p` | Pricing par backward induction |
| Convergence vers BSM quand N → ∞ | Tracer la courbe de convergence |

### Étape 4 · Modèle Black-Scholes-Merton `~7h`

| 📖 Hull Ch.15 | 💻 Code — `black_scholes.py` |
|---|---|
| Mouvement brownien géométrique | Formules Call & Put |
| Hypothèses marchés parfaits | Paramètres `S₀`, `K`, `T`, `r`, `σ`, `q` |
| Vol. historique vs implicite | Reproduire les exemples numériques de Hull |

> ✅ **Point de contrôle** : Vérifier que `CRR(N=1000) ≈ BSM`. Tracer la convergence avant de passer aux Greeks.

---

## Phase 3 — Sensibilités & Stratégies

### Étape 5 · Les Greeks `~6h`

| 📖 Hull Ch.19 | 💻 Code — Module 2 |
|---|---|
| Formules analytiques Δ, Γ, Vega, Θ, ρ | Implémenter les 5 Greeks |
| Delta hedging, portefeuille Δ-neutre | Vérifier Δ Call ∈ [0,1], Γ ≥ 0 |
| Équation BSM en termes de Greeks | Comparer aux différences finies numériques |

### Étape 6 · Stratégies d'options `~4h`

| 📖 Hull Ch.12 | 💻 Code — `strategies.py` |
|---|---|
| Straddle, Strangle, Bull/Bear Spreads | P&L net (prime déduite) à l'échéance |
| Butterfly — logique économique | Visualisation superposée des stratégies |

---

## Phase 4 — Visualisations & Finition

### Étape 7 · Visualisations `~5h`

| 💻 Livrable | Description |
|---|---|
| Heatmap prix | Grille (S, σ) ou (S, T) avec Matplotlib |
| Greeks vs S | Δ, Γ, Vega, Θ en subplots, Call vs Put |
| Convergence CRR → BSM | Prix CRR(N) vs BSM en fonction de N |
| Payoff strategies | P&L Straddle, Spread, Butterfly |

### Étape 8 · Interface Streamlit + README `~4h`

| 💻 Livrable | Description |
|---|---|
| `app.py` Streamlit | Sliders S, K, T, r, σ, q — prix et Greeks en temps réel |
| GIF de démo | Capture de l'interface pour le README |
| README complet | Formules LaTeX, screenshots, instructions d'installation |
| Dépôt GitHub public | Code propre, commenté, badge de tests |

---

## 📚 Récapitulatif des lectures

| Chapitre Hull | Contenu | Étape associée |
|---|---|---|
| Ch.10 | Mécanismes de marché des options | Étape 1 |
| Ch.11 | Propriétés des prix, parité Call-Put | Étape 2 |
| Ch.13 | Arbres binomiaux (CRR) | Étape 3 |
| Ch.15 | Modèle Black-Scholes-Merton | Étape 4 |
| Ch.19 | Les Greeks analytiques | Étape 5 |
| Ch.12 | Stratégies d'options | Étape 6 |

---

## ⏱️ Estimation totale

| Phase | Durée estimée |
|---|---|
| Phase 1 — Foundations | ~10h |
| Phase 2 — Pricing | ~13h |
| Phase 3 — Greeks & Stratégies | ~10h |
| Phase 4 — Viz & Finition | ~9h |
| **Total** | **~42h (~4 semaines)** |