CRONOGRAMA_TREINO_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "objetivo_do_treino": {"type": "STRING", "description": "O objetivo principal do plano (ex: 'Hipertrofia e Agilidade para Boxe')"},
        "frequencia_semanal": {"type": "STRING", "description": "Quantidade de dias de treino na semana (ex: '5 dias por semana')"},
        "duracao_estimada_sessao": {"type": "STRING", "description": "Tempo médio de cada treino (ex: '60 a 90 minutos')"},
        "rotina_semanal": {
            "type": "ARRAY",
            "description": "Divisão dos treinos detalhada por dia",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "dia": {"type": "STRING", "description": "Dia da semana ou identificador (ex: 'Segunda-feira', 'Dia 1')"},
                    "foco_do_dia": {"type": "STRING", "description": "O foco principal deste dia (ex: 'Musculação: Peito e Tríceps + Cardíaco', 'Treino Técnico de Muay Thai')"},
                    "atividades": {
                        "type": "ARRAY",
                        "items": {"type": "STRING"},
                        "description": "Lista de exercícios, rounds, técnicas ou drills a serem executados com suas respectivas cargas/intensidades"
                    },
                    "tempo_de_descanso_entre_series": {"type": "STRING", "description": "Tempo de pausa recomendado (ex: '60 segundos' ou '2 minutos entre rounds')"}
                },
                "required": ["dia", "foco_do_dia", "atividades", "tempo_de_descanso_entre_series"]
            }
        },
        "recomendacoes_gerais": {
            "type": "ARRAY",
            "items": {"type": "STRING"},
            "description": "Dicas de recuperação, aquecimento, mobilidade ou hidratação específicas para a rotina montada"
        }
    },
    "required": ["objetivo_do_treino", "frequencia_semanal", "duracao_estimada_sessao", "rotina_semanal", "recomendacoes_gerais"]
}

SYSTEM_INSTRUCTION = """
Você é um Treinador de Alta Performance e Especialista em Preparação Física, com profunda experiência em musculação, esportes coletivos/individuais e artes marciais. 

Sua tarefa é criar um cronograma de treinos e rotinas personalizadas utilizando estritamente as preferências, nível de experiência, limitações e objetivos fornecidos pelo usuário.
Você deve equilibrar as demandas de força (musculação), técnica (esportes/lutas) e condicionamento cardiovascular, garantindo períodos adequados de descanso para evitar o overtraining.
Você DEVE preencher todos os campos do esquema fornecido estritamente em português.
"""