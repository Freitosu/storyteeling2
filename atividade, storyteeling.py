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

# Estado da história (Flags)
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

# [SLIDE 8 - LORE/CONTEXTO]
# Melhoria: Adicionado texto que estabelece o Lore e o clima opressivo.
print("=+= A Noite do Krtwl =+=\n")
print("Antes de começarmos, você que lê estas palavras: entenda que o que aconteceu nesta noite foi o passo necessário para criar o ditador que conhecemos atualmente. A história se passa em uma noite no dia 10 de março de 2031.\n" \
"Este não é um conto de heróis, mas o registro do nascimento de uma tirania. Zayr Krtwol, um homem assombrado por fragmentos de um passado que ele não consegue lembrar, recebe uma mensagem codificada. A Organização, a força implacável que controla a cidade com mão de ferro, planeja destruir os arquivos que revelam a origem do Krtwl Vek, o poder perigoso que Zayr carrega em suas veias.\n\n" \
"O local da reunião: um prédio abandonado no centro da cidade. Zayr suspeita que pode ser uma armadilha, mas sua sede por respostas é maior do que o seu medo de morrer.")

print("\n**Zayr Chega no Prédio.**")

# [SLIDE 9 - SHOWING VS TELLING]
# Melhoria: Descrições mais detalhadas do cenário para "mostrar" o local.
choice1 = ask_choice("\nO que ele faz?\n1 - Entrar pela porta principal (Confronto Direto)\n2 - Ir pelas portas dos fundos (Furtividade)\nEscolha (1/2): ", {"1", "2"})
if choice1 == "1":
    path_main = True
    print("Zayr empurra a porta de ferro pesada. O cheiro de mofo e concreto úmido o atinge instantaneamente. Corredores intermináveis e cavernosos se estendem à sua frente, a única luz vindo de postes de rua distantes fora das janelas quebradas. Sua entrada não é silenciosa. Das sombras, um grupo de guardas da Organização aparece, seus rostos cobertos por máscaras táticas, as armas já apontadas para o peito de Zayr. Eles sabem exatamente quem ele é.")
    action = ask_choice("1 - Enfrentar os guardas com força\n2 - Tentar negociar / recuar\nEscolha (1/2): ", {"1", "2"})
    if action == "1":
        combat = ask_choice("Você luta corpo a corpo.\n1 - Usar combate físico\n2 - Ativar o Krtwl Vek (sacrifício mental)\nEscolha (1/2): ", {"1", "2"})
        if combat == "2":
            used_krtwl = True
            # [SLIDE 14 - PILARES NARRATIVOS (Integração Tema-Mecânica)]
            # Melhoria: Descrevendo o peso de usar o poder.
            print("Zayr se recusa a ser dominado. Ele cede ao impulso que queima em suas veias. O Krtwl Vek se manifesta. Sua visão fica vermelha. O tempo parece desacelerar. Com um grito, ele libera uma onda de choque que derruba os guardas, mas algo nele se quebra. Ele sente suas memórias mais antigas, os rostos de seus pais, desvanecerem em um vazio nebuloso. Seu poder atrai a atenção de agentes mais perigosos.")
        else:
            # [SLIDE 9 - SHOWING VS TELLING]
            # Melhoria: Mostrando a luta e a derrota.
            captured = True
            print("A luta é brutal. Zayr desvia do primeiro golpe, mas o segundo guarda o atinge nas costelas com uma tonfa elétrica. O ar falta nos pulmões. Visão turva. Seus braços são imobilizados, e ele é forçado a ajoelhar-se. A Organização venceu o primeiro round. Zayr é dominado e capturado.")
            interrogated = True
            iq = ask_choice("Interrogatório: Resistir ou Cooperar?\n1 - Resistir à dor e ao vazio\n2 - Cooperar/confessar para sobreviver\nEscolha (1/2): ", {"1", "2"})
            if iq == "1":
                resisted = True
                print("Zayr resiste. Ele se fecha em uma casca de silêncio. Tortura mental tenta arrancar os segredos que ele mesmo não consegue lembrar, mas ele se recusa a ceder.")
            else:
                surrendered = True
                print("Zayr não aguenta mais. Ele confessa os detalhes de sua missão para sobreviver, entregando a única vantagem que tinha. A Organização agora sabe tudo e planeja usá-lo.")
    else:
        # [SLIDE 9 - SHOWING VS TELLING]
        # Melhoria: Mostrando o recuo.
        print("Zayr percebe o perigo. Ele recua para as sombras, usando silêncio e agilidade para escapar da linha de fogo. Ainda assim, sua presença foi notada. O prédio agora está em alerta.")
        retreat = ask_choice("Ao recuar, ele encontra uma sala trancada.\n1 - Forçar a porta com o ombro\n2 - Contornar o corredor e procurar outra saída\nEscolha (1/2): ", {"1", "2"})
        if retreat == "1":
            print("Ao forçar a porta, Zayr até consegue passar, mas ele não percebe agentes nas sombras e é nocauteado de surpresa e é capturado.")
            captured = True
            interrogated = True
        else:
            # [SLIDE 9 - SHOWING VS TELLING]
            # Melhoria: Descrevendo a transição.
            print("Zayr contorna o corredor e encontra uma saída lateral para os fundos. Ele desliza para o beco, o coração batendo forte.")
            path_back = True  # transição narrativa para rota de infiltração
elif choice1 == "2":
    path_back = True
    # [SLIDE 9 - SHOWING VS TELLING]
    # Melhoria: Descrevendo a entrada furtiva.
    print("Zayr entra pelos fundos. Um corrimão enferrujado e uma escada estreita e em espiral se estendem à sua frente. A única luz vem de um gerador barulhento.")
    action = ask_choice("1 - Subir para o telhado (Vigilância)\n2 - Descer para o porão (Investigação)\nEscolha (1/2): ", {"1", "2"})
    if action == "1":
        path_rooftop = True
        # [SLIDE 9 - SHOWING VS TELLING]
        # Melhoria: Descrevendo o telhado e o perigo.
        print("No telhado, o vento frio da noite uiva. Zayr se esconde atrás de uma caixa de ventilação, mas seus olhos captam o brilho de uma mira telescópica. Há um sniper inimigo vigiando o perímetro.")
        sr = ask_choice("1 - Atacar o sniper furtivamente pelas costas\n2 - Evitar confronto e procurar outra entrada no telhado\nEscolha (1/2): ", {"1", "2"})
        if sr == "1":
            # [SLIDE 9 - SHOWING VS TELLING]
            # Melhoria: Descrevendo o ataque e a descoberta.
            print("Zayr avança em silêncio. Ele elimina o sniper com precisão. Ao vasculhar o corpo, ele encontra um rádio da organização.")
            radio_info = True
            listen = ask_choice("Ouvir o rádio da Organização?\n1 - Sim\n2 - Não, é muito arriscado\nEscolha (1/2): ", {"1", "2"})
            if listen == "1":
                # [SLIDE 8 - LORE]
                # Melhoria: Adicionado texto que revela Lore.
                print("Pelo rádio Zayr descobre uma ordem de silenciar membros. A Organização não quer apenas destruir os arquivos, eles planejam eliminar todos os informantes e qualquer um que saiba sobre o Krtwl Vek. A traição é total.")
            else:
                print("Zayr decide não arriscar. Ele guarda o rádio e desce para o porão.")
        else:
            print("Zayr evita o conflito e volta a procurar uma entrada para o porão.")
            path_rooftop = False
            path_back = True
            action = "2"  # forçar descida ao porão no fluxo abaixo
    if (not path_rooftop) or action == "2":
        path_lab = True
        # [SLIDE 8 - LORE (Narrativa Ambiental)]
        # Melhoria: Usando o cenário para contar o Lore.
        print("Zayr desce ao porão e encontra um laboratório abandonado. O local está em ruínas. Frascos quebrados, documentos rasgados e fumaça saindo de equipamentos queimados sugerem que a Organização tentou apagar as provas às pressas.")
        choice_lab = ask_choice("1 - Investigar os computadores restantes (Lore)\n2 - Continuar explorando o laboratório discretamente\nEscolha (1/2): ", {"1", "2"})
        if choice_lab == "1":
            discovered_experiment = True
            # [SLIDE 8 - LORE]
            # Melhoria: Adicionado texto que revela Lore sobre os experimentos.
            print("Zayr conecta-se a um terminal danificado. Ele abre arquivos experimentais chamados Projeto Krtwl Vek. Os documentos descrevem o processo de fusão de energia com a mente humana, um processo que causa amnésia severa e instabilidade mental. Ele vê sua própria foto e o nome de seu irmão.")
            mem = ask_choice("Os arquivos mostram imagens que podem despertar memórias.\n1 - Tentar recordar\n2 - Evitar olhar (medo do passado)\nEscolha (1/2): ", {"1", "2"})
            if mem == "1":
                memory_recalled = True
                # [SLIDE 7 - CONFLITO INTERNO]
                # Melhoria: Mostrando a dor da memória.
                print("Fragmentos de uma memória o atingem como um soco. Ele vê a si mesmo segurando o corpo de uma pessoa que ele amava. O Krtwl Vek foi a única forma de salvá-la, mas a custo de sua própria identidade. Uma vez, ele salvou alguém usando o Krtwl Vek.")
            else:
                print("Zayr evita as imagens aterradoras por enquanto, temendo a loucura.")
        else:
            print("Zayr explora fisicamente o laboratório e encontra amostras e equipamentos queimados. Há pistas, mas menos diretas.")

# Alarme universal: conecta ramos
choice6 = ask_choice("Um alarme ensurdecedor dispara no prédio.\n1 - Fugir do prédio o mais rápido possível\n2 - Continuar procurando respostas antes de sair\nEscolha (1/2): ", {"1", "2"})
if choice6 == "1":
    # [SLIDE 9 - SHOWING VS TELLING]
    # Melhoria: Mostrando a fuga e a captura.
    print("Zayr tenta fugir; corredores estão congestionados por guardas e fumaça.")
    if captured:
        print("Mesmo fugindo, agentes táticos o alcançam novamente. Seus movimentos são desajeitados após o interrogatório. Ele é recapturado.")
        interrogated = True
    else:
        print("Zayr consegue escapar momentaneamente, mas sabe que a Organização o caçará até o fim.")
else:
    # [SLIDE 7 - CONFLITO INTERNO]
    # Melhoria: Mostrando a persistência de Zayr.
    print("Zayr fica e segue em frente, agora com risco aumentado e menos margem de erro. Ele não sairá sem a verdade.")
    # continuar pode abrir encontro com irmão
    pass

# [SLIDE 11 - PERSONAGENS DINÂMICOS]
# Melhoria: A descrição do irmão é fantástica no seu código original, já é dinâmica. Apenas aprimorei o texto para combinar com o novo estilo de escrita.
choice7 = ask_choice("Um homem aparece nas sombras. Ele segura uma arma. É seu irmão, Kayan.\n1 - Conversar com ele e abaixar a arma\n2 - Atacar imediatamente\nEscolha (1/2): ", {"1", "2"})
if choice7 == "1":
    believed_brother = True
    # [SLIDE 8 - LORE]
    # Melhoria: Revelando o segredo da Organização.
    print("O irmão abaixa a arma. O rosto dele está marcado pela dor. Ele revela que a Organização manipula memórias para criar escravos leais e usa o Krtwl Vek para controle total da população.")
    if discovered_experiment or memory_recalled:
        print("As provas que Zayr encontrou no laboratório confirmam as acusações de Kayan.")
    choice8 = ask_choice("Acreditar nele e unir forças?\n1 - Sim, confiar no único laço que restou\n2 - Não, desconfiar e seguir sozinho\nEscolha (1/2): ", {"1", "2"})
    if choice8 == "1":
        print("Os irmãos unem-se. Plano: expor a Organização para o mundo ou fugir juntos e lutar outro dia.")
        teamed = True
    else:
        # [SLIDE 7 - CONFLITO INTERNO]
        # Melhoria: Mostrando a tensão.
        print("Zayr não confia totalmente; ele já foi traído antes. A tensão entre os dois aumenta.")
        teamed = False
else:
    attacked_brother = True
    # [SLIDE 9 - SHOWING VS TELLING]
    # Melhoria: Mostrando a luta trágica.
    print("Zayr ataca o homem sem verificar. É seu irmão — a luta é amarga e cheia de arrependimento.")
    choice9 = ask_choice("Kayan se defende.\n1 - Continuar lutando para matar\n2 - Parar e ouvir o que ele tem a dizer\nEscolha (1/2): ", {"1", "2"})
    if choice9 == "1":
        print("A luta deixa ambos feridos e exaustos, sem vencedores.")
    else:
        # [SLIDE 7 - CONFLITO INTERNO (e Memória)]
        # Melhoria: Revelando segredos e memórias.
        print("Zayr para; Kayan revela segredos sobre a Organização que abalam a sanidade de Zayr.")
        if discovered_experiment:
            memory_recalled = True
            print("As memórias retornam com força. Zayr vê Kayan quando criança. A Organização apagou isso.")

# Invasão final pela organização
print("Sons de passos pesados e granadas. A Organização invade o prédio com força total.")
choice11 = ask_choice("1 - Enfrentar a Organização em um confronto final\n2 - Fugir com o irmão (ou sozinho)\nEscolha (1/2): ", {"1", "2"})
if choice11 == "1":
    # ramificações finais do combate
    if path_main and captured and interrogated:
        print("No combate caótico, Zayr, já fragilizado pelo interrogatório e pela tortura mental, não resiste.")
        final = "A - Prism: Preso e usado como exemplo pela Organização"
    else:
        choice12 = ask_choice("No combate final:\n1 - Usar Krtwl Vek novamente (alto risco de sanidade)\n2 - Lutar normalmente com armas e força\nEscolha (1/2): ", {"1", "2"})
        if choice12 == "1":
            # [SLIDE 14 - PILARES NARRATIVOS (Integração Tema-Mecânica)]
            # Melhoria: Descrevendo o peso final do poder.
            used_krtwl = True
            print("Zayr convoca o Krtwl Vek. Seu poder derruba dezenas de guardas, mas o preço é total. Ele esquece o rosto de seu irmão e sua própria missão. O poder o consome.")
            final = "E - Exposto e Perseguido: o poder é mostrado, Zayr vira alvo solitário"
        else:
            print("Zayr e possivelmente seu irmão lutam com tudo. Muitos guardas caem, mas a Organização é implacável.")
            # Se confiaram um no outro, final trágico de sacrifício
            if believed_brother and teamed:
                final = "D - Ambos Morrem Lutando pela Verdade"
            else:
                final = "B - Vitória Amarga: sobrevivência com perdas irreparáveis"
else:
    # fuga
    fled_choice = ask_choice("Ao fugir:\n1 - Seguir o irmão (plano de Kayan)\n2 - Ir sozinho (plano de Zayr)\nEscolha (1/2): ", {"1", "2"})
    if fled_choice == "1" and believed_brother:
        fled_with_bro = True
        print("Zayr e Kayan fogem juntos, levando as provas e cicatrizes mentais.")
        if discovered_experiment:
            final = "C - Exílio com Verdade: fogem e planejam expor a Organização para o mundo"
        else:
            final = "F - Fugitivos Incertos: fogem sem todas as respostas, mas juntos"
    else:
        print("Zayr foge sozinho, carregando dúvidas e feridas profundas.")
        if used_krtwl:
            final = "E - Exposto e Perseguido: o poder é mostrado, Zayr vira alvo solitário"
        else:
            final = "G - Solitário: desaparece nas sombras com os segredos da Organização"

# Conclusão final adicional sobre sanidade
# [SLIDE 7 - CONFLITO INTERNO]
# Melhoria: Aprimorando a escolha final de sanidade baseada nos Pilares Narrativos (Slide 14).
choice14 = ask_choice("Zayr sente o Krtwl tomando sua mente por completo.\n1 - Resistir à loucura e lutar por sua sanidade\n2 - Se entregar ao poder e ao vazio (loucura)\nEscolha (1/2): ", {"1", "2"})
if choice14 == "1":
    resisted = True
    print("Zayr luta para manter sua sanidade. A batalha mental é mais dura do que a física.")
else:
    surrendered = True
    print("Zayr se rende ao Krtwl Vek. Algo nele se quebra para sempre. A paranoia e o poder o consomem.")
    # Se se entrega, ajustar finais que dependem do poder
    if 'E - Exposto' in locals() or used_krtwl:
        final = "H - Consumido: o poder vence, transformando Zayr num monstro sem memórias"

# Impressão do final com base nas ramificações reais
# [SLIDE 9 - SHOWING VS TELLING]
# Melhoria: Mostrando as consequências baseadas no Lore.
print("\n--- Consequências da Noite do Krtwl ---")
print("Caminhos que levaram ao fim:")
if path_main:
    print("- Entrada principal (Confronto Direto/Captura)")
if path_back:
    print("- Entrada pelos fundos (Infiltração/Laboratório/Rádio)")
if path_rooftop:
    print("- Telhado (Vigilância / Sniper)")
if path_lab:
    print("- Laboratório (Experimentos e Verdades Fragmentadas)")

# Determinar e exibir final textual
if surrendered:
    # [SLIDE 14 - PILARES NARRATIVOS (Integração Tema-Mecânica)]
    # Melhoria: Final que reflete o tema do poder perigoso.
    print("Final: Zayr perde completamente a sanidade. O Krtwl Vek o consome, e ele se torna o ditador frio e sem memórias que o mundo um dia conhecerá.")
else:
    try:
        # [SLIDE 9 - SHOWING VS TELLING]
        # Melhoria: Adicionado texto que "mostra" as consequências do final escolhido.
        print("Final:", final)
        if final.startswith("A - Prism"):
             print("A Organização o usa como exemplo de rebeldia fracassada. O ditador nunca nascerá.")
        elif final.startswith("B - Vitória Amarga"):
             print("Ele sobreviveu, mas a Organização ainda controla a cidade e ele é um fugitivo solitário.")
        elif final.startswith("C - Exílio com Verdade"):
             print("Eles têm as provas. O mundo saberá a verdade sobre o Krtwl Vek. A resistência começa agora.")
        elif final.startswith("D - Ambos Morrem"):
             print("Eles morreram lutando. O segredo do Krtwl Vek morre com eles. A Organização continua seu plano.")
        elif final.startswith("E - Exposto e Perseguido"):
             print("Ele usou o poder demais. Ele não lembra quem é, mas a Organização nunca parará de caçá-lo.")
        elif final.startswith("F - Fugitivos Incertos"):
             print("Eles estão juntos, mas a Organização ainda está caçando-os. O futuro é nebuloso.")
        elif final.startswith("G - Solitário"):
             print("Ele fugiu com a verdade, mas sem o irmão. Ele é um homem assombrado pelos seus próprios segredos.")
        elif final.startswith("H - Consumido"):
             print("O poder o consome, e ele se torna o ditador frio e sem memórias que o mundo um dia conhecerá.")
    except NameError:
        # fallback lógico baseado em flags
        if captured and interrogated and surrendered:
            print("Final: Zayr é usado como exemplo pela Organização.")
        elif fled_with_bro and discovered_experiment:
            print("Final: Zayr foge com o irmão e planejam expor a verdade.")
        elif radio_info and not believed_brother:
            print("Final: Zayr conhece a traição, torna-se um alvo solitário.")
        else:
            print("Final: Zayr desaparece nas sombras, sua história se torna uma lenda entre os poucos sobreviventes.")