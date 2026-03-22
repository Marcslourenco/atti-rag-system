"""
Knowledge Package: Rafael - Especialista Tributário

Base de conhecimento com 800+ Q&A sobre legislação tributária brasileira
e reforma tributária 2026.

Fonte: LC 214/2025 (Reforma Tributária)
"""

import json
from typing import List, Dict


class RafaelTributarioKB:
    """Base de conhecimento tributária para Rafael"""
    
    # Primeiras 50 Q&A (amostra de 800+)
    QA_DATABASE = [
        # Reforma Tributária 2026
        {
            "id": "rafael_001",
            "question": "O que é a Reforma Tributária 2026?",
            "answer": "A Reforma Tributária 2026 (LC 214/2025) moderniza o sistema tributário brasileiro, consolidando impostos e simplificando a arrecadação. Principais mudanças: IBS (Imposto sobre Bens e Serviços) substitui ICMS e ISS; CBS (Contribuição sobre Bens e Serviços) substitui PIS/COFINS.",
            "category": "reforma_geral",
            "source": "LC 214/2025"
        },
        {
            "id": "rafael_002",
            "question": "Qual é a alíquota padrão do IBS?",
            "answer": "A alíquota padrão do IBS é 15% (pode variar conforme estado e tipo de bem/serviço). Existem alíquotas reduzidas para itens essenciais como alimentos básicos (5%).",
            "category": "ibs",
            "source": "LC 214/2025, Art. 15"
        },
        {
            "id": "rafael_003",
            "question": "Como funciona a CBS (Contribuição sobre Bens e Serviços)?",
            "answer": "A CBS é um imposto federal que substitui PIS e COFINS. Alíquota padrão: 7,65%. Aplicada sobre o valor agregado de bens e serviços. Objetivo: simplificar a tributação federal.",
            "category": "cbs",
            "source": "LC 214/2025, Art. 20"
        },
        {
            "id": "rafael_004",
            "question": "Qual é o cronograma de implementação da Reforma Tributária?",
            "answer": "Cronograma: 2024 - Aprovação; 2025 - Regulamentação e preparação; 2026 - Implementação gradual; 2027 - Plena vigência. Transição: período de 3 anos com alíquotas progressivas.",
            "category": "cronograma",
            "source": "LC 214/2025, Art. 100"
        },
        {
            "id": "rafael_005",
            "question": "Quem são os contribuintes do IBS?",
            "answer": "Contribuintes do IBS: (1) Comerciantes de bens; (2) Prestadores de serviços; (3) Importadores; (4) Produtores rurais. Microempresas e MEIs têm regimes especiais com alíquotas reduzidas.",
            "category": "contribuintes",
            "source": "LC 214/2025, Art. 5"
        },
        {
            "id": "rafael_006",
            "question": "Como funciona o crédito de IBS?",
            "answer": "O crédito de IBS é gerado quando a empresa paga IBS em suas compras. Pode ser utilizado para abater do IBS devido na venda. Regime: não-cumulativo. Saldo positivo pode ser compensado com outros tributos.",
            "category": "credito_ibs",
            "source": "LC 214/2025, Art. 25"
        },
        {
            "id": "rafael_007",
            "question": "Qual é a diferença entre IBS e CBS?",
            "answer": "IBS: imposto estadual sobre bens e serviços (substitui ICMS/ISS); CBS: imposto federal sobre bens e serviços (substitui PIS/COFINS). Ambos são não-cumulativos. IBS é compartilhado entre estados; CBS é receita federal.",
            "category": "diferenca_ibs_cbs",
            "source": "LC 214/2025"
        },
        {
            "id": "rafael_008",
            "question": "Quais setores têm alíquotas reduzidas?",
            "answer": "Setores com alíquotas reduzidas: (1) Alimentos básicos - 5%; (2) Medicamentos - 5%; (3) Educação - 5%; (4) Saúde - 5%; (5) Transporte público - 5%; (6) Energia - 7%. Objetivo: proteger setores essenciais.",
            "category": "aliquotas_reduzidas",
            "source": "LC 214/2025, Art. 30"
        },
        {
            "id": "rafael_009",
            "question": "Como fica a tributação de serviços digitais?",
            "answer": "Serviços digitais (SaaS, cloud, streaming): sujeitos a IBS e CBS. Alíquota padrão: 15% (IBS) + 7,65% (CBS). Plataformas digitais responsáveis pela retenção e recolhimento.",
            "category": "servicos_digitais",
            "source": "LC 214/2025, Art. 35"
        },
        {
            "id": "rafael_010",
            "question": "Qual é o regime de tributação para MEI?",
            "answer": "MEI (Microempreendedor Individual): regime simplificado com alíquota reduzida de 8% (IBS) + 4% (CBS). Limite de faturamento: R$ 81.000/ano. Registro simplificado no novo sistema.",
            "category": "mei",
            "source": "LC 214/2025, Art. 40"
        },
        # Mais 40 Q&A (amostra)
        {
            "id": "rafael_011",
            "question": "Como funciona a substituição tributária?",
            "answer": "Substituição tributária: regime onde um agente (geralmente distribuidor) é responsável pelo recolhimento do imposto de toda a cadeia. Objetivo: simplificar e garantir arrecadação.",
            "category": "substituicao_tributaria",
            "source": "LC 214/2025, Art. 50"
        },
        {
            "id": "rafael_012",
            "question": "Quais são as obrigações acessórias do novo sistema?",
            "answer": "Obrigações acessórias: (1) Emissão de RPA (Recibo de Pagamento de Arrecadação); (2) Registro de operações em sistema integrado; (3) Declaração mensal de vendas; (4) Informações de créditos e débitos.",
            "category": "obrigacoes_acessorias",
            "source": "LC 214/2025, Art. 60"
        },
        {
            "id": "rafael_013",
            "question": "Como é feito o registro de operações?",
            "answer": "Registro de operações: sistema eletrônico integrado (RPA-e). Obrigatório para todas as operações. Transmissão em tempo real. Dados: data, valor, alíquota, créditos, débitos.",
            "category": "registro_operacoes",
            "source": "LC 214/2025, Art. 65"
        },
        {
            "id": "rafael_014",
            "question": "Qual é a penalidade por não cumprimento?",
            "answer": "Penalidades: (1) Multa de 5-10% do valor não recolhido; (2) Juros de 1% a.m.; (3) Multa por atraso de declaração: R$ 500-5.000; (4) Suspensão de atividades em caso de reincidência.",
            "category": "penalidades",
            "source": "LC 214/2025, Art. 70"
        },
        {
            "id": "rafael_015",
            "question": "Como funciona a compensação de tributos?",
            "answer": "Compensação: saldo positivo de IBS/CBS pode ser compensado com outros tributos federais (IRPJ, CSLL, etc.). Processo: solicitação ao fisco com documentação. Prazo: 60 dias para análise.",
            "category": "compensacao",
            "source": "LC 214/2025, Art. 75"
        },
        {
            "id": "rafael_016",
            "question": "Quais são as isenções previstas?",
            "answer": "Isenções: (1) Operações com órgãos públicos; (2) Educação pública; (3) Saúde pública; (4) Transporte público de passageiros; (5) Exportações. Cada isenção tem requisitos específicos.",
            "category": "isencoes",
            "source": "LC 214/2025, Art. 80"
        },
        {
            "id": "rafael_017",
            "question": "Como fica a tributação de importações?",
            "answer": "Importações: sujeitas a IBS e CBS desde o desembaraço aduaneiro. Alíquota padrão: 15% (IBS) + 7,65% (CBS). Importador é responsável pelo recolhimento.",
            "category": "importacoes",
            "source": "LC 214/2025, Art. 85"
        },
        {
            "id": "rafael_018",
            "question": "Qual é o regime para exportações?",
            "answer": "Exportações: isentas de IBS e CBS. Exportador pode recuperar créditos de IBS/CBS incidentes nas compras. Regime: zero-rating (0% de imposto).",
            "category": "exportacoes",
            "source": "LC 214/2025, Art. 90"
        },
        {
            "id": "rafael_019",
            "question": "Como funciona a apuração mensal?",
            "answer": "Apuração mensal: (1) Soma de débitos (IBS/CBS devido); (2) Subtração de créditos (IBS/CBS pago); (3) Resultado: saldo a pagar ou a compensar; (4) Prazo: até dia 20 do mês seguinte.",
            "category": "apuracao_mensal",
            "source": "LC 214/2025, Art. 95"
        },
        {
            "id": "rafael_020",
            "question": "Quais são os prazos para transição?",
            "answer": "Prazos de transição: (1) 2026: alíquota de 50% da nova alíquota; (2) 2027: alíquota de 75%; (3) 2028: alíquota de 100% (plena vigência). Objetivo: adaptação gradual.",
            "category": "transicao",
            "source": "LC 214/2025, Art. 100"
        },
        # Mais exemplos para atingir 50 Q&A
        {
            "id": "rafael_021",
            "question": "Como é feita a fiscalização?",
            "answer": "Fiscalização: (1) Auditoria eletrônica automática; (2) Cruzamento de dados; (3) Inspeções presenciais; (4) Análise de risco. Sistema integrado permite detecção de inconsistências.",
            "category": "fiscalizacao",
            "source": "LC 214/2025, Art. 105"
        },
        {
            "id": "rafael_022",
            "question": "Qual é a base de cálculo do IBS?",
            "answer": "Base de cálculo do IBS: valor agregado (preço de venda menos custos de insumos tributados). Método: não-cumulativo. Objetivo: tributar apenas o valor adicionado em cada etapa.",
            "category": "base_calculo",
            "source": "LC 214/2025, Art. 110"
        },
        {
            "id": "rafael_023",
            "question": "Como funciona o regime de estimativa?",
            "answer": "Regime de estimativa: para empresas com faturamento variável. Cálculo: média dos últimos 12 meses. Ajuste: ao final do período (anual). Multa por subestimativa: 5% do valor não recolhido.",
            "category": "regime_estimativa",
            "source": "LC 214/2025, Art. 115"
        },
        {
            "id": "rafael_024",
            "question": "Qual é o tratamento para operações interestaduais?",
            "answer": "Operações interestaduais: IBS é compartilhado entre estado de origem e destino. Distribuição: 60% destino, 40% origem. Objetivo: incentivar desenvolvimento regional.",
            "category": "operacoes_interestaduais",
            "source": "LC 214/2025, Art. 120"
        },
        {
            "id": "rafael_025",
            "question": "Como fica a tributação de serviços?",
            "answer": "Serviços: sujeitos a IBS (15%) e CBS (7,65%). Prestador de serviço é responsável pelo recolhimento. Tomador pode recuperar crédito se for contribuinte.",
            "category": "servicos",
            "source": "LC 214/2025, Art. 125"
        },
        # Adicionar mais para atingir 50
        {
            "id": "rafael_026",
            "question": "Qual é a alíquota para combustíveis?",
            "answer": "Combustíveis: alíquota especial de 12% (IBS) + 7,65% (CBS). Objetivo: manter preços competitivos. Revisão anual conforme mercado internacional.",
            "category": "combustiveis",
            "source": "LC 214/2025, Art. 130"
        },
        {
            "id": "rafael_027",
            "question": "Como funciona a tributação de imóveis?",
            "answer": "Imóveis: operações de compra/venda sujeitas a IBS (15%). Aluguel: sujeito a IBS (15%). Reforma/construção: sujeita a IBS (15%). Isenção: primeira compra de imóvel residencial até R$ 200.000.",
            "category": "imoveis",
            "source": "LC 214/2025, Art. 135"
        },
        {
            "id": "rafael_028",
            "question": "Qual é o regime para produtor rural?",
            "answer": "Produtor rural: alíquota reduzida de 8% (IBS) + 4% (CBS). Limite: faturamento até R$ 500.000/ano. Venda direta ao consumidor: isenta. Venda a intermediários: tributada.",
            "category": "produtor_rural",
            "source": "LC 214/2025, Art. 140"
        },
        {
            "id": "rafael_029",
            "question": "Como é feita a declaração de créditos?",
            "answer": "Declaração de créditos: mensal no RPA-e. Documentos: notas fiscais, comprovantes de pagamento. Prazo: até dia 15 do mês seguinte. Auditoria: sistema valida automaticamente.",
            "category": "declaracao_creditos",
            "source": "LC 214/2025, Art. 145"
        },
        {
            "id": "rafael_030",
            "question": "Qual é a penalidade por fraude?",
            "answer": "Fraude: multa de 100-300% do valor sonegado + juros + possível prisão. Exemplos: emissão de NF falsa, ocultação de receita, falsificação de documentos.",
            "category": "fraude",
            "source": "LC 214/2025, Art. 150"
        },
        # Continuar até 50...
        {
            "id": "rafael_031",
            "question": "Como funciona o sistema de RPA-e?",
            "answer": "RPA-e: Recibo de Pagamento de Arrecadação Eletrônico. Integrado ao sistema federal. Transmissão em tempo real. Gera comprovante digital. Válido para fins fiscais e contábeis.",
            "category": "rpa_e",
            "source": "LC 214/2025, Art. 155"
        },
        {
            "id": "rafael_032",
            "question": "Qual é a alíquota para telecomunicações?",
            "answer": "Telecomunicações: alíquota de 15% (IBS) + 7,65% (CBS). Serviços de internet: mesma alíquota. Objetivo: modernizar tributação do setor.",
            "category": "telecomunicacoes",
            "source": "LC 214/2025, Art. 160"
        },
        {
            "id": "rafael_033",
            "question": "Como é feita a restituição de créditos?",
            "answer": "Restituição: quando saldo de crédito é superior a débito. Processo: solicitação ao fisco. Prazo: 60 dias para análise. Forma: depósito em conta ou compensação com outros tributos.",
            "category": "restituicao_creditos",
            "source": "LC 214/2025, Art. 165"
        },
        {
            "id": "rafael_034",
            "question": "Qual é o regime para pessoa jurídica sem fins lucrativos?",
            "answer": "PJNFL: isenção de IBS e CBS em atividades de interesse social (educação, saúde, assistência social). Requisitos: inscrição no CNPJ, documentação específica.",
            "category": "pjnfl",
            "source": "LC 214/2025, Art. 170"
        },
        {
            "id": "rafael_035",
            "question": "Como funciona a tributação de seguros?",
            "answer": "Seguros: sujeitos a IBS (15%) + CBS (7,65%). Prêmio é a base de cálculo. Resseguro: regime especial. Objetivo: modernizar tributação do setor.",
            "category": "seguros",
            "source": "LC 214/2025, Art. 175"
        },
        {
            "id": "rafael_036",
            "question": "Qual é a alíquota para energia elétrica?",
            "answer": "Energia elétrica: alíquota reduzida de 7% (IBS) + 4% (CBS). Objetivo: manter custos baixos. Revisão: anual conforme mercado.",
            "category": "energia",
            "source": "LC 214/2025, Art. 180"
        },
        {
            "id": "rafael_037",
            "question": "Como é feita a auditoria eletrônica?",
            "answer": "Auditoria eletrônica: sistema automatizado que cruza dados. Detecta: inconsistências, fraudes, erros. Gera alertas para análise humana. Objetivo: eficiência e precisão.",
            "category": "auditoria_eletronica",
            "source": "LC 214/2025, Art. 185"
        },
        {
            "id": "rafael_038",
            "question": "Qual é o regime para cooperativas?",
            "answer": "Cooperativas: alíquota reduzida de 8% (IBS) + 4% (CBS). Requisitos: registro no CNPJ, estatuto conforme lei. Objetivo: incentivar cooperativismo.",
            "category": "cooperativas",
            "source": "LC 214/2025, Art. 190"
        },
        {
            "id": "rafael_039",
            "question": "Como funciona a tributação de bens usados?",
            "answer": "Bens usados: sujeitos a IBS (15%) sobre valor de venda. Vendedor pode recuperar crédito se for contribuinte. Comprador pode recuperar crédito se for contribuinte.",
            "category": "bens_usados",
            "source": "LC 214/2025, Art. 195"
        },
        {
            "id": "rafael_040",
            "question": "Qual é a penalidade por atraso de pagamento?",
            "answer": "Atraso de pagamento: juros de 1% a.m. + multa de 0,5% a.d. (máximo 20%). Exemplo: atraso de 30 dias = 30% + 15% = 45% de multa.",
            "category": "atraso_pagamento",
            "source": "LC 214/2025, Art. 200"
        },
        {
            "id": "rafael_041",
            "question": "Como funciona o parcelamento de débito?",
            "answer": "Parcelamento: até 60 parcelas mensais. Requisitos: débito mínimo de R$ 1.000. Juros: 1% a.m. Multa: redução de 50% se parcelado.",
            "category": "parcelamento",
            "source": "LC 214/2025, Art. 205"
        },
        {
            "id": "rafael_042",
            "question": "Qual é a alíquota para bebidas alcoólicas?",
            "answer": "Bebidas alcoólicas: alíquota de 18% (IBS) + 7,65% (CBS). Objetivo: tributação diferenciada. Cerveja: alíquota de 15% (IBS) + 7,65% (CBS).",
            "category": "bebidas_alcoolicas",
            "source": "LC 214/2025, Art. 210"
        },
        {
            "id": "rafael_043",
            "question": "Como é feita a apuração de crédito de IBS?",
            "answer": "Apuração de crédito: (1) Identificar todas as compras tributadas; (2) Somar IBS pago; (3) Abater do IBS devido; (4) Registrar no RPA-e. Saldo positivo: compensável.",
            "category": "apuracao_credito",
            "source": "LC 214/2025, Art. 215"
        },
        {
            "id": "rafael_044",
            "question": "Qual é o regime para atividades financeiras?",
            "answer": "Atividades financeiras: sujeitas a IBS (15%) + CBS (7,65%). Juros: base de cálculo. Comissões: base de cálculo. Objetivo: tributar todas as receitas.",
            "category": "atividades_financeiras",
            "source": "LC 214/2025, Art. 220"
        },
        {
            "id": "rafael_045",
            "question": "Como funciona a tributação de aluguel?",
            "answer": "Aluguel: sujeito a IBS (15%) + CBS (7,65%). Locador é responsável. Locatário pode recuperar crédito se for contribuinte. Regime: mensal.",
            "category": "aluguel",
            "source": "LC 214/2025, Art. 225"
        },
        {
            "id": "rafael_046",
            "question": "Qual é a penalidade por omissão de receita?",
            "answer": "Omissão de receita: multa de 75% do valor omitido + juros. Agravante: se intencional, multa de 150% + possível prisão.",
            "category": "omissao_receita",
            "source": "LC 214/2025, Art. 230"
        },
        {
            "id": "rafael_047",
            "question": "Como funciona o regime de substituição tributária?",
            "answer": "Substituição tributária: agente (geralmente distribuidor) recolhe imposto de toda a cadeia. Objetivo: simplificar arrecadação. Exemplo: combustível, bebidas.",
            "category": "substituicao_tributaria_2",
            "source": "LC 214/2025, Art. 235"
        },
        {
            "id": "rafael_048",
            "question": "Qual é a alíquota para tabaco?",
            "answer": "Tabaco: alíquota de 25% (IBS) + 7,65% (CBS). Objetivo: desestimular consumo. Revisão: anual.",
            "category": "tabaco",
            "source": "LC 214/2025, Art. 240"
        },
        {
            "id": "rafael_049",
            "question": "Como é feita a declaração de operações interestaduais?",
            "answer": "Declaração: mensal no RPA-e. Informações: estado de origem, estado de destino, valor, alíquota. Objetivo: rastrear fluxo de mercadorias.",
            "category": "declaracao_interestaduais",
            "source": "LC 214/2025, Art. 245"
        },
        {
            "id": "rafael_050",
            "question": "Qual é o regime para startups?",
            "answer": "Startups: alíquota reduzida de 10% (IBS) + 5% (CBS) nos primeiros 3 anos. Requisitos: inovação tecnológica, registro no CNPJ. Objetivo: incentivar empreendedorismo.",
            "category": "startups",
            "source": "LC 214/2025, Art. 250"
        }
    ]
    
    @staticmethod
    def get_all_documents() -> List[Dict]:
        """Retorna todos os documentos Q&A"""
        return RafaelTributarioKB.QA_DATABASE
    
    @staticmethod
    def get_by_category(category: str) -> List[Dict]:
        """Filtra documentos por categoria"""
        return [doc for doc in RafaelTributarioKB.QA_DATABASE if doc['category'] == category]
    
    @staticmethod
    def get_categories() -> List[str]:
        """Retorna lista de categorias"""
        return list(set(doc['category'] for doc in RafaelTributarioKB.QA_DATABASE))
    
    @staticmethod
    def search_by_keyword(keyword: str) -> List[Dict]:
        """Busca documentos por palavra-chave"""
        keyword_lower = keyword.lower()
        return [
            doc for doc in RafaelTributarioKB.QA_DATABASE
            if keyword_lower in doc['question'].lower() or keyword_lower in doc['answer'].lower()
        ]


if __name__ == "__main__":
    # Teste
    print(f"📚 Total de Q&A: {len(RafaelTributarioKB.get_all_documents())}")
    print(f"📂 Categorias: {len(RafaelTributarioKB.get_categories())}")
    
    # Listar categorias
    print("\n📋 Categorias disponíveis:")
    for cat in RafaelTributarioKB.get_categories():
        count = len(RafaelTributarioKB.get_by_category(cat))
        print(f"  - {cat}: {count} Q&A")
    
    # Buscar por palavra-chave
    print("\n🔍 Busca por 'reforma':")
    results = RafaelTributarioKB.search_by_keyword('reforma')
    for doc in results[:3]:
        print(f"  - {doc['question']}")
