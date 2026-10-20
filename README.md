# Residência Aberta (Open_residency)

**PT-BR** | [English below](#english)

Infraestrutura aberta para preparação de residência médica no Brasil, pensada para candidatos de baixa renda.

> **Status: fase inicial (early-stage).** O projeto acaba de começar. Ainda não há plataforma pronta, usuários nem resultados. Este repositório documenta o plano e os primeiros componentes.

## O problema

A preparação para residência médica depende, na prática, de bancos de questões, cursos e mentorias pagos. Não existe infraestrutura aberta, em português, para quem não pode pagar.

## O que o projeto pretende liberar (código MIT, conteúdo CC-BY quando juridicamente possível)

1. **Motor de explicações com fontes verificáveis (RAG):** toda explicação cita fontes versionadas (diretrizes, documentos do Ministério da Saúde/SUS) e se recusa a responder quando não há evidência suficiente.
2. **Esquema de anotação de questões:** tema, competência exigida e tipo de erro. Veja `schema/question.schema.json`.
3. **Conjunto de avaliação independente:** com checagem automática de citações e fluxo de revisão por médicos.
4. **Agendador de revisão espaçada:** guiado pelo perfil de erros de cada estudante.

## O que o projeto NÃO faz

- Não presta atendimento a pacientes nem substitui decisão clínica.
- Não promete aprovação em provas.
- Não redistribui provas protegidas por direitos autorais.
- Não usa dados de pacientes.

## Como contribuir

Veja [CONTRIBUTING.md](CONTRIBUTING.md) e o [ROADMAP.md](ROADMAP.md). Procuramos estudantes de medicina, médicos revisores e desenvolvedores.

## Aviso importante

Conteúdo gerado ou assistido por IA pode conter erros. Nada neste repositório deve ser usado para conduta clínica. Todo material educacional passa por revisão humana antes de ser marcado como `revisado`.

---

## English

Open infrastructure for medical residency exam preparation in Brazil, built for low-income candidates.

**Status: early-stage.** No finished platform, users, or results yet. This repository documents the plan and first components.

Planned open components: a citation-grounded explanation engine (refuses to answer without sufficient evidence); a question-annotation schema (topic, skill, error type); a held-out evaluation set with citation checks and physician review workflow; and a spaced-review scheduler driven by learner error profiles.

Non-goals: patient care, exam-approval promises, redistribution of copyrighted exams, patient data.

License: code MIT, content CC-BY where legally allowed.
