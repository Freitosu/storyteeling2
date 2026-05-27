import os

def clear():
    os.system('clear')

def ask_choice(prompt, valid):
    while True:
        ans = input(prompt).strip()
        clear()
        if ans in valid:
            return ans
        print("Opção inválida. Tente novamente.")

# Estado da história
used_krtwl = False
attacked_brother = False
fled_with_bro = False
surrendered = False
resisted = False
believed_brother = False

# Novos flags para ramificações reais
path_main = False
path_back = False
path_rooftop = False
path_lab = False
captured = False
interrogated = False
discovered_experiment = False
radio_info = False
memory_recalled = False

print("A Noite do Krtwl\n")
print(" Antes de começarmos,você que está lendo essa história. Entenda que tudo que aconteceu aqui foi necessário para criar o ditador que conhecemos atualmente. Não sei como foi que ele ficou assim ou o que se passou antes desses eventos." \
"mas pelo menos essa parte da história você precisa conhecer, talvez seja uma parte importante para resolver o problema que estamos enfrentando e encontrar uma possível solução.\n" \
"A história se passa em uma noite no dia 10 de março de 2031.")
print("Zayr recebe uma mensagem urgente da organização. Um informante afirma ter descoberto arquivos secretos que podem revelar a origem do Krtwl Vek.")
print("Mas algo está errado. O local da reunião é um prédio abandonado no centro da cidade. Zayr suspeita que pode ser uma armadilha. Ele decide investigar.")
print("**Zayr Chega no Prédio.**")

# Escolha inicial: porta principal ou fundos (ramificação real)
choice1 = ask_choice("O que ele faz?\n1 - Entrar pela porta principal\n2 - Ir pelas portas dos fundos\nEscolha (1/2): ", {"1", "2"})
if choice1 == "1":
    path_main = True
    print("Zayr entra pela frente. Corredores amplos, comum para prédios abandonados e escuros. Um grupo de guardas aparece, já sabendo quem ele é, avançam em sua direção.")
    action = ask_choice("1 - Enfrentar os guardas\n2 - Tentar negociar / recuar\nEscolha (1/2): ", {"1", "2"})
    if action == "1":
        # Combate direto -> possibilidade de captura ou recurso extremo
        combat = ask_choice("Você luta corpo a corpo.\n1 - Usar combate físico\n2 - Ativar o Krtwl Vek (risco mental)\nEscolha (1/2): ", {"1", "2"})
        if combat == "2":
            used_krtwl = True
            print("Zayr ativa o Krtwl Vek. Os guardas caem, mas uma assinatura do poder atrai agentes externos.")
            # Após usar Krtwl, rastreamento leva à caçada
        else:
            # derrota provável -> captura
            captured = True
            print("A luta é dura. Zayr é dominado e capturado pelos guardas.")
            interrogated = True
            # Interrogatório com escolhas que determinam final A/B
            iq = ask_choice("Interrogatório: Resistir ou Cooperar?\n1 - Resistir\n2 - Cooperar/confessar\nEscolha (1/2): ", {"1", "2"})
            if iq == "1":
                resisted = True
                print("Zayr resiste. Tortura mental tenta arrancar segredos.")
            else:
                surrendered = True
                print("Zayr confessa detalhes para sobreviver; a organização o manipula a partir dali.")
    else:
        print("Zayr tenta negociar com os guardas mas eles não o escutam obrigando-o a  recuar, usando silêncio e sombras. Ainda assim, sua presença foi notada.")
        # empurra para encontro com o irmão ou inspeção que pode levar a fuga
        retreat = ask_choice("Ao recuar ele encontra uma sala trancada.\n1 - Forçar a porta\n2 - Contornar o corredor\nEscolha (1/2): ", {"1", "2"})
        if retreat == "1":
            print("Ao forçar a porta, Zayr até consegue passar mas ele não percebe agentes nas sombras e é nocauteado de surpresa e é capturado.")
            captured = True
            interrogated = True
        else:
            print("Zayr contorna o corredor e encontra uma saída lateral para os fundos.")
            path_back = True  # transição narrativa para rota de infiltração
elif choice1 == "2":
    path_back = True
    print("Zayr entra pelos fundos. Um corrimão enferrujado leva a uma escada.")
    action = ask_choice("1 - Subir para o telhado\n2 - Descer para o porão\nEscolha (1/2): ", {"1", "2"})
    if action == "1":
        path_rooftop = True
        print("No telhado há um sniper inimigo observando os arredores.")
        sr = ask_choice("1 - Atacar o sniper furtivamente\n2 - Evitar confronto e procurar outra entrada\nEscolha (1/2): ", {"1", "2"})
        if sr == "1":
            print("Zayr elimina o sniper com precisão e encontra um rádio da organização.")
            radio_info = True
            # ouvir rádio revela traição interna
            listen = ask_choice("Ouvir o rádio?\n1 - Sim\n2 - Não\nEscolha (1/2): ", {"1", "2"})
            if listen == "1":
                print("Pelo rádio Zayr descobre uma ordem de silenciar membros — a organização planeja eliminar seus informantes.")
            else:
                print("Zayr decide não arriscar. Guarda o rádio e desce.")
        else:
            print("Zayr evita o conflito e volta a procurar uma entrada para o porão.")
            path_rooftop = False
            path_back = True
            action = "2"  # forçar descida ao porão no fluxo abaixo
    if (not path_rooftop) or action == "2":
        path_lab = True
        print("Zayr desce ao porão e encontra um laboratório abandonado.")
        choice_lab = ask_choice("1 - Investigar os computadores\n2 - Continuar explorando o laboratório discretamente\nEscolha (1/2): ", {"1", "2"})
        if choice_lab == "1":
            discovered_experiment = True
            print("Zayr conecta-se a um terminal e abre arquivos experimentais sobre o Krtwl Vek.")
            # Revelação de memória possível
            mem = ask_choice("Os arquivos mostram imagens que podem despertar memórias.\n1 - Tentar recordar\n2 - Evitar olhar (medo)\nEscolha (1/2): ", {"1", "2"})
            if mem == "1":
                memory_recalled = True
                print("Fragmentos de uma memória o atingem: uma vez ele salvou alguém usando o Krtwl Vek.")
            else:
                print("Zayr evita as imagens aterradoras por enquanto.")
        else:
            print("Zayr explora fisicamente o laboratório e encontra amostras e equipamentos queimados. Há pistas, mas menos diretas.")

# Alarme universal: conecta ramos
choice6 = ask_choice("Um alarme dispara no prédio.\n1 - Fugir do prédio\n2 - Continuar procurando respostas\nEscolha (1/2): ", {"1", "2"})
if choice6 == "1":
    print("Zayr tenta fugir; corredores estão congestionados.")
    if captured:
        print("Mesmo fugindo, agentes o alcançam novamente — ele é recapturado.")
        interrogated = True
    else:
        print("Zayr consegue escapar momentaneamente, mas sabe que será caçado se voltar.")
else:
    print("Zayr fica e segue em frente, agora com risco aumentado e menos margem de erro.")
    # continuar pode abrir encontro com irmão
    pass

# Encontro com o irmão (ponto chave que pode aparecer em múltiplos ramos)
choice7 = ask_choice("Um homem aparece nas sombras. É seu irmão.\n1 - Conversar com ele\n2 - Atacar imediatamente\nEscolha (1/2): ", {"1", "2"})
if choice7 == "1":
    believed_brother = True
    print("O irmão fala que a organização manipula memórias e usa o Krtwl Vek para controle.")
    if discovered_experiment or memory_recalled:
        print("As provas do laboratório confirmam as acusações do irmão.")
    choice8 = ask_choice("Acreditar nele?\n1 - Sim, confiar\n2 - Não, desconfiar\nEscolha (1/2): ", {"1", "2"})
    if choice8 == "1":
        print("Os irmãos unem-se. Plano: expor a organização ou fugir juntos.")
        teamed = True
    else:
        print("Zayr não confia totalmente; tensão entre os dois aumenta.")
        teamed = False
else:
    attacked_brother = True
    print("Zayr ataca o homem sem verificar. É seu irmão — a luta é amarga.")
    choice9 = ask_choice("O irmão se defende.\n1 - Continuar lutando\n2 - Parar e ouvir\nEscolha (1/2): ", {"1", "2"})
    if choice9 == "1":
        print("A luta deixa ambos feridos e exaustos.")
    else:
        print("Zayr para; o irmão revela segredos que abalam Zayr.")
        if discovered_experiment:
            memory_recalled = True
            print("As memórias retornam com força.")

# Invasão final pela organização
print("Sons de passos. A organização invade o prédio.")
choice11 = ask_choice("1 - Enfrentar a organização\n2 - Fugir com o irmão (ou sozinho)\nEscolha (1/2): ", {"1", "2"})
if choice11 == "1":
    # ramificações finais do combate
    if path_main and captured and interrogated:
        print("No combate caótico, Zayr, já fragilizado pelo interrogatório, não resiste.")
        final = "A - Prism: Preso e usado como exemplo"
    else:
        choice12 = ask_choice("No combate final:\n1 - Usar Krtwl Vek novamente (alto risco)\n2 - Lutar normalmente\nEscolha (1/2): ", {"1", "2"})
        if choice12 == "1":
            used_krtwl = True
            print("Zayr convoca o Krtwl Vek. Seu poder derruba inimigos, mas cobra um preço.")
            final = "E - Exposto e Perseguido: o poder é mostrado, Zayr vira alvo"
        else:
            print("Zayr e possivelmente seu irmão lutam com tudo. Muitos caem.")
            # Se confiaram um no outro, final trágico de sacrifício
            if believed_brother and teamed:
                final = "D - Ambos Morrem Lutando pela Verdade"
            else:
                final = "B - Vitória Amarga: sobrevivência com perdas"
else:
    # fuga
    fled_choice = ask_choice("Ao fugir:\n1 - Seguir o irmão\n2 - Ir sozinho\nEscolha (1/2): ", {"1", "2"})
    if fled_choice == "1" and believed_brother:
        fled_with_bro = True
        print("Zayr e o irmão fogem juntos, levando provas e cicatrizes.")
        if discovered_experiment:
            final = "C - Exílio com Verdade: fogem e planejam expor a organização"
        else:
            final = "F - Fugitivos Incertos: fogem sem todas as respostas"
    else:
        print("Zayr foge sozinho, carregando dúvidas e feridas.")
        if used_krtwl:
            final = "E - Exposto e Perseguido: o poder é mostrado, Zayr vira alvo"
        else:
            final = "G - Solitário: desaparece nas sombras com segredos"

# Conclusão final adicional sobre sanidade
choice14 = ask_choice("Zayr sente o Krtwl tomando sua mente.\n1 - Resistir\n2 - Se entregar ao poder\nEscolha (1/2): ", {"1", "2"})
if choice14 == "1":
    resisted = True
    print("Zayr luta para manter sua sanidade.")
else:
    surrendered = True
    print("Zayr se rende ao Krtwl Vek. Algo nele se quebra.")
    # Se se entrega, ajustar finais que dependem do poder
    if 'E - Exposto' in locals() or used_krtwl:
        final = "H - Consumido: o poder vence, transformando Zayr num monstro perseguido"

# Impressão do final com base nas ramificações reais
print("\n--- Final ---")
print("Caminhos seguidos:")
if path_main:
    print("- Entrada principal (Combate/Interrogatório)")
if path_back:
    print("- Entrada pelos fundos (Infiltração/Laboratório/Telhado)")
if path_rooftop:
    print("- Telhado (Sniper / Rádio)")
if path_lab:
    print("- Laboratório (Experimentos sobre o Krtwl)")

# Determinar e exibir final textual
if surrendered:
    print("Final: Zayr perde completamente a sanidade. O Krtwl Vek o consome.")
else:
    try:
        print("Final:", final)
    except NameError:
        # fallback lógico baseado em flags
        if captured and interrogated and surrendered:
            print("Final: Zayr é usado como exemplo pela organização.")
        elif fled_with_bro and discovered_experiment:
            print("Final: Zayr foge com o irmão e planejam expor a verdade.")
        elif radio_info and not believed_brother:
            print("Final: Zayr conhece a traição, torna-se um alvo solitário.")
        else:
            print("Final: Zayr desaparece nas sombras, sua história faz ele se tornar uma lenda entre os sobreviventes.")