# PL2024

**Autor**: Mariana Gonçalves, a100662


Este trabalho de casa consiste numa soma de valores quando um número aparece após um ON.
Contudo, se aparecer um OFF, os números seguintes, mesmo que já tenha aparecido um ON, não contribuem.
O "=" funciona como "print"; quando aparece, imprimimos o valor somado até ao momento.

Coloquei esta linha em comentário: #print(f"Soma final: {resultado}") por este pequeno pormenor: 
Por exemplo, no "7ahaONha12ahah=aah13ahOFFhah23ahON7hah=", 
como acaba em "=", mostra o valor do somador final.

Mas se o exemplo for: "7ahaONha12ahah=aah13ahOFFhah23ahON7hah=ahah5",
imprime 12;
imprime 32; 
depois soma o 5, mas não imprime porque não aparece o "=", ou seja, a minha dúvida é imprimirmos o final, acabando ou não em "=", ou descartamos mesmo que, depois do último "=", se somarem mais números. 
Fica então em comentário para que qualquer que seja das opções exista aqui a dualidade necessária.
