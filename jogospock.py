# -*- coding: utf-8 -*-

vitorias = 0
derrotas = 0  

while vitorias < 3 and derrotas < 3:
    
    from random import randint
    number = randint(0,5)
    
    p2 = ""
    
    def number_to_p2(number):
        global p2
        if number == 0:
            p2 = "pedra"
        elif number == 1:
            p2 = "papel"
        elif number == 2:
            p2 = "tesoura"
        elif number == 3:
            p2 = "lagarto"
        else:
            p2 = "spock"
            
        
    p1 = input("qual a sua escolha?")
    number_to_p2(number)
    
    
    if p1 == "pedra" and p2 == "pedra":
        print("p2 escolheu PEDRA, empataram")
    if p1 == "pedra" and p2 == "papel":
        print("p2 escolheu PAPEL, vc perdeu")
        derrotas += 1
    if p1 == "pedra" and p2 == "tesoura":
        print("p2 escolheu TESOURA, vc ganhou")
        vitorias += 1
    if p1 == "pedra" and p2 == "lagarto":
        print("p2 escolheu LAGARTO, vc ganhou")
        vitorias += 1
    if p1 == "pedra" and p2 == "spock":
        print("p2 escolheu SPOCK, vc perdeu")
        derrotas += 1
        
            
    if p1 == "papel" and p2 == "pedra":
        print("p2 escolheu PEDRA, vc ganhou")
        vitorias += 1
    if p1 == "papel" and p2 == "papel":
        print("p2 escolheu PAPEL, empataram")
    if p1 == "papel" and p2 == "tesoura":
        print("p2 escolheu TESOURA, vc perdeu")
        derrotas += 1
    if p1 == "papel" and p2 == "lagarto":
        print("p2 escolheu LAGARTO, vc perdeu")
        derrotas += 1
    if p1 == "papel" and p2 == "spock":
        print("p2 escolheu SPOCK, vc ganhou")
        vitorias += 1
        
            
    if p1 == "tesoura" and p2 == "pedra":
        print("p2 escolheu PEDRA, vc perdeu")
        derrotas += 1
    if p1 == "tesoura" and p2 == "papel":
        print("p2 escolheu PAPEL, vc ganhou")
        vitorias += 1
    if p1 == "tesoura" and p2 == "tesoura":
        print("p2 escolheu TESOURA, empataram")
    if p1 == "tesoura" and p2 == "lagarto":
        print("p2 escolheu LAGARTO, vc ganhou")
        vitorias += 1
    if p1 == "tesoura" and p2 == "spock":
        print("p2 escolheu SPOCK, vc perdeu")
        derrotas += 1
        
            
    if p1 == "lagarto" and p2 == "pedra":
        print("p2 escolheu PEDRA, vc perdeu")
        derrotas += 1
    if p1 == "lagarto" and p2 == "papel":
        print("p2 escolheu PAPEL, vc ganhou")
        vitorias += 1
    if p1 == "lagarto" and p2 == "tesoura":
        print("p2 escolheu TESOURA, vc perdeu")
        derrotas += 1
    if p1 == "lagarto" and p2 == "lagarto":
        print("p2 escolheu LAGARTO, empataram")
    if p1 == "lagarto" and p2 == "spock":
        print("p2 escolheu SPOCK, vc ganhou")
        vitorias += 1
            
            
    if p1 == "spock" and p2 == "pedra":
        print("p2 escolheu PEDRA, vc ganhou")
        vitorias += 1
    if p1 == "spock" and p2 == "papel":
        print("p2 escolheu PAPEL, vc perdeu")
        derrotas += 1
    if p1 == "spock" and p2 == "tesoura":
        print("p2 escolheu TESOURA, vc ganhou")
        vitorias += 1
    if p1 == "spock" and p2 == "lagarto":
        print("p2 escolheu LAGARTO, vc perdeu")
        derrotas += 1
    if p1 == "spock" and p2 == "spock":
        print("p2 escolheu SPOCK, empataram")   
    
    if vitorias == 3:
        print("PARABENS, VC GANHOU O JOGO!!!")
    if derrotas == 3:
        print("VC PERDEU O JOGO, MAIS SORTE DA PROXIMA VEZ")
    