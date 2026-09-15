# ==========================================
# SISTEMA INTELIGENTE DE CONTROLE DE ACESSOS
# ==========================================

print("=== BEM-VINDO AO PORTAL DE ACESSO ===")

# 1. Banco de Dados Simulado (Lista Mutável)
cadastros_oficiais = ["Guilherme Gomes", "Amanda Michelle", "Eduardo Portela"]

# 2. Entrada de Dados Interativa pelo Usuário (Terminal)
nome_usuario = input("Digite o seu nome completo: ")
idade_usuario = int(input("Digite a sua idade: "))

# Verificando se o usuário possui cadastro no sistema
possui_cadastro = nome_usuario in cadastros_oficiais

# 3. Estrutura Condicional (if/else) Principal
if possui_cadastro:
    print(f"\n[SUCESSO] Olá, {nome_usuario}! Cadastro confirmado no sistema.")
    
    # Validação de idade para liberação da catraca
    if idade_usuario >= 18:
        print("[AUTORIZADO] Maior de idade. Acesso liberado à catraca geral!")
    else:
        print("[BLOQUEADO] Menor de idade. Acesso negado pela legislação.")
        
else:
    print(f"\n[ATENÇÃO] O nome '{nome_usuario}' NÃO foi encontrado na base de dados.")
    
    # Pergunta interativa se deseja se cadastrar agora
    opcao_cadastro = input("Deseja realizar o cadastro agora? (s/n): ").strip().lower()
    
    if opcao_cadastro == 's':
        cadastros_oficiais.append(nome_usuario)
        print(f"\n[REGISTRADO] Parabéns, {nome_usuario}! Seu cadastro foi realizado com sucesso.")
        print(f"Nova lista de usuários oficiais no sistema: {cadastros_oficiais}")
    else:
        print("\n[ENCERRADO] Cadastro não realizado. Acesso negado ao evento.")