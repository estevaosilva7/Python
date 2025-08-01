import subprocess # Não precisa de pip install para funcionar 

def listar_processos():
    resultado = subprocess.run(["tasklist"], capture_output=True, text=True)
    linhas = resultado.stdout.splitlines()

    # Ignora cabeçalho de 3 linhas 
    dados = linhas[3:]

    processos = []

    for linha in dados:
        if linha.strip() == "":
            continue
        nome = linha[:25].strip()
        pid = linha[25:34].strip()
        sessao = linha[34:50].strip()
        memoria = linha[50:].strip()
        processos.append((nome, pid, sessao, memoria))

    # Tabela 
    print(f"{'Nome do Processo':<25} {'PID':<7} {'Sessão':<15} {'Memória':<10}")
    print("-" * 60)
    for proc in processos:
        print(f"{proc[0]:<25} {proc[1]:<7} {proc[2]:<15} {proc[3]:<10}")

if __name__ == "__main__":
    listar_processos()
