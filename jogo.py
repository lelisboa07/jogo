from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Ataques Paranormais")
janela.geometry("700x400")

# FASES

def fase2():
    messagebox.showinfo("Escolha certa!", "Parabéns! Vocês conseguiram derrotar a criatura que estava escondida nessa sala, mas esse foi só o começo...")
    titulo_intro.destroy()
    texto_intro.destroy()

    texto1.config(text="Vocês acabam de verificar algumas outras salas e agora já podem seguir até o final do corredor.")
    fase.config(text="Chegando lá vocês encontram duas portas e devem escolher entre...")
    escolha1.config(text= "Entrar no laboratório",command=fase3)
    escolha2.config(text= "Entrar no refeitório", command=escolha_errada2)

def fase3():
    messagebox.showinfo("Escolha certa!", "Parabéns! Vocês entraram a tempo de pegar uma criatura pelas costas.")

    texto1.config(text="Agora que vocês limparam mais uma das salas da escola, poderão seguir para as próximas.")
    fase.config(text="Dentro do laboratório vocês conseguem ver mais um corredor com duas portas e precisam escolher novamente...")
    escolha1.config(text= "Entrar em uma sala de aula",command=escolha_errada3)
    escolha2.config(text= "Entrar no banheiro", command=fase4)
    

def fase4():
    messagebox.showinfo("Escolha certa!", "Parabéns! Vocês derrotam mais duas criaturas que estavam prestes a sair do banheiro.")

    texto1.config(text="Sua equipe está começando a ficar cansada, mas a missão ainda não acabou.\n Voltando para o corredor, vocês decidem entrar na sala de aula.")
    fase.config(text="Não havia nada. Apenas uma porta que dá acesso ao refeitório. O que vocês irão fazer?")
    escolha1.config(text= "Entrar no refeitório", command=fase5)
    escolha2.config(text= "Voltar para o corredor e ir embora",command=escolha_errada4)

def fase5():
    messagebox.showinfo("Escolha certa!", "Parabéns! Vocês conseguiram matar duas criaturas que estavam esperando vocês atrás da outra porta do refeitório.")

    texto1.config(text="Estando dentro do refeitório vocês conseguem ver mais uma porta com uma placa indicando o ginásio.")
    fase.config(text="Tudo parece muito silencioso e agora vocês tem mais duas opções...")
    escolha1.config(text= "Verificar o ginásio", command=encerramento)
    escolha2.config(text= "Ir embora",command=escolha_errada4)

def encerramento():
    messagebox.showinfo("Escolha certa!", "Parabéns! Vocês surpreenderam mais criaturas que estavam escondidas no ginásio.")
    fase.destroy()
    escolha1.destroy()
    escolha2.destroy()

    texto1.config(text="Agora que toda a escola já foi verificada e não há mais criaturas paranormais, vocês já podem ir embora e voltar para suas casas.\n Fim!")



# ESCOLHAS ERRADAS

# seguir até o final
def escolha_errada1():
    messagebox.showinfo("Escolha errada!", "Vocês morreram! Continuaram andando e foram atacados pelas costas.")
    janela.destroy()

# Refeitório
def escolha_errada2():
    messagebox.showinfo("Escolha errada!", "Vocês morreram! Haviam duas criaturas escondidas ao lado da porta e vocês foram pegos desprevenidos.")
    janela.destroy()

# Sala de aula
def escolha_errada3():
    messagebox.showinfo("Escolha errada!", "Vocês morreram! Duas criaturas saíram do banheiro e surpreenderam vocês.")
    janela.destroy()

# Ir embora
def escolha_errada4():
    messagebox.showinfo("Escolha errada!", "Vocês falharam! Ainda existem criaturas na escola, a missão não foi concluída.")
    janela.destroy()



# INTRODUÇÃO
titulo_intro = Label(janela, text="Seja bem vindo(a)!")
texto_intro = Label(janela, text="Agora você faz parte de uma equipe treinada para lutar contra ataques paranormais.\n Olha que sorte, você já recebeu sua primeira missão.\n Um ataque está acontecendo em uma escola e você e sua equipe devem acabar com ele.")



# FASE 1
texto1 = Label(janela, text="Chegando na escola parece estar tudo bem, exceto pela neblina no corredor.")
fase = Label(janela, text="E agora vocês devem escolher se irão...")
escolha1 = Button(janela, text= "Seguir até o final", command=escolha_errada1)
escolha2 = Button(janela, text= "Entrar na primeira porta", command=fase2)



titulo_intro.pack()
texto_intro.pack()
texto1.pack()
fase.pack()
escolha1.pack()
escolha2.pack()

 
janela.mainloop()